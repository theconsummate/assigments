#Outta Control: Laws of Semantic Change and Inherent Biases in Word Representation Models, Dubossarsky et al. (2017)

Author:

Dhruv Mishra, st154709@stud.uni-stuttgart.de, Matriculation number: 3293775

## Abstract
This paper evaluates the validity of previously stated laws of semantic change in literature by applying them on a randomized controlled data set. The claim is that if semantic change indeed be represented by the theoretical laws, their effect should not be seen on a randomized data set, or at least get significantly diminished.

The goal is to specifically analyze these laws:

- The Law of Conformity: Frequency is negatively correlated with semantic change.
- The Law of Innovation: Polysemy is positively correlated with semantic change.
- The Law of Prototypicality: Prototypicality is negatively correlated with semantic change.

## Method
#### Real Data
The historical data-set used is Google Books 5-grams of English fiction. Equally sized samples of 10 million 5-grams per year were taken for the period 1900-1999. To account for outliers, uncommon word were removed and the 100,000 most frequent words were used as the vocabulary.

### Controlled data
#### Continuously shuffled corpus (Shuffle)
This corpus tries to distribute the meaning change uniformly across the whole time period. To do this, the 5-grams in the real data were randomly shuffled to achieve a uniform distribution.

#### One synchronous corpus (sample)
The underlying assumption in all models of semantic change is that no meaning change happens within the same year. Therefore 10 million 5-grams were randomly subsampled from all the 5-grams of the year 1999 and this process was repeated 30 times. Any changes observed in this corpus will be attributed to “noise”.

### Validity of controlled data
To prove that the controlled data created above is indeed valid to carry out the evaluation of semantic laws, it should satisfy the following three conditions:
<!-- write this in own words -->
- The change scores are diminished as compared to the genuine condition
- Change scores are uniform across decades (since decades are shuffled)
- The variance of change scores is smaller that in the genuine condition.


## Word meaning representations
### Counts
Co-occurrence counts were collected for all the words in the vocabulary per decade. 


### PPMI
Sparse square matrices of size equal to that of vocabulary size were created to store the pointwise mutual information (PPMI) scores for each decade. These scores were based on co-occurrence counts.
Based on co-occurrence counts.

### SVD
The PPMI matrix was reduced into lower dimensions by singular vector decomposition. The resulting embeddings were then aligned with the orthogonal Procrustes method.

## Results and discussion

## What I liked about the paper
- It provides a method for more stricter evaluation and testing, something which often gets neglected.
- The argument made in this paper, which can be said to have been thought of based on intuition, was presented with experimental results and theoretical proofs, thus making the entire analysis very rigorous and compelling.

## What I disliked about the paper
- The structure of the paper could have been improved; there was no straight line one could follow to understand the paper.
- The authors did not share the code, as compared to Hamilton et. al who have open sourced their code. Partial code is not very appealing!


### References
