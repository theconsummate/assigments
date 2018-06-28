# Outta Control: Laws of Semantic Change and Inherent Biases in Word Representation Models, Dubossarsky et al. (2017)

Author:

Dhruv Mishra, st154709@stud.uni-stuttgart.de, Matriculation number: 3293775

## Abstract
This paper evaluates the validity of previously stated laws of semantic change in literature by applying them on a randomized controlled data set. The claim is that if semantic change can indeed be represented by the theoretical laws, their effect should not be seen on a randomized data set, or at least get significantly diminished.

The goal is to specifically analyze these laws:

- The Law of Conformity: Frequency is negatively correlated with semantic change.
- The Law of Innovation: Polysemy is positively correlated with semantic change.
- The Law of Prototypicality: Prototypicality is negatively correlated with semantic change.

## Method
#### Real Data
The historical data-set used is Google Books 5-grams of English fiction. Equally sized samples of 10 million 5-grams per year were taken for the period 1900-1999. To account for outliers, uncommon word were removed and the 100,000 most frequent words were used as the vocabulary. Since this data spans an entire century, it is big enough to assume the presence of semantic change, thereby making it appropriate for carrying out the testing process.

### Controlled data
#### Continuously shuffled corpus (Shuffle)
This corpus tries to distribute the meaning change uniformly across the whole time period. To do this, the 5-grams in the real data were randomly shuffled to achieve a uniform distribution. Any semantic change trends which were previously present should get significantly diminished in this new shuffled corpus.

#### One synchronous corpus (sample)
The underlying assumption in all models of semantic change is that no meaning change happens within the same year. Therefore 10 million 5-grams were randomly subsampled from all the 5-grams of the year 1999 and this process was repeated 30 times. Any changes observed in this corpus will be attributed to “noise”.

### Validity of controlled data
To prove that the controlled data created above is indeed valid to carry out the evaluation of semantic laws, it should satisfy the following three conditions:
- Semantic change of words should get diminished as compared to the original corpus.
- Semantic change, if present by chance, should be uniformly distributed across time.
- The variance of semantic change should be very small.

The shuffled corpus satisfied all these three conditions and therefore it can be used as valid control condition.


## Word meaning representations
The words in the corpus were mathematically represented in the following ways:

### Counts
Co-occurrence counts were collected for all the words in the vocabulary per decade. 

### PPMI
Sparse square matrices of size equal to that of vocabulary size were created to store the pointwise mutual information (PPMI) scores for each decade. These scores were based on co-occurrence counts.
Based on co-occurrence counts.

### SVD
The PPMI matrix was reduced into lower dimensions by singular vector decomposition. The resulting embeddings were then aligned with the orthogonal Procrustes method.

## Results and discussion
### Testing the law of Conformity
#### Subsample Condition
The authors calculated the correlation between frequency of words and their corresponding change scores for the year 1999. Since the assumption was that there is no semantic change within a year, the correlation should be negligible. However, for the word count representation, the correlation was -0.915 while it was -0.295 and -0.793 for PPMI and SVD respectively. This is clearly in violation of the law. The authors also point out that the correlation for SVD is misleading because of the mathematical distortions carried out while reducing the dimensions. Therefore, in principle, the actual correlation must have been lesser than what was observed. However, in any case, the law of conformity is not holding up for the subsample condition.

#### Shuffle Condition
Now the correlation was calculated between semantic change scores and frequency for the whole century using the shuffle corpus. In stark contrast to expectations, almost identical correlation coefficients were observed for both the original and the shuffled corpus. This tells us that the effect of frequency is not really as great as has been reported in literature.

### Testing the law of Innovation and Prototypicality
To test these two laws, the authors did a regression analysis with frequency and polysemy as the independent variables for the law of innovation and frequency and prototypicality for the law of prototypicality. For these two-predictor models, the authors compared the the $\beta$ and the explained variance for both the original and shuffled corpus.

Again, contrary to expectations, not much difference was seen between the two corpus. In case of polysemy, the explained variance for PPMI+SVD representations was 68% and 60% for original and shuffle respectively. This difference is way too less and it can be concluded that the law of innovation is not very strong. The reason according to the paper is that polysemy is highly collinear with frequency and therefore does not make any strong contributions to the two variable regression model.

Similarly for prototypicality for PPMI+SVD representations, the explained variance was 65% and 60% for the genuine and shuffle corpus respectively. Once again, the difference was too low and the law of prototypicality does not seem to be holding up.


## Theoretical analysis
The paper starts by analyzing the relationship between sampling variability and cosine similarity. The lemma says that cosine distance is directly related to the variance of the variable. As a measure of caution, the cosine distance should only be used when it is larger than the empirically calculated variance.

Next the paper proves that for a given word w, the cosine distance of two iid samples from the distribution of count vector of w is monotonically decreasing with the word frequency. For polysemy, the paper proves that cosine distance between two samples of the word w becomes larger when the word has more meanings.


## Conclusion and General Discussion
The paper showed the failure of three laws of semantic change which had been reported in literature. The extent of the relationship as claimed was not observed when tested with randomized control data. This shows the fragility of the current state of research and points out the vulnerabilities of the mathematics and data used to prove these laws. The paper also presents mathematical proofs deconstructing the fallacy and while they are instructive, I have chosen not to include them in this report to avoid copying the proofs here.

The paper also showed that the output of a model of semantic change is often dependent on the word representations it is using. As was seen in subsample case of the law of conformity, different representations provided different correlation values. The authors argue that the representations using count vectors inherently introduce a dependence of word frequency, which then leads to misleading observations. The authors leave the task of finding out if other word representations (Skip Gram Negative Sampling etc)

In my opinion, the people who published these laws went too far in their claims by calling relationships between two variables a "law". The laws of motion suggested by Issac Newton are rightfully laws but those of semantic change should not be attached the same label. The relationship only appears to be present by chance and  it may or may not be replicable under a variety of conditions. Therefore it does not indicate anything and should be reconsidered.

The positive aspect is that the paper presented a framework for testing and evaluating the results of a model before it gets generalized. This is a very important contribution as testing is something which often gets neglected by people.

## What I liked about the paper
- It provides a method for more stricter evaluation and testing, something which often gets neglected.
- The argument made in this paper, which can be said to have been thought of based on intuition, was presented with experimental results and theoretical proofs, thus making the entire analysis very rigorous and compelling.

## What I disliked about the paper
- The structure of the paper could have been improved; there was no straight line one could follow to understand the paper.
- The authors did not share the code, as compared to Hamilton et. al who have open sourced their code. Partial code is not very appealing!


### References
Dubossarsky, H., Weinshall, D., & Grossman, E. (2017). Outta Control: Laws of Semantic Change and Inherent Biases in Word Representation Models. In Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing (pp. 1136-1145).