# Solutions to Homework 5, Introdution to Modern Cryptography
Authors:

1. Dhruv Mishra, st154709@stud.uni-stuttgart.de, Matriculation number: 3293775

2. Ishan Adhaulia, st159571@stud.uni-stuttgart.de, Matriculation number: 3319219


## Problem 1
According to the lemma given in slides, n is not a prime number if there exists $a \in Z_n$ such that $a^2\ mod\ n = 1\ and\ a\not\in \{1, -1\ mod\ n\}$.

Since $n-1 = -1\ mod\ n$, it means that 1 and n-1 can not be used as witness for the primalty test.

## Problem 2
Let the Miller Rabin function be Miller-Rabin(n,m,l) where n is the input number, m and l are such that $n-1=m2^l$. Miller-Rabin(n,m,l) returns true if n is probably prime and false if n is composite.

Miller-Rabin-Iter(n,i):
1) Find m and l are such that $n-1=m2^l$
2) Do following i times
    ```
    if (Miller-Rabin(n,m,l) == false)
        return false
    ```
3) Return true.

From the slides, it is given that the probability of being wrong is less than 1/4. For i iterations, this probability will be 1/4i. As i increases, this value will become very small and therefore will be negligible.

## Problem 3
#### (a)
For public key (n,e) and message m, textbook RSA gives a ciphertext $c = m^e mod\ n$.

Given (n,e) = (77,17) and m = 9, we have to compute $9^{17} mod\ 77$. Binary for of 17 is 10001.

l = 4, i = l, h = 1, k = 9
|i|h|k|
|---|---|---|
|4|1|9|
|3|9|81 mod 77 = 4|
|2|9|16 mod 77 = 16|
|1|9|256 mod 77 = 25|
|0|9|625 mod 77 = 9|
|-1|81 mod 77 = 4||

return h = 4

Therefore, c = 4

#### (b)
Since n= 77, it can be seen that p = 11 and q= 7 since n = pq.

$\phi(n) = (p-1)(q-1) = 60$

The public and private keys are related by $e.d\ mod\ \phi(n) = 1$

As e= 17, the solutions to the equation $x_017 + y_060 = gcd(17,60)$ using the extended eucledian algorithm are $x_0 = -7$ and $y_0 = 2$

Therefore, $d = x_0\ mod\ n = -7\ mod\ 60 = 53$

The decryption will be $y^d\ mod\ n = 70^{53}\ mod\ 77$. The binary for 53 is 110101.

l = 5, i = l, h = 1, k = 70
|i|h|k|
|---|---|---|
|5|1|70|
|4|70|70*70 mod 77 = 49|
|3|70|49*49 mod 77 = 14|
|2|14*70 mod 77 = 56|14*14 mod 77 = 42|
|1|56|42*42 mod 77 = 70|
|0|70*56 mod 77 = 70|70*70 mod 77 = 49|
|-1|70*49 mod 77 = 42||

return h = 42.

Therefore, the decrypted plaintext message is 42.

## Problem 4
The attacker knows
1. n = p.q
2. $\phi(n) = (p-1)(q-1)$

Substituting the value of q from 1 into 2,

$\phi(n) = (p-1)(n/q-1)$

$p\phi(n) = (p-1)(n-p)$

$p^2 + p(\phi(n) -n -1) + n = 0$

Finding the roots of this quadratic equation is trivial. Thus p and q can be computed efficiently.

## Problem 5
1. $Z^*_{13} = \{1,2,3,4,5,6,7,8,9,10,11,12\}$

Let g be the generator. Since $Z^*_{13}$ is a cyclic group, it follows that

2. $Z^*_{13}= \{1,g,g^2,g^3,g^4,g^5,g^6,g^7,g^8,g^9,g^{10},g^{11},g^{12}\}$

Comparing (1) and (2), it can be seen that 2 is the generator of $Z^*_{13}$. This can be verified by calculating the modular exponents of 2.

- $2^1 mod\ 13= 2$
- $2^2 mod\ 13= 4$
- $2^3 mod\ 13= 8$
- $2^4 mod\ 13= 3$
- $2^5 mod\ 13= 6$
- $2^6 mod\ 13= 12$
- $2^7 mod\ 13= 11$
- $2^8 mod\ 13= 9$
- $2^9 mod\ 13= 5$
- $2^10 mod\ 13= 10$
- $2^11 mod\ 13= 7$
- $2^12 mod\ 13= 1$

Therefore, g = 2

Pick $g^3$ and $g^4$ as the random ElGamal key pairs for Alice and Bob respectively.

If Alice is sending the message, she would send $(g^3, 7.(g^4)^3)$, that is (8, 7) to Bob.

## Problem 6
#### (a)
$E(1^\eta):\{0,1\}$

$1.\ Generate\ keys$

$(k, \hat{k} \xleftarrow{\textdollar} Gen(1^\eta))$

$2.\ Find\ phase$

$(z_0, z_1) \xleftarrow{\textdollar} AF(1^\eta, k)$

$3.\ Selection$

$b \xleftarrow{\textdollar} \{0,1\}; y \xleftarrow{\textdollar}E(z_b,k)$

$4.\ Guess\ phase$

$b' \xleftarrow{\textdollar} AG(1^\eta, k, y)$

$5. Output$

$return\ b'$

The Adversary AG can make any number of decryption queries in polynomial time with the constraint that it can not query the given challenge ciphertext.


#### (b)
Let g be the chosen generator and a be the private key, thus $g^a= p$ be the public key.

- Given the ciphertext $C = (x, y) = (g^k, m*p^k)$
- Calculate $C' = (x*g^{k'}, y*p^{k'}*m')$
- Give C' to the decryption oracle and get m'' in return.

It can be observed that if $C' = (x',y')$, then

- $x' = x*g^{k'} = g^k*g^{k'} = g^{k+k'} = g^{k''}$
- $y' = y*p^{k'}*m' = m*p^k*p^{k'}*m' = (m*m')*p^{k+k'} = m''*p^{k''}$

Therefore, the decryption of C' will give $m''=m*m'$. The original message can be retireved as $m = m''*(m')^{-1}$.