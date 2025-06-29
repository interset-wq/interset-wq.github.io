---
comments: true
# status: new
title: 概率统计-概率论
# pdf: true
---

:material-pen-plus: `本文创建于2025-5-1`

## 第一章 随机事件与概率 

??? info "预备知识"
    - **加法原理** 如果完成某件事有 $m$ 种途径,  每种途径有 $n_i (i=1,  2,  ...,  m)$ 种不同的方法,  那么完成该件事共有 $n_1 + n_2 + ... + n_m$ 种不同的方法．
    - **乘法原理** 如果完成某件事须经过 $m$ 个步骤,  而完成每个步骤分别有 $n_i$ 种不同的方法,  那么完成该件事共有 $n_1 \times n_2 \times ... \times n_m$ 种不同的方法．
    - **重复排列** 从 $n$ 个不同的元素中任意取出 $r$ 个元素$(1 ≤ r ≤ n)$,  按照一定顺序允许重复出现排成一列,  称为从 $n$ 个元素取出 $r$ 个元素的重复排列,  排列总数为 $n^r$． 
    - **选排列** 从 $n$ 个不同的元素中任取出 $r$ 个$(1 ≤ r ≤ n)$元素按照一定顺序不重复地排成一列,  称为从 $n$ 个元素中取出 $r$ 个元素的选排列,  记为 $A_n ^r$,  且有 $A_n ^r = \frac{n!}{(n-r)!}$．
    - **全排列** $r = n$ 的选排列称为全排列,  记为 $P_n$ , 且有 $P_n = n!$.
    - **组合** 从 $n$ 个不同的元素中任意取出 $r$ 个$(0 ≤ r ≤ n)$元素组成一组(不考虑次序),  称为从 $n$ 个元素中取出 $r$ 个元素的一个组合,  记为 $C_n ^r$ , 且有 $C_n ^r = \frac{A_n ^r}{P_r}= \frac{n!}{(n-r)! \cdot r!}$.

### 1.1  随机事件及其运算 

#### 1.1.1 确定性现象与不确定性现象

- **确定性现象** 例如：每天早晨太阳从东方升起；水在标准大气压下加温到100℃沸腾
- **不确定性现象(随机现象)** 例如：掷一枚硬币,  正面朝上还是反面朝上,  一天内进入某超市的顾客数

**随机现象的统计规律性** 随机现象的各种结果会表现出一定的规律性,  这种规律性称之为统计规律性． 

**随机试验**$E$ 对随机现象进行观察或试验．

- 可重复进行
- 结果有多个
- 每一次试验的结果是不可预言的,  但所有可能结果试验前已知

**样本空间**$\varOmega$ 由随机试验的一切可能结果组成的一个集合$\varOmega$．其每个元素称为样本点$\omega$．

??? question "例题——样本空间"
    写出下列试验的样本空间．

    - $E_1$ ：将一枚硬币连抛两次,  考虑正反面出现的情况；$\varOmega$ = {(正, 正) ,  (正, 反) ,  (反, 正) ,  (反, 反)}
    - $E_2$ ：掷一颗均匀骰子,  考虑可能出现的点数；$\varOmega$ = { 1,  2,  3,  4,  5,  6 }
    - $E_3$ ：记录某网站一分钟内受到的点击次数；$\varOmega = \{ 1,  2,  ... \}$
    - $E_4$ ：任选一人,  记录他的身高(m)和体重(kg)．$\varOmega = \{ (h, g) | 0 < h < 3,  \space 0 < g < 400 \}$

???+ warning
    - 样本空间是一个集合
    - 对于一个随机试验而言,  样本空间并不唯一
   
    ???+ example 
        掷两枚均匀的骰子一次

        - 若实验的目的是观察所有可能出现的结果 $\varOmega _1$ = { (1,  1),  ...,  (1,  6),  ...,  (6,  1),  ...,  (6,  6) }
        - 若试验目的是观察出现的点数和 $\varOmega _2 = \{ 2,  3,  4,  ...,  12 \}$

**随机事件** 样本空间 $\varOmega$ 的某个子集．用A,  B,  C等字母表示

??? example
    在掷骰子试验中,  事件A：出现偶数点,  则$A = \{ 2,  4,  6 \}$

- 基本事件：由一个样本点构成的集合
- 复合事件：由多个样本点构成的集合

**事件的发生**  $A$ 发生 $\Longleftrightarrow$ A 所包含的某一个样本点出现

**必然事件** $\varOmega$ 与 **不可能事件** $\varnothing$

{==事件之间的关系==}

