# Solutions to Homework 0, Introdution to Modern Cryptography
Authors:

1. Dhruv Mishra, st154709@stud.uni-stuttgart.de, Matriculation number: 3293775

2. Ishan Adhaulia, st159571@stud.uni-stuttgart.de, Matriculation number: 3319219

3. Lukas Fromme, st101379@stud.uni-stuttgart.de, Matriculation number: 2798268

## 1. Possibilistic security
A possibilistically secure system can encrypt and decrypt messages, just like a perfectly secure system. However, a possibilistically secure system can potentially provide an attacker with information about the likelihood that a certain key was used. 

## 2. Variant of Vernam

#### (a) Define a decryption function d such that (X, K, Y, e, d) is a cryptosystem. Prove this statement.

choose d: $d(y,k) = y \oplus k \oplus c$

#### Show Perfect Correctness: $d(e(x,k),k) = x$
$d(e(x,k)k) = x \leftrightarrow d((x \oplus k \oplus c),k) = x \leftrightarrow (x \oplus k \oplus c) \oplus k \oplus c = x \leftrightarrow x \oplus k \oplus k \oplus c \oplus c = x \leftrightarrow x \oplus 0 \oplus 0 = x$

#### Show that there are no unnecessary ciphertexts: $y=\{e(x,k)|x,k \in \{0,1\}^l\}$
$y = \{0,1\}^l = \{x \oplus 0^l \oplus 0 | x \in \{0,1\}^l\} \subseteq \{e(x,k) | x,k \in \{0,\}^l\}$


#### (b) Show that this system is possibilistically secure: $\forall x \in X, y in Y, \exists k \in K with e(x,k) = y$
$e(x,k) = x \oplus k \oplus c = y$
$x = x(0)x(1)...x(l), y = y(0)y(1)...y(l)$

choose k and c, so that $x(i) \oplus k(i) \oplus c(i) = y(i), with 0 \leq i \leq l$:
if:
$x(i) = 1$ and $y(i) = 1: k(i) = c(i) = 0$

$x(i) = 1$ and $y(i) = 0: k(i) = 1, c(i) = 0$

$x(i) = 0$ and $y(i) = 1: k(i) = 1, c(i) = 0$

$x(i) = 0$ and $y(i) = 0: k(i) = 0, c(i) = 0$


  
## 3. Properites of probability distribution
#### (a) Show that for all $A \subseteq B \subseteq \Omega : P(B$ \ $A) = P(B) - P(A)$

Using the given information, we have:
1. $P(\Omega$ \ $A) = 1 - P(A)$
2. $P(\Omega$ \ $B) = 1 - P(B)$

Since $A \subseteq B$, it follows that $P(B$ \ $A) = P(\Omega$ \ $A) - P(\Omega$ \ $B)$

Subtracting (2) from (1), we get:
$P(\Omega$ \ $A) - P(\Omega$ \ $B)= (1 - P(A)) -(1 - P(B))$

$\Rightarrow P(B$ \ $A) = P(B) - P(A)$

#### (b) Show that for all $A \subseteq B \subseteq \Omega : P(A) \le P(B)$

From $A \subseteq B$, it follows that $|A| \le |B|$. Additionally, since A can only contain elements from B, there is no element in A that would cause $P(A) > P(B)$.

Therefore, $P(A) \le P(B)$

#### (c) Show that for all $A,B \subseteq \Omega : P(A \cup B) = P(A) + P(B) - P(A \cap B)$

Since, $A \cap B \subseteq A, B$,  We have the following from (a)
1. $P(A$ \ $A \cap B) = P(A) - P(A \cap B)$
2. $P(B$ \ $A \cap B) = P(B) - P(A \cap B)$

Now,
$P(A \cup B) = P(A$ \ $A \cap B) + P(B$ \ $A \cap B) + P(A \cap B)$ 


Using (1) and (2),

$P(A \cup B) = P(A) - P(A \cap B) + P(B) - P(A \cap B) + P(A \cap B)$

$\Rightarrow P(A \cup B) = P(A) + P(B) - P(A \cap B)$ 


## 4. Conditional probability is a probability distribution
#### Show that the function lies between [0,1]
Let $\{w\} \in \Omega$ be any input event. Therefore,

$P(w|B) = P(w \cap B)/P(B)$

Since $w \cap B \subseteq B \Rightarrow P(w \cap B) \le P(B)$ and $P(B) > 0$, it follows that $P(w|B) \in [0,1]$

As $w$ is any random input event, the conditional probaility $P(w|B)$ can be considered as a function whose output lies in the range [0,1].

#### Show that $P(\Omega) = 1$
$P(\Omega|B) = P(\Omega \cap B)/P(B)$

Since $\Omega$ is the entire event sent, $P(\Omega \cap B) = P(B)$

Therefore, $P(\Omega|B) = P(B)/P(B) = 1$

#### Show $P(X \cup Y) = P(X) + P(Y)$ if X and Y are disjunctive
$P(X \cup Y | B) = P(X \cup Y \cap B)/P(B)$

because X and Y are disjuntive, $X \cup Y \cap B = (X\cap B) \cup (Y \cap B)$ where $(X\cap B)$ and $(Y \cap B)$ are also disjuntive.

$P(X \cup Y | B) = P((X\cap B) \cup (Y \cap B))/P(B)$

$\Rightarrow P(X \cup Y | B) = (P(X\cap B) + P(Y \cap B))/P(B)$

$\Rightarrow P(X \cup Y | B) = P(X|B) + P(Y|B)$

Thus the conditional probability satisfies all the requirements for a probability distribution.

## 5. Alternative formulation of independent events
$P(A \cap B) = P(A)P(B)$

$\Rightarrow P(A \cap B)/P(B) = P(A)$

Using definition of conditional probability,

$\Rightarrow P(A |B) = P(A)$