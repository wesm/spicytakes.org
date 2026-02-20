---
title: "Dropping hashes: an idiom used to demonstrate provenance of documents"
date: 2020-04-21
url: https://www.kalzumeus.com/essays/dropping-hashes/
slug: dropping-hashes
word_count: 921
---


There exists an idiom called “dropping a hash” which is widely understood in the security community and not widely understood elsewhere. Somewhat surprisingly, there does not appear to be a canonical explanation. I have dropped hashes before and wrote this up to explain the significance of it to non-specialists.


This explanation assumes very little familiarity with cryptography, hashing, or the sociology of security research. It is written to be broadly comprehensible to professionals, including non-technologists.


You can, if you are skeptical, check these representations with any professional security researcher or cryptographer.


## Some properties of cryptographically secure hashes


There exist a family of algorithms called hashing algorithms, which are closely related to the field of cryptography. A useful property of a cryptographically secure hashing algorithm is that, given any bit of data, you can produce a relatively short series of letters and numbers constituting a “hash” of that data.


SHA-512 is broadly considered a cryptographically secure hashing algorithm. If anyone had proof to the contrary, the global economy would be in substantial jeopardy, because much secure communication over the Internet relies upon this property.


This is what a SHA-512 hash looks like:


`9ca61274537c9f9398bcd74f3d21c1ae5df50737764e2ddbaa2ede6a779c8871fb1b3a31794bbf3b2fc5103421e9ee83646df0b83363afbec2e9c7e67b881b88`


That is a hash of the phrase: “This is what a hash looks like.”, with no quotes. You could produce a SHA-512 hash of any data: a photo, a video, a document, etc. If you alter so much as a letter of the hashed data, the hash radically changes. Take off the period and the hash becomes:


`19e38c497fa028936823325fb6a57f25142f25152f5b086882c0fa38ab885538d364ffd8941cde001033b4d99d4fc5f35ea66d08d060fb6dd959b3d36f518e04`


The definition of “cryptographically secure” rounds to “Even with hundreds of millions of dollars of computer time and the smartest mathematicians on the planet, it is impossible to produce two documents with the same hash, or to go from a hash to the document which produced it.”


In simple terms: you cannot, given a hash, produce a text that matches it without first knowing the *exact* text. It is *beyond the bounds of modern science*.


## One application of cryptographically secure hashes


The computer security field abuts cryptography, and makes use of it for extremely important uses (such as securing most communication over the Internet) and less important uses, such as claiming credit for knowing things before they were widely known.


In computer security, sometimes one can produce dangerous information. Perhaps one could discover, through application of one’s professional skillset, that it is possible to break into Google. To publish that information incurs a risk of enabling someone to do a very bad thing. Many researchers would choose to inform Google privately of their results.


This is not optimal from a professional incentive standpoint, because it is a very professionally significant event to have discovered how to break into Google. This is an achievement in the same way that a scientific paper with an important novel result is an achievement. It could result in lucrative job offers, consulting contracts, or Hacker News karma.


If you let Google fix the issue, you might not be able to credibly say “Prior to Google telling the world about the issue they fixed, I knew about it, *because I did the research that uncovered this problem*.”


Enter cryptographically secure hashing. Write up your research in any fashion. Publish the SHA-512 hash of it, *only*, in a widely read forum. Inform Google of your findings privately. After Google has fixed the issue, publish your research, pointing to the earlier publication of the hash. All people professionally relevant to you will understand that they are certain, to far beyond the threshold they would need to bet their life savings on the matter, that you had the document as of the publication of the hash.


Importantly, this property of cryptographically secure hashing works for *anyone*. It is not magic. It is not simply a shibboleth or ritual unique to the security community. It is *a reproducible technology*, available to anyone, that makes guarantees backed by the present limits of human understanding of the world we live in and the math which governs it.


Any cryptography professor or clueful security engineer will tell you that the above is a layman’s gloss over effectively settled science, that it is secure enough to stake a material portion of the economy on, and that factually a material portion of the economy is staked on it this very second.


## How do you verify a dropped hash?


Download the file. Calculate the hash of the file, using the same algorithm that was used to produce it. The author will generally state this or consider it sufficiently implied by the length and structure of the hash. The author will likely use a well-understood algorithm generally considered by the community to be secure for this purpose. SHA-512 is one such algorithm.


Compare it to a hash previously posted someplace where the hash cannot be edited, generally a widely distributed location such as a mailing list or Twitter.


For example, if you are verifying a SHA-512 hash, you can do this using a command available on every modern operating system. If you don’t know how to do this, ask a technologist.


> shasum -a 512 name-of-the-file.txt


This will output the SHA-512 hash of that file. You can then compare it, via trivial use of the computer or visually, to the previously claimed hash.


If they match, and they should match *exactly*, then you know the file was *beyond any reasonable doubt* the file the author claimed to possess at the point of dropping the hash and that it has not been altered in the interim.