???+ success inline end
    ![pro1.webp](https://s2.loli.net/2025/06/03/aEbp2n6lcPLXHVJ.webp)

    ![pro2.webp](https://s2.loli.net/2025/06/03/WN6GmT7h9SRepVw.webp)

- **事件的包含** A 发生必然导致B发生,  则称 A 包含于 B ,  记为 $A \subset B$
- **事件的相等** $A = B$
- **事件的互斥 (互不相容)** A 与 B 不能同时发生,  则称 A 与 B互斥．即 $AB = \varnothing$

    ???+ warning
        - 基本事件之间是互斥的
        - $\varnothing$与任何事件互斥 

---

#### 1.1.2 事件的运算

???+ success inline end
    ![pro3.webp](https://s2.loli.net/2025/06/03/jBXdz5f4koJFqUu.webp)
        
    ![pro4.webp](https://s2.loli.net/2025/06/03/ngx8VkjlemBvh9y.webp)

    ![pro5.webp](https://s2.loli.net/2025/06/03/LsYGebhV6iaP2qg.webp)

- **并 (和)** $A,  B$ 中至少有一个发生的事件．即 $A \cup B = \{ \omega | \omega \in A 或 \omega \in B \}$
- **交 (积)** $A ,  B$ 同时发生的事件．即 $A \cap B = AB = \{ \omega | \omega \in A 且 \omega \in B \}$

    ???+ note
        和、积运算可推广到有限个和可列无穷多个的情形． 

- **差** A发生而B不发生的事件,  称为A与B的差．即$A - B = \{ \omega | \omega \in A 且 \omega \notin B \}$

    ???+ note "推论"
        - $A - B = A - AB$
        - 若A,  B互斥,  则$A - B = A,  B- A = B$
        - $A - (B-C) \not ={A - B + C}$

- **逆 (对立事件)** 若A与B满足 $A \cup B = \varOmega$,  且 $AB = \varnothing$,  称 A与B互逆．

    ???+ warning
        - 事件互斥与互逆(对立事件)的区别: 互斥两事件之和不一定是 $\varOmega$,  对立事件之和为 $\varOmega$
        - $A - B = A \overline{B}$

#### 1.1.3 事件的运算律

???+ success inline end
    ![pro3.webp](https://s2.loli.net/2025/06/03/jBXdz5f4koJFqUu.webp)

- 交换律、结合律
- 分配律
    - $A \cup (B \cap C) = (A \cup B) \cap (A \cup C) = (A \cup B)(A \cup C)$
    - $A \cap (B \cup C) = (A \cap B) \cup (A \cap C) = AB \cup AC$
- 对偶律
    - $\overline{ A \cup B } = \overline{A} \cap \overline{B} = \bar{A} \bar{B}$ (和的逆=逆的积)
    - $\overline{ A \cap B } = \overline{AB} = \overline{A} \cup \overline{B}$ (积的逆=逆的和) 

??? question "事件的运算"
    用A、B、C的运算关系表示下列各事件：

    - 三个事件中至少一个发生： $A \cup B \cup C$
    - 没有一个事件发生： $\bar{A} \bar{B} \bar{C} = \overline{A \cup B \cup C}$
    - 恰有一个事件发生： $A \bar{B} \bar{C} \cup \bar{A} B \bar{C} \cup \bar{A} \bar{B} C$
    - 至多有两个事件发生：$\overline{ ABC } = \bar{A} \cup \bar{B} \cup \bar{C}$(考虑其对立事件)
    - 至少有两个事件发生： (由对偶律)$AB \bar{C} \cup A \bar{B} C \cup \bar{A} BC \cup ABC = AB \cup BC \cup CA$

### 1.2  随机事件的概率 

**频率** 在相同的条件下重复进行了 $N$ 次试验,  若 $A$ 发生了 $\mu$ 次,  则称 $F_N(A) = \frac{\mu}{N}$ 为 $A$ 在 $N$ 次试验中出现的频率．

**概率的统计定义** 独立重复地做 $N$ 次试验,  当 $N$ 很大时,  若事件 $A$ 发生的频率稳定地在某一数值 $p$ 附近摆动,  则称 $p$ 为 $A$ 发生的概率．

???+ warning
    概率是确定的,  而频率与试验次数有关． 

#### 1.2.1 古典概率

**古典型随机试验**

- 有限性
- 等可能性

古典概率的定义：古典型试验的样本空间为 $\varOmega = \{ \omega _1,  \omega _2,  ...,  \omega _n \}$,  若事件A中含有 $k(k \le n)$个样本点,  则称 $\frac{k}{n}$为 A发生的概率,  记为
$$
P(A) = \frac{k}{n} = \frac{A中的样本点个数}{\varOmega 中的样本点个数}
$$

???+ note "古典概率的性质"
    - 非负性：对任意A,  $P(A) \ge 0$
    - 规范性：$P(\varOmega) = 1$
    - 可加性：若A和B互斥,  则 $P(A \cup B) = P(A) + P(B)$
    - $P(\varnothing)= 0$
    - $P(\bar{A}) = 1 - P(A)$
 
#### 1.2.2 几何概率

**几何型随机试验：**

- 无限性
- 等可能性

几何概率的定义：在几何型随机试验中,  定义事件$A$发生的概率为  
$$
P(A) = \frac{A的测度(长度,  面积,  体积)}{\varOmega 的测度(长度,  面积,  体积) }
$$

???+ example "会面问题" 
    ???+ success inline end
        ![meet.webp](https://s2.loli.net/2025/06/03/MX7zAY4kUGcQ9V8.webp)

    两人相约7点到8点在某地会面,  先到者等候另一人20分钟后就可离去,  试求这两人能会面的概率．

    **解** 以 x,  y分别表示两人到达时刻 (7点设为零时刻),  则会面的充要条件 为 $| x - y | \leq 20$,  这是一几何概率问题,   可能的结果全体是边长为60的正方形里的点,  能会面的点为图中阴影部分,  所求概率

    $$
    P = \frac{60^2 - 40^2}{60^2} = \frac{5}{9}
    $$

#### 1.2.3 概率的性质

- **有限可加性** (可推广到可列可加性) 设 $A_1 ,  A_2 ,  ...,  A_n$ 是 $n$ 个两两互不相容的事件,  即 $A_i A_j = \varnothing ,  \space i \not ={j} \space , i, j = 1,  2,  ...,  n$,  则有$P(A_1 \cup A_2 \cup ... \cup A_n) = P(A_1) + P(A_2) + ... + P(A_n)$
- **事件差** A,  B 是两个事件,  则 $P(A - B) = P(A) - P(AB)$
- **单调性** 若事件$A \supset B$ ,  则 $P(A) \ge P(B)$
- **加法公式** 对任意两事件A,  B,  有 $P(A \cup B) = P(A) + P(B) - P(AB)$

    ???+ note "推广"
        推广到任意 n 个事件 $A_1 ,  A_2 ,  ...,  A_n$ 的情形．
        
        $P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(AB) - P(BC) - P(AC) + P(ABC)$

- **互补性** $P(\bar{A}) = 1 - P(A)$
- **可分性** 对任意两事件 A,  B,  有 $P(A) = P(AB) + P(A \bar{B})$

### 1.3  条件概率与事件的相互独立性

#### 1.3.1 条件概率

**定义** 对于事件 A,  B,   且 $P(B) \ge 0$,  称 $P(A | B) = \frac{P(AB)}{P(B)}$ 为在 B 发生的条件下 A 发生的条件概率．

???+ warning
    - $P(B) = 0$ 时,  $P(A | B)$ 无意义．
    - $P(A | \varOmega) = \frac{P(A \varOmega)}{P(\varOmega)} = P(A)$ 

???+ note "条件概率的性质"
    - $P(\varnothing | B) = 0$
    - $P(\bar{A} | B) = 1 - P(A | B)$
    - $P(A_1 \cup A_2 | B) = P(A_1 | B) + P(A_2 | B) - P(A_1 A_2 | B)$

???+ example "条件概率"
    设10件产品中有3件次品,  现无放回的抽取2件,  求在第一次抽到次品的条件下,  第二次抽到次品的概率．

    **解** 设 $A_i = \{第 i 次抽到次品 \}$,  问题转化为了求 $P(A_2|A_1)$

    - **解法一(条件概率)** 

        $$
        P(A_2|A_1) = \frac{P(A_2 A_1)}{P(A_1)} = \frac{C_3 ^2/ C_10 ^2}{C_3 ^1/ C_10 ^1} = \frac{2}{9}
        $$

    - **解法二** 按照常识很容易就可以得出答案

#### 1.3.2 乘法公式

设 $A,  B \subset \varOmega$,  

- 若 $P(B) > 0$,  则 $P(AB) = P(B) \cdot P(A | B)$
- 若 $P(A) > 0$,  则 $P(AB) = P(A) \cdot P(B | A)$

???+ note
    $$
    P(A|B) = \frac{P(AB)}{P(B)} \Rightarrow P(AB) = P(B) \cdot P(A|B) \\
    P(B|A) = \frac{P(BA)}{P(A)} \Rightarrow P(AB) = P(A) \cdot P(B|A)
    $$

???+ note "推广"
    一般地,  设$A_1 ,  A_2 ,  ...,  A_n \subset \varOmega$,   若 $P(A_1 A_2 ...  A_{n-1} ) > 0$,  则 $P(A_1 A_2 ...  A_n ) = P(A_1 )P(A_2 | A_1 )P(A_3 | A_1 A_2 ) ... P(A_n | A_1 ... A_n )$．
 
???+ example "乘法公式-验证抓阄的科学性"
    设口袋中有a只白球、b只黑球,  无放回取球,  求第二次取出白球的概率．

    **解** $A_i = \{第 i 次取到白球 \}$,  则 $\bar{A_1} = \{第1次取到黑球 \}$,  问题转化为了求 $P(A_2)$

    可知 $P(A_1) = \frac{a}{a+b},  \space P(\bar{A_1}) = \frac{b}{a+b}$

    $P(A_2|A_1) = \frac{a-1}{a+b-1},  \space P(A_2|\bar{A_1}) = \frac{a}{a+b-1}$

    $$
    P(A_2) = P(A_2 \varOmega) = P(A_2 \cap \varOmega) = P(A_2 \cap (A_1 \cup \bar{A_1})) \\
    = P((A_2 \cap A_1) \cup (A_2 \cap \bar{A_1})) = P(A_1 A_2 \cap \bar{A_1} A_2) \\
    = P(A_1) P(A_2|A_1) + P(\bar{A_1}) P(A_2|\bar{A_1}) = \frac{a}{a+b} = P(A_1)
    $$

    同理 $P(A_k) = \frac{a}{a+b}$

???+ example "乘法公式-摸奖"
    盒子里有 n 个球,  其中n -1 个白球,  1个黑球．n 个人依次取一个球,  不放回．问第 i 个人取到黑球的概率．

    **解** $A_i$ = {第 i 个人摸到黑球},  $P(A_1) = \frac{1}{n}$

    $$
    P(A_2) = P(\bar{A_1} A_2) = P(\bar{A_1}) P(A_2|\bar{A_1}) = \frac{n-1}{n} \cdot \frac{1}{n-1} = \frac{1}{n}
    $$

    同理 $P(A_n) = \frac{1}{n}$

#### 1.3.3 全概率公式

**完备事件组** 

???+ success inline end
    ![p1.webp](https://s2.loli.net/2025/06/04/y2gJNR91Hs8l4dr.webp)

事件组 $A_1 ,  A_2 ,  ...,  A_n$,  若满足：

- $\bigcup_{i=1}^n A_i = \varOmega$

- $A_i A_j = \varnothing (i \not ={j} ), i, j = 1,  2, ...,  n$

则称 $A_1 ,  A_2 ,  ...,  A_n$ 为 $\varOmega$ 的一个分割或完备事件组．

**全概率公式** 

???+ success inline end
    ![p2.webp](https://s2.loli.net/2025/06/04/IhOA94Bs7zCleRV.webp)

设 $A_1 ,  A_2 ,  ...,  A_n$ 是 $\varOmega$ 的一个分割,  且 $P(A ) > 0 (i =  1,  2,  ...,  n)$．则对$\forall B$,  有

$$
P(B) = \sum _{i=1} ^n P(A_i B) =  \sum _{i=1} ^n P(A_i )P(B | A_i )
$$

称为全概率公式．

???+ example "全概率公式"
    设某工厂有三个车间,  生产同一种产品,  混合后从中任取一件,  求该产品为次品的概率．

    | 产品 | 一 | 二 | 三 |
    | --- | --- | --- | --- |
    | 次品率 | 0.05 | 0.03 | 0.01 |
    | 产量 | 2500 | 2000 | 1500 |

    **解** 设B表示取到得产品为次品；$A_i$ 表示取到第 i 个车间的产品．i = 1,  2,  3. 问题转化为了求 $P(B)$

    $$
    P(B) = P(A_1 B) + P(A_2 B) + P(A_3 B) \\
    = P(A_1)P(B | A_1 ) + P(A_2)P(B | A_2) + P(A_3)P(B | A_3) \\
    = \frac{2500}{6000} \times 0.05 + \frac{2000}{6000} \times 0.03 + \frac{1500}{6000} \times 0.01 \approx 3.3 \%
    $$

???+ example "全概率公式"
    已知一个袋子中有12个乒乓球,  其中9个新球,  3个旧球,  现从中任取3个球进行比赛,  比赛结束后,  将3个球放回袋中．第二天,  再任取3球进行比赛,  求第二次抽出的3个球全是新球的概率是多少？

    **解** 设 $A_i$ 表示第一次取出 i 个新球 i = 0,  1,  2,  3,  B 表示第二次取出3个新球,  问题转换为了求$P(B)$

    $$
    P(B) = P(A_0 B) + P(A_1 B) + P(A_2 B) + P(A_3 B) \\
    = P(A_0)P(B | A_0) + P(A_1)P(B | A_1) + P(A_2)P(B | A_2) + P(A_3)P(B | A_3) \\
    = \frac{C_3 ^3}{C_12 ^3} \frac{C_9 ^3}{C_12 ^3} + \cdots
    $$

#### 1.3.4 贝叶斯公式(逆转因果)

设 $A_1 ,  A_2 ,  ...,  A_n$ 是 $\varOmega$ 的一个分割,  且$P(A ) > 0 (i =1,  2,  ...,  n)$.则对$\forall B$,   若$P(B) > 0$,  有

$$
P(A_j | B) = \frac{P(A_j B)}{P(B)} = \frac{P(A_j ) P(B | A_j )}{\sum _{i=1} ^n P(A_i ) P(B | A_i )}
$$

称为贝叶斯公式 (或逆全概率公式)． 

???+ example "全概率公式和贝叶斯公式"
    某传染病临床上统计发生下述症状的易感者患病概率为：

    | | 仅发热 | 仅干咳 | 既发热又干咳 | 无上述现象 |
    | --- | ----- | ------ | ----------- | ---------- |
    | 概率 | 0.03 | 0.01 | 0.05 | 0.0001 |

    现对某疫区25000人检查发现：

    |  | 仅发热 | 仅干咳 | 既发热又干咳 |
    | --- | ----- | ------ | ----------- |
    | 人数/人 | 500 | 1000 | 250 |

    > 1. 疫区中任取一人,  他为该传染病患者的概率；
    > 1. 某人为该传染病患者,  计算他临床表现为“仅发热”的概率． 

    **解** 设 A={仅发热病人},  B={仅干咳病人},  C={既发热又干咳病人},  D={无明显症状的病人},  E={得了该传染病}

    1. 问题转换为求$P(E)$,  由全概率公式得：

        $P(E) = P(A)P(E | A) + P(B)P(E | B)+P(C)P(E | C) + P(D)P(E | D) = \frac{500}{25000} \times 0.03 + \cdots = 0.001593 $

    2. 问题转换为求$P(A|E)$ ,  由贝叶斯公式得：

        $P(A|E) = \frac{P(A)P(E|A)}{P(E)} = 0.37648$

???+ example "贝叶斯公式"
    商店论箱出售玻璃杯,  每箱20只,  其中每箱含有 0,  1,  2 只次品的概率分别为0.8,  0.1,  0.1,  某顾客选中一箱,  从中任选4只检查,  结果都是好的,   便买下了这一箱．问这一箱含有一个次品的概率是多少？

    **解** 设 A表示从一箱中任取4只检查,  结果都是好的．$B_i$ 表示事件每箱含 i 只次品,  i = 0, 1, 2. 问题转化为了求 $P(B_1|A)$

    已知 $P(B_1) = 0.8,  P(B_2) = 0.1,  P(B_3) = 0.1$

    $P(A|B_0) = 1,  \space P(A|B_1) = \frac{C_19 ^4}{C_20 ^4} = \frac{4}{5},  \space P(A|B_2) = \frac{C_18 ^4}{C_20 ^4} = \frac{12}{19}$

    由贝叶斯公式得 

    $$
    P(B_1|A) = \frac{P(AB_1)}{P(A)} = \frac{P(B_1)P(A|B_1)}{P(B_0)P(A|B_0) + P(B_1)P(A|B_1) + P(B_2)P(A|B_2)} = 0.0848
    $$

<!-- ???+ example 
例8 三个盒子分别装着2个红球,  2个蓝球,  1红1蓝,  
现从中抽取一个盒子,  再从盒子中抽出一个球,  发现是
红球,  问另一个球也是红球的概率?
解 设 A ,  A ,  A 分别表示抽到第1,  2,  3 个盒子,  B 表示第一个球是红球
1 2 3
P(B) = P(A )P(B | A ) + P(A )P(B | A ) + P(A )P(B | A )
1 1 2 2 3 3
1 1 1 1 1
= \cdot 1+ \cdot  + \cdot 0 =
3 3 2 3 2
P(A )P(B | A )
1/ 3 2
P(A | B)= 1 1 = =
1
P(B) 1/ 2 3 

例8 三个盒子分别装着2个红球,  2个蓝球,  1红1蓝,  
现从中抽取一个盒子,  再从盒子中抽出一个球,  发现是
红球,  问另一个球也是红球的概率?
解法2 缩小样本空间法,   不考虑盒子,  只考虑6个球,  抽走一个红球,  
2
淘汰两个蓝球,  只剩下2红1蓝,   则第二次抽到红球的概率为 ．
3  -->

???+ note "全概率公式与贝叶斯公式说明"
    令 $A_i$ 表示“原因”,   $B$ 表示“结果”,  则$P(A_i)$表示第 $i$ 种原因发生的概率．$P(B | A_i) $表示原因 $A_i$引起结果 $B$ 发生的可能性大小．

    - **全概率公式** 综合引起结果的各种原因,  导致该结果出现的可能性大小．
    - **贝叶斯公式** 当结果出现时,  它是由某原因引起的可能性大小． 逆转因果

#### 1.3.5 事件的相互独立性

**两事件独立** 若$A,  B$两个事件满足 $P(AB) = P(A) P(B)$,  则称事件A与B相互独立．

???+ note
    - $\varOmega,  \varnothing$ 与任何事件相互独立
    - 事件的独立与事件的互斥无联系
    - 判别独立的方法
        - 定义验证
        - 对实际问题,  由经验验证． 

???+ example "事件独立-由生活经验判断"
    掷两枚均匀的骰子一次,  求出现双6点的概率．

    **解** 设 $A_i$ ={第 i 枚骰子出现6点},  i = 1,  2,  易知 $A_1,  A_1$ 独立,  问题转化为求 $P(A_1A_2)$

    $P(A_1A_2)= P(A_1) \cdot  P(A_2) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36}$

???+ example "事件独立-由定义判断"
    从一付52张(去掉王)的扑克牌中任意抽取一张,  令 A={抽出一张 K },  B={抽出一张黑桃},  问 A 与 B 是否独立?

    **解** $\because P(A) = \frac{4}{52} ,   P(B) = \frac{13}{52} ,   P(AB) = \frac{1}{52} = P(A)P(B)$

    $\therefore$ 两事件相互独立

???+ tip
    - $A,  B$ 相互独立 $\iff P(A | B) = P(A), P(B) > 0 \iff P(B | A) = P(B) , P(A) > 0$
    - 若事件$A$与$B$独立,  则$A$与$\bar{B}$、$\bar{A}$与$B$、$\bar{A}$与$\bar{B}$ 也相互独立．
 

<!-- 例11 两射手同时向同一目标射击一次,  其命中率分别为 0.8 和 0.6 ,  
求在一次射击中目标被击中的概率．
解 设 A ={甲中},   B= {乙中},   C= {目标被击中},  
解法1 P(C) = P(A \cup B) = P(A) + P(B) - P(AB)
= 0.8 + 0.6 - 0.8  \times  0.6 = 0.92．
解法2 用对立事件公式
P(C) = 1- P(AB)
= 1- P(A)P(B) = 1- 0.2 \times  0.4 = 0.92．  -->

**多个事件的独立** 若三个事件 $A,  B,  C$ 满足 

$$P(AB) = P(A) P(B) ,  P(AC) = P(A) P(C) ,  P(BC) = P(B) P(C)
$$

则称事件 $A,  B,  C$ 两两独立．若在此基础上还满足 $P(ABC) = P(A) P(B) P(C)$ 则称事件 $A,  B,  C$ 相互独立． 

<!-- 注 两两独立 相互独立
例如 有4张同样大小的卡片,  上面标有数字,  每张被抽到的概率相同,  
1, 2, 3 1    2    3   
令 A = {抽到的卡片上有数字 i },  i = 1,  2,  3
i
1
则 P(A ) = P(A ) = P(A ) = ,  
1 2 3
2 

1
P(A A ) = = P(A )P(A )
1 2 1 2
4
1
P(A A ) = = P(A )P(A )
两两独立
2 3 2 3
4
1
P(A A ) = = P(A )P(A )
1 3 1 3
4
1 1
但 P(A A A ) =  P(A )P(A )P(A ) =
1 2 3 1 2 3
4 8
即三个事件不相互独立． 1, 2, 3 1    2    3    

一般地,  设 A ,  A ,  ...,  A 是 n 个事件,  若以下等式成立
1 2 n
P(A A ) = P(A )P(A ) 1 \leq i < j \leq n,  
i j i j
P(A A A ) = P(A )P(A )P(A ) 1 \leq i < j < k \leq n,  
i j k i j k
......
P(A A ... A ) = P(A )P(A )...P(A )
1 2 n 1 2 n
则称 n 个事件 A ,  A ,  ...,  A 相互独立．
1 2 n  -->

???+ note "事件独立性的应用-加法公式的简化"
    若事件 $A_1,  A_2,  ...,  A_n$ 相互独立,   则 $P(A_1 \cup A_2 \cup ... \cup A_n ) =1 - P(\bar{A_1} \bar{A_2} \cdots \bar{A_n}) =1- P(\bar{A_1}) ... P(\bar{A_n})$

    > $\overline{ A \cup B } = \overline{A} \cap \overline{B} = \bar{A} \bar{B}$ (和的逆=逆的积)


<!-- 例12 用步枪射击飞机,  每支步枪的命中率为0.004,  
求：- 现用250支步枪同时射击飞机一次,  飞机被击中
的概率．
- 假如想以99%的概率击中飞机,  至少需要多少支步枪同时射击．
解 设 A ={第 i 支步枪击中飞机},  
i
- P(A \cup A \cup...\cup A ) = 1- P(A )...P(A ) = 1- 0.996250  0.63,  
1 250
1 2 250
- 由 1- 0.996n \ge 0.99  n 1150． 

例13 如图,  1、2、3、4、5表示继电器触点,   假设
1 4
3
L R
每个触点闭合的概率为p,   且各继电器接点闭合与否相
2 5
互独立,  求 L 至 R 是通路的概率．
解 设 A={L至R为通路},  A ={第 i 个继电器通},  i = 1,  2,  3,  4,  5
i
易知,  A 与A 构成了一完备事件组,   1 4
3 3
L R
从而有 P(A | A ) = P(A A \cup A A ) = 2 p2 - p4 ,   2 5
3
1 4 2 5 

例13 如图,  1、2、3、4、5表示继电器触点,   假设
1 4
3
L R
每个触点闭合的概率为p,   且各继电器接点闭合与否相
2 5
互独立,  求 L 至 R 是通路的概率．
P(A | A ) = P((A \cup A )  (A \cup A ))= P(A \cup A )P(A \cup A ) = (2 p - p2)2 ,  
3 1 2 4 5 1 2 4 5
由全概率公式
1 4
P(A) = P(A )P(A | A ) + P(A )P(A | A ) L R
3 3
3 3
2 5
= 2 p2 + 2 p3 - 5 p4 + 2 p5 ． 
-->

## 第二章 随机变量及其概率分布 

### 2.1  随机变量的概念 

???+ abstract 
    有些随机试验的结果是一个数值．例如：掷骰子试验、产品的次品率检验等．有些试验的结果不是数值,  但可转化为数值表示．例如：掷硬币试验,  可以用1表示正面,  0表示反面．综上所述,  {==所有随机试验的结果均可用数值表示==}．因此,  可以引入一个变量来表示随机试验的结果． 

**定义** 设试验 $E$ 的样本空间为 $\varOmega$,  若对于每个样本点 $\omega \in \varOmega$ 均有一个实数 $X (\omega)$ 与之对应,  这样就得到一个定义在 $\varOmega$上的单值函数 $X = X (\omega)$,  称 $X$ 为随机变量．

??? warning
    - 随机变量是一个定义在样本空间上的实函数,  它取值的随机性是由样本点的随机性引起的
    - 引入随机变量是为了将随机试验数量化,  这样就可以用微积分的理论对随机现象的规律性进行研究． 

???+ example
    若用 X 表示掷一枚骰子的试验中出现的点数,  则 $\{X < 5 \}$ 表示掷出点数小于 5 这一事件,  $\{X = 3 \}$ 表示掷出的点数为 3 点这一事件． 

### 2.2  随机变量的概率分布 

#### 2.2.1 随机变量的分布函数 $F(x)$

**定义** 设 $X$ 为一随机变量,   $x$ 为任意实数,  称函数 $F(x) = P \{X \leq x \}$ 为 $X$ 的分布函数．

???+ warning
    - $F(x)$ 是一普通函数,  其定义域为 $(- \infty,  + \infty)$
    - $F(x)$ 的值为事件 $\{ X \leq x \}$ 的概率
    - $F(x)$ 可以完全地描述随机变量取值的规律性．

???+ example
    $P\{x_1 < X \leq x_2 \} = P \{X \leq x_2 \}  - P \{X \leq x_1 \}  = F(x_2 ) - F(x_1 )$．

???+ note "分布函数 $F(x)$ 的性质"
    - **单调不减性** 若 $x_1 < x_2$ ,  则 $F(x_1 ) \leq F(x_2 )$
    - **规范性** 

        $$
        F(- \infty) = \lim _{x \to - \infty} F(x) = 0 \\
        F(+ \infty) = \lim _{x \to + \infty} F(x) = 1
        $$

      - **右连续性** $\forall x \in \R$,  有 
     
        $$
        \lim _{x \to x_0 ^+} F(x) = F(x_0 )
        $$

???+ note
    任一满足以上三个性质的函数,  都可以作为某随机变量的分布函数． 

??? example "分布函数的性质"
    设随机变量 X 的分布函数为 $F(x) = A + B arctan x ,  \space - \infty < x < +\infty$,  求 A 和 B 的值．

    **解** 由规范性知 $F(-\infty) = A - \frac{\pi}{2} \cdot  B = 0,  \space F(+\infty) = A + \frac{\pi}{2} \cdot B = 1$

    解得 $A = \frac{1}{2},   B =\frac{1}{\pi}$

???+ example "分布函数"
    设某随机变量的分布函数为

    $$
    F(x) = 
    \begin{cases} 
    0 ,  \space x \le 0 \\
    Ax^2 ,  \space0 < x \le 1 \\
    1 ,  \space x > 1
    \end{cases}
    $$

    求 A 及 $P \{0.3 < X \leq 0.7 \}$．

    **解** 利用右连续性知 $F(1^+) = F(1)$,  则 A = 1．

    $P\{0.3 < X \leq 0.7\}  = F(0.7) - F(0.3) = 0.72 - 0.32 = 0.4$

???+ note
    设 $X \sim F(x),  \forall a,  b \in \R$,  且 $a < b$,   则有

    - $P \{ X \le b \} = F(b)$
    - $P \{ X < b \} = F(b ^-)$
    - $P \{ X = b \} = P \{ X \le b \} - P \{ X < b \} = F(b) - F(b ^-)$
    - $P \{X > a \} = 1 - P \{X \leq a \} = 1 - F(a)$
    - $P \{X \geq a \} = 1 - P \{X < a \} = 1 - F(a ^-)$
    - $P \{a < X < b \} = P \{X < b \} - P \{X \leq a \} = F(b^-) - F(a)$

???+ info "随机变量的分类"
    - **离散型随机变量** 取值为有限个或可列个．例如：一批产品中的次品数．
    - **连续型随机变量** 取值为某一区间上的值．例如：零件尺寸与规定尺寸的偏差． 

#### 2.2.2 离散型随机变量的分布律

**定义** 设 $x_i (i = 1,  2,  ...)$为离散型随机变量 $X$ 的所有可能取值,  事件 $\{X = x_i \}$  的概率 $P\{X = x_i \}  = p_i ,  i = 1,  2,  ...$ 称为 $X$ 的分布律 (列),  常写成表格形式：

$$
\begin{array}{c|cccc}
X & x_1 & x_2 & \cdots & x_n \cdots \\
\hline
P & p_1 & p_2 & \cdots & p_n \cdots
\end{array}
$$

???+ note "离散型随机变量分布律的性质"
    - **非负性** $p_i \geq 0$,   $i = 1,  2,  ...$
    - **规范性** $\sum p_i = 1$

    任一满足这两条性质的数列,  都可作为某离散型随机变量的分布律．
 
???+ example "离散型随机变量的分布律和分布函数"
    袋中有编号为1-5的5个球,  从中任取3个球,  求取出球的最大号 X 的分布律和分布函数．

    **解** X 的可能取值为3,  4,  5

    $P\{X = 3 \}  = \frac{1}{C_5 ^3} = \frac{1}{10},  \space P\{X = 4 \} = \frac{C_3 ^2}{C_5 ^3} = \frac{3}{10},  \space P\{X = 5\}  = \frac{C_4 ^2}{C_5 ^3} = \frac{6}{10}$

    所以 X 的分布律为

    $$
    \begin{array}{c|cccc}
    X & 3 & 4 & 5 \\
    \hline
    P & \frac{1}{10} & \frac{3}{10} & \frac{6}{10}
    \end{array}
    $$

    ???+ success inline end
        ![fx.webp](https://s2.loli.net/2025/06/05/3udGmq9zTcoQ8fn.webp)

    则 X 的分布函数为

    $$
    F(x) = P \{X \le x \}
    \begin{cases} 
    0 ,  \space x < 3 \\
    \frac{1}{10} ,  \space 3 \le x < 4 \\
    \frac{4}{10} ,  \space 4 \le x < 5 \\
    1 ,  \space x \ge 5
    \end{cases}
    $$

#### 2.2.3 连续型随机变量的概率密度函数 $f(x)$

???+ success inline end "连续性随机变量概率密度函数几何意义"
    ![概率密度函数.png](https://s2.loli.net/2025/05/07/GazSHucAJnjsomF.png)

**定义** 设 $X \sim F(x)$,  若存在一个非负可积的函数 $f (x)$,  使 $\forall x \in \R$,  有

$$
F(x) = P \{ X \le x \} = \int _ {-\infty} ^x f (t) dt
$$

则称 X 为连续型随机变量,  $f (x)$称为 X 的概率密度函数或分布密度函数．连续型随机变量的分布函数 $F(x)$ 是连续函数．

???+ note "概率密度函数 $f (x)$ 的性质"
    - **非负性** $f (x) \geq 0$
    - **规范性** $F(+\infty) =  \int _ {-\infty} ^ {+\infty} f (x) dx = 1$

        > 任一满足以上两条性质的函数,  都可以作为某连续型随机变量的概率密度函数．

    - $P\{a < X \leq b\}  = F(b) - F(a) = \int _a ^b f(x) dx$
    - 若 $f (x)$ 在 $x$ 处连续,  则 $F' (x) = f (x)$． 
  
    > 设 $X$ 为一连续型随机变量,   $a$ 为任意常数,  则有 $P\{X = a\}  = 0$ (概率为0的事件未必是不可能事件)

    **证明** $\because F(x)$ 是连续的 $\Rightarrow F(a^-) = F(a)$

    $\therefore P \{X = a \} = P \{X \leq a \} - P \{X < a\} = F(a) - F(a^-) = F(a) - F(a) = 0$

    $\therefore P \{a < X \leq b \} = P \{a \leq X \leq b \} = P \{a < X < b \}= P \{a \leq X < b \} = \int _a ^b f (x)dx$

???+ example "概率为0的事件未必不可能发生"
    已知 $P(A \cup B) = 0.8 ,  P(A) = 0.3,  P(B) = 0.5$,  则事件 A 与B 的关系为 ( D )．

    - [ ] (A) 事件 A 与B 相互独立
    - [ ] (B) 事件 A与 B 互不相容
    - [ ] (C) 事件 A与 B 对立
    - [x] (D) 事件 A 与B 有可能同时发生

    **解析** 由 $P(A \cup B) = P(A) + P(B) - P(AB)$,  易得 $P(AB) = 0$,  排除 (A)；互不相容的定义是事件不能同时发生,  由于概率为 0 的事件是有可能发生的事件,  因此本题答案为 (D)． 

???+ example "连续型随机变量"
    设连续型随机变量 $X$ 的概率密度函数为 

    $$
    f(x) = 
    \begin{cases} 
    kx(1-x) ,  \space 0 < x < 1 \\
    0 ,  \space 其他
    \end{cases}
    $$

    求 $k$ 的值,  $P\{X > 0.3\}$ 及分布函数 $F(x)$．

    **解** 利用规范性得 $1 = \int _{- \infty} ^{+ \infty} f (x)dx = \int _{- \infty} ^0  f (x)dx + \int _0 ^1 f (x)dx + \int _0 ^{+ \infty} f (x)dx$

    即 $\int _0 ^1 kx(1- x)dx = 1 \implies k = 6$

    $P \{X > 0.3 \} = \int _{0.3} ^{+ \infty} f (x)dx = \int _{0.3} ^1 6x(1- x)dx = 0.784$

    $$
    F(x) = \int _{- \infty} ^x f(t) dt
    \begin{cases} 
    0 ,  \space x \le 0 \\
    3x^2 - 2x^3 ,  \space 0 < x < 1 \\
    1 ,  \space x \ge 1
    \end{cases}
    $$

### 2.3  随机变量函数的分布  

#### 2.3.1 离散型随机变量函数的分布

???+ example "离散型随机变量函数的分布"
    设离散型随机变量 X 的分布律为：

    $$
    \begin{array}{c|cccc}
    X & -1 & 0 & 1 & 2 \\
    \hline
    P & 0.2 & 0.3 & 0.1 & 0.4
    \end{array}
    $$

    则 $Y = X^2 +1$ 的分布律为：

    $$
    \begin{array}{c|cccc}
    Y & 1 & 2 & 5 \\
    \hline
    P & 0.3 & 0.3 & 0.4
    \end{array}
    $$

#### 2.3.2 连续型随机变量函数的分布

**定理** 设连续型随机变量 $X$ 的概率密度函数为 $f_X (x)$,  又设 $y = g(x)$ 是处处可导的单调函数,  则 $Y = g(X )$ 是连续型随机变量,  且 Y 的概率密度函数为：

$$
f_Y(y) = 
\begin{cases}
f_X [h(y)] \cdot | h'(y) |,  & \alpha < y < \beta \\
0,  & \text{其他 }
\end{cases}
$$

其中 $x = h(y)$ 是 $y = g(x)$ 的反函数,  $\alpha$ 是 $y = g(x)$ 的最小值,  $\beta$ 是 $y = g(x)$ 的最大值.

<!-- \lambdae-\lambdax,   x \ge 0
例2 设 X \sim f (x) = (\lambda > 0),  求 Y = eX 的概率密度函数 f (y)．

X Y
0,   x < 0

解法一 y = ex 的反函数是 x = ln y ,  
1
反函数 x 对 y 的导数为 ,  又由 x \ge 0  y = ex \ge 1,  
y
 1
 \lambdae-\lambdaln y ,   y \ge 1,   \lambday-(1+\lambda) ,   y \ge 1,  
因此 f (y) = y 则 f ( y) =
 
Y Y
0,   y < 1．
 
0,   y < 1,  
 

\lambdae-\lambdax,   x \ge 0
例2 设 X \sim f (x) = (\lambda > 0),  求 Y = eX 的概率密度函数 f (y)．

X Y
0,   x < 0

解法二 先求 Y 分布函数F (y),  
Y
\{ \} 
F (y) = P\{Y \leq y\}  = P eX \leq y ,   由 X > 0得,  Y = eX >1,  
Y
\{ \} 
当 y < 1 时,  F (y) = P eX \leq y = 0,  
Y
ln y
\{ \} 
当 y \ge 1 时,   F (y) = P eX \leq y = P\{X \leq ln y\}  = \int \lambdae-\lambdaxdx = 1- y-\lambda ,  
Y
0
\lambday-(1+\lambda) ,   y \ge1,  
则 f ( y) =

Y
0,   y < 1．
 

1- | x |,   -1 < x < 1,  
例3 设 X\sim f (x) = 求随机变量Y = X 2 +1 的分布

X 0,   其它,  

函数与概率密度函数．
解 X 的取值范围为 (-1,  1) ,  则 Y 的取值范围为 [1,  2) ,  
当 y < 1 时,  F (y) = P\{Y \leq y\}  = 0； 当 y \ge 2 时,  F ( y) = P\{Y \leq y\}  = 1；
Y Y
\{ \}  \{ \} 
当1 \leq y < 2 时,  F (y) = P\{Y \leq y\}  = P X 2 +1 \leq y = P - y -1 \leq X \leq y -1
Y
y-1  2
= \int (1- | x |)dx = 1- 1- y -1 ．
- y-1 

1- | x |,   -1 < x < 1,  
例3 设 X\sim f (x) = 求随机变量Y = X 2 +1 的分布

X 0,   其它,  

函数与概率密度函数．
 0,   y <1

  2
综上知,  Y 的分布函数 F (y) = 1- 1- y -1 ,   1\leq y < 2
Y

分段点处的导
1,   y \ge 2


数按定义求！
 1
-1,   1< y < 2,  

所以Y 的密度函数为 f (y) =  y -1
Y

0,   其它．
  -->

### 2.4 二维随机变量及其分布 

#### 2.4.1 二维随机变量

**定义** 设 $X,  Y$ 是两个随机变量,  则由它们构成的二维向量 $(X ,  Y )$ 称为二维随机变量． 

**联合分布函数** 设 $(X ,  Y )$是二维随机变量,  $\forall x ,  y \in \R$,  称二元函数 $F(x,  y) = P\{X \leq x,  Y \leq y\}$ 为$(X ,  Y )$ 的联合分布函数．

???+ success inline end "几何意义"
    ![几何意义.png](https://s2.loli.net/2025/05/07/dsQHW8p4kBMDfKZ.png)

???+ note
    - **几何意义：** $(X ,  Y )$落在点 $(x,  y)$ 的左下方无穷矩形域内的概率．
    - $P\{x_1 < X \leq x_2 ,  y_1 < Y \leq y_2 \} = F(x_2 ,  y_2 ) - F(x_1 ,  y_2 ) - F(x_2 ,  y_1) + F(x_1 ,  y_1 )$．

    > 此处事件中的逗号表示 "且"

???+ note "性质"
    - $F(x,  y)$ 关于 $x,  y$ 具有单调不减性；
    - $F(+ \infty,  + \infty) = 1,  F(-\infty,  - \infty) = 0,  F(x,  - \infty) = 0,  F(-\infty,  y) = 0$
    - $F(x,  y)$ 关于 $x,  y$ 具有右连续性；
    - 对$\forall x_1 < x_2 ,  y_1 < y_2$均有 $F(x_2 ,  y_2 ) - F(x_1 ,  y_2 ) - F(x_2 ,  y_1 ) + F(x_1 ,  y_1 ) \ge 0$

**边缘分布函数** 

- $F_X (x) = P\{X \leq x\} = F(x,  + \infty)$
- $F_Y (y) = F(+\infty,  y)$

#### 2.4.2 二维离散型随机变量

**定义** 若 $(X ,  Y )$ 的全部可能取值只有有限多对或可列多对,  则称$(X ,  Y )$ 是二维离散型随机变量,  而称 $P \{X = x_i ,  Y = y_j \} = p_{ij} (i,  j = 1,  2,  ...)$ 为二维离散型随机变量 $(X ,  Y )$ 的联合分布律．

**性质** 

- $p \ge 0,   i,  j = 1,  2,  ...$
- $\sum _i \sum _j p_{ij} = 1$

**边缘分布律**

- $P\{X = x_i \}  = \sum _j p_{ij} = p_i$
- $P\{Y = y_j \}  = \sum _i p_{ij} = p_j$

$(X ,  Y )$的联合分布律通常用如下表格给出：

$$
\begin{array}{c|ccccc}
X \backslash Y & y_1 & y_2 & \cdots & y_j & \cdots \\
\hline
x_1 & p_{11} & p_{12} & \cdots & p_{1j} & \cdots \\
x_2 & p_{21} & p_{22} & \cdots & p_{2j} & \cdots \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
x_i & p_{31} & p_{32} & \cdots & p_{3j} & \cdots \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
\end{array}
$$

联合分布律的行或列相加即得边缘分布律：

$$
\begin{array}{c|ccccc|c}
X \backslash Y & y_1 & y_2 & \cdots & y_j & \cdots & P \{X= x_i \} = p_{i \cdot} \\
\hline
x_1 & p_{11} & p_{12} & \cdots & p_{1j} & \cdots & p_{1 \cdot} \\
x_2 & p_{21} & p_{22} & \cdots & p_{2j} & \cdots & p_{2 \cdot} \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
x_i & p_{31} & p_{32} & \cdots & p_{3j} & \cdots & p_{i \cdot} \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
\hline
P \{Y= y_j \} = p_{\cdot j} & p_{\cdot 1} & p_{\cdot 2} & \cdots & p_{\cdot j} & \cdots & 1 \\
\end{array}
$$

#### 2.4.3 二维连续型随机变量

**定义** 设 $(X ,  Y ) \sim F(x,  y)$,  若存在一个非负可积的函数 $f (x,  y)$,  使 $\forall (x,  y) \in \R^2$,  有 $F(x,  y) = \int _{- \infty} ^x \int _{- \infty} ^y f (u,  v)dvdu$,  则称 $(X ,  Y )$为二维连续型随机变量,   $f (x,  y)$ 称为 $(X ,  Y )$ 的联合概率密度函数． 

$f (x,  y)$ 的性质:

- 非负性 $f (x,  y) \ge 0$
- 规范性 $\int _{- \infty} ^{+ \infty} \int _{- \infty} ^{+ \infty} f (x,  y)dxdy = 1$
- 若 $f (x,  y)$在点 $(x,  y)$ 连续,  则 $\frac{\partial ^2 F(x, y)}{\partial x \partial y} = f (x,  y)$
- $P \{(X, Y) \in D \} = \iint _D f(x, y) dx dy$

边缘密度函数:

- $F_X (x) = \int _{- \infty} ^{+ \infty} f (x, y) dy$
- $F_Y (y) = \int _{- \infty} ^{+ \infty} f (x, y) dx$

???+ example "二维连续型随机变量"
    设 $(X ,  Y )$ 的联合概率密度函数为 

    $$
    f(x) = 
    \begin{cases} 
    Ce^{-2(x+y)} ,  \space x > 0,  y > 0 \\
    0 ,  \space 其他
    \end{cases}
    $$

    > 1. 求常数$C,  F(x,  y),  f_X (x),  f_Y (y)$
    > 2. 求 $P\{(X ,  Y )\in D\}$ ,  D由 $x = 0,  y = 0,  x + y = 1$ 围成．

    **解** 由规范性 $1= \int _{- \infty} ^{+ \infty} \int _{- \infty} ^{+ \infty} f (x,  y)dxdy = \int _0 ^{+ \infty} \int _0 ^{+ \infty} Ce^{-2(x+y)} dxdy = \frac{C}{4} \implies C = 4$

    $$
    F(x,  y) = \int _{- \infty} ^x \int _{- \infty} ^y f (u,  v)dvdu \\ = 
    \begin{cases} 
    \int _0 ^{+ \infty} \int _0 ^{+ \infty} 4e^{-2(x+y)} dvdu,  \space x > 0,  y>0 \\
    0 ,  \space 其他
    \end{cases}
    \\ =
    \begin{cases} 
    (1-e^{-2x})(1-e^{-2y}),  \space x > 0,  y>0 \\
    0 ,  \space 其他
    \end{cases}
    $$

    $$
    f_X(x) = \int _{- \infty} ^{+ \infty} f(x, y) dy \\ =
    \begin{cases} 
    \int _0 ^{+ \infty} 4e^{-2(x+y)} dy ,  \space x > 0 \\
    0 ,  \space 其他
    \end{cases}
    \\ = 
    \begin{cases} 
    2e^{-2x} ,  \space x > 0 \\
    0 ,  \space 其他
    \end{cases}
    $$

    ???+ success inline end
        ![pro.webp](https://s2.loli.net/2025/06/06/S9RzymEOuPVphnA.webp)

    同理

    $$
    f_Y(y) = \int _{- \infty} ^{+ \infty} f(x, y) dx \\ =
    \begin{cases} 
    2e^{-2y} ,  \space y > 0 \\
    0 ,  \space 其他
    \end{cases}
    $$

    ---

    $P \{(X, Y) \in D \} = \iint _D f(x, y) dx dy = \int _0 ^1 dx \int _0 ^{1-x} 4e^{-2(x+y)}dy = 1 - 3e^{-2}$


<!-- 
例3 设 (X ,  Y )的联合概率密度函数为 f (x,  y) = 
0,   其它,  

 1 1 
求：- 求 P 0 < X < ,   < Y < 1 及P\{X < Y\} ．
 
 2 4 
-求(X ,  Y ) 的边缘概率密度函数及联合分布函数．
 1 1  1 1 15
1 1
解 - P 0 < X < ,   < Y < 1 = \int 2 \int 4xy dydx = \int 2 2xdx\int 2y dy = ,  
1 1
 2 4  0 0 64
4 4
y
1
1 y
\{ \} 
P X < Y = \int\int 4xy dxdy = \int 2ydy\int 2xdx = ,   1
0 0 2
D
x
O 1 

4xy,   0 < x < 1,  0 < y < 1,  
例3 设 (X ,  Y )的联合概率密度函数为 f (x,  y) = 
0,   其它,  

 1 1 
求：- 求 P 0 < X < ,   < Y < 1 及P\{X < Y\} ．
 
 2 4 
-求(X ,  Y ) 的边缘概率密度函数及联合分布函数．
+\infty
- f (x) = \int f (x,  y)dy,  当 x \leq 0 或 x \ge1 时,  由于 f (x,  y) = 0,  得 f (x) = 0
X X
-\infty
1
当 0 < x < 1 时,   f (x) = \int 4xy dy = 2x,  
X
0
2x,   0 < x <1,   2y,   0 < y < 1,  
综上 f (x) =  同理 f (y) =

X  0,   其它,   Y 0,   其它,  
 

4xy,   0 < x < 1,  0 < y < 1,  
例3 设 (X ,  Y )的联合概率密度函数为 f (x,  y) = 
0,   其它,  

 1 1 
求：- 求 P 0 < X < ,   < Y < 1 及P\{X < Y\} ．
 
 2 4 
-求(X ,  Y ) 的边缘概率密度函数及联合分布函数．
当 x \leq 0 或 y \leq 0 时,   有 F(x,  y) = 0,   x y
F(x,  y) = \int \int f (u,  v)dvdu
-\infty -\infty
当0 < x < 1且 0 < y < 1时,  
x y x y
F(x,  y) = \int \int f (u,  v)dvdu = \int \int 4uvdvdu = x2 y2,  
-\infty -\infty 0 0 

4xy,   0 < x < 1,  0 < y < 1,  
例3 设 (X ,  Y )的联合概率密度函数为 f (x,  y) = 
0,   其它,  

 1 1 
求：- 求 P 0 < X < ,   < Y < 1 及P\{X < Y\} ．
 
 2 4 
-求(X ,  Y ) 的边缘概率密度函数及联合分布函数．
x y x 1
当0 < x < 1且 y \ge 1 时,  F(x,  y) = \int \int f (u,  v)dvdu = \int \int 4uvdvdu = x2,  
-\infty -\infty 0 0
x y 1 y
当 x \ge 1 且 0 < y < 1 时,  F(x,  y) = \int \int f (u,  v)dvdu = \int \int 4uvdvdu = y2,  
-\infty -\infty 0 0
x y 1 1
当 x \ge 1 且 y \ge 1 时,   F(x,  y) = \int \int f (u,  v)dvdu = \int \int 4uvdvdu = 1,  
-\infty -\infty 0 0 

4xy,   0 < x < 1,  0 < y < 1,  
例3 设 (X ,  Y )的联合概率密度函数为 f (x,  y) = 
0,   其它,  

 1 1 
求：- 求 P 0 < X < ,   < Y < 1 及P\{X < Y\} ．
 
 2 4 
-求(X ,  Y ) 的边缘概率密度函数及联合分布函数．
 0,   x \leq 0 或 y \leq 0,  

x2 y2,   0 < x < 1,  0 < y < 1,  


综上 F(x,  y) = x2,   0 < x < 1,  y \ge 1,  


y2,   x \ge 1,  0 < y < 1,  

 1,   x \ge 1,  y \ge 1．
  -->

### 2.5 随机变量的相互独立性  

**定义** 设 $(X ,  Y )$ 是二维随机变量,  若 $\forall (x,  y) \in \R ^2$,  有 $P\{X \leq x,  Y \leq y \}  = P\{X \leq x\} P\{Y \leq y\}$ ,  即 $F(x,  y) = F_X (x)F_Y ( y)$,  则称 $X$ 与 $Y$ 相互独立．

特别地,  

- 对离散型随机变量：$X$ 与 $Y$ 相互独立 $\Longleftrightarrow p_{ij} = p_i p_j,  \forall i,  j$
- 对连续型随机变量：$X$ 与 $Y$ 相互独立 $\Longleftrightarrow f (x,  y) = f_X (x) f_Y ( y)$

<!-- 2e-(2x+y) x > 0,  y > 0
例1 (X ,  Y ) \sim f (x,  y) =  判断 X 与 Y 是否相互独立．
0 其它

 +\infty
+\infty \int 2e-(2x+y)dy = 2e-2x,   x > 0,  
解 f (x) = \int f (x,  y)dy =
 0
X
-\infty
 0,   其它,  

 +\infty
\int 2e-(2x+y)dx = e-y,   y > 0,  
+\infty
f (y) = \int f (x,  y)dx =
 0
Y
-\infty
 0,   其它,  

因为 f (x,  y) = f (x) f ( y),  所以 X 与 Y 相互独立．
X Y 

Y 1 2 3
X
例2 设 (X ,  Y ) \sim
1 1/8 a 1/24
2 b 1/4 1/8
求 - a, ab,  b 满足的条件；- 若 X 与 Y 独立,  求 a,  b 的值．
\{ a \ge 0
解 -由分布律的非负性和规范性知 b \ge 0
11
a + b =
24 

Y 1 2 3
X
例2 设 (X ,  Y ) \sim
1 1/8 a 1/24
2 b 1/4 1/8
求 - a, ab,  b 满足的条件；- 若 X 与 Y 独立,  求 a,  b 的值．
- 由 X 与 Y 独立,  得 p = p p ,   \forall i,  j,  从而有
ij i\cdot  \cdot  j
 11  1
a + b = a =
 
 24  12

 
1  3  1 3
 + b =  b =
 

6  8  8  8  -->

???+ note
    - 独立性的概念可推广到$n$个随机变量的情形,  且若 $X_1 ,  X_2 ,  ...,  X_n$是相互独立的随机变量,  则随机变量的函数 $f_1 (X_1 ),  f_2 (X_2 ),  ...,  f_n (X_n )$也是相互独立的
    - 随机变量的相互独立性是事件独立性的扩充,  常可由试验的独立性来判定随机变量的独立性

{==两个随机变量的函数分布==}

<!-- 离散型
 -1 1 
例3 设 X ,  Y 的分布律均为 ,  且 X 与 Y 相互独立,  
 
1/ 2 1/ 2
 
求：- (X ,  Y ) 的联合分布律；
- Z = X + Y 的分布律；
③ P\{X = Y\} ． 

解 - 由 X 与 Y 相互独立,  p = p p ,   则 (X ,  Y )的联合分布律为
ij i\cdot  \cdot  j
Y
-1 1
X
1 1 1 1
-1 \cdot  \cdot 
2 2 2 2
1 1 1 1 1
\cdot  \cdot 
2 2 2 2
- 的分布律为
Z = X + Y
Z -2 0 2
p 1/ 4 1/ 2 1/ 4
1
③ P\{X = Y\}  = P\{X = -1,  Y = -1\}  + P\{X = 1,  Y =1\}  = ．
2 

连续型 引例 设二维连续型随机变量(X ,  Y ) 的联合概率密度为
f (x,  y),  求 Z = X + Y 的概率密度函数 f (z)．
Z
解 F (z) = P\{Z \leq z\}  = P\{X + Y \leq z\}  = \int\int f (x,  y)dxdy
Z
x+y\leqz
+\infty z-x +\infty z
= \int dx\int f (x,  y)dy = \int dx\int f (x,  t - x)dt t = y + x
-\infty -\infty -\infty -\infty
z +\infty y
= \int [\int f (x,  t - x)dx] dt 交换积分顺序
-\infty -\infty
x + y = z
+\infty
两边对 z 求导得 f (z) = \int f (x,  z - x)dx；
Z
-\infty
+\infty
同理可得 f (z) = \int f (z - y,  y)dy ． o x
Z
-\infty 

特别地,  当 X 与 Y 相互独立时,  有
+\infty +\infty
f (z) = \int f (x,  z - x)dx = \int f (x) f (z - x)dx
Z X Y
-\infty -\infty
+\infty +\infty
= \int f (z - y,  y)dy = \int f (z - y) f (y)dy
X Y
-\infty -\infty
这两个积分即是函数 f (x) 与 f (y) 的卷积．
X Y 

例4 已知 X 与 Y 相互独立,  它们概率密度函数分别为
2x,   0 \leq x \leq 1,   e-y,   y \ge 0,  
f (x) = f (y) =
 
X 0,   其它,   Y 0,   y < 0,  
 
求 Z = X + Y 的概率密度函数．
+\infty +\infty
解1 (卷积公式) f (z) = \int f (z - y) f (y)dy = \int e-y f (z - y)dy
Z X Y X
-\infty 0
2(z - y),   0 \leq z - y \leq1,   2(z - y),   z -1\leq y \leq z,  
f (z - y) =  即 f (z - y) = 
X 0,   其它,   X 0,   其它．
  

 y \in[0,  + \infty) 2(z - y),   z -1\leq y \leq z ,  
f (z - y) =

 取公共部分,   X 0,   其它,  

y \in[z -1,  z]

e-y ,   y \ge 0,  
f (y) =

Y
0,   y < 0．
+\infty 
f (z) = \int e-y f (z - y)dy
则
Z X
0
0,   z < 0,  
z
\int 2(z - y)e-ydy = 2(e-z + z -1),   0 \leq z \leq 1,  
=
0
z
\int 2(z - y)e-ydy = 2e-z,   z > 1．
z-1 

+\infty 1
解2 (卷积公式) f (z) = \int f (x) f (z - x)dx = \int 2xf (z - x)dx
Z X Y Y
-\infty 0
2x,   0 \leq x \leq 1,   ex-z,   x \leq z,  
f (x) = f (z - x) =
 
X 0,   其它,   Y 0,   x > z,  
 
0,   z < 0,  
x \in(-\infty,  z]

z
f (z) = \int 2xex-zdx = 2(e-z + z -1),   0 \leq z \leq 1,    x \in[0,  1]
Z
0
1
\int 2xex-zdx = 2e-z,   z > 1．
0 

3．M = max(X ,  Y ) 及 N = min(X ,  Y )的分布
设 X \sim F (x),  Y \sim F (y),  且 X 与 Y 相互独立,  则
X Y
F (z) = P{M \leq z} = P{X \leq z,  Y \leq z}= P{X \leq z}P{Y \leq z}= F (z)F (z)
max X Y
F (z) = P{N \leq z} = 1- P{N > z}= 1- P{X > z,  Y > z}
min
= 1- P{X > z}P{Y > z}= 1- (1- P{X \leq z})(1- P{Y \leq z})
= 1- (1- F (z))(1- F (z))．
X Y 

3 4
例5 设 P{X \ge 0,  Y \ge 0} = ,  P{X \ge 0} = P{Y \ge 0} = ,  求 P{max(X ,  Y ) \ge 0}.
7 7
解 P{max(X ,  Y ) \ge 0} = P{(X \ge 0) \cup (Y \ge 0)}
= P{X \ge 0}+ P{Y \ge 0}- P{X \ge 0,  Y \ge 0}
4 4 3 5
加法公式！
= + - = ．
7 7 7 7  -->
 

## 第三章 随机变量的数字特征 

???+ abstract
    通常把刻划随机变量的某些特征的确定的数值称为数字特征．

    - 反映随机变量取值的集中位置——数学期望
    - 反映随机变量取值的分散程度——方差
    - 反映两个随机变量的线性关联程度——相关系数

### 3.1  数学期望 

#### 3.1.1 随机变量的数学期望

**离散型随机变量的数学期望** 设离散型随机变量 $X$ 的分布律为 $P \{X = x_i \} = p_i$ ,  若级数 $\sum _i x_i p_i$ 绝对收敛,  则称该级数和为 $X$ 的数学期望,   记为 $E(X ) = \sum _i x_i \cdot p_i$

**连续型随机变量的数学期望** 设连续型随机变量 $X$ 的概率密度函数为 $f(x)$ ,  若积分 $\int _{- \infty} ^{+ \infty} xf(x)dx$ 绝对收敛,  则称积分值为 $X$ 的数学期望,   记为 $E(X ) = \int _{- \infty} ^{+ \infty} xf(x)dx$

???+ example "数学期望"
    设随机变量 $X$ 的概率密度函数为 

    $$
    f (x) =
    \begin{cases} 
    x ,  \space 0 \le x \le 1 \\
    2 - x ,  \space 1 < x \le 2 \\
    0 ,  \space 其他
    \end{cases}
    $$

    求 $X$ 的数学期望 $E(X )$

    **解** 由定义可知 $E(X ) = \int _{- \infty} ^{+ \infty} xf(x)dx = \int _0 ^1 x \cdot xdx + \int _1 ^2 x \cdot (2-x)dx = 1$

#### 3.1.2 随机变量函数的数学期望

**定理** 设 $Y = g(X )$ ($g$为连续函数),  

- 若 $X \sim P\{X = x_i \}  = p_i ,  i = 1,  2,  ...$,  则 $E(Y ) = E[g(X )] = \sum _i g(x_i ) p_i$
- 若 $X \sim f (x)$,  则 $E(Y ) = E[g(X )] = \int _{- \infty} ^{+ \infty} g(x) f (x)dx$

???+ example "数学期望"
    对圆的半径作近似测量,  假设其值 $X$ 均匀的分布在 $[a,  b]$ 内,  即

    $$
    F(x) = 
    \begin{cases} 
    \frac{1}{b-a} ,  \space a \le x \le b \\
    0 ,  \space 其他
    \end{cases}
    $$

    求圆的面积的数学期望．

    **解** 设 $Y$ 表示圆的面积,  则 $Y = \pi X ^2$ 

    $E(Y ) = E(\pi X^2) = \int _{- \infty} ^{+ \infty} \pi x^2 f (x)dx = \int _a ^b  \pi x^2 \frac{1}{b-a} dx  = \frac{\pi (a^2 + ab + b^2)}{3}$

???+ warning
    - 定理的意义在于不用求$Y$的分布,  只需用 $X$ 的分布,  就可算出$E(Y)$
    - 定理可推广到二维随机变量函数的情形：设 $Z = g(X ,  Y )$ ($g$为连续函数),  
        - 若 $(X ,  Y ) \sim P \{X = x_i ,  Y = y_i \} = p _{ij},  (i,  j = 1,  2,  ...)$,  则 $E(Z) = E[g(X ,  Y )] = \sum _i \sum _j g(x_i,  y_j ) p_{ij}$
        - 若 $(X ,  Y ) \sim f (x,  y)$,  则 $E(Z) = E[g(X ,  Y )] = \int _{- \infty} ^{+ \infty} \int _{- \infty} ^{+ \infty} g(x,  y) f (x,  y)dxdy$

???+ example "数学期望"
    $$
    (X ,  Y ) \sim f (x,  y) = 
    \begin{cases} 
    x+y ,  \space 0 \le x \le 1,  0 \le y \le 1 \\
    0 ,  \space 其他
    \end{cases}
    $$ 

    求 $E(X + Y )$

    **解** $E(X + Y ) = \int _{- \infty} ^{+ \infty} \int _{- \infty} ^{+ \infty} (x + y) f (x,  y)dxdy = \int _0 ^1 \int _0 ^1 (x + y) \cdot (x+y)dxdy = \frac{7}{6}$


#### 3.1.3 数学期望的性质

1. 若 $a \leq X \leq b$ ,  则 $a \leq E(X ) \leq b$．特别 $E(c) = c$．
2. **线性性质** $E(aX + bY + c)= aE(X ) + bE(Y ) + c$．
3. 若 $X$ 与 $Y$ 相互独立,  则 $E(XY )= E(X )E(Y )$．(反之不成立)

???+ note
    性质2,  3可推广到 $n$ 个随机变量的情形． 

### 3.2  方差  

方差反映的是 $X$ 的取值与其期望值的偏离程度．

**定义** 设 $X$ 是一随机变量,  若 $E[X - E(X )]^2$ 存在,  则称其为 $X$ 的方差,  记为 $Var(X ) = D(X ) = E[X - E(X )]^2 $．而称 $\sigma (X ) = \sqrt{D(X )}$ 为 $X$ 的标准差(或均方差)． 

#### 3.2.1 方差的计算

- 方差是随机变量函数 $g(X ) = [X - E(X )]^2$ 的期望
    - 设 $X \sim P \{X = x _i\} = p_i ,  i =1,  2,  ...$, 则 $D(X ) = \sum _i [x - E(X )] ^2 p_i$
    - 设 $X \sim f (x)$,  则 $D(X ) = \int _{- \infty} ^{+ \infty} [x - E(X )] ^2 f (x)dx$
- $D(X ) = E(X ^2) - E^2 (X )$

    > **证** $D(X ) = E[X - E(X )]^2 = E[X ^2 - 2X \cdot E(X ) + E^2(X )] = E(X ^2) - 2E(X ) \cdot E(X ) + E^2(X )= E(X ^2) - E^2(X )$

#### 3.2.2 方差的性质

- $D(C) = 0$
- $D(aX + b) = a ^2 D(X )$
- 若 $X ,  Y$ 相互独立,  则 $D(X \pm Y ) = D(X ) + D(Y )$
    - **推论** 设 $X_1 ,  X_2 ,  ...,  X_n$ 相互独立,  则 
    
        $$
        D (\sum _{i=0} ^n X_i) = \sum _{i=0} ^n D(X_i )
        $$

???+ example "方差"
    设 $X$ 的期望 $E(X ) = \mu$ ,  方差 $D(X ) = \sigma ^2 \not = 0$,  求标准化随机变量 $X^* = \frac{X - \mu}{\sigma}$ 的期望和方差.

    **解** $E(X *) = E(\frac{X - \mu}{\sigma}) = \frac{1}{\sigma} E(X - \mu) = \frac{1}{\sigma} [E(X ) - \mu] = 0$

    $D(X *) = D(\frac{X - \mu}{\sigma})  = D(\frac{X}{\sigma} - \frac{\mu}{\sigma}) = (\frac{1}{\sigma})^2 D(x) = 1$

### 3.3 协方差与相关系数 

#### 3.3.1 相关系数的定义和计算

**定义** 称 $Cov(X ,  Y ) = E \Big[ \big(X - E(X ) \big) \cdot \big(Y - E(Y ) \big) \Big]$ 为 $X$ 与 $Y$ 的协方差,  称标准化随机变量的协方差.

$$
\rho _{\tiny XY} = \frac{Cov(X ,  Y )}{\sqrt{D(X )} \sqrt{D(Y )}}
$$

为 $X$ 与 $Y$ 的相关系数．

???+ note 
    - $\rho _{\tiny XY},  \space | \rho _{\tiny XY} | \leq 1$ 是随机变量间线性关系的量度
    - 当 $\rho = 0$ 时,  称 $X$ 与 $Y$ 不相关．

???+ note "协方差的性质"
    - $Cov(X ,  Y ) = E(XY ) - E(X )E(Y )$,  特别的,  $Cov(X ,  X ) = D(X )$

        > **证** $Cov(X ,  Y ) = E \Big[ \big(X - E(X ) \big) \cdot \big(Y - E(Y ) \big) \Big] = E [ XY - XE(Y) - YE(X) + E(X)E(Y) ] = E(XY) - E(X)E(Y) - E(Y)E(X) + E(X)E(Y) = E(XY ) - E(X )E(Y )$

    - $Cov(aX ,  bY ) = ab \cdot Cov(X ,  Y )$
    - $Cov(X_1 + X _2,  Y ) = Cov(X_1 ,  Y ) + Cov(X_2 ,  Y )$
    - $D(X \pm Y ) = D(X ) + D(Y ) \pm 2Cov(X ,  Y )$ 

???+ example "协方差"
    设 $D(X ) = 36,  D(Y ) = 25,  \rho _{\tiny XY} = 0.4$,  求 $D(X \pm Y )$．

    **解** 

    $$
    \rho _{\tiny XY} = \frac{Cov(X ,  Y )}{\sqrt{D(X )} \sqrt{D(Y )}} = \frac{Cov(X ,  Y )}{6 \times 5} = 0.4 \\
    \implies Cov(X ,  Y ) = 12
    $$

    - $D(X + Y ) = D(X ) + D(Y ) + 2Cov(X ,  Y ) = 36 + 25 + 24 = 85$
    - $D(X -Y ) = D(X ) + D(Y ) - 2Cov(X ,  Y )= 36 + 25 - 24 = 37$

#### 3.3.2 协方差与相关系数的性质

**定理** 对于随机变量 X 与 Y ,  下列命题等价：

- $E(XY ) = E(X )E(Y )$
- $D(X \pm Y ) = D(X ) + D(Y )$
- $Cov(X ,  Y ) = 0$
- $\rho _{\tiny XY} = 0$

???+ warning
    - 独立性表示不存在任何直接关系,  而不相关表示不存在线性关系,  但不排除有其它的关系
    - 所有数字特征的计算都归结为期望的计算
    - X与Y独立可以推出上面四个结论, 但上面四个结论无法推出X与Y独立

???+ example
    设 $(X ,  Y )$ 的联合概率密度函数为 

    $$
    f(x, y) = 
    \begin{cases} 
    \frac{1}{\pi} ,  x^2 + y^2 \le 1 \\
    0 ,  \space 其他
    \end{cases}
    $$

    试求 $E(X ),  E(Y ),  E(XY ),  D(X ),  D(Y ),  Cov(X ,  Y ),  \rho _{\tiny XY}$ 

    > 注意观察函数的构造, 使用对称性和奇偶性简化计算

    **解** 记 $D：x^2 + y^2 \leq 1,  E(X ) = \iint _{\R ^2} xf(x, y)  dxdy = \iint _D xf(x, y)  dxdy = \iint _D x \cdot \frac{1}{\pi} dxdy = 0$ (奇偶性)

    同理：$E(Y ) = 0$

    $E(XY ) = \iint _{\R ^2} xy \cdot f(x, y)  dxdy = \iint _D xy \cdot f(x, y)  dxdy = 0$

    $D(X) = E(X^2) - E^2 (X) = E(X^2) = \iint _{\R ^2} x^2 \cdot f(x, y)  dxdy = \iint _D x^2 \cdot f(x, y)  dxdy = \iint _D x^2 \cdot \frac{1}{\pi} dxdy = \frac{1}{4}$

    同理 $D(Y ) = \frac{1}{4} ,  Cov(XY ) = E(XY ) - E(X )E(Y ) = 0,  \rho _{\tiny XY} = 0$

## 第四章 几类重要的概率分布 

### 4.1  二项分布 $X \sim B(n,  p)$

???+ abstract
    两点分布(伯努利分布)是特殊的二项分布.

#### 4.1.1 两点分布(伯努利分布)

**伯努利试验** 只有两种可能结果的试验称为伯努利试验．通常把这两个结果 $A$ 和 $\bar{A}$ 称为“成功”和“失败”．

> 任一试验均可视为只有结果 $A$ 和 $\bar{A}$ 的伯努利试验．

**两点分布** 在一次伯努利试验中,  设 $P(A) = p \space (0 < p < 1)$,  记 $X$ 为 $A$ 发生的次数,  则 $X$ 的分布律为

$$
\begin{array}{c|cc}
X & 0 & 1 \\
\hline
P & 1-p & p
\end{array}
$$

称 $X$ 服从 **伯努利分布(Bernoulli Distribution)或两点分布**,  记为$X \sim B(1,  p)$． 

#### 4.1.2 二项分布

**n重伯努利试验** 将伯努利试验独立重复地进行 n 次．

???+ example
    连续抛掷两枚均匀的硬币100次,  令 $X$ 表示双正面出现的次数,  则 $P \set{ X = 30 } = C_{100} ^{30} (\frac{1}{4})^{30} (1- \frac{1}{4}) ^{100-30} $

**二项分布** 在 $n$ 重伯努利试验中,  设 $P(A) = p (0 < p < 1)$,  则事件 $A$ 恰好发生 $k$ 次的概率为 $P \set{X = k} = P_n (k) = C _n ^k p^k (1- p) ^{n-k} ,  k = 0,  1,  2,  ...,  n$ ,  称 $X$ 服从参数为 $n,  p$ 的二项分布,  记为 $X \sim B(n,  p)$．

???+ note "二项分布的数字特征" 
    设 $X \sim B(n,  p)$．则 

    - $E(X ) = np$
    - $D(X ) = np(1- p)$

???+ example "二项分布-有放回的抽样"
    若在 M 件产品中有 N 件次品,  现进行有放回的 n 次抽样检查,  问共取得 k 件次品的概率．

    **解** 由于是有放回的抽样,  因此过程是 n 重伯努利试验．记 A 为“抽到次品”,  则 $P(A) = \frac{N}{M}$ ,   令 $X$ 为 n 次抽样检查中抽到的次品数,  则 $X \sim B (n, \frac{N}{M})$,由二项分布得 

    $P \set{X = k} = C _n ^k (\frac{N}{M})^k (1- \frac{N}{M}) ^{n-k}$

#### 4.1.3 几何分布

???+ example "几何分布"
    设某批产品的次品率为p,  对该批产品做有放回的抽样检查,  直到第一次抽到一只次品为止 (在此之前抽到的全是正品),  求所抽到的产品数 X 的分布律．

    **解** X 的所有可能取值为1,  2,  ...,  设 $A_i$ = {抽到的第 i 个产品是正品},  则

    $P \set{X = k} = (1 - p)^{k - 1}p, \space k = 1, 2, 3, \cdots$

    > 几何分布用来描述某试验“首次成功”的概率模型． 

### 4.2  泊松分布 $X \sim P(\lambda)$

**定义** 设离散型随机变量 $X$ 的分布律为 $P \{X = k \} = \frac{\lambda ^k}{k!} e ^{- \lambda} ,   \lambda > 0,  k = 0,  1,  2,  ...$,  则称 $X$ 服从参数为 $\lambda$ 的 **泊松分布(Poisson Distribution)**,  记为 $X \sim P(\lambda)$ ． 

???+ note "泊松分布的数字特征"
    设 $X \sim P(\lambda)$,   即 $P \{X = k \} = \frac{\lambda ^k}{k!} e ^{- \lambda} ,   \lambda > 0,  k = 0,  1,  2,  ...$,  则 

    - $E(X ) = \lambda$
    - $D(X ) = \lambda$

???+ tip
    - “流量”问题 (电话接到的呼叫次数,  车站来到的乘客数,  热电子辐射数等) 大都服从泊松分布；
    - 作为大量试验中稀有事件 (不幸事件,  意外事故,  非常见病,  自然灾害等) 发生的概率模型． 

{==二项分布的泊松逼近==}

**定理** 设 $X \sim B(n,  p)$,  则当 $n \to \infty$ 时,  $X$ 近似服从 $P(\lambda)$,   即有 $C _n ^k p^k (1- p) ^{n-k} \approx \frac{\lambda ^k}{k!} e ^{- \lambda} ,   \lambda > 0,  k = 0,  1,  2,  ...$．其中 $\lambda = np$

> 当 $n$ 很大且 $p$ 很小时,  才能使近似计算的误差较小． 

???+ example "二项分布的泊松逼近"
    假设儿童在注射某疫苗产生不良反应的概率为0.001,  试确定2000个儿童中有3个以及2个以上产生不良反应的概率．

    **解** 设 $X$ 表示注射疫苗的儿童中产生不良反应的个数,  则 $X \sim B(2000,  0.001)$,  因 $n$ 很大且 $p$ 很小,  所以由二项分布的泊松逼近得 $X \sim P(2)$

    $P \set{X = k} = \frac{2^k}{k!} e^{-2},  k = 0,  1,  \cdots$

    故 $P \set{X = 3} = \frac{2^3}{3!} e^{-2} = 0.18045$ 
    
    $ P \set{X > 2} = P \set{X \ge 3} \approx \sum _{k=3} ^{+\infty} \frac{3^k}{k!} e^{-2}  = 0.32332$

    > 需要查表

???+ example "二项分布的泊松逼近"
    设某保险公司为社会提供一项人寿保险,  已知参保人死亡概率为0.0020,  每年需交120元保险金,  死亡时家属可领取 2 万元保险金,  现有2500人参保,  求该保险公司亏本以及年赢利不少于10万元的概率?

    **解** 设 $X$ 为参保人员死亡的人数,  则 $X \sim B(2500,  0.002)$ ,  由二项分布的泊松逼近 可得 $X \sim P(5)$

    P{公司亏本} = $P \set{X > 15} = P \set{X \ge 16} \approx \sum _{k=16} ^{+\infty} \frac{5^k}{k!} e^{-2}  = 0.00007$

    P{赢利不少于10万} = $P \set{X \leq 10} = 1 - P \set{X > 10} = 1 - P \set{X \ge 11} \approx 1 - \sum _{k=11} ^{+\infty} \frac{5^k}{k!} e^{-2}  = 0.9863$

    > 计算过程省略了通过不等式求亏损和盈利的步骤, 需要查表


### 4.3  正态分布 $X \sim N(\mu,  \sigma ^2)$

#### 4.3.1 正态分布

**定义** 若随机变量 $X$ 的概率密度函数为

$$
f (x) = \frac{1}{\sqrt{2 \pi} \sigma} e ^{\frac{-(x- \mu) ^2}{2 \sigma ^2}},  \space - \infty < x < + \infty
$$

其中 $\mu,  \sigma \space (\sigma  > 0)$ 是常数,  则称 $X$ 服从参数为 $\mu,  \sigma ^2$ 的 **正态分布(Normal Distribution)或Gauss分布**,   记为 $X \sim N(\mu,  \sigma ^2)$．

特别地,  当 $\mu = 0,  \sigma  =1$ 时,  称 $X$ 服从标准正态分布,  记为 $X \sim N(0,  1)$,  其概率密度函数、分布函数记为 $\varphi (x)$ 和 $\varPhi (x)$． 

概率密度函数 $f (x) = \frac{1}{\sqrt{2 \pi} \sigma} e ^{\frac{-(x- \mu) ^2}{2 \sigma ^2}}$ 的性质：

???+ success inline end
    ![正态分布.png](https://s2.loli.net/2025/05/09/AaodmsVkIY45lg6.png)

- $f (x)$ 的各阶导数均存在
- 密度曲线以 $x$ 轴为渐近线；
- $f (x)$ 关于 $x = \mu$ 对称
- $f (x)$ 在 $x = \mu$ 取得最大值 $\frac{1}{\sqrt{2 \pi} \sigma}$ 

???+ note "正态分布的数字特征"
    设 $X \sim N(\mu,  \sigma ^2)$,  则

    - $E(X ) = \mu$
    - $D(X ) = \sigma ^2$ 

???+ success inline end
    ![标准正态分布.png](https://s2.loli.net/2025/05/09/kXftWSj4A6pYFsd.png)

???+ note "标准正态分布的计算"
    $\forall x > 0,  \varPhi (-x) = 1- \varPhi (x)$ , 计算时查表即可．

???+ example
    设 $X \sim N(0,  1)$,  则有

    - $P\{X \leq 2.38\}  =\varPhi (2.38)= 0.991344$
    - $P\{X < -2.38\}  =\varPhi (-2.38) = 1-\varPhi (2.38) = 0.008656$
    - $P\{-2 < X < 0\}  =\varPhi (0) -\varPhi (-2) = 0.5 -[1-\varPhi (2)] = 0.47725$

#### 4.3.2 非标准正态分布的计算

将非标准正态分布转换为标准正态分布进行计算.

若 $X \sim N(\mu,  \sigma ^2)$,  则有 $Y = \frac{X - \mu}{\sigma} \sim N(0,  1)$,  从而可得

$$
P\{X \leq x\}  = P\{\frac{X - \mu}{\sigma} \leq \frac{x - \mu}{\sigma} \} \\
= P\{Y \leq \frac{x - \mu}{\sigma} \}= \varPhi (\frac{x - \mu}{\sigma})
$$

???+ example
    设 $X \sim N(2,  9)$,  则有 $P \{1 \leq X < 5 \} = P \{\frac{1-2}{3} \leq \frac{X-2}{3} < \frac{5-2}{3} \} =\varPhi (1) -\varPhi ( - \frac{1}{3}) = 0.47064$

???+ tip "正态分布的应用"
    零件的尺寸、物种的生理特征、测量误差、某地区年降雨量等绝大多数随机现象都服从正态分布． 

???+ note "有关正态分布的结论"
    - 若 $X \sim N(\mu ,  \sigma ^2)$,  则对任意常数$a ,  b$ 有 $aX + b \sim N(a \mu + b ,  a ^2 \sigma ^2)$
    - 若 $X \sim N(\mu _1,  \sigma _1 ^2),  Y \sim N(\mu _2,  \sigma _2 ^2)$,  且 $X$ 与 $Y$ 独立,  则 $X \pm Y \sim N(\mu _1 \pm \mu _2 ,  \sigma _1 ^2 + \sigma _2 ^2)$
    
    > 一般地,  n 个相互独立且服从正态分布的随机变量的线性组合仍服从正态分布

???+ note "$3 \sigma$  法则" 
    若 $X \sim N(\mu ,  \sigma ^2)$,  则

    - $P \{\mu - \sigma \leq X \leq \mu + \sigma \} = P \{-1 \leq \frac{X - \mu}{\sigma} \leq 1 \} = \varPhi (1) - \varPhi (-1) = 2 \varPhi (1) - 1 = 0.6826$
    - $P \{\mu - 2 \sigma \leq X \leq \mu + 2 \sigma \} = P \{-2 \leq \frac{X - \mu}{\sigma} \leq 2 \} = \varPhi (2) - \varPhi (-2) = 2 \varPhi (2) - 1 = 0.9545$
    - $P \{\mu - 3 \sigma \leq X \leq \mu + 3 \sigma \} = P \{-3 \leq \frac{X - \mu}{\sigma} \leq 3 \} = \varPhi (3) - \varPhi (-3) = 2 \varPhi (3) - 1 = 0.9973$

???+ example "正态分布"
    设 $X \sim N(0,  1),  Y \sim N(1,  2)$,  且它们相互独立,  试求 $Z = 2X + Y -1$ 的概率密度函数．

    **解** 因 Z 也服从正态分布,  故只需确定 Z 的期望和方差即可求出 Z 的概率密度函数．

    - $E(Z) = 2E(X ) + E(Y ) -1 = 2 \times  0 +1-1 = 0$
    - $D(Z) = 2^2 D(X ) + D(Y ) = 2^2  \times 1+ 2 = 6$

    所以 Z 的概率密度函数为 

    $$
    f (x) = \frac{1}{\sqrt{2 \pi} \sqrt{6}} e ^{- \frac{x^2}{12}},  \space Z \in \R
    $$

???+ example "正态分布"
    公共汽车车门高度是按男子与车门顶碰头机率在0.01以下设计,  设男子身高 $X \sim N(170,  6^2)$ (单位cm),  试确定车门高度．

    **解** 设车门高度为 x cm,  则 $P\{X > x\}  < 0.01$ 即 $P\{X \leq x\}  > 0.99$

    $P \set{X \leq x} = P \set{\frac{X - 170}{6} \le \frac{x - 170}{6}} = \varPhi (\frac{x - 170}{6})  > 0.99$

    查表得 $\varPhi (2.33) = 0.9901 > 0.99$ 则 $\frac{x - 170}{6} = 2.33$

    解得 $x =183.98cm$

### 4.4  二维正态分布 $(X ,  Y ) \sim N(\mu _1 ,  \mu _2 ；\sigma _1 ^2,  \sigma _2 ^2；\rho)$

**定义** 若二维随机变量 $(X ,  Y )$的联合概率密度函数为

$$
f(x,  y) = \frac{1}{2 \pi \sigma _1 \sigma_2 \sqrt{1- \rho ^2}} \exp \{(-\frac{1}{2(1-\rho^2)}[(\frac{x-\mu_1}{\sigma_1})^2 - 2\rho(\frac{x-\mu_1}{\sigma_1})(\frac{y-\mu_2}{\sigma_2}) + (\frac{y-\mu_2}{\sigma_2})^2] \}
$$

???+ success inline end
    ![n.webp](https://s2.loli.net/2025/06/08/gBpC8lHYcFJh4mn.webp)

其中 $\mu ,  \mu ,  \sigma  ,  \sigma  ,  \rho$ 为常数,  并且有 $\sigma _1 > 0,  \sigma _2 > 0,  | \rho |<1$,  则称 $(X ,  Y )$ 服从二维正态分布,   记为 $(X ,  Y ) \sim N(\mu _1 ,  \mu _2 ；\sigma _1 ^2,  \sigma _2 ^2；\rho)$

**定理** 若 $(X ,  Y ) \sim N(\mu _1 ,  \mu _2 ；\sigma _1 ^2,  \sigma _2 ^2；\rho)$,  则有

- $E(X ) = \mu _1,  D(X ) = \sigma _1 ^2$
- $E(Y ) = \mu  _2,  D(Y ) = \sigma _2 ^2$
- $Cov(X ,  Y ) = \rho \sigma _1 \sigma _2 ,  \rho _{XY} = \rho$
- $X \sim N(\mu _1,  \sigma _1  ^2),  Y \sim N(\mu _2,  \sigma _2 ^2)$
- 如果 $X$ 与 $Y$ 相互独立 $\implies \rho = 0$

> $(X ,  Y )$服从二维正态分布的充要条件是 $X$ 与 $Y$ 的任一线性组合服从一维正态分布． 

???+ example "二维正态分布"
    已知随机变量 $X$ 和 $Y$ 分别服从正态分布 $N(1,  3^2)$ 和 $N(0,  4^2)$ ,  且 $X$ 与 $Y$ 的相关系数 $\rho _{\tiny XY} = - \frac{1}{2}$ ,  设 $Z = \frac{1}{3} X + \frac{1}{2} Y$,  求： $Z$ 的数学期望 $E(Z)$ 和方差 $D(Z)$ ； $X$ 与 $Z$ 的相关系数 $\rho _{\tiny XZ}$

    **解** 由已知得 $E(X ) = 1,  D(X ) = 3^2 ,  E(Y ) = 0 ,  D(Y ) = 4^2 $

    $Cov(X ,  Y ) = \rho {\tiny XY} \sqrt{D(X )} \sqrt{D(Y )} = - \frac{1}{2} \times 3 \times  4 = -6$

    - $E(Z) = E(\frac{1}{3} X + \frac{1}{2}Y) = \frac{1}{3} E(X ) + \frac{1}{2} E(Y ) = \frac{1}{3} \times 1 + \frac{1}{2} \times 0 = \frac{1}{3}$
    - $D(Z) = D(\frac{1}{3} X + \frac{1}{2}Y) + 2 Cov(\frac{1}{3}X \cdot \frac{1}{2}Y) = \frac{1}{9} D(X ) + \frac{1}{4} D(Y ) + 2 \cdot \frac{1}{3} \cdot \frac{1}{2} Cov(X, Y) = \frac{1}{9} \times 9 + \frac{1}{4} \times 16 + 2 \cdot \frac{1}{3} \cdot \frac{1}{2} \cdot (-6) = 3$
    - $Cov(X ,  Z) = Cov (X ,  \frac{1}{3} X + \frac{1}{2}Y) = \frac{1}{3} Cov(X ,  X ) + \frac{1}{2}Cov(X ,  Y ) = \frac{1}{3} D(X ) + \frac{1}{2} Cov(X ,  Y ) = 0$

    $\therefore \rho _{\tiny XZ} = 0$

### 4.5 指数分布 $X \sim E(\lambda)$ 或 $X \sim Exp(\lambda)$

**定义** 若随机变量 $X$ 的概率密度函数为 

$$
f(x) = \begin{cases} 
\lambda e ^{- \lambda x},  \space  x \ge 0 \\ 
0,  \space x < 0 
\end{cases}
\space , \lambda > 0
$$

则称 $X$ 为服从参数为 $\lambda$ 的指数分布,  记为 $X \sim E(\lambda)$

分布函数 

$$
F(x) = \int _{- \infty} ^x \space f(t) dt = \begin{cases}
1- e ^{- \lambda x},  \space  x \ge 0 \\
0,  \space x < 0
\end{cases}
$$

???+ note "指数分布的数字特征"
    设 $X \sim E(\lambda)$,  则 

    - $E(X ) = \frac{1}{\lambda}$
    - $D(X ) = \frac{1}{\lambda ^2}$

???+ tip "指数分布的应用" 
    电子元件的寿命,  随机服务系统中的服务时间等． 

???+ note "无记忆性 (永葆青春的分布)"
    设 $X \sim E(\lambda)$,  则 $\forall t > 0,  s > 0$,  有条件概率

    $$
    P \{X > s + t \space | \space X > t \} = \frac{P \{X > s + t \}}{P \{X > t \}} \\
    \space \\
    = \frac{1 - P \{X \leq s + t \}}{1 - P \{X \leq t \}} \\
    \space \\
    = \frac{1 - [1 - e ^{- \lambda (s + t)}]}{1 - (1 - e ^{- \lambda t})} = e ^{- \lambda s}
    $$

    > 结果与 $t$ 没有关系,  即再活多少年的概率是一样的． 

???+ example "指数分布"
    设打电话所用的时间 $X \sim E(\lambda)$ 的指数分布,  且打一次电话平均用时为5分钟,  求一次通话用时在5-10分钟的概率．

    **解** 因为 $X \sim E(\lambda)$,  而 $E(X ) = \frac{1}{\lambda} = 5$,  所以 $X \sim E(\frac{1}{5})$ ,  则 X 的密度函数为 

    $$
    f(x) = \begin{cases} 
    \frac{1}{5} e ^{- \frac{x}{5}},  \space  x \ge 0 \\ 
    0,  \space x < 0 
    \end{cases}
    $$

    $P \set{5 \leq X \leq 10} = \int _5 ^{10} \frac{1}{5} e ^{- \frac{x}{5}} dx = 0.2326$

### 4.6 均匀分布 $X \sim U[a,  b]$

**定义** 若随机变量 $X$ 的概率密度函数为

$$
f (x) = \begin{cases}
\frac{1}{b - a},  \space a \leq x \leq b \\
0,  \space 其他
\end{cases}
\space , a < b
$$

则称 $X$ 在区间 $[a,  b]$ 上服从均匀分布,   记为 $X \sim U[a,  b]$．

???+ note "均匀分布的数字特征"
    设 $X \sim U[a,  b]$．则 

    - $E(X ) = \frac{a + b}{2}$
    - $D(X ) = \frac{(b - a) ^2}{12}$

???+ tip "均匀分布应用"
    四舍五入造成的误差,  计算机产生的随机数等． 

???+ example "均匀分布"
    设随机变量 $X \sim  E(2)$ 的指数分布,  证明随机变量 $Y = 1- e^{-2X}$ 在区间 [0,  1] 上服从均匀分布．

    **解** X 的概率密度函数为

    $$
    f(x) = \begin{cases} 
    2 e ^{- 2x},  \space  x \ge 0 \\ 
    0,  \space x < 0 
    \end{cases}
    $$

    $Y$ 的分布函数为 
    
    $$
    F_Y ( y) = P \set{Y \leq y} = P \set{1- e^{-2X} \leq y} \\
    \begin{cases} 
    P(\empty) = 0,  \space  y < 0 \\ 
    P \set{X \le - \frac{1}{2}ln(1-y)} = y,  \space  y \le 1 \\ 
    P(\varOmega) = 1,  \space y > 1 
    \end{cases}   
    $$

    求导得到概率密度函数,服从均匀分布


### 4.7  二维均匀分布

**定义** 设$D$是平面上的一个有界区域,  其面积为$A$,  若二维随机变量$(X ,  Y )$ 的联合概率密度函数为

$$
f (x,  y) = \begin{cases}
\frac{1}{A},  (x ,  y ) \in D \\
0,  (x ,  y ) \notin D
\end{cases}
$$

则称 $(X ,  Y )$在 $D$ 上服从二维均匀分布．

例如,  矩形区域上的均匀分布,  其概率密度函数为

$$
f (x,  y) = \begin{cases}
\frac{1}{(b-a)(d-c)},  a \le x \le b,  \space c \le y \le d \\
0,  其他
\end{cases}
$$

???+ example "二维均匀分布"
    设二维随机变量 $(X ,  Y )$ 在圆域 $x^2 + y^2 \leq r^2$ 上服从二维均匀分布, 求 X 与Y 的相关系数 $\rho _{\tiny XY}$ ；问 X 与Y 是否相互独立．

    **解** (X ,  Y )的联合概率密度函数为

    $$
    f (x,  y) = \begin{cases}
    \frac{1}{\pi r^2},  x^2 + y^2 \leq r^2 \\
    0,  其他
    \end{cases}
    $$

    记 $D: \space x^2 + y^2 \leq r^2$

    - $E(X ) = \iint _D x \cdot \frac{1}{\pi r^2}  dxdy = 0$ 
    - $E(Y ) = \iint _D y \cdot \frac{1}{\pi r^2}  dxdy = 0$ 
    - $E(XY ) = \iint _D  xy \cdot \frac{1}{\pi r^2}  dxdy = 0$

    $\therefore Cov(X ,  Y ) = E(XY ) - E(X )E(Y ) = 0 \implies \rho _{\tiny XY} = 0$

    ---

    $f_X (x) = \int _{- \infty} ^{+ \infty} f (x,  y)dy$ 

    - 当 $|x| > r$ 时,  $f_X (x) = 0$
    - 当 $|x| \leq r$ 时,   

        $$
        f_X (x) = \int _{- \sqrt{r^2 - x^2}} ^{+ \sqrt{r^2 - x^2}} \frac{1}{\pi r^2} dy = \frac{2}{\pi r^2} \sqrt{r^2 - x^2}
        $$

    $$
    \therefore
    f_X(x) = 
    \begin{cases} 
    \frac{2}{\pi r^2} \sqrt{r^2 - x^2} , \space |x| \le r \\
    0 , \space |x| > r
    \end{cases}
    $$

    同理

    $$
    f_Y(y) = 
    \begin{cases} 
    \frac{2}{\pi r^2} \sqrt{r^2 - y^2} , \space |y| \le r \\
    0 , \space |y| > r
    \end{cases}
    $$

    $$
    f(x,y) = 
    \begin{cases} 
    \frac{1}{\pi r^2} , x^2 + y^2 \le r^2 \\
    0 , \space 其他
    \end{cases}
    $$

    $\therefore f(x,y) \not = f_X(x) f_Y(y)$

    $\therefore X$ 与 $Y$ 不相互独立

## 第五章 基本极限定理 

### 5.1 切比雪夫不等式与大数定律

???+ abstract
    - 频率的稳定性,  用频率代替概率的科学性．
    - 用来阐明大量随机现象平均结果的稳定性的一系列定理称为大数定律．

#### 5.1.1 切比雪夫不等式

设 $X$ 的数学期望 $E(X ) = \mu$ ,  方差 $D(X ) = \sigma ^2 < \infty$ ,  则 $\forall \varepsilon > 0$ ,  有

- $P\{| \space X - \mu \space | \ge \varepsilon \} \le \frac{\sigma ^2}{\varepsilon ^2}$
- $P\{| \space X - \mu \space | < \varepsilon \} \ge 1- \frac{\sigma ^2}{\varepsilon ^2}$

> 切比雪夫不等式常用来在 $E(X )$ 和 $D(X )$ 已知时,   对事件 $P\{| \space X - E(X) \space | < \varepsilon \}$ 发生的概率进行估计． 

???+ example "切比雪夫不等式"
    已知我校有1万盏电灯,  夜晚每一盏灯开灯的概率均为0.8,  且它们开关与否相互独立,  试用切比雪夫不等式估计夜晚同时开灯 7800-8200 盏之间的概率．

    **解** 设 X 表示夜晚开灯数,  则 $X \sim B(10000,  0.8)$,  则 $E(X ) = 8000,  
    D(X ) = 1600$,  则由切比雪夫不等式知

    $P \set{7800 < X < 8200}= P \set{|X - 8000| < 200} \ge 1 - \frac{1600}{200^2} = 0.96 $

    > 这个概率说明只需供应8200盏灯的电力就能以相当大的概率保证这1万盏灯的正常使用

#### 5.1.2 切比雪夫大数定律

设相互独立的随机变量 $X_1 ,  X_2 ,  ...,  X_n ,  ...$ 具有有限的期望和方差,  若$\exists$ 常数 $C$ 使 $D(X_i ) \leq C$ ,  则 $\forall \varepsilon  > 0$,  有 

$$
\lim_{n \to \infty} P\{|\space \frac{1}{n} \sum_{i=1}^n X_i - E(\frac{1}{n} \sum _{i=1}^n X_i) \space | < \varepsilon \} = 1
$$

即

$$
\frac{1}{n} \sum_{i=1}^n X_i \xrightarrow{p}  E(\frac{1}{n} \sum _{i=1}^n X_i) \space (n \to \infty)
$$

**推论** 设相互独立的随机变量 $X_1 ,  X_2 ,  ...,  X_n ,  ...$ 服从相同的分布,  且 $E(X ) = \mu ,  D(X ) = \sigma ^2,  i = 1,  2,  ...$,  则有

$$
\frac{1}{n} \sum_{i=1}^n X_i \xrightarrow{p}  \mu \space (n \to \infty)
$$

???+ note
    该结论的实际意义在于,  为了减少测量的随机误差,  常常用测量的平均值来代替真实值,  即 

    $$
    \frac{1}{n} \sum_{i=1}^n X_i \approx \mu
    $$

#### 5.1.3 伯努利大数定律 (切比雪夫大数定律推论的特殊形式)

设 $u_n$ 是 $n$ 重伯努利试验中事件$A$发生的次数,  且 $P(A) = p$ ,  则有 

$$
\frac{u_n}{n} \xrightarrow{p}  p \space (n \to \infty) \\
\space \\
\frac{u_n}{n} = \frac{1}{n} \sum_{i=1}^n X_i \space ,  \space X_i \sim B(n,  p)
$$

> 该结论的实际意义在于,  当试验次数很大时,  便可以用事件发生的频率来代替其概率． 

#### 5.1.4 辛钦大数定律

设相互独立的随机变量 $X_1 ,  X_2 ,  ...,  X_n ,  ...$ 服从相同的分布,  且 $E(X_i ) = \mu \space,  i = 1,  2,  ...$,  则有

$$
\frac{1}{n} \sum_{i=1}^n X_i \xrightarrow{p}  \mu \space (n \to \infty)
$$

> 辛钦大数定律要求同分布但并不要求方差存在． 

### 5.2 中心极限定理 

???+ abstract
    若一个量受到大量独立的随机因素综合影响,  而每一因素在总影响中所起的作用并不大,  则这个量通常近似服从正态分布．

#### 5.2.1 独立同分布的中心极限定理

**Levy-Lindeberg中心极限定理** 设相互独立的随机变量 $X_1 ,  X_2 ,  ...,  X_n ,  ...$ 服从相同的分布,  且 $E(X ) = \mu ,  D(X ) = \sigma ^2 (\sigma  > 0)$,  则$\forall x \in \R$,  有

$$
\lim_{n \to \infty} P\{ \frac{\sum _{i=1}^n X_i - n \mu}{\sqrt{n} \sigma} \le x \} = \varPhi (x)
$$

即

$$
\frac{\sum _{i=1}^n X_i - n \mu}{\sqrt{n} \sigma} \sim  N(0,  1) \space (n \to \infty) \\
\\ 
\sum _{i=1}^n X_i \sim  N(n \mu,  n \sigma ^2) \space (n \to \infty)
$$

???+ example "独立同分布的中心极限定理"
    设某食品用机器装袋,  每袋净重的期望为100g,  标准差为4g, 一箱装100袋,  求一箱净重大于10100g的概率．

    **解** 设$ X_i$ 表示第 i 袋食品的净重,  则 $X_1 ,  X_2 ,  ...,  X_{100}$ 独立同分布,  且 $E(X_i ) = 100,  D(X_i ) = 16$,  而一箱净重 $X = \sum _{i=1} ^{100} X_i$ 

    由独立同分布的中心极限定理可知：$\frac{X - 100 E(X_i)}{\sqrt{100}D(X_i)} \sim N(0, 1)$,  即 $\frac{X - 10000}{40} \sim N(0, 1)$

    所以 $P\{X > 10100\}  = 1- P\{X \leq 10100\}  = 1- P \set{\frac{X - 10000}{40} \leq  \frac{10100 - 10000}{40}} = 1-\varPhi (2.5) = 0.0062$

    > 需要查表

#### 5.2.2 独立同分布的中心极限定理的特殊形式

**棣莫弗-拉普拉斯中心极限定理** 设 $u_n$ 是$n$重伯努利试验中事件$A$发生的次数,  且 $P(A) = p$,  则有 

$$
\frac{u_n -np}{\sqrt{np(1-p)}} \sim N(0,  1) \space (n \to \infty)
$$

???+ note "推论"
    设 $X \sim B(n,  p)$,  当$n$比较大时,  对 $\forall a < b$ 有

    $$
    P\{a < X \le b\} \approx \varPhi (\frac{b -np}{\sqrt{np(1-p)}}) - \varPhi (\frac{a -np}{\sqrt{np(1-p)}})
    $$

???+ example "拉普拉斯中心极限定理"
    保险公司多年统计资料表明,  因被盗理赔的用户占20%,  以 X 表示100个理赔用户中因被盗理赔的个数,  试写出X 的概率分布,  并利用拉普拉斯中心极限定理,  求被盗理赔用户大于14且不多于30户的概率近似值．

    **解** 易知 $X \sim B(100,  0.2)$,   则 X 的分布律为

    $P\{X = k\}  = C _{100} ^k 0.2^k 0.8^{100-k} ,   k = 0,  1,  ...,  100$

    已知 $n = 100,  p = 0.2, np = 20$,  由拉普拉斯中心极限定理得

    $P\{14 < X \le 30 \} \approx \varPhi (\frac{30 -20}{\sqrt{20(1-0.2)}}) - \varPhi (\frac{14 -20}{\sqrt{20(1-0.2)}}) = \varPhi(2.5) - \varPhi(-1.5) = 0.927$ 

    > 需要查表

???+ example "拉普拉斯中心极限定理"
    已知甲乙两地有A、B两种交通工具,  每天有1000人要从甲地去往乙地,  这1000人等概率的随机选择 A、B 两种工具中的其中一个,  问A、B两种交通工具上至少各准备多少个座位,  才能有99%的可能不会出现座位不够．

    **解** 设每种交通工具需准备 x个座位,  每天有 X 个人乘坐A交通工具
    易知 $X \sim B(1000,  0.5)$,  则 $n = 1000, p = 0.5, np = 500, 1 - p = 0.5$

    $P\{X \leq x\}  = P \set{\frac{X - 500}{\sqrt{500 \times 0.5}} \le \frac{x - 500}{\sqrt{500 \times 0.5}}} = \varPhi(\frac{x - 500}{\sqrt{500 \times 0.5}}) \ge 0.99$

    查表得 $\frac{x - 500}{\sqrt{500 \times 0.5}} \ge 2.33,  x \ge 536.8$,  每种交通工具需准备537个座位．

