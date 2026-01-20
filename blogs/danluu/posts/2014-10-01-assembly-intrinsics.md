---
title: "Assembly v. intrinsics"
date: 2014-10-01
url: https://danluu.com/assembly-intrinsics/
slug: assembly-intrinsics
word_count: 3031
---


Every once in a while, I hear how intrinsics have improved enough that it's safe to use them for high performance code. That would be nice. The promise of intrinsics is that you can write optimized code by calling out to functions (intrinsics) that correspond to particular assembly instructions. Since intrinsics act like normal functions, they can be cross platform. And since your compiler has access to more computational power than your brain, as well as a detailed model of every CPU, the compiler should be able to do a better job of micro-optimizations. Despite decade old claims that intrinsics can make your life easier, it never seems to work out.

The last time I tried intrinsics was around 2007; for more on why they were hopeless then (see this exploration by the author of VirtualDub). I gave them another shot recently, and while they've improved, they're still not worth the effort. The problem is that intrinsics are so unreliable that you have to manually check the result on every platform and every compiler you expect your code to be run on, and then tweak the intrinsics until you get a reasonable result. That's more work than just writing the assembly by hand. If you don't check the results by hand, it's easy to get bad results.

For example, as of this writing, the first two Google hits forpopcnt benchmark(and 2 out of the top 3 bing hits) claim that Intel's hardwarepopcntinstruction is slower than a software implementation that counts the number of bits set in a buffer, via a table lookup using theSSSE3pshufbinstruction. This turns out to be untrue, but it must not be obvious, or this claim wouldn't be so persistent. Let's see why someone might have come to the conclusion that thepopcntinstruction is slow if they coded up a solution using intrinsics.

One of the top search hits has sample code and benchmarks for both nativepopcntas well as the software version usingpshufb.Their coderequires MSVC, which I don't have access to, but their firstpopcntimplementation just calls thepopcntintrinsic in a loop, which is fairly easy to reproduce in a form that gcc and clang will accept. Timing it is also pretty simple, since we're just timing a function (that happens to count the number of bits set in some fixed sized buffer).

```
uint32_t builtin_popcnt(const uint64_t* buf, int len) {
  int cnt = 0;
  for (int i = 0; i < len; ++i) {
    cnt += __builtin_popcountll(buf[i]);
  }
  return cnt;
}

```

This is slightly different from the code I linked to above, since they use the dword (32-bit) version ofpopcnt, and we're using the qword (64-bit) version. Since our version gets twice as much done per loop iteration, I'd expect our version to be faster than their version.

Runningclang -O3 -mpopcnt -funroll-loopsproduces a binary that we can examine. On macs, we can useotool -tvto get the disassembly. On linux, there'sobjdump -d.

```
_builtin_popcnt:
; address                        instruction
0000000100000b30        pushq   %rbp
0000000100000b31        movq    %rsp, %rbp
0000000100000b34        movq    %rdi, -0x8(%rbp)
0000000100000b38        movl    %esi, -0xc(%rbp)
0000000100000b3b        movl    $0x0, -0x10(%rbp)
0000000100000b42        movl    $0x0, -0x14(%rbp)
0000000100000b49        movl    -0x14(%rbp), %eax
0000000100000b4c        cmpl    -0xc(%rbp), %eax
0000000100000b4f        jge     0x100000bd4
0000000100000b55        movslq  -0x14(%rbp), %rax
0000000100000b59        movq    -0x8(%rbp), %rcx
0000000100000b5d        movq    (%rcx,%rax,8), %rax
0000000100000b61        movq    %rax, %rcx
0000000100000b64        shrq    %rcx
0000000100000b67        movabsq $0x5555555555555555, %rdx
0000000100000b71        andq    %rdx, %rcx
0000000100000b74        subq    %rcx, %rax
0000000100000b77        movabsq $0x3333333333333333, %rcx
0000000100000b81        movq    %rax, %rdx
0000000100000b84        andq    %rcx, %rdx
0000000100000b87        shrq    $0x2, %rax
0000000100000b8b        andq    %rcx, %rax
0000000100000b8e        addq    %rax, %rdx
0000000100000b91        movq    %rdx, %rax
0000000100000b94        shrq    $0x4, %rax
0000000100000b98        addq    %rax, %rdx
0000000100000b9b        movabsq $0xf0f0f0f0f0f0f0f, %rax
0000000100000ba5        andq    %rax, %rdx
0000000100000ba8        movabsq $0x101010101010101, %rax
0000000100000bb2        imulq   %rax, %rdx
0000000100000bb6        shrq    $0x38, %rdx
0000000100000bba        movl    %edx, %esi
0000000100000bbc        movl    -0x10(%rbp), %edi
0000000100000bbf        addl    %esi, %edi
0000000100000bc1        movl    %edi, -0x10(%rbp)
0000000100000bc4        movl    -0x14(%rbp), %eax
0000000100000bc7        addl    $0x1, %eax
0000000100000bcc        movl    %eax, -0x14(%rbp)
0000000100000bcf        jmpq    0x100000b49
0000000100000bd4        movl    -0x10(%rbp), %eax
0000000100000bd7        popq    %rbp
0000000100000bd8        ret

```

Well, that's interesting. Clang seems to be calculating things manually rather than usingpopcnt. It seems to be usingthe approach described here, which is something like

```
x = x - ((x >> 0x1) & 0x5555555555555555);
x = (x & 0x3333333333333333) + ((x >> 0x2) & 0x3333333333333333);
x = (x + (x >> 0x4)) & 0xF0F0F0F0F0F0F0F;
ans = (x * 0x101010101010101) >> 0x38;

```

That's not bad for a simple implementation that doesn't rely on any kind of specialized hardware, but that's going to take a lot longer than a singlepopcntinstruction.

I've got a pretty old version of clang (3.0), so let me try this again after upgrading to 3.4, in case they added hardwarepopcntsupport “recently”.

```
0000000100001340        pushq   %rbp         ; save frame pointer
0000000100001341        movq    %rsp, %rbp   ; new frame pointer
0000000100001344        xorl    %ecx, %ecx   ; cnt = 0
0000000100001346        testl   %esi, %esi
0000000100001348        jle     0x100001363
000000010000134a        nopw    (%rax,%rax)
0000000100001350        popcntq (%rdi), %rax ; “eax” = popcnt[rdi]
0000000100001355        addl    %ecx, %eax   ; eax += cnt
0000000100001357        addq    $0x8, %rdi   ; increment address by 64-bits (8 bytes)
000000010000135b        decl    %esi         ; decrement loop counter; sets flags
000000010000135d        movl    %eax, %ecx   ;  cnt = eax; does not set flags
000000010000135f        jne     0x100001350  ; examine flags. if esi != 0, goto popcnt
0000000100001361        jmp     0x100001365  ; goto “restore frame pointer”
0000000100001363        movl    %ecx, %eax
0000000100001365        popq    %rbp         ; restore frame pointer
0000000100001366        ret

```

That's better! We get a hardwarepopcnt! Let's compare this to the SSSE3pshufbimplementationpresented hereas the fastest way to do a popcnt. We'll use a table like the one in the link to show speed, except that we're going to show a rate, instead of the raw cycle count, so that the relative speed between different sizes is clear. The rate is GB/s, i.e., how many gigs of buffer we can process per second. We give the function data in chunks (varying from 1kb to 16Mb); each column is the rate for a different chunk-size. If we look at how fast each algorithm is for various buffer sizes, we get the following.

[Table]

| Algorithm | 1k | 4k | 16k | 65k | 256k | 1M | 4M | 16M |
| Intrinsic | 6.9 | 7.3 | 7.4 | 7.5 | 7.5 | 7.5 | 7.5 | 7.5 |
| PSHUFB | 11.5 | 13.0 | 13.3 | 13.4 | 13.1 | 13.4 | 13.0 | 12.6 |

That's not so great. Relative to the the benchmark linked above, we're doing better because we're using 64-bitpopcntinstead of 32-bitpopcnt, but the PSHUFB version is still almost twice as fast1.

