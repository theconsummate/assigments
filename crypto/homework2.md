# Solutions to Homework 2, Introdution to Modern Cryptography
Authors:

1. Dhruv Mishra, st154709@stud.uni-stuttgart.de, Matriculation number: 3293775

2. Ishan Adhaulia, st159571@stud.uni-stuttgart.de, Matriculation number: 3319219

3. Lukas Fromme, st101379@stud.uni-stuttgart.de, Matriculation number: 2798268

### Given functions from slides,
```
The S-box,
S(x) = {
    0000 -> 0101,
    0001 -> 0100,
    0010 -> 1101,
    0011 -> 0001,
    0100 -> 0011,
    0101 -> 1100,
    0110 -> 1011,
    0111 -> 1000,
    1000 -> 1010,
    1001 -> 0010,
    1010 -> 0110,
    1011 -> 1111,
    1100 -> 1001,
    1101 -> 1110,
    1110 -> 0000,
    1111 -> 0111,
}

The P-box, (permutation box)
P(x) = {
    0 -> 4,
    1 -> 5,
    2 -> 8,
    3 -> 9,
    4 -> 0,
    5 -> 1,
    6 -> 10,
    7 -> 11,
    8 -> 2,
    9 -> 3,
    10 -> 6,
    11 -> 7,
}
```

## Problem 1
$u_1(10)$ and $u_1(11)$ are the 3rd and 4th bits for the 3rd S-box. Therefore the approximation for I = {10,11} will be the same as that for I = {2,3}

Using the table for Sbox on Slide set 02, slide 47, it can be seen that the combinations which have a better orientation for I = {2,3} are J = {3} and {0,3} with absolute orientation being 1/2.

Thus the other possibilities are J = {7}, {11}, {4,7}, {8,11}

## Problem 2
Using the linear dependence for the first S-box,

$x(0)\oplus x(1)\oplus x(3) = u_1(2)$

Using the P-box,
$v_1(8)=u_1(2)$

Now after the round key function, $u_2(8) = v_1(8)$

The above equalities imply that $x(0)\oplus x(1)\oplus x(3) = u_2(8)$

Finally, according to the given architecture, $x(0)\oplus x(1)\oplus x(3) = u_2(6)$, it follows that

$u_2(8) = u_2(6)$

This means that the 3rd bit of the 2nd word must be equal to the 1st bit of the 3rd word. If the 2nd and 3rd word are concatenated into a single word, this situation can be visualized as a 8 bit string where the 3rd and 5th bit are equal.

The remaining 6 bits can either take 0 or 1. Therefore, total bit permutations will be 2\*2^6 = 128. Similarly, the number of cases where the linear dependence will not hold will be 128.

Orientation of the 2nd S-box will then be 1 - (2\*128)/2^8 = 0.

Thus the overall orienation of architecture is also 0.

## Problem 3
using the lemma, $\epsilon^J_I[f] = Exp(X^J_I[f])$, we have $\epsilon^L_I[g \circ f] = Exp(X^L_I[g \circ f])$

Using the property,

$Exp(X^L_I[g \circ f]) = \int^L_Ixg(x)f(x)dx = Exp(X^L_I[gf])$

Using the lemma, $Exp(XY) = Exp(X)Exp(Y)$, we have:

$Exp(X^L_I[g \circ f]) = Exp(X^L_I[gf]) = Exp(X^L_I[f])Exp(X^L_I[g])$

Since the random variable for $g$ is only defined for $(J,L)$ and that for $f$ is only defined for $(I,J)$, the above expression reduces to,

$Exp(X^L_I[g \circ f]) = Exp(X^J_I[f])Exp(X^L_J[g]) = \epsilon^J_I[f]\epsilon^L_J[g]$




## Problem 4
#### (a)
Since the output of A(x) only depends on the product of a and b, and since a and b are independent of each other, the probability space of A(x) will be the product of probability spaces of a and b.

Therefore, $P(A(x)) = P(a)P(b) = \{0,1\} * \{0,...,19\}$

#### (b)
A(x) will be zero when either a is zero or b is zero. There are 21 such events in the set P(A(x)). The total number of events in P(A(x)) is 40.

Therefore, $Pr[A(x) = 0] = 21/40 = 0.525$

#### (c)
E will occur when b is less than 8. Thus E is independent of a.

$Pr[E|a = 1] = Pr[E] = Pr[b<8] = 8/20 = 0.4$

#### (d)
$d = 0^{42}$ imlies the event $b \ge 8$. Therefore, $Pr[A(x) > 0 | d = 0^{42}] = Pr[A(x) > 0 | b \ge 8]$

Using definition of conditional probability,

$Pr[A(x) > 0 | b \ge 8] = Pr[A(x) > 0 \cap b \ge 8]/Pr[b \ge 8]$

$Pr[A(x) > 0 \cap b \ge 8] = 12/40 = 0.3$ (counting events from the product space of A(x))

$Pr[b \ge 8] = 12/20 = 0.6$

Thus, $Pr[A(x) > 0 | b \ge 8] = 0.3/0.6 = 0.5$

## Problem 5
A(x) will only give the output c' whenever $\langle y =c \rangle$. The probability of this event will be same as the conditional probability given $y = c$.

However, if y is assigned n times, assume that $c_1, c_2....c_n$ are the chosen samples. Then the corresponding probability will be

$Pr[A(x)\langle y = c \rangle = c'] = Pr[A(x) = c' | y = c_n | y = c_{n-1} | ... | y = c_1]$ 

This is different from the given lemma.

The given expression holds true for i equal to 1, 2 and 3.
This is because

- for 50% events, $b_1$ will not be assigned even once
- for 25% events, $b_2$ will not be assigned even once
- for 12.5% events, $b_3$ will not be assigned even once

Therefore the lemma proved above will not hold as it requires that a random variable is assigned once.

## Problem 6
$X_{n+1}$ = ((A$X_n+C)\bmod P) \bmod M$

where $X_{n+1}$ is the next random number

$X_n$ is previous random number

A is multiplier   0 < A < P

C is constant     0 < C < M

P is prime number 

M is the size of the set

By this algorithm, we can generate random numbers from a finite set which all have same probability. Since the second modulo makes the generated number in the range of 0 to M-1. Hence we will have pseudo random number from the set. 
