# Solutions to Homework 1, Introdution to Modern Cryptography
Authors:

1. Dhruv Mishra, st154709@stud.uni-stuttgart.de, Matriculation number: 3293775

2. Ishan Adhaulia, st159571@stud.uni-stuttgart.de, Matriculation number: 3319219

3. Lukas Fromme, st101379@stud.uni-stuttgart.de, Matriculation number: 2798268

## 1. Perfect Secrecy of Cryptosystems
#### (a)
From the lecture, we know that the following holds: a cryptosystem is perfectly secret $\Leftrightarrow P_k(\{k|k \in K, e(x,k)=y\}) = P_k(\{k|k \in K, e(x',k)=y\})$

$P(k|e(a,k)=A)=8/16$
$P(k|e(b,k)=A)=8/16$

The same holds for B.
Thus, according to the Lemma from the lecture, (a) is a perfectly secret cryptosystem.

#### (b)
$P(k|e(a,k)=A)=2/4$
$P(k|e(a,k)=B)=1/4$
$P(k|e(a,k)=C)=1/4$

Without further investigation, we can already say that, according to the above Lemma, (b) is not a perfectly secure cryptosystem.

## 2. Probabilities of plaintexts in cryptosystems
Using the lemma, If A is independent of B, then $P(A|B) = P(A)$

Since $P_X$ is independent of $P_K$, it follows that

$P(X) = P(\{(x,k,y) | k \in K, y \in Y\}) = P(x)$

## 3. Perfect Secrecy and Key Distributions
#### (a)
Since $V$ is perfectly secret, it follows that
- $P(y|x) = P(y)$
- $P(y|x') = P(y)$

Thus it follows that $P(y|x) = P(y|x')$

#### (b)
From the slides, it follows that
- $P(y|x) = P_K({k|k \in K, e(x,k)=y})$
- $P(y|x') = P_K({k|k \in K, e(x',k)=y})$

Using (a)
- $P_K({k|k \in K, e(x,k)=y}) = P_K({k|k \in K, e(x',k)=y})$

## 4.
Let S be the Cryptosystem from Problem 1 (a), which is perfectly secret.
Switch probabilities of k1 and k3. The probability distribution is now
different and the system is still pefectly secure. (This can be
verified by simply repeating the steps in 1 (a)).
As such, S is a perfectly secret cryptosystem that has at least 2 possible
distributions of keys.

## 5. 
In SPCS , S-box is typically used to obscure the relationship between the key and the ciphertext. If we replace S-box functionality with identity, then for every input, the system doesn't generate unique outputs instead  the adversary can use the pairs of plaintext & ciphertext as it will always be permutation of the string, the pattern will come up. In the end, adversary will come to know the key.