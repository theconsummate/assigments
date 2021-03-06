# Solutions to Homework 4, Introdution to Modern Cryptography
Authors:

1. Dhruv Mishra, st154709@stud.uni-stuttgart.de, Matriculation number: 3293775

2. Ishan Adhaulia, st159571@stud.uni-stuttgart.de, Matriculation number: 3319219


## Problem 1
It is assumed that the key is constant. Collission can be detected as follows:

- Choose a message, $m_1$, and let the counter used for this challenge be $r_c$. Record the cipher text as $c_1$.
- Keep requesting the system to encrypt $m_1$. Since it is given that a collission will occur in constant time, wait for it to happen. A collission can be detected when a new ciphertext, $c_2$ is equal to $c_1$.
- After collission, save the output of the counter, $E(r_c) = m_1 \oplus c_1$

The attacker will win the indistinguishability game since it can easily detect ciphertexts which are the encryptions of the same message.

## Problem 2
Since the attack is chosen ciphertext, the adversary has access to the decryption oracle D. Consider the following attack:

- Adversary sends $m_0 = 0^n$ and $m_1 = 1^n$ to the encryption oracle.
- Since the decryption oracle will not accept the encryption of the challenge messages ($m_0\ or\ m_1$) as input, the adversary will flip the first bit in the encryption of $m_b$ and send it to the decryption oracle.
- The adversary can now tell from what he gets back. If $m_b=m_0$, then the output will be $10^{n-1}$  whereas if $m_b=m_1$ was encrypted, then output will be $01^{n-1}$.

The adversary clearly has an advantage of 1 since it can perfectly distinguish between challenge ciphertexts.

## Problem 3

## Problem 4
Since o(g) is finite, $g^{o(g)} = 1$ for the group generated by g.

m is a multiple of o(g), therefore let m = k*o(g) for some natural number k.

$g^{m} = g^{k*o(g)} = (g^{o(g)})^k = (1)^k = 1$

## Problem 5
Let c be the inverse of a and let the unit element be 1. It is also given that $b^2=a$

Therefore, $ca = 1 \rightarrow cb^2=1 \rightarrow (cb)b = 1$

Since the inverse of b which is "cb" exists, it is invertible.