# Solutions to Homework 6, Introdution to Modern Cryptography
Authors:

1. Dhruv Mishra, st154709@stud.uni-stuttgart.de, Matriculation number: 3293775

2. Ishan Adhaulia, st159571@stud.uni-stuttgart.de, Matriculation number: 3319219


## Problem 1
In simple terms, $P^\eta_b$ returns the encryption of the plaintext $g^b$ where $g$ is the generator chosen by the cryptosystem $S$. That is $P^\eta_b = Enc(g^b, k)$

Since $S$ is CPA-secure, it means that an adversary can't distinguish between the ciphertexts $Enc(g^0, k)$ and $Enc(g^1, k)$. This implies that the $P^\eta_0$ and $P^\eta_1$ are also indistuinguishable.

## Problem 2
Take two bit strings $a$ and $b$. If $a(0) \not= b(0)$, the resulting hash values from $H'$ will not be equal thus making it collision resistant.

Now consider if $a(0) = b(0)$.

The resulting hash values from $H'$ will be $a(0) || h(a)$ and $b(0)||h(b)$ where $h(a)$ and $h(b)$ are hash values returned from $H$. Since $H$ is collision resistant, $h(a) \not= h(b)$ which implies that $a(0)||h(a) \not= b(0)||h(b)$.

Thus $H'$ is collision resistant in this case also.

## Problem 3

## Problem 4

## Problem 5