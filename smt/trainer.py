import json
import sys
from operator import itemgetter
from copy import deepcopy


def get_corpus(filename):
    '''
    Load corpus file located at `filename` into a list of dicts
    '''
    with open(filename, 'r') as f:
        corpus = json.load(f)

    return corpus


def get_words(corpus):
    '''
    From a `corpus` object, build a dict whose keys are 'en' and 'fr',
    and whose values are sets. Each dict[language] set contains every
    word in that language which appears in the corpus
    '''
    def source_words(lang):
        for pair in corpus:
            for word in pair[lang].split():
                yield word
    return {lang: set(source_words(lang)) for lang in ('en', 'fr')}


def init_translation_probabilities(corpus):
    '''
    Given a `corpus` generate the first set of translation probabilities,
    which can be accessed as
    p(e|s) <=> translation_probabilities[e][s]
    we first assume that for an `e` and set of `s`s, it is equally likely
    that e will translate to any s in `s`s
    '''
    words = get_words(corpus)
    return {
        word_en: {word_fr: 1 / len(words['en'])
                  for word_fr in words['fr']}
        for word_en in words['en']}


def train_iteration(corpus, words, total_s, prev_translation_probabilities):
    '''
    Perform one iteration of the EM-Algorithm

    corpus: corpus object to train from
    words: {language: {word}} mapping

    total_s: counts of the destination words, weighted according to
             their translation probabilities t(e|s)

    prev_translation_probabilities: the translation_probabilities from the
                                    last iteration of the EM algorithm
    '''
    translation_probabilities = deepcopy(prev_translation_probabilities)

    counts = {word_en: {word_fr: 0 for word_fr in words['fr']}
              for word_en in words['en']}

    totals = {word_fr: 0 for word_fr in words['fr']}

    for (es, fs) in [(pair['en'].split(), pair['fr'].split())
                     for pair in corpus]:
        for e in es:
            total_s[e] = 0

            for f in fs:
                total_s[e] += translation_probabilities[e][f]

        for e in es:
            for f in fs:
                counts[e][f] += (translation_probabilities[e][f] /
                                 total_s[e])
                totals[f] += translation_probabilities[e][f] / total_s[e]

    for f in words['fr']:
        for e in words['en']:
            translation_probabilities[e][f] = counts[e][f] / totals[f]

    return translation_probabilities


def is_converged(probabilties_prev, probabilties_curr, epsilon):
    '''
    Decide when the model whose final two iterations are
    `probabilties_prev` and `probabilties_curr` has converged
    '''
    delta = distance(probabilties_prev, probabilties_curr)

    return delta < epsilon


def train_model(corpus, epsilon):
    '''
    Given a `corpus` and `epsilon`, train a translation model on that corpus
    '''
    words = get_words(corpus)

    total_s = {word_en: 0 for word_en in words['en']}
    prev_translation_probabilities = init_translation_probabilities(corpus)

    converged = False
    iterations = 0
    while not converged:
        translation_probabilities = train_iteration(corpus, words, total_s, prev_translation_probabilities)

        converged = is_converged(prev_translation_probabilities,
                                 translation_probabilities, epsilon)
        prev_translation_probabilities = translation_probabilities
        iterations += 1
    return translation_probabilities, iterations


def summarize_results(translation_probabilities):
    '''
    from a dict of source: {target: p(source|target}, return
    a list of mappings from source words to the most probable target word
    '''
    return {
        # for each english word
        # sort the words it could translate to; most probable first
        k: sorted(v.items(), key=itemgetter(1), reverse=True)
        # then grab the head of that == `(most_probable, p(k|most probable)`
        [0]
        # and the first of that pair (the actual word!)
        [0]
        for (k, v) in translation_probabilities.items()
    }


def distance(table_1, table_2):
    '''
    modelling the tables as vectors, whose indices are essentially some
    hashing function applied to each (row key, col key) pair, return the
    euclidean distance between them, where euclidean distance is defined as

    sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + ... + (a[n] - b[n])**2)

    assumes that table_1 and table_2 are identical in structure
    '''
    row_keys = table_1.keys()
    cols = list(table_1.values())
    col_keys = cols[0].keys()

    result = 0
    for (row_key, col_key) in zip(row_keys, col_keys):
        delta = (table_1[row_key][col_key] -
                 table_2[row_key][col_key]) ** 2
        result += delta

    return result ** 0.5


def main(infile, outfile=None, epsilon=0.001, verbose=False):
    '''
    IBM Model 1 SMT Training Example

    infile: path to JSON file containing English-French sentence pairs
            in the form [ {"en": <sentence>, "fr": <sentence>}, ... ]

    outfile: path to output file (defaults to stdout)

    epsilon: Acceptable euclidean distance between translation probability
             vectors across iterations

    verbose: print running info to stderr
    '''
    corpus = get_corpus(infile)

    probabilities, iterations = train_model(corpus, epsilon)
    print(probabilities)
    result_table = summarize_results(probabilities)
    if outfile:
        with open(outfile, 'w') as f:
            json.dump(result_table, f)
    else:
        json.dump(result_table, sys.stdout)

        print('Performed {} iterations'.format(iterations))


if __name__ == '__main__':
    main(sys.argv[1])
