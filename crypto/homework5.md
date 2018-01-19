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

## Problem 4

## Problem 5

## Problem 6