One odd thing is the waycntgets accumulated.cntis stored inecx. But, instead of adding the result of thepopcnttoecx, clang has decided to addecxto the result of thepopcnt. To fix that, clang then has to move that sum intoecxat the end of each loop iteration.

The other noticeable problem is that we only get onepopcntper iteration of the loop, which means the loop isn't getting unrolled, and we're paying the entire cost of the loop overhead for eachpopcnt. Unrolling the loop can also let the CPU extract more instruction level parallelism from the code, although that's a bit beyond the scope of this blog post.

Using clang, that happens even with-O3 -funroll-loops. Using gcc, we get a properly unrolled loop, but gcc has other problems, as we'll see later. For now, let's try unrolling the loop ourselves by calling__builtin_popcountllmultiple times during each iteration of the loop. For simplicity, let's try doing fourpopcntoperations on each iteration. I don't claim that's optimal, but it should be an improvement.

```
uint32_t builtin_popcnt_unrolled(const uint64_t* buf, int len) {
  assert(len % 4 == 0);
  int cnt = 0;
  for (int i = 0; i < len; i+=4) {
    cnt += __builtin_popcountll(buf[i]);
    cnt += __builtin_popcountll(buf[i+1]);
    cnt += __builtin_popcountll(buf[i+2]);
    cnt += __builtin_popcountll(buf[i+3]);
  }
  return cnt;
}

```

The core of our loop now has

```
0000000100001390        popcntq (%rdi,%rcx,8), %rdx
0000000100001396        addl    %eax, %edx
0000000100001398        popcntq 0x8(%rdi,%rcx,8), %rax
000000010000139f        addl    %edx, %eax
00000001000013a1        popcntq 0x10(%rdi,%rcx,8), %rdx
00000001000013a8        addl    %eax, %edx
00000001000013aa        popcntq 0x18(%rdi,%rcx,8), %rax
00000001000013b1        addl    %edx, %eax

```

with pretty much the same code surrounding the loop body. We're doing fourpopcntoperations every time through the loop, which results in the following performance:

[Table]

| Algorithm | 1k | 4k | 16k | 65k | 256k | 1M | 4M | 16M |
| Intrinsic | 6.9 | 7.3 | 7.4 | 7.5 | 7.5 | 7.5 | 7.5 | 7.5 |
| PSHUFB | 11.5 | 13.0 | 13.3 | 13.4 | 13.1 | 13.4 | 13.0 | 12.6 |
| Unrolled | 12.5 | 14.4 | 15.0 | 15.1 | 15.2 | 15.2 | 15.2 | 15.2 |

Between using 64-bitpopcntand unrolling the loop, we've already beaten the allegedly fasterpshufbcode! But it's close enough that we might get different results with another compiler or some other chip. Let's see if we can do better.

So, what's the deal with thispopcnt false dependency bugthat's been getting a lot of publicity lately? Turns out,popcnthas a false dependency on its destination register, which means that even though the result ofpopcntdoesn't depend on its destination register, the CPU thinks that it does and will wait until the destination register is ready before starting thepopcntinstruction.

x86 typically has two operand operations, e.g.,addl %eax, %edxaddseaxandedx, and then places the result inedx, so it's common for an operation to have a dependency on its output register. In this case, there shouldn't be a dependency, since the result doesn't depend on the contents of the output register, but that's an easy bug to introduce, and a hard one to catch2.

In this particular case,popcnthas a 3 cycle latency, but it's pipelined such that apopcntoperation can execute each cycle. If we ignore other overhead, that means that a singlepopcntwill take 3 cycles, 2 will take 4 cycles, 3 will take 5 cycles, and n will take n+2 cycles, as long as the operations are independent. But, if the CPU incorrectly thinks there's a dependency between them, we effectively lose the ability to pipeline the instructions, and that n+2 turns into 3n.

We can work around this by buying a CPU from AMD or VIA, or by putting thepopcntresults in different registers. Let's making an array of destinations, which will let us put the result from eachpopcntinto a different place.

