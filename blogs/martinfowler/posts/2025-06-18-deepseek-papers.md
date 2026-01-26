---
title: "The DeepSeek Series: A Technical Overview"
description: "The appearance of DeepSeek Large-Language Models has caused a lot of   discussion and angst since their latest versions appeared at the beginning of 2025. But   much of the value of DeepSeek's work co"
date: 2025-06-18T00:00:00
tags: ["generative ai"]
url: https://martinfowler.com/articles/deepseek-papers.html
slug: deepseek-papers
word_count: 3423
---


This article provides a cohesive overview of four technical reports from
    DeepSeek:

1. [DeepSeek-LLM](https://arxiv.org/abs/2401.02954v1) *(Jan '24)*: an early
      investigation of scaling laws and data-model tradeoffs.
2. [DeepSeek-V2](https://arxiv.org/abs/2405.04434) *(Jun '24)*: introducing
      Multi-Head Latent Attention (MLA) and DeepSeekMoE to improve memory and
      training efficiency.
3. [DeepSeek-V3](https://arxiv.org/abs/2412.19437) *(Dec '24)*: scaling sparse MoE networks to 671B
      parameters, with FP8 mixed precision training and intricate HPC co-design
4. [DeepSeek-R1](https://arxiv.org/abs/2501.12948) *(Jan '25)*:
      building upon the efficiency foundations of the previous papers and using
      *large-scale reinforcement learning* to incentivize emergent
      chain-of-thought capabilities, including a âzero-SFTâ variant.


For additional context on DeepSeek itself and the market backdrop that
    has caused claims made by the DeepSeek team to be taken out of context and
    spread widely, please take a look at my colleague Prasanna Pendse's post:
    [Demystifying Deepseek](https://www.thoughtworks.com/insights/blog/generative-ai/demystifying-deepseek). For the purposes of
    this article, we'll be focusing analysis and commentary on the technical
    work itself, its merits, and what it may signal for the future.


Much of this article assumes significant knowledge of the terminology and
    concepts of building LLMs, more so than is typical for articles on this
    site. In future weeks we hope to expand this article to provide explanations
    of these concepts to make this article easier to follow for those not
    familiar with this world. We shall post any such updates on this site's
    [usual channels](https://martinfowler.com/recent-changes.html).


All four papers revolve around a *singular challenge*: building
    ever-larger language models with minimal cost, memory overhead, and training
    instability. In each iteration, the authors refine both *architecture* and
    *infrastructure* - a strategy often referred to as *HPC co-design*.


Key arcs in this series include:

- **Cost and Memory Efficiency:** Methods like Multi-Head Latent Attention
      (MLA) compression, mixture-of-experts (MoE), and FP8-based optimizations all aim
      to make massive-scale training and inference feasible.
- **Sparsity + HPC Co-Design:** From V2 to V3, we see mixture-of-experts
      architecture evolve alongside specialized HPC scheduling—allowing 671B-parameter
      models to be trained on H800 clusters without blowing up the budget.
- **Emergent Reasoning:** In R1, large-scale Reinforcement Learning (RL)
      unlocks advanced chain-of-thought capabilities, culminating in “R1-Zero” and its
      purely RL-driven approach to reasoning tasks.


## DeepSeek-LLM: Laying the Foundation


### Motivation & Overview


The authors set out to answer an important question: Given a fixed
        compute budget for pre-training, how do we choose the scale of the model
        and how much training data to use? Prior studies (e.g. Chinchilla vs.
        GPT-3) differed on the ratio between these two factors. DeepSeek-LLM
        addresses that by measuring scale in a different way. Earlier work
        measured scale in terms of how many parameters were in the model,
        DeepSeek-LLM instead measured scale as *non-embedding FLOPs/token*1 They then found they could predict
        computation with:


1: Non-embedding FLOPs are the amount of FLOPs (Floating
        Point Operations per Second) used for pre-training certain layers of the transformer
        (non-embedding). The authors found only some layers contributed to the
        scaling formula.


$$
          C = M \times D
        $$


where $C$ is the compute budget, $M$ is non-embedding
        FLOPs/token, and $D$ is data size.


This more granular representation helps them predict how a 7B or 67B model
        might train on 2T tokens of bilingual data.


### Training Instability


A central concern they grapple with is training instability (sudden irrecoverable 
        divergences in the training process), which can often manifest in 
        large-scale language models—especially those with mixture-of-experts 
        or very long contexts.


By carefully tuning learning rates, batch sizes, and other
        hyperparameters 2, DeepSeek-LLM
        demonstrates that stable large-scale training is achievable, but it
        requires meticulous design of the architecture of the transformer model
        together with the infrastructure of the High Performance Computing (HPC)
        data center used to train it. This interwoven design of both architecture and
        infrastructure is called **HPC Co-Design**.


2: A model consists of billions of internal
        variables, which are called its *parameters*. These parameters gain
        their values (weights) during training. Before training, developers will
        set a number of different variables that control the training process
        itself, these are called *hyperparameters*.


### Data Quality & Model Scale


A point the authors make is about how data quality shifts the optimal
        ratio—i.e., *higher-quality data can justify a bigger model for the same
        number of tokens*. You can intuit this by imagining two scenarios:

- Scenario A: You have a 100-billion-token corpus full of duplicates,
          spammy text, or incomplete sentences. The model might not glean much new
          knowledge because the data is partly redundant or low-value.
- Scenario B: You have a carefully curated 100-billion-token corpus with
          broad coverage of code, math, multi-lingual dialogues, factual text, etc. Each
          token is more “information-rich,” so the model can “afford” to use more
          parameters without hitting diminishing returns prematurely.


In other words, when data is denser in useful information, scaling the
        model further pays off because each parameter can learn from richer
        signals.


### Key Takeaways

- Hyperparameter Scaling: They propose simple power-law fits to pick batch
          size and learning rate as compute $C$ grows.
- Bilingual Data: They train two base sizes (7B, 67B) on 2T tokens
          covering English/Chinese, then do Supervised Fine Tuning (SFT) and a simpler
          preference-based alignment called *Direct Preference Optimization (DPO)*.
- Results: The resulting DeepSeek-LLM67B âOutperforms LLaMA-2 70Bâ on
          math/coding tasks, illustrating how HPC co-designed approaches can keep training
          stable while efficiently pushing scale.


The seeds planted here - scaling laws and infrastructure for extremely large
        training - will reappear in subsequent works.


## DeepSeek-V2: Multi-Head Latent Attention & MoE


### Expanding the Model While Reducing Memory


Where DeepSeek-LLM mostly explored high-level scale tradeoffs,
        DeepSeek-V2 dives into specifics of Transformer architecture overhead. Two
        big obstacles in large LLMs are:

1. Attention KV Cache: Storing Key/Value vectors for thousands of tokens
          is memory-intensive.
2. Feed-Forward Computation: Typically the largest consumption of FLOPs
          in a Transformer.


To tame both, they propose:

1. Multi-Head Latent Attention (MLA): compresses Key/Value vectors to
          reduce memory.
2. DeepSeekMoE: a sparse Mixture-of-Experts approach that
          activates a fraction of the feed-forward capacity per token.


### Multi-Head Latent Attention (MLA)


**Attention** is the process by which the model decides
        which tokens in the input stream to pay attention to when it's trying to
        predict the next token. In standard attention, each token's Q/K/V3 
        can be as large as $d_{model}$4 times the 
        number of heads5. MLA folds them into smaller âlatentâ
        vectors:


3:  Q/K/V stand for “Query,” “Key,” and “Value” vectors. At each layer, 
        the model uses learned linear transformations to produce these vectors from 
        the hidden states of the input. The attention mechanism then computes 
        similarities between Q and K to decide how much of each Value vector to incorporate.


4: $d_{model}$ is the dimension of the model’s hidden representation. You 
        can think of this hidden representation as the internal “space” in which the 
        model’s computations occur. A larger dimension can capture richer and more 
        complex patterns, though at increased computational and memory cost.


5:  In multi-head attention, a *head* is a parallel attention mechanism with 
        its own parameters. From a software-engineering perspective, each head is a 
        distinct transform that runs in parallel with the others, letting the model attend 
        to different aspects of the input simultaneously.


$$
          \quad
          \mathbf{c}_{t}^{KV} = W^{DKV}\mathbf{h}_t,
          \quad
          \mathbf{k}_{t}^{C} = W^{UK}\mathbf{c}_t^{KV},
          \quad
          \mathbf{v}_{t}^{C} = W^{UV}\mathbf{c}_t^{KV},
          \quad
        $$


Where $c_{t}^{KV}$ is the compressed latent vector for keys and values.
        $W^{DKV}$ is the down-projection matrix, and $W^{UK}, W^{UV}$ are the
        up-projection matrices for keys and values, respectively. In simpler terms:

1. Replaces the standard QKV computation by using low rank factorization to
          turn one matrix of dim (*in, out*) into two matrices of (*in, rank*) and
          (*rank, out*)
2. Project the compressed KV latent vector for each head to get the full K
          and V head corresponding to each Q head
3. Cache the compressed KV latent vector instead of each of the KV heads in
          full, and compute the KV heads on the fly from the latent vector.


### DeepSeekMoE: Sparsely Activated FFNs


Next, they adopt a Mixture-of-Experts (MoE) in the feed-forward
        blocks. **Mixture-of-Experts (MoE)** is a design technique that logically
        splits the model into separate areas (experts) each having specialized parameters 
        for different domains of knowledge. Because each token is only routed to the experts 
        most relevant to it, MoE can drastically reduce the compute required compared to a fully 
        dense approach. This approach ties directly into the HPC co-design arc, as each expert 
        can reside on different GPU devices. By limiting cross-device communication 
        (e.g., device-limited routing), MoE effectively scales to extremely large parameter 
        counts without incurring prohibitive memory or data-transfer costs.


DeepSeek uses more fine-grained experts than previous models, dividing them into
        two kinds:

- *Shared Experts* handle universal patterns for every token.
- *Routed Experts* handle specialized sub-problems, chosen dynamically via
          gating.


During training, they consider *Auxiliary Loss* to ensure
        balanced usage so no expert collapses (i.e. is never used).


They further limit cross-device6 routing with 
        a âdevice-limited routingâ scheme - instead of allowing any token to access any expert, 
        DeepSeekMoE selects a limited number of devices ($M$) per token, and performs expert
        selection only within these devices. The basic process is as
        follows:


6:  Here, a *device* usually means a single GPU (or specialized accelerator). Large-scale 
        training typically distributes the model across many devices in a cluster to handle 
        computation and memory constraints.

- Identify top $M$ devices that contain experts with the highest affinity
          to the token
- Perform top $K_r$ expert selection within these $M$ devices
- Assign the selected experts to process the token


Without device-limited routing, MoE models can generate excessive
        communication overhead which is incompatible with the hardware limitations
        imposed on the DeepSeek team. In addition, MoE models typically risk uneven
        expert utilization, where some experts are overused while others remain
        inactive. To prevent this, DeepSeekMoE introduces three balancing loss
        functions:

- Expert-level Balance Loss ($L_{ExpBal}$):
- Device-level Balance Loss ($L_{DevBal}$):
- Communication Balance Loss ($L_{CommBal}$):


### Training & Outcomes


DeepSeek-V2, with ~236B total params (21B activated), is pre-trained on
        8.1T tokens. They do Supervised Fine Tuning (SFT) on 1.5M instruction samples,
        then reinforcement learning (RL) for alignment7. The end result:


7:  Alignment refers to techniques (like supervised fine-tuning or reinforcement 
        learning) that steer the model toward producing responses considered correct, 
        helpful, or safe within certain guidelines or objectives.

- Inference and training are both faster and cheaper (MLA + sparse
          experts)
- They remain stable at scale


This paper is really when iteration gains due to HPC Co-Design start to
        become apparent. By designing the model architecture with the training
        infrastructure in mind, and implementing a training regime that considers the
        realities of the hardware (e.g. low interconnect speeds on H800s), the team
        was able to lay the foundation for their most notable breakthrough.


## DeepSeek-V3: HPC Co-Design


### Scaling MoE to 671B While Preserving Efficiency


Building on V2, DeepSeek-V3 further extends sparse models to *671B*
        parameters (*37B activated*), training on 14.8T tokens in under **2.8M H800
        GPU hours**. The authors credit extensive HPC co-design:


> Lastly, we emphasize again the economical training costs of
>           DeepSeek-V3, summarized in Table 1, achieved through our optimized
>           co-design of algorithms, frameworks, and hardware.
> -- [DeepSeek-V3 Tech. Report, p.5](https://arxiv.org/abs/2412.19437)


The major novelties are:

1. Refined MLA
2. Refined DeepSeekMoE
3. Co-Designed Training & Inference
          Frameworks


### Refined MLA


Multi-Head Latent Attention was introduced in V2 to reduce KV cache overhead.
        In V3, it is further refined with several new features:

- **Improved RoPE Handling**: V2 only partially decoupled keys8, but V3 extends
          the concept for more stable 128K context. They track a “decoupled shared key”
          that reduces numerical drift9 in extremely long generations.
- **Joint KV Storage**: V2 stored compressed keys and values separately. V3
          merges them into a shared compressed representation to further reduce memory
          traffic during multi-node inference10.
- **Layer-Wise Adaptive Cache**: Instead of caching *all* past tokens for all
          layers, V3 prunes older KV entries at deeper layers. This helps keep memory
          usage in check when dealing with 128K context windows.


Together, these MLA refinements ensure that while DeepSeek-V3 can attend across *very* long sequences, 
        the memory overhead remains manageable. While many popular LLMs cap out around 4K to 32K tokens, 128K pushes 
        that envelope significantly, enabling the model to process or reference an entire large document in a single pass. 
        This bigger context window puts added pressure on GPU memory—hence the importance of refining MLA 
        to keep overhead in check.


### Refined DeepSeekMoE: Auxiliary-Loss-Free, Higher Capacity


On the MoE side, DeepSeek-V3 drops the auxiliary-loss approach from V2.
        Instead of an explicit penalty term, each expert acquires a dynamic bias
        $b_i$. If an expert is overloaded at a step, $b_i$ decreases; if
        underloaded, $b_i$ increases. The gating decision then adds $b_i$ to the
        token's affinity:


$$
          s'_{i,t} = s_{i,t} + b_i
        $$


Key Improvements:

- **No Token Dropping**: V2 occasionally dropped tokens if certain experts got
          overloaded, but the new bias-based method keeps everything.
- **More Activated Experts**: They raise the number of routed experts from 6
          to 8 per token, improving representational power.
- **Higher Stability**: By removing auxiliary losses, they avoid potential
          interference with the main training objective, focusing purely on the
          *intrinsic* gating signals plus bias adjustments11.


Hence, the final feed-forward module is a combination of a small set of
        shared experts plus up to 8 specialized experts chosen adaptively.


### Co-Designed Frameworks: FP8, DualPipe, and PTX Optimizations


Scaling an MoE model to 671B demanded HPC-level solutions for training and
        inference. The authors emphasize:


> Through the co-design of algorithms, frameworks, and hardware, we
>         overcome the communication bottleneck in cross-node MoE training, achieving
>           near-full computation- communication overlap.
> -- [DeepSeek-V3 Tech. Report, p.5](https://arxiv.org/abs/2412.19437)


**FP8 Mixed Precision**


They adopt an FP8 data format for General Matrix Multiplications (GEMMs),
        halving memory. The risk is *reduced numeric range* so they offset it
        with:

- Block-wise scaling (e.g., 1x128 or 128x128 tiles).
- Periodic âpromotionâ to FP32 after short accumulation intervals to avoid
          overflow/underflow.


**DualPipe Parallelism**


They propose **DualPipe** to overlap forward/backward computation with the MoE
        all-to-all dispatch. It rearranges pipeline stages to ensure that network
        communication (particularly across InfiniBand12) is hidden behind local matrix
        multiplications.


12: InfiniBand is a high-speed, low-latency network interconnect often used in HPC clusters. 
        “Hiding” network traffic behind other computations means overlapping communication with local GPU operations 
        so that data transfer time has minimal impact on the total runtime.


**PTX-Level & Warp Specialization**


To fully exploit InifiniBand(IB) and NVLink:

- They tune *warp-level*13 instructions in PTX (a level lower than CUDA),
          auto-tuning the chunk size for all-to-all dispatch.
- They dynamically partition Streaming Microcontrollers into communication vs.
          compute tasks so that token dispatch never stalls local GEMM14.


As a result, training costs were cut to 2.8M H800 GPU hours per run - low
        for a 14.8T token corpus.


### Outcomes


The resulting DeepSeek-V3 excels at code, math, and some multilingual
        tasks, outperforming other open-source LLMs of similar scale. Deep HPC
        co-design (FP8, DualPipe, PTX-level optimization) plus refined MLA/MoE
        implementation achieve *extreme* scale with stable training.


## DeepSeek-R1: Reinforcement Learning for Deeper Reasoning


It's worth noting that both DeepSeek R1 and DeepSeek R1-Zero are
      architecturally identical to DeepSeek V3. They both take the pre-trained
      base model of V3 and apply differing amounts of post-training.


### Emergent Reasoning Behaviors Through RL-Only


All prior DeepSeek releases used Supervised Fine-Tuning (SFT), plus
        occasional Reinforcement Learning (RL). By contrast,
        DeepSeek-R1-Zero tries an extreme: *no supervised warmup*, just RL from
        the base model. They adopt Group Relative Policy Optimization (GRPO),
        which:

1. Samples a group of old-policy outputs ${o_1, ..., o_G}$
2. Scores each with a reward (in this case, rule-based)
3. Normalizes the advantage $A_i$ by group mean/stdev
4. Optimizes a clipped PPO-like objective15


The reward function for the R1 models is rule-based - a simple weighted
        sum between 2 components

- *Accuracy Reward* - if the task has an objective correct answer (e.g. a
          math problem, coding task, etc.), correctness is verified using mathematical
          equation solvers for step-by-step proof checking, and code execution & test
          cases for code correctness verification
- *Format Reward* - the model is rewarded for following a structured
          reasoning process using explicit reasoning markers `<think></think>` and
          `<answer></answer>`


The relative advantage $A_i$ for a given output is calculated as:


$$
          A_i = \frac{r_i - mean(\{r_1, r_2, ..., r_G\})}{std(\{r_1, r_2, ..., r_G\})}
        $$


where $r_i$ is the reward calculated for the given output. The model's
        policy is updated to favor responses with higher rewards while constraining
        changes using a clipping function which ensures that the new policy remains
        close to the old.


In so many words: the authors created a testing/verification harness around
        the model which they exercised using reinforcement learning, and gently guided
        the model using simple Accuracy and Format rewards. In doing so, emergent
        reasoning behaviors were observed:

- **Self-verification** where the model double-checks its own answers
- **Extended chain-of-thought** where the model learns to explain its
          reasoning more thoroughly
- **Exploratory reasoning** - the model tries different approaches before
          converging on an answer
- **Reflection** - the model starts questioning its own solutions and
          adjusting reasoning paths dynamically


R1-Zero is probably the most interesting outcome of the R1 paper for
        researchers because it learned complex chain-of-thought patterns from raw reward
        signals alone. However, the model exhibited notable issues:

- **Readability Problems**: Because it never saw any human-curated language
          style, its outputs were sometimes jumbled or mixed multiple languages.
- **Instability in Non-Reasoning Tasks**: Lacking SFT data for general
          conversation, R1-Zero would produce valid solutions for math or code but be
          awkward on simpler Q&A or safety prompts.
- **Limited Domain**: Rule-based rewards worked well for verifiable tasks
          (math/coding), but handling creative/writing tasks demanded broader
          coverage.


Hence, the authors concluded that while “pure RL” yields strong reasoning
        *in verifiable tasks*, the model’s overall user-friendliness was lacking. This
        led them to **DeepSeek-R1**: an alignment pipeline combining small cold-start
        data, RL, rejection sampling, and more RL, to “fill in the gaps” from R1-Zero’s
        deficits.


### Refined Reasoning Through SFT + RL


DeepSeek-R1 addresses R1-Zero's limitations by injecting a small amount
        of supervised data before RL and weaving in additional alignment steps.


#### Stage 1: “Cold-Start” SFT


They gather a small number (~thousands) of
          curated, “human-friendly” chain-of-thought data covering common sense Q&A,
          basic math, standard instruction tasks, etc. Then, they do a short SFT pass on
          the base model. This ensures the model acquires:

- Better readability: Polished language style and formatting.
- Non-reasoning coverage: Some conversation, factual QA, or creative tasks
            not easily rewarded purely by rule-based checks.


In essence, the authors realized you can avoid the “brittleness” of a
          zero-SFT approach by giving the model a *seed* of user-friendly behaviors.


#### Stage 2: Reasoning-Oriented RL


Next, as in R1-Zero, they apply large-scale RL for tasks like math and
          code. The difference is that now the model starts from a “cold-start SFT”
          checkpoint—so it retains decent language style while still learning verifiable
          tasks from a rule-based or tool-based reward. This RL stage fosters the same
          emergent chain-of-thought expansions but *without* the random “language
          mixing” or bizarre structure.


#### Stage 3: Rejection Sampling + Additional SFT


Once that RL converges, they generate multiple completions per prompt from
          the RL checkpoint. Using a combination of automatic verifiers and some human
          checks, they pick the best outputs (“rejection sampling”) and build a new SFT
          dataset. They also incorporate standard writing/factual/safety data from
          DeepSeek-V3 to keep the model balanced in non-verifiable tasks. Finally, they
          re-fine-tune the base model on this curated set.


This step addresses the “spotty coverage” problem even further: The best RL
          answers become training targets, so the model improves at chain-of-thought
          *and* clarity.


#### Stage 4: RL for “All Scenarios”


Lastly, they do another RL pass on diverse prompts—not just math/code but
          general helpfulness, safety, or role-playing tasks. Rewards may come from a
          combination of rule-based checks and large “preference” models (trained from
          user preference pairs). The final result is a model that:

- Retains strong chain-of-thought for verifiable tasks,
- Aligns to broad user requests in everyday usage,
- Maintains safer, more controlled outputs.


## Connecting the Arcs: Efficiency & Emergence


Despite covering different angles - scaling laws, MoE, HPC scheduling, and
      large-scale RL - DeepSeek's work consistently follows these arcs:

1. **Cost and Memory Efficiency**
2. **Sparse + HPC Co-Design**
3. **Emergent Reasoning**


Taken as a whole, the DeepSeek series highlights how architecture,
      algorithms, frameworks, and hardware must be co-designed to handle LLM
      training at trillion-token scales. Looking to the future, it indicates that
      toolchain builders may want to find ways to capture some of these HPC
      optimizations as part of the model compilation path or training apparatus,
      and AI research teams may want to work closely with HPC expertise even in
      the early days of architecture ideation.


---
