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
Take arbitrary $l(\eta)$ bit strings $n, n'$ and $c$ where $n \not= n'$. Given that,

- $t_n = T(n, k)$
- $t_{n'} = T(n', k)$
- $t_{n1c} = T(n||1||c, k)$

Now it can be easily seen that the tag $T(n'||1||t_n\oplus t_{n'} \oplus c)$ is the same as $t_{n1n'}$. 

The reason is that while processing the block $t_n\oplus t_{n'} \oplus c$, CBC will use the initial vector as the output of the block $n'||1$ which is $t_{n'}$. The xor operation in CBC will cancel out $t_{n'}$ from the input message (for that particular block) leaving behind $t_n$ which represents $n||1$.

## Problem 4

## Problem 5
Since M is a secure MAC, it implies that for a message-tag pair $(m,t)$ provided by the adversary,

$t \not= T(m,k)$

concatenating the same bit string on both sides,

$\Rightarrow m[0, l(\eta -1)]\ ||\ t \not= m[0, l(\eta -1)]\ ||\ T(m,k)$

$\Rightarrow t' \not= T'(m,k)$

Therefore, the MAC M' is also secure if M is secure.