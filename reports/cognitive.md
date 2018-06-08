# Modality exclusivity norms for 400 nouns: The relationship between perceptual experience and surface word form, Lynott and Conell

Author:

Dhruv Mishra, st154709@stud.uni-stuttgart.de, Matriculation number: 3293775

## Abstract
This paper presents modality exclusivity norms for 400 randomly selected noun words, composed by asking participants for perceptual experience ratings for five sense:
- Auditory (by hearing)
- Gustatory (by tasting)
- Haptic (by feeling through touch)
- Olfactory (by smelling)
- Visual (by seeing)

These ratings are then used to find a relationship between how a word is perceived by people in real life and the corresponding lexical attributes the given word has.

## Method for collecting perceptual ratings
- The participants were a group of 34 native speakers of English.
- A random list of 400 words taken from the MRC psycho-linguistic database.

Procedure:

- The material set was randomly split into two lists of 200 items and presented to participants for perceptual strength ratings.
- Each word was presented on a separate screen with a line that read “To what extent do you experience WORD”
- Each participant rated the word on a scale of 0 (not at all) to 5 (greatly).
- The participants were informed that there was no right or wrong answer, and they should select the values which they feel are correct.
- The experiment was paced by the participants and generally lasted between 45 and 60 mins.

Dominant modality:

- For each word, the modality which received the highest rating was assigned as the dominant modality for that word.
- For four words, ties existed and the dominant modality was then chosen randomly from the tied values.


## Results and discussion
Basic exploratory analysis showed that the following observations:

- Visual was the most strongest modality with a mean rating of 3.54, followed next by Auditory with a mean of 2.15 while Gustatory was the most weakest with a mean rating of 0.53.
- High inter-annotator agreement was observed implying that the collected data can be considered as representative.
- The 95% Confidence Intervals were quite small (less than 0.11) implying that the data is quite reliable.

### Modality exclusivity
It is a measure of the extent to which a particular concept is perceived through a single perceptual modality, calculated per word as the rating range divided by the sum, and extending from 0% for completely multimodal, to 100% for completely unimodal. A high score means that the word has a very specific meaning whereas a low score means that the meaning is general and depends very often on the context.

The most frequent modality observed was visual, which accounted for almost 90% data, while the second most frequent was auditory. The other three modalities were very infrequent and it's not clear if any statistically significant inference can be derived from them. In terms of modality exclusivity, Auditory was the most exclusive amongst all the others.

Gustatory-olfactory ratings were observed to have strong correlation, quite possible due to the fact that food items are usually both smelled and tasted. Visual-haptic also had a strong correlation, because a vast majority of things which can be seen can also be touched. The word "reflection" is an exception here. Auditory ratings were negatively correlated with haptic ratings and had negligible relationship with other modalities.

### Difference between nouns and adjectives
Modality exclusivity scores for nouns (M = 39.2%) were significantly lower than those for adjectives (M = 46.1%). The adjective scores were taken from Lynott and Connells 2009 study. This difference can be explained by the different characteristics of nouns and adjectives. Adjectives capture very specific attributes which describe an object whereas Nouns are more general in their descriptive capability and can incorporate multiple meanings. For example, the noun "copper" carries within itself adjectives like "shiny", "inedible", "tensile", "malleable" etc.

### Comparison with abstractness/concreteness ratings
While the paper does not talk about this topic, I am presenting my own ideas and those discussed in the talk. The authors are not concerned with the meaning of a particular word. The concept of abstractness/concreteness which is typically related to the meaning a word has, can be observed through modality exclusivity scores. A word which is concrete can be expected to have a high modality exclusivity score with only one dominant modality which depicts the associated perceptual experience whereas, an abstract word will tend to be more multi-modal and have a low modality exclusivity score. For example, the noun "reflection" has a modality exclusivity score of 84% with Visual being the dominant modality. While the abstractness/concreteness score is not known, it feels from intuition that "reflection" refers to a very specific phenomena and therefore must be concrete. The noun "item", on the other hand has a modality exclusivity score of 8.3% and has high perceptual ratings for Haptic and Visual. This noun is therefore, highly abstract, as can also be seen from intuition because "item" is highly general in meaning and is used to denote an object or idea.


## Perceptual Strength and lexical Characteristics
The authors test the hypothesis that the perceptual information of a particular noun is related to the surface qualities of the word used to denote it. Based on the previous analysis, it can be expected that if the hypothesis holds true, the following statements must be observed:

- The strength in the auditory modality should be the most closely related to the lexical properties of words.
- Because auditory experience is negatively related or unrelated to other perceptual experience, any effects of auditory strength should pull in the opposite direction from other modalities.

### Modelling
The following variables were extracted for the 400 nouns used in the study.

#### Dependent Lexical Variables
Measures of word length:

- Number of syllables
- Number of phonemes
- Number of morphemes
- Number of letters

#### Dependent Measures of word frequency
- Frequency count
- Contextual diversity, ie. variety of different contexts in which a word appears.

#### Dependent Measures of word-form distinctiveness
Phonological neighborhood size: number of words that can be generated by switching one phoneme.
Orthographic neighborhood size: number of words that can be generated by switching one letter
Phonographic neighborhood size: number of words in the overlap between phonological and orthographic neighbors

#### Design
The variables described above served as dependent variables in a regression model. Different models were trained for each variable, with the perceptual ratings being the input data. Distinctiveness and frequency variables were log-transformed to normalize for skewed distributions.

### Analysis
The relationships were consistent with previous literature. 

- Zipf's law: Word length is negatively correlated with word frequency
- Word length is negatively correlated with neighborhood size
- Neighborhood sized and frequency are positively correlated.
- Length increased with higher auditory ratings but decreased with higher haptic ratings. Therefore, things which can be touched have shorter names
- Things which can be seen or smelled have both long and short words.
- Things which are heard or tasted have longer words.
- Perceptual strength only explains 6-9% of the variance.
- Neighborhood size increases with higher haptic ratings and decreases with higher auditory ratings.

## Conclusion
- The paper presents perceptual modality exclusivity norms for 400 randomly selected nouns across five sensory modalities (i.e. hearing, taste, touch, smell and vision)
- The conceptual content of nouns is more multimodal than that of adjectives.
- As with adjectives, noun concepts tend to show high visual dominance, with auditory-dominant concepts also having the highest modality exclusivity scores for both adjectives and nouns.
- Words that refer to sounds and other intangible entities tend to be long, frequent and unusual in their construction.
- Words that refer to touch tend to be short, frequent and common in form.
- The norms were then used to show a systematic relationship between strength of perceptual experience in the referent concept and surface word form, such that distinctive perceptual experience tends to attract distinctive lexical labels.

## What I liked about the paper
- This paper describes new features (at least for me!) which can be used as additional input in a machine learning model.
- The information is very data driven and every claim/hypothesis was presented with an associated experiment.


## What I disliked about the paper
- The data collection is manual, so using this idea in any meaningful way would be very expensive.
- No results stated about potential applications. Does it really improve performance in Language models or it is only some extra information which is useless?


### References
- Dermot Lynott and Louise Connell. Modality Exclusivity Norms for 400 Nouns: The Relationship
between Perceptual Experience and Surface Word Form. Behavior Research Methods, 45:516–526,
2013