---
title: "Status update, November 2020"
date: 2020-11-15
url: https://drewdevault.com/2020/11/15/Status-update-November-2020.html
slug: Status-update-November-2020
word_count: 506
---

Greetings, humanoids! Our fleshy vessels have aged by 2.678×10⁶ seconds, and you
know what that means: time for another status update! Pour a cup of your
favorite beverage stimulant and gather ‘round for some news.

First off, today is the second anniversary of SourceHut’s alpha being opened to
the public, and as such, I’ve prepared a special  [blog post](https://sourcehut.org/blog/2020-11-15-sourcehut-2-year-alpha/)  for
you to read. I’ll leave the sr.ht details out of this post and just send you off
to read about it there.

What else is new? Well, a few things. For one, I’ve been working more on Gemini.
I added CGI support to  [gmnisrv](https://sr.ht/~sircmpwn/gmnisrv)  and wrote a
few  [CGI scripts](https://git.sr.ht/~sircmpwn/cgi-scripts)  to do neato Gemini
things with. I’ve also added regexp routing and URL rewriting support. We can
probably ship gmnisrv 1.0 as soon as the last few bugs are flushed out, and a
couple of minor features are added, and we might switch to another SSL
implementation as well. Thanks to the many contributors who’ve helped out:
William Casarin, Tom Lebreux, Kenny Levinsen, Eyal Sawady, René Wagner,
dbandstra, and mbays.

In  [BARE](https://baremessages.org)  news: Elm, Erlang, Java, and Ruby
implementations have appeared, and I have submitted a
 [draft RFC](https://datatracker.ietf.org/doc/draft-devault-bare/)  to the IETF
for standardization.

Finally, I wrote a new Wayland server for you. Its only dependencies are a POSIX
system and a C11 compiler — and it works with Nvidia GPUs, or even systems
without OpenGL support at all. Here’s the code:

```
#include <poll.h>
#include <signal.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ioctl.h>
#include <sys/mman.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <time.h>
#include <unistd.h>

	typedef int16_t i16; typedef int32_t i32; typedef uint16_t u16;
   typedef uint32_t u32; typedef uint8_t u8; typedef int I; typedef size_t S;
	  typedef struct{int b;u32 a,c,d;char*e;i32 x,y,w,h,s,fmt;}O;
	       typedef struct{char*a;u32 b;I(*c)(I,I,u32,u16);}G;

	  struct pollfd fds[33];char a[0xFFFF];I b=0,c=1,d=-1;u32 e=0;
			      O f[128][128];G g[];

#define AR I z,I y,u32 x,u16 c
#define SN(n) (((n)%4)==0?(n):(n)+(4-((n)%4)))

void u8w(FILE*f,u32 ch){char b[4];for (I i=2;i>0;--i){b[i]=(ch&0x3f)|0x80;ch>>=6
;}b[0]=ch|0xE0;fwrite(b,1,3,f);}void xrgb(u32*data,i32 w,i32 h,i32 s){struct
winsize sz;ioctl(0,TIOCGWINSZ,&sz);--sz.ws_row;printf("\x1b[H\x1b[2J\x1b[3J");
for(I y=0;y<sz.ws_row;++y){for(I x=0;x<sz.ws_col;++x){I i=0;u32 c = 0x2800;const
I f[]={0,3,1,4,2,5,6,7};for(I my=0;my<4;++my)for(I mx=0;mx<2;++mx){u32 p=data[((
y*4+my)*h)/(sz.ws_row*4)*(s/4)+((x*2+mx)*w)/(sz.ws_col*2)];u8 avg=((p&0xFF)+((p
>>8)&0xFF)+((p>>16)&0xFF))/3;if(avg>0x80)c|=1<<f[i++];}u8w(stdout,c);}putchar(
'\n');}fflush(stdout);}O*ao(I z,u32 y,I x){for(S i=0;i<128;++i)if(f[z][i].a==0){
f[z][i].a=y;f[z][i].b=x;return &f[z][i];}return 0;}O*go(I z,u32 y){for(S i=0;i<
128;++i)if(f[z][i].a==y)return &f[z][i];return 0;}void wh(I z,i32 y,i16 x, i16 w
){write(z,&y,4);i32 u=((w+8)<<16)|x;write(z,&u,4);}void ws(I z,char*y){i32 l=
strlen(y)+1;write(z,&l,4);l=SN(l);write(z,y,l);}I rs(I z){u32 l;read(z,&l,4);l=
SN(l);read(z,a,l);return l+4;}I ga(I z,I y,u32 x,u16 w){u32 b,u,t,s=0;read(y,&u,
4);I sz=rs(y)+12;read(y,&b,4);read(y,&t,4);--u;ao(z,t,u);switch(u){case 1:++s;wh
(y,t,0,4);write(y,&s,4);--s;break;case 6:s=0;break;default:return sz;}wh(y,t,0,4
);write(y,&s,4);return sz;}I gb(AR){u32 w,u;read(y,&w,4);I t=d;d=-1;read(y,&u,4);
O *o=ao(z,w,15);o->e=mmap(0,u,PROT_READ,MAP_PRIVATE,t,0);return 8;}I gc(AR){u32
w;read(y,&w,4);ao(z,w,8+c);return 4;}I gd(AR){O*o,*r,*t;i32 u,w;switch(c){case 1
:read(y,&u,4);read(y,&w,4);read(y,&w,4);go(z,x)->d=u;if(!u==0){O *b=go(z,u);xrgb
((u32*)b->e,b->w,b->h,b->s);}wh(y,u,0,0);return 12;case 2:read(y,&u,4);read(y, &
u, 4);read(y, &u, 4);read(y, &u, 4);return 16;case 3:read(y,&w,4);struct timespec
ts={.tv_sec=0,.tv_nsec=1.6e6};nanosleep(&ts,0);wh(y,w,0,4);write(y,&w,4);return
4;case 6:o=go(z,x);r=go(z,o->c);if(r&&r->b==12){t=go(z,r->c);if(t->b==13){u32
s=0; wh(y,t->a,0,12);write(y,&s,4);write(y,&s,4);write(y,&s,4);}wh(y,r->a,0,4);
write(y,&e,4);++e;}break;}return 0;}I ge(AR){u32 w,u;if(c==2){read(y,&w,4);read(
y,&u,4);O*o=ao(z,w,12);o->d=u;go(z,u)->c=w;return 8;}return 0;}I gf(AR){u32 w,ae
;switch(c){case 1:read(y,&w,4);O*obj=ao(z,w,13);obj->d=x;go(z,x)->c=w;return 4;
case 4:read(y,&ae,4);return 4;}return 0;}I gg(AR){I sz;switch(c){case 2:sz=rs(y)
;return sz;}return 0;}I gh(AR){i32 w,u;switch(c){case 0:read(y,&w,4);read(y,&u,4
);O*b=ao(z,w,10);b->e=&go(z,x)->e[u];read(y,&b->w,4);read(y,&b->h,4);read(y,&b->
                  s,4);read(y,&b->fmt,4);return 24;}return 0;}

G g[]={{0,0,ga},{"wl_shm",1,gb},{"wl_compositor",1,gc},{"wl_subcompositor",1,0},
{"wl_data_device_manager",3,0},{"wl_output",3,0},{"wl_seat",7,0},{"xdg_wm_base",
2,ge},{0,0,gd},{0,0,0},{0,0,0},{0,0,0},{0,0,gf},{0,0,gg},{0,0,0},{0,0,gh}};

void gi(AR){u32 w;switch(c){case 0:read(y,&w,4);wh(y,w,0,4);write(y,&w,4);break;
case 1:read(y,&w,4);ao(z,w,0);for(S i=0;i<sizeof(g)/sizeof(g[0]);){G*z=&g[i++];
if(!z->b)continue;I gl=strlen(z->a)+1;wh(y,w,0,4+SN(gl)+4+4);write(y,&i,4);ws(y,
                z->a);write(y,&z->b,4);}break;}}void si(){c=0;}

I main(I _1,char**_2){I z=socket(AF_UNIX,SOCK_STREAM,0);struct sockaddr_un y={.
sun_family=AF_UNIX};char *x=getenv("XDG_RUNTIME_DIR");if(!x)x="/tmp";do{sprintf(
 y.sun_path,"%s/wayland-%d",x,c++);}while(access(y.sun_path,F_OK)==0);bind(z, (
struct sockaddr *)&y,sizeof(y));listen(z,3);for(S i=0;i<sizeof(fds);++i){fds[i].
events=POLLIN|POLLHUP;fds[i].revents=0;fds[i].fd=0;}fds[b++].fd=z;signal(SIGINT,
si);memset(&f,0,sizeof(f));while(poll(fds,b,-1)!=-1&&c){if(fds[0].revents){I u=
accept(z,0,0);fds[b++].fd=u;}for(I i=1;i<b;++i){if(fds[i].revents&POLLHUP){
memmove(&fds[i],&fds[i+1],32-i);memset(f[i-1],0,128*sizeof(**f));--b;continue;}
else if(!fds[i].revents){continue;}I u=i-1;I t=fds[i].fd;u32 s,r;char q[
CMSG_SPACE(8)];struct cmsghdr *p;struct iovec n={.iov_base=&s,.iov_len=4};struct
msghdr m={0};m.msg_iov=&n;m.msg_iovlen=1;m.msg_control=q;m.msg_controllen=sizeof
(q);recvmsg(t,&m,0);p=CMSG_FIRSTHDR(&m);if(p){d=*(I *)CMSG_DATA(p);}read(t,&r,4)
;u16 o=((r>>16)&0xFFFF)-8,c=r&0xFFFF;if(s==1){gi(u,t,s,c);}else{for(S j=0;j<128;
++j){if(f[u][j].a==s&&g[f[u][j].b].c){o-=g[f[u][j].b].c(u,t,s,c);break;}}if(o>0)
                     {read(t,a,o);}}}}unlink(y.sun_path);}
```

You’re welcome!