```
uint32_t builtin_popcnt_unrolled_errata(const uint64_t* buf, int len) {
  assert(len % 4 == 0);
  int cnt[4];
  for (int i = 0; i < 4; ++i) {
    cnt[i] = 0;
  }

  for (int i = 0; i < len; i+=4) {
    cnt[0] += __builtin_popcountll(buf[i]);
    cnt[1] += __builtin_popcountll(buf[i+1]);
    cnt[2] += __builtin_popcountll(buf[i+2]);
    cnt[3] += __builtin_popcountll(buf[i+3]);
  }
  return cnt[0] + cnt[1] + cnt[2] + cnt[3];
}

```

And now we get

```
0000000100001420        popcntq (%rdi,%r9,8), %r8
0000000100001426        addl    %ebx, %r8d
0000000100001429        popcntq 0x8(%rdi,%r9,8), %rax
0000000100001430        addl    %r14d, %eax
0000000100001433        popcntq 0x10(%rdi,%r9,8), %rdx
000000010000143a        addl    %r11d, %edx
000000010000143d        popcntq 0x18(%rdi,%r9,8), %rcx

```

That's better -- we can see that the first popcnt outputs intor8, the second intorax, the third intordx, and the fourth intorcx. However, this does the same odd accumulation as the original, where instead of adding the result of thepopcnttocnt[i], it does the opposite, which necessitates moving the results back tocnt[i]afterwards.

```
000000010000133e        movl    %ecx, %r10d
0000000100001341        movl    %edx, %r11d
0000000100001344        movl    %eax, %r14d
0000000100001347        movl    %r8d, %ebx

```

Well, at least in clang (3.4). Gcc (4.8.2) is too smart to fall for this separate destination thing and “optimizes” the code back to something like our original version.

[Table]

| Algorithm | 1k | 4k | 16k | 65k | 256k | 1M | 4M | 16M |
| Intrinsic | 6.9 | 7.3 | 7.4 | 7.5 | 7.5 | 7.5 | 7.5 | 7.5 |
| PSHUFB | 11.5 | 13.0 | 13.3 | 13.4 | 13.1 | 13.4 | 13.0 | 12.6 |
| Unrolled | 12.5 | 14.4 | 15.0 | 15.1 | 15.2 | 15.2 | 15.2 | 15.2 |
| Unrolled 2 | 14.3 | 16.3 | 17.0 | 17.2 | 17.2 | 17.0 | 16.8 | 16.7 |

To get a version that works with both gcc and clang, and doesn't have these extramovs, we'll have to write the assembly by hand3:

```
uint32_t builtin_popcnt_unrolled_errata_manual(const uint64_t* buf, int len) {
  assert(len % 4 == 0);
  uint64_t cnt[4];
  for (int i = 0; i < 4; ++i) {
    cnt[i] = 0;
  }

  for (int i = 0; i < len; i+=4) {
    __asm__(
        "popcnt %4, %4  \n\
        "add %4, %0     \n\t"
        "popcnt %5, %5  \n\t"
        "add %5, %1     \n\t"
        "popcnt %6, %6  \n\t"
        "add %6, %2     \n\t"
        "popcnt %7, %7  \n\t"
        "add %7, %3     \n\t" // +r means input/output, r means intput
        : "+r" (cnt[0]), "+r" (cnt[1]), "+r" (cnt[2]), "+r" (cnt[3])
        : "r"  (buf[i]), "r"  (buf[i+1]), "r"  (buf[i+2]), "r"  (buf[i+3]));
  }
  return cnt[0] + cnt[1] + cnt[2] + cnt[3];
}

```

This directly translates the assembly into the loop:

```
00000001000013c3        popcntq %r10, %r10
00000001000013c8        addq    %r10, %rcx
00000001000013cb        popcntq %r11, %r11
00000001000013d0        addq    %r11, %r9
00000001000013d3        popcntq %r14, %r14
00000001000013d8        addq    %r14, %r8
00000001000013db        popcntq %rbx, %rbx

```

Great! Theadds are now going the right direction, because we specified exactly what they should do.

[Table]

