# Solutions to Homework 3, Introdution to Modern Cryptography
Authors:

1. Dhruv Mishra, st154709@stud.uni-stuttgart.de, Matriculation number: 3293775

2. Ishan Adhaulia, st159571@stud.uni-stuttgart.de, Matriculation number: 3319219

### Alternative definition of indistinguishable game

- Adversary chooses x1, x2.
- Sender chooses $k \leftarrow {0, 1}^n, i \leftarrow \{1, 2\}$ and sends $y = E_k(x_i)$ to the adversary.
- For as long as adversary desires (but less than poly(n)— its running time), adversary
chooses a message x and gets Ek(x). Note that it is legitimate for the adversary to
choose x = x1 or x = x2 but it can also choose other messages.
- Adversary comes up with a guess j. She wins if i = j.

## Problem 1: Importance of the bit permutation in SPCSs
If the bit permutation is an identity function, any small change in the plaintext/ciphertext would result in a small change in the resulting ciphertext/plaintext.

Take two plaintext messages $x_1= m_1,m_2 ...$ and $x_2 = m_2,m_1...$ where $m_1$ and $m_2$ are two words. Let the given ciphertext be $c=c_1,c_2...$

#### Distinguisher
- Assume that the ciphertext for $x_i$ be represented as $c_i=c^i_1,c^i_2...$
- Construct a new message $x_3= m_1,m_1 ...$ and compute it's ciphertext.
- Since there is no bit permutation, it follows that $c^1_1=c^2_2$ and $c^1_2 = c^2_1$ and $c^1_1=c^3_1$
- If $c_1 == c^3_1$, output 1 else output 2.

## Problem 2
The adversary can keep on selecting plaintexts for as long as it wants but it will never see the same ciphertext again. Therefore, assuming that there is an upper bound on runtime, the distinguisher will simply end up making a guess using coin toss and after it is out of time.

## Problem 3
Assuming that the security parameter is implicit,

random $k \leftarrow \{0,1\}^{2\eta}$

The success probability
##### Game 1
$Game^1_1:$

$1. Choose\ random\ key$

$b=1$

$k \leftarrow \{0,1\}^\eta\ and\ x = G(k)$

$2. Guess\ phase$

$b' \leftarrow U(1^\eta, x)$

$3. Output$

$return\ b'$

The random key generation can be replaced by a random function without any change in the probabilities.

$Game^1_2:$

$1. Choose\ random\ key$

$b=1$

$F \leftarrow \mathscr{F}_{\{0,1\}^{l(\eta)}}\ and\ x = G(F)$

$2. Guess\ phase$

$b' \leftarrow U(1^\eta, x)$

$3. Output$

$return\ b'$

Let's assume that the distinguisher makes $q(\eta)$ queries to the G. Let's denote randomly chosen counters by $r_1,...,r_{q(\eta)}$ and therefore the numbers returned by G for any $i^{th}$ counter look like
- $G^{r_i}(F) = E(r_i,F)||E(r_i +1, F)$

We choose the random counters $\vec{r} = r_1,...,r_{q(\eta)}$ and the responses of F, $\vec{k} = k_1,...,k_{q^2(\eta)}$ at the beginning of the game and we then simulate G(F) by a procedure $SIM(\vec{r}, \vec{k})$ which works as follows:

For the i-th query it chooses $r_i$ at random and for the outputs of F it uses $\vec{k}$ as follows:
- If F was called with a new value, the next unused $k_i$ is used as output of F.
- Otherwise the $y_j$ that was previously chosen as output is returned as output of F.

$Game^1_3:$

$1. Choose\ randomness$

$b=1$

$r_1 \leftarrow \{0,1\}$

$F \leftarrow \mathscr{F}_{\{0,1\}^{l(\eta)}}\ and\ x = G(F)$

$2. Guess\ phase$

$b' \leftarrow U(1^\eta, x)$

$3. Output$

$return\ b'$


## Problem 4

## Problem 5
