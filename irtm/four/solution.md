# Assignment 4
Authors:

1. Dhruv Mishra, st154709@stud.uni-stuttgart.de, Matriculation number: 3293775

2. Ishan Adhaulia, st159571@stud.uni-stuttgart.de, Matriculation number: 3319219


## Task1
P(c1) = P(c2) = 2/4 = 0.5

c1 “new year”
c1 “holiday year”
c2 “work again”
c2 “never work”

Conditional Probabilities: (bins = 6)

P(new|c1) = (1+1)/(4+6) = 2/10
P(year|c1) = (1+2)/(4+6) = 3/10
P(holiday|c1) = (1+1)/(4+6) = 2/10
P(work|c1) = (0+1)/(4+6) = 1/10
P(again|c1) = (0+1)/(4+6) = 1/10
P(never|c1) = (0+1)/(4+6) = 1/10

P(new|c2) = (0+1)/(4+6) = 1/10
P(year|c2) = (0+1)/(4+6) = 1/10
P(holiday|c2) = (0+1)/(4+6) = 1/10
P(work|c2) = (2+1)/(4+6) = 3/10
P(again|c2) = (1+1)/(4+6) = 2/10
P(never|c2) = (1+1)/(4+6) = 2/10

For the given document "never holiday",
P(d|c1) = P(c1)P(never|c1)P(holiday|c1) = (1/2)(1/10)(2/10) = 1/100 = 0.01
P(d|c2) = P(c2)P(never|c2)P(holiday|c2) = (1/2)(2/10)(1/10) = 1/100 = 0.01

The model will think that the document is equally likely to belong to either of the two classes.

## Task2
### Task 2.1

For y = SPAM, the features f1, f3, f7 will be equal to 1 and the other features will be 0.

p(SPAM|x1) = exp(0.2 + 0.5 + 0.1) = 2.46

For y = HAM, the features f2, f4, f8 will be 1 and the other features will be 0.

p(HAM|x1) = exp(-0.1 - 0.2 + 0) = 0.74

Normalising,
P(SPAM|x1) = 2.46/(2.46+0.74) = 0.77

### Task 2.2
dA/dlambda6 = 0 + 0 + 0 + 0 + 1 + 1 = 2

since f6(SPAM,x) will be zero, we only need to consider terms for f6(HAM,x)

dB/dlambda6 = p(HAM|x1)f6(HAM,x1) + p(HAM|x2)f6(HAM,x2) + p(HAM|x3)f6(HAM,x3) + p(HAM|x4)f6(HAM,x4) + p(HAM|x5)f6(HAM,x5) + p(HAM|x6)f6(HAM,x6)

= p(HAM|x3) + p(HAM|x5) + p(HAM|x6)

p(HAM|x3) = exp(-0.1+0.4+0)/(exp(-0.1+0.4+0) + exp(0.2-0.1+0.1)) = exp(0.3)/(exp(0.3) + exp(0.2)) = 0.52

p(HAM|x5) = exp(-0.2+0.4+0)/(exp(-0.2+0.4+0) + exp(0.5-0.1+0.1)) = exp(0.2)/(exp(0.2)+exp(0.5)) = 0.42

p(HAM|x6) = exp(-0.1+0.4+0)/(exp(-0.1+0.4+0) + exp(0.2-0.1+0.1)) = exp(0.3)/(exp(0.3) + exp(0.2)) = 0.52

dA/dlambda6 - dB/dlambda6 = 2 - (0.52 + 0.42 + 0.52) = 0.54

## Task3