| Algorithm | 1k | 4k | 16k | 65k | 256k | 1M | 4M | 16M |
| Intrinsic | 6.9 | 7.3 | 7.4 | 7.5 | 7.5 | 7.5 | 7.5 | 7.5 |
| PSHUFB | 11.5 | 13.0 | 13.3 | 13.4 | 13.1 | 13.4 | 13.0 | 12.6 |
| Unrolled | 12.5 | 14.4 | 15.0 | 15.1 | 15.2 | 15.2 | 15.2 | 15.2 |
| Unrolled 2 | 14.3 | 16.3 | 17.0 | 17.2 | 17.2 | 17.0 | 16.8 | 16.7 |
| Assembly | 17.5 | 23.7 | 25.3 | 25.3 | 26.3 | 26.3 | 25.3 | 24.3 |

Finally! A version that blows away thePSHUFBimplementation. How do we know this should be the final version? We can see fromAgner's instruction tablesthat we can execute, at most, onepopcntper cycle. I happen to have run this on a 3.4Ghz Sandy Bridge, so we've got an upper bound of8 bytes / cycle * 3.4 G cycles / sec = 27.2 GB/s. That's pretty close to the26.3 GB/swe're actually getting, which is a sign that we can't make this much faster4.

In this case, the hand coded assembly version is about 3x faster than the original intrinsic loop (not counting the version from a version of clang that didn't emit apopcnt). It happens that, for the compiler we used, the unrolled loop using thepopcntintrinsic is a bit faster than thepshufbversion, but that wasn't true of one of the two unrolled versions when I tried this withgcc.

It's easy to see why someone might have benchmarked the same code and decided thatpopcntisn't very fast. It's also easy to see why using intrinsics for performance critical code can be a huge time sink5.

Thanks toScottfor some comments on the organization of this post, and toLeahfor extensive comments on just about everything

If you liked this, you'll probably enjoythis post about how CPUs have changed since the 80s.

---

1. see thisfor the actual benchmarking code. On second thought, it's an embarrassingly terrible hack, and I'd prefer that you don't look.[return]
2. If it were the other way around, and the hardware didn't realize there was a dependency when there should be, that would be easy to catch -- any sequence of instructions that was dependent might produce an incorrect result. In this case, some sequences of instructions are just slower than they should be, which is not trivial to check for.[return]
3. This code is a simplified version ofAlex Yee's stackoverflow answer about the popcnt false dependency bug[return]
4. That's not quite right, since the CPU has TurboBoost, but it's pretty close. Putting that aside, this example is pretty simple, but calculating this stuff by hand can get tedious for more complicated code. Luckily, theIntel Architecture Code Analyziercan figure this stuff out for us. It finds the bottleneck in the code (assuming infinite memory bandwidth at zero latency), and displays how and why the processor is bottlenecked, which is usually enough to determine if there's room for more optimization.You might have noticed that the performance decreases as the buffer size becomes larger than our cache. It's possible to do a back of the envelope calculation to find the upper bound imposed by the limits of memory and cache performance, but working through the calculations would take a lot more space this this footnote has available to it. You can see a good example of how do it for one simple casehere. The comments by Nathan Kurz and John McCaplin are particularly good.[return]
5. In the course of running these benchmarks, I also noticed that_mm_cvtsi128_si64produces bizarrely bad code on gcc (although it's fine in clang)._mm_cvtsi128_si64is the intrinsic for moving an SSE (SIMD) register to a general purpose register (GPR). The compiler has a lot of latitude over whether or not a variable should live in a register or in memory. Clang realizes that it's probably faster to move the value from an SSE register to a GPR if the result is about to get used. Gcc decides to save a register and move the data from the SSE register to memory, and then have the next instruction operate on memory, if that's possible. In ourpopcntexample, clang uses about 2x for not unrolling the loop, and the rest comes from not being up to date on a CPU bug, which is understandable. It's hard to imagine why a compiler would do a register to memory move when it's about to operate on data unless it either doesn't do optimizations at all, or it has some bug which makes it unaware of the register to register version of the instruction. But at least it gets the right result,unlike this version of MSVC.icc and armcc are reputed to be better at dealing with intrinsics, but they're non starters for most open source projects. Downloading icc's free non-commercial version has been disabled for the better part of a year, and even if it comes back, who's going to trust that it won't disappear again? As for armcc, I'm not sure it's ever had a free version?[return]
