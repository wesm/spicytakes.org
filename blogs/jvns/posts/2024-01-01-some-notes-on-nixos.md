---
title: "Some notes on NixOS"
date: 2024-01-01
url: https://jvns.ca/blog/2024/01/01/some-notes-on-nixos/
slug: some-notes-on-nixos
word_count: 1990
---


Hello! Over the holidays I decided it might be fun to run NixOS on one of my
servers, as part of my continuing experiments with Nix.


My motivation for this was that previously I was using [Ansible](https://www.ansible.com/) to
provision the server, but then I’d ad hoc installed a bunch of stuff on the
server in a chaotic way separately from Ansible, so in the end I had no real
idea of what was on that server and it felt like it would be a huge pain to
recreate it if I needed to.


This server just runs a few small personal Go services, so it seemed like a
good candidate for experimentation.


I had trouble finding explanations of how to set up NixOS and I needed to
cobble together instructions from a bunch of different places, so here’s a
very short summary of what worked for me.


### why NixOS instead of Ansible?


I think the reason NixOS feels more reliable than Ansible to me is that NixOS **is**
the operating system. It has full control over all your users and services and
packages, and so it’s easier for it to reliably put the system into the state
you want it to be in.


Because Nix has so much control over the OS, I think that if I tried to make
any ad-hoc changes at all to my Nix system, Nix would just blow them away the
next time I ran `nixos-rebuild`. But with Ansible, Ansible only controls a few
small parts of the system (whatever I explicitly tell it to manage), so it’s
easy to make changes outside Ansible.


That said, here’s what I did to set up NixOS on my server and run a Go service on it.


### step 1: install NixOS with nixos-infect


To install NixOS, I created a new Hetzner instance running Ubuntu, and then ran [nixos-infect](https://github.com/elitak/nixos-infect/tree/master#hetzner-cloud) on it to convert the Ubuntu installation into a NixOS install, like this:


```
curl https://raw.githubusercontent.com/elitak/nixos-infect/master/nixos-infect | PROVIDER=hetznercloud NIX_CHANNEL=nixos-23.11 bash 2>&1 | tee /tmp/infect.log

```


I originally tried to do this on DigitalOcean, but it didn’t work for some
reason, so I went with Hetzner instead and that worked.


This isn’t the only way to install NixOS ([this wiki page](https://nixos.wiki/wiki/NixOS_friendly_hosters) lists options for setting up NixOS cloud servers), but it seemed to work.
It’s possible that there are problems with installing that way that I don’t
know about though. It does feel like using an ISO is probably better because that way you don’t have to do this transmogrification of Ubuntu into NixOS.


I definitely skipped Step 1 in `nixos-infect`’s README (“Read and understand
[the script](https://github.com/elitak/nixos-infect/blob/master/nixos-infect)”), but I didn’t feel too worried because I was running it on a
new instance and I figured that if something went wrong I’d just delete it.


### step 2: copy the generated Nix configuration


Next I needed to copy the generated Nix configuration to a new local Git
repository, like this:


```
scp root@SERVER_IP:/etc/nixos/* .

```


This copied 3 files: `configuration.nix`, `hardware-configuration.nix`, and `networking.nix`. `configuration.nix` is the main file. I didn’t touch anything in `hardware-configuration.nix` or `networking.nix`.


### step 3: create a flake


I created a flake to wrap `configuration.nix`. I don’t remember why I did this
(I have some idea of what the advantages of flakes are, but it’s not clear to
me if any of them are actually relevant in this case) but it seems to work. Here’s
my `flake.nix`:


```
{ inputs.nixpkgs.url = "github:NixOS/nixpkgs/23.11";

  outputs = { nixpkgs, ... }: {
    nixosConfigurations.default = nixpkgs.lib.nixosSystem {
      system = "x86_64-linux";

      modules = [ ./configuration.nix ];
    };
  };
}

```


The main gotcha about flakes that I needed to remember here was that you need
to `git add` every `.nix` file you create otherwise Nix will pretend it doesn’t
exist.


The rules about git and flakes seem to be:

- you do need to `git add` your files
- you **don’t** need to commit your changes
- unstaged changes to files are also fine, as long as the file has been `git add`ed


These rules feel very counterintuitive to me (why require that you `git add`
files but allow unstaged changes?) but that’s how it works. I think it might be
an optimization because Nix has to copy all your `.nix` files to the Nix store for some
reason, so only copying files that have been `git add`ed makes the copy faster. There’s a [GitHub issue tracking it here](https://github.com/NixOS/nix/issues/7107) so maybe the way this works will change at some point.


### step 4: figure out how to deploy my configuration


Next I needed to figure out how to deploy changes to my configuration.  There are a bunch
of tools for this, but I found the blog post [Announcing nixos-rebuild: a “new” deployment tool for NixOS](https://www.haskellforall.com/2023/01/announcing-nixos-rebuild-new-deployment.html)
that said you can just use the built-in `nixos-rebuild`, which has
`--target-host` and `--build-host` options so that you can specify which host
to build on and deploy to, so that’s what I did.


I wanted to be able to get Go repositories and build the Go code on the target
host, so I created a bash script that runs this command:


```
nixos-rebuild switch --fast --flake .#default --target-host my-server --build-host my-server --option eval-cache false

```


Making `--target-host` and `--build-host` the same machine is certainly not
something I would do for a Serious Production Machine, but this server is
extremely unimportant so it’s fine.


This `--option eval-cache false` is because Nix kept not showing me my errors
because they were cached – it would just say `error: cached failure of attribute 'nixosConfigurations.default.config.system.build.toplevel'` instead
of showing me the actual error message. Setting `--option eval-cache false`
turned off caching so that I could see the error messages.


Now I could run `bash deploy.sh` on my laptop and deploy my configuration to the server! Hooray!


### step 5: update my ssh config


I also needed to set up a `my-server` host in my `~/.ssh/config`. I set up SSH
agent forwarding so that the server could download the private Git repositories
it needed to access.


```
Host my-server
   Hostname MY_IP_HERE
   User root
   Port 22
   ForwardAgent yes

AddKeysToAgent yes

```


### step 6: set up a Go service


The thing I found the hardest was to figure out how to compile and configure a
Go web service to run on the server. The norm seems to be to define your package and define your
service’s configuration in 2 different files, but I didn’t feel like doing that
– I wanted to do it all in one file. I couldn’t find a simple example of how
to do this, so here’s what I did.


I’ve replaced the actual repository name with `my-service` because it’s a
private repository and you can’t run it anyway.


```
{ pkgs ? (import <nixpkgs> { }), lib, stdenv, ... }: 
let myservice = pkgs.callPackage pkgs.buildGoModule {
  name = "my-service";
  src = fetchGit {
    url = "git@github.com:jvns/my-service.git";
    rev = "efcc67c6b0abd90fb2bd92ef888e4bd9c5c50835"; # put the right git sha here
  };
  vendorHash = "sha256-b+mHu+7Fge4tPmBsp/D/p9SUQKKecijOLjfy9x5HyEE"; # nix will complain about this and tell you the right value
}; in { 
  services.caddy.virtualHosts."my-service.example.com".extraConfig = ''
    reverse_proxy localhost:8333
  '';

  systemd.services.my-service = {
    enable = true;
    description = "my-service";
    after = ["network.target"];
    wantedBy = ["multi-user.target"];
    script = "${myservice}/bin/my-service";
    environment = {
      DB_FILENAME = "/var/lib/my-service/db.sqlite";
    };
    serviceConfig = {
      DynamicUser = true;
      StateDirectory = "my-service"; # /var/lib/my-service
    };
  };
}

```


Then I just needed to do 2 more things:

1. add `./my-service.nix` to the imports section of `configuration.nix`
2. add `services.caddy.enable = true;` to `configuration.nix` to enable Caddy


and everything worked!!


Some notes on this service configuration file:

1. I used `extraConfig` to configure Caddy because I didn’t feel like learning
Nix’s special Caddy syntax – I wanted to just be able to refer to the Caddy
documentation directly.
2. I used systemd’s `DynamicUser` to create a user dynamically to run the
service. I’d never used this before but it seems like a great simple way to
create a different user for every service without having to write a bunch of
repetitive boilerplate and being really careful to choose unique UID and
GIDs. The blog post [Dynamic Users with systemd](https://0pointer.net/blog/dynamic-users-with-systemd.html) talks
about how it works.
3. I used `StateDirectory` to get systemd to create a persistent directory where I could store a SQLite database. It creates a directory at `/var/lib/my-service/`


I’d never heard of `DynamicUser` or `StateDirectory` before Kamal told me about
them the other day but they seem like cool systemd features and I wish
I’d known about them earlier.


### why Caddy?


One quick note on [Caddy](https://caddyserver.com/): I switched to Caddy a while back from nginx
because it automatically sets up Let’s Encrypt certificates. I’ve only been
using it for tiny hobby services, but it seems pretty great so far for that,
and its configuration language is simpler too.


### problem: “fetchTree requires a locked input”


One problem I ran into was this error message:


```
error: in pure evaluation mode, 'fetchTree' requires a locked input, at «none»:0

```


I found this really perplexing – what is `fetchTree`? What is `«none»:0`? What did I do wrong?


I learned 4 things from debugging this (with help from the folks in the Nix discord):

1. In Nix, `fetchGit` calls an internal function called `fetchTree`. So errors that say `fetchTree` might actually be referring to `fetchGit`.
2. Nix truncates long stack traces by default. Sometimes you can get more information with `--show-trace`.
3. It seems like Nix doesn’t always give you the line number in your code which caused the error, even if you use `--show-trace`. I’m not sure why this is. Some people told me this is because `fetchTree` is a built in function but – why can’t I see the line number in my nix code that **called** that built in function?
4. Like I mentioned before, you can pass `--option eval-cache false` to turn off caching so that Nix will always show you the error message instead of `error: cached failure of attribute 'nixosConfigurations.default.config.system.build.toplevel'`


Ultimately the problem turned out to just be that I forgot to pass the Github
revision ID (`rev = "efcc67c6b0abd90fb2bd92ef888e4bd9c5c50835";`) to `fetchGit`
which was really easy to fix.


### nix syntax is still pretty confusing to me


I still don’t really understand the nix language syntax that well, but I
haven’t felt motivated to get better at it yet – I guess learning new language
syntax just isn’t something I find fun. Maybe one day I’ll learn it. My plan
for now with NixOS is to just keep copying and pasting that `my-service.nix`
file above forever.


### some questions I still have


I think my main outstanding questions are:

- When I run `nixos-rebuild`, Nix checks that my systemd services are still
working in some way. What does it check exactly? My best guess is that it
checks that the systemd service **starts** successfully, but if the service
starts and then immediately crashes, it won’t notice.
- Right now to deploy a new version of one of my services, I need to manually
copy and paste the Git SHA of the new revision. There’s probably a better
workflow but I’m not sure what it is.


### that’s all!


I really do like having all of my service configuration defined in one file,
and the approach Nix takes does feel more reliable than the approach I was
taking with Ansible.


I just started doing this a week ago and as with all things Nix I have no idea
if I’ll end up liking it or not. It seems pretty good so far though!


I will say that I find using Nix to be very difficult and I really struggle
when debugging Nix problems (that `fetchTree` problem I mentioned sounds
simple, but it was SO confusing to me at the time), but I kind of like it
anyway. Maybe because I’m not using Linux on my laptop right now I miss having
[linux evenings](https://fabiensanglard.net/a_linux_evening/) and Nix feels
like a replacement for that :)
