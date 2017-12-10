# Solutions to Homework 3, Introdution to Modern Cryptography
Authors:

1. Dhruv Mishra, st154709@stud.uni-stuttgart.de, Matriculation number: 3293775

2. Ishan Adhaulia, st159571@stud.uni-stuttgart.de, Matriculation number: 3319219


## Problem 1: Importance of the bit permutation in SPCSs
We use the CPA definition of security and use the corresponding game where the adversary comes up with two plaintexts and is then provided by a challenge ciphertext.

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

Let's assume that the distinguisher makes $q(\eta)$ queries to the G.
We choose the responses of F, $\vec{k} = k_1,...,k_{q(\eta)}$ at the beginning of the game and we then simulate G(F) by a procedure $SIM(\vec{k})$ which works as follows:

For the i-th query it uses $\vec{k}$ as follows:
- If F was called with a new value, the next unused $k_i$ is used as output of F.
- Otherwise the $k_j$ that was previously chosen as output is returned as output of F.

$Game^1_3:$

$1. Choose\ randomness$

$b=1$

$k_1 \leftarrow \{0,1\}^\eta,...,k_{q(\eta)} \leftarrow \{0,1\}^\eta$

$x = SIM(\vec{k})$

$2. Guess\ phase$

$b' \leftarrow U(1^\eta, x)$

$3. Output$

$return\ b'$

We transform this game into another game which is exactly similar with one difference, that is, it returns $\perp$ whenever there is a collission.

$Game^1_4:$

$1. Choose\ randomness$

$b=1$

$k_1 \leftarrow \{0,1\}^\eta,...,k_{q(\eta)} \leftarrow \{0,1\}^\eta$

$if\ collission\ occurs, return\ \perp$

$x = SIM(\vec{k})$

$2. Guess\ phase$

$b' \leftarrow U(1^\eta, x)$

$3. Output$

$return\ b'$

Now if we change $b = 0$ and use a truly random function to generate keys (instead of a psuedorandom function), the difference in probabilities will be negligible pseudo-randomness property of $\mathscr{F}$ should guarantee that this modification has only a negligible effect on the behavior of the adversary. Therefore,

$Game^0_4:$

$1. Choose\ randomness$

$b=0$

$k_1 \leftarrow \{0,1\}^\eta,...,k_{q(\eta)} \leftarrow \{0,1\}^\eta$

$if\ collission\ occurs, return\ \perp$

$x = SIM(\vec{k})$

$2. Guess\ phase$

$b' \leftarrow U(1^\eta, x)$

$3. Output$

$return\ b'$

Now undoing the steps for $b=1$, we can reach to $Game^0_0$ with negligible change in probability.

Thus following the sequence of games, it can be interpreted that $|Game^1_0 - Game^0_0|$ (which is the advanatege) is negligible and thus the G is a secure block cryptosystem.

## Problem 4
#### (a)

##### Padding scheme:
Add a 1 and then set the remaining bits to 0. For example, consider the string '11000' which has to be padded for a 8 block cipher. The resulting string after padding will be '1100100'.

##### Encryption:
S' pads the plaintext messages and encyptes using S.

##### Decryption:
S' decrypts the ciphertext messages using S to get the padded plaintext message. Then it starts from the end of string and keeps going back till it keeps seeing 0's. Once the first 1 bit is encountered, everything to the left of that point is returned as the plaintext message.

This can be demonstrated by the following python code:

```python
# s is the decrypted string with padding
def removePadding(s):
    i = len(s) - 1
    while i > 0 and not s[i] == 1 :
        i = i-1
    # loop ends when first 1 is encounted when iterating
    # backwards from the end
    # drop the last 1 bit and return everything to the left.
    return s[:i-1]

```

#### (b) S' is CPA-secure
Since the padding is a constant time method, it can be assumed that the adversary already knows this and it can pad messages of arbitary length itself and use the $E_S$ directly without quering $E'_S$ at all.

Given an adversary $A = (AF, AG)$ for the encryptioin scheme S, an adversary $A' = (AF', AG')$ for S' can be implemented like such:

AF':

1. Generate two messages $m_1$ and $m_2$ using AF
2. Pad them using the know padding scheme to get $mp_1$ and $mp_2$
3. Return $mp_1$ and $mp_2$

GF':
1. Given a ciper text c, make a guess using GF.
2. Compare the guessed plaintext with $mp_1$ and $mp_2$ and return the message index.

Since message padding and removing the padding are deterministic processes, the A' has the same advantage as A and therefore S' is secure if S is secure.


## Problem 5
