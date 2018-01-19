# Solutions to Homework 5, Introdution to Modern Cryptography
Authors:

1. Dhruv Mishra, st154709@stud.uni-stuttgart.de, Matriculation number: 3293775

2. Ishan Adhaulia, st159571@stud.uni-stuttgart.de, Matriculation number: 3319219


## Problem 1
slide 58, set 5 proof given.

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

## Problem 6
