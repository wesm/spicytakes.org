---
title: "TOTP for 2FA is incredibly easy to implement. So what's your excuse?"
date: 2022-10-18
url: https://drewdevault.com/2022/10/18/TOTP-is-easy.html
slug: TOTP-is-easy
word_count: 506
---

[Time-based one-time passwords](https://en.wikipedia.org/wiki/Time-based_one-time_password)  are one of the more secure approaches to 2FA
— certainly much better than SMS. And it’s much easier to implement than
SMS as well. The algorithm is as follows:

1. Divide the current Unix timestamp by 30
2. Encode it as a 64-bit big endian integer
3. Write the encoded bytes to a SHA-1 HMAC initialized with the TOTP shared key
4. Let offs = hmac[-1] & 0xF
5. Let hash = decode hmac[offs .. offs + 4] as a 32-bit big-endian integer
6. Let code = (hash & 0x7FFFFFFF) % 1000000
7. Compare this code with the user’s code

You’ll need a little dependency to generate QR codes with the  [otpauth:// URL
scheme](https://github.com/google/google-authenticator/wiki/Key-Uri-Format) , a little UI to present the QR code and store the shared secret in
your database, and a quick update to your login flow, and then you’re good to
go.

Here’s the implementation SourceHut uses in Python. I hereby release this code
into the public domain, or creative commons zero, at your choice:

```
import base64
import hashlib
import hmac
import struct
import time

def totp(secret, token):
    tm = int(time.time() / 30)
    key = base64.b32decode(secret)

    for ix in range(-2, 3):
        b = struct.pack(">q", tm + ix)
        hm = hmac.HMAC(key, b, hashlib.sha1).digest()
        offset = hm[-1] & 0x0F
        truncatedHash = hm[offset:offset + 4]
        code = struct.unpack(">L", truncatedHash)[0]
        code &= 0x7FFFFFFF
        code %= 1000000
        if token == code:
            return True

    return False
```

This implementation has a bit of a tolerance added to make clock skew less of an
issue, but that also means that the codes are longer-lived. Feel free to edit
these tolerances if you so desire.

Here’s another one written in Hare, also public domain/CC-0.

```
use crypto::hmac;
use crypto::mac;
use crypto::sha1;
use encoding::base32;
use endian;
use time;

// Computes a TOTP code for a given time and key.
export fn totp(when: time::instant, key: []u8) uint = {
	const now = time::unix(when) / 30;
	const hmac = hmac::sha1(key);
	defer mac::finish(&hmac);

	let buf: [8]u8 = [0...];
	endian::beputu64(buf, now: u64);
	mac::write(&hmac, buf);

	let mac: [sha1::SIZE]u8 = [0...];
	mac::sum(&hmac, mac);

	const offs = mac[len(mac) - 1] & 0xF;
	const hash = mac[offs..offs+4];
	return ((endian::begetu32(hash)& 0x7FFFFFFF) % 1000000): uint;
};

@test fn totp() void = {
	const secret = "3N2OTFHXKLR2E3WNZSYQ====";
	const key = base32::decodestr(&base32::std_encoding, secret)!;
	defer free(key);
	const now = time::from_unix(1650183739);
	assert(totp(now, key) == 29283);
};
```

In any language, TOTP is just a couple of dozen lines of code even if there
isn’t already a library — and there is probably already a library. You
don’t have to store temporary SMS codes in the database, you don’t have to worry
about phishing, you don’t have to worry about SIM swapping, and you don’t have
to sign up for some paid SMS API like Twilio. It’s more secure and it’s trivial
to implement — so implement it already! Please!

**Update 2022-10-19 @ 07:45 UTC** : A reader pointed out that it’s important to
have rate limiting on your TOTP attempts, or else a brute force attack can be
effective. Fair point!
