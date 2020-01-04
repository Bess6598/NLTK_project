import sys
import codecs
import nltk
import numpy
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import conlltags2tree, tree2conlltags, ne_chunk
import statistics
import math
import re
from operator import itemgetter

CONST_INCREMENTAL = 5


class Corpus:
    name = None  # name of file and corpus
    raw = None  # output of readed file
    nltk_ = None  # nltk data
    token = None  # tokenized copy of the corpus
    sentences = None  # sentence-tokenized copy of the corpus
    pos_tag_universal = None  # pos-tagged (with universal tag) version of the corpus
    pos_tag = None # pos-tagged version of the corpus
    n_token = None  # number of tokens
    n_sentences = None  # number of sentences

    # CONSTRUCTOR
    # Args:
    #   file_name: name of the txt file that contain the corpus
    def __init__(self, file_name):
        self.name = file_name
        temp = codecs.open(self.name, "r", "utf-8-sig")
        self.raw = temp.read().lower()
        self.nltk_ = nltk.data.load("tokenizers/punkt/english.pickle")

        # Copyright Simone Martelli
        # tmp1 = self.nltk_.tokenize(self.raw)
        # l = 0
        # for t in tmp1:
        #   l = l + len(nltk.word_tokenize(t))
        # tmp2 = len(nltk.word_tokenize(self.raw))
        # print(l)
        # print(tmp2)

    # Getter and setter methods
    def get_name(self):
        return self.name

    def _set_name(self):
        raise AttributeError("Attribute can't be changed")

    def get_raw(self):
        return self.raw

    def _set_raw(self):
        raise AttributeError("Attribute can't be changed")

    def get_nltk(self):
        return self.nltk_

    def _set_nltk(self):
        raise AttributeError("Attribute can't be changed")

    def get_token(self):
        if self.token is None:
            self._set_token()
        return self.token

    def _set_token(self):
        self.token = word_tokenize(self.get_raw())

    def get_sentences(self):
        if self.sentences is None:
            self._set_sentences()
        return self.sentences

    def _set_sentences(self):
        self.sentences = sent_tokenize(self.get_raw())

    def get_pos_tag_universal(self):
        if self.pos_tag_universal is None:
            self._set_pos_tag_universal()
        return self.pos_tag_universal

    def _set_pos_tag_universal(self):
        self.pos_tag_universal = pos_tag(self.get_token(), tagset="universal")

    def get_pos_tag(self):
        if self.pos_tag is None:
            self._set_pos_tag()
        return self.pos_tag

    def _set_pos_tag(self):
        self.pos_tag = pos_tag(self.get_token())

    def get_n_sentences(self):
        return len(self.get_sentences())

    def _set_n_sentences(self):
        raise AttributeError("Attribute can't be changed")

    def get_n_token(self):
        return len(self.get_token())

    def _set_n_token(self):
        raise AttributeError("Attribute can't be changed")

    # Returns the arithmetic mean of number of tokens in the sentences of the corpus.
    def mean_sentences(self):
        temp = []
        for i in self.get_sentences():
            temp.append(len(word_tokenize(i)))
        return statistics.mean(temp)

    # Returns the arithmetic mean of number of letters in the tokens of the corpus.
    def mean_token(self):
        temp = []
        for i in self.get_token():
            temp.append(len(i))
        return statistics.mean(temp)

    # Returns the vocabulary length of the corpus (given corpus dimension)
    # Args:
    #   dimension: length of the corpus whose vocabulary is measured
    def vocabulary_length(self, dimension=None):
        if dimension is None:
            dimension = self.get_n_token()
        return len(list(dict.fromkeys(self.get_token()[:dimension])))

    # Returns an array with length of vocabulary of corpus of incremental dimension
    def incremental_vocabulary_length(self):
        vocabulary_length = dict()
        for i in range(0, self.get_n_token(), CONST_INCREMENTAL):
            vocabulary_length[i] = self.vocabulary_length(i)
        return vocabulary_length

    # Returns the hapax distribution for a portion of the corpus
    # Args:
    #   dimension: length of the corpus whose hapax distribution is measured
    def hapax_distribution(self, dimension=None):
        if dimension is None:
            dimension = self.get_n_token()
        temp = dict()  # keys-> word | value -> f(word)
        output = []  # f(word) = 1
        token_l = self.get_token()[:dimension]
        for i in token_l:
            if i not in temp:
                temp[i] = 0
            temp[i] += 1
        for i in temp:
            if temp[i] == 1:
                output.append(i)
        return len(output)

    # Returns an array with hapax distribution of corpus of incremental dimension
    def incremental_hapax_distribution(self):
        hapax_distribution = dict()
        for i in range(0, self.get_n_token(), CONST_INCREMENTAL):
            hapax_distribution[i] = self.hapax_distribution(i)
        return hapax_distribution

    # Returns ratio between A POS-category and B POS-category
    def ratio(self, a, b):
        a_count = 0
        b_count = 0
        pos_tag_l = self.get_pos_tag_universal()
        for i in pos_tag_l:
            if i[1] == a.upper():
                a_count += 1
            elif i[1] == b.upper():
                b_count += 1
        return a_count / b_count

    # Returns an ordinated(most common to less common) list containing the tag of the pos tagged corpus
    def most_frequent_pos(self, dimension=None):
        if dimension is None:
            dimension = self.get_n_token()
        token, cat = zip(*self.get_pos_tag_universal())  # separate the POS-tag list in to 2 different lists
        temp = dict()
        for i in range(dimension):
            if cat[i] in temp.keys():
                temp[cat[i]] += 1
            else:
                temp[cat[i]] = 1
        temp = list(sorted(temp.items(), key=itemgetter(1), reverse=True))
        cat, frequency = zip(*temp)
        return cat

    # Returns an ordinated(highest to lowest) list containing conditioned probability of bigrams
    def conditioned_probability(self):
        freq_category = dict()
        freq_bigrams = dict()
        prob = dict()  # output
        pos_tag_l = self.get_pos_tag_universal()
        for i in range(len(pos_tag_l) - 1):
            if pos_tag_l[i][1] not in freq_category:
                freq_category[pos_tag_l[i][1]] = 0
            freq_category[pos_tag_l[i][1]] += 1
            if (pos_tag_l[i][1], pos_tag_l[i + 1][1]) not in freq_bigrams:
                freq_bigrams[(pos_tag_l[i][1], pos_tag_l[i + 1][1])] = 0
            freq_bigrams[(pos_tag_l[i][1], pos_tag_l[i + 1][1])] += 1
        # checking the last element of the array
        if pos_tag_l[len(pos_tag_l) - 1][1] not in freq_category:
            freq_category[pos_tag_l[len(pos_tag_l) - 1][1]] = 0
        freq_category[pos_tag_l[len(pos_tag_l) - 1][1]] += 1
        for i in freq_bigrams:
            prob[i] = freq_bigrams[i] / freq_category[i[1]]
        prob = list(sorted(prob.items(), key=itemgetter(1), reverse=True))
        # inverts element in tuples (P[Noun|Det] --> f[Det|Noun]/f[Det])
        for i in range(len(prob)):
            prob[i] = (prob[i][0][::-1], prob[i][1])
        return prob

    # Returns an ordinated(highest to lowest) list containing the local mutual information of every bigram in the corpus
    def collocations(self):
        freq_word = dict()
        freq_bigrams = dict()
        lmi = dict()  # output
        pos_tag_l = self.get_pos_tag_universal()
        for i in range(len(pos_tag_l) - 1):
            if pos_tag_l[i][0] not in freq_word:
                freq_word[pos_tag_l[i][0]] = 0
            freq_word[pos_tag_l[i][0]] += 1
            if (pos_tag_l[i][0], pos_tag_l[i + 1][0]) not in freq_bigrams:
                freq_bigrams[(pos_tag_l[i][0], pos_tag_l[i + 1][0])] = 0
            freq_bigrams[(pos_tag_l[i][0], pos_tag_l[i + 1][0])] += 1
        # checking the last element of the array
        if pos_tag_l[len(pos_tag_l) - 1][0] not in freq_word:
            freq_word[pos_tag_l[len(pos_tag_l) - 1][0]] = 0
        freq_word[pos_tag_l[len(pos_tag_l) - 1][0]] += 1
        for i in freq_bigrams:
            # LMI(<u, v>) = f(<u, v>) * (log2((f<u, v> * N )/ (f(u) * f(v))))
            lmi[i] = freq_bigrams[i] * \
                     (math.log(((freq_bigrams[i] * len(self.get_pos_tag_universal())) / (freq_word[i[0]] * freq_word[i[1]])), 2))
        lmi = list(sorted(lmi.items(), key=itemgetter(1), reverse=True))
        return lmi

    def human_name(self):
        chunked = ne_chunk(self.get_pos_tag())
        for node in chunked:
            if "PERSON" in str(node):
                temp = re.sub(r"\(PERSON (\w|.)*/\w* *(\w|.)*/*\w*\ *(\w|.)*/*\w*\)", r"\1\2\3", str(node))
                print(temp)
            #if hasattr(node, 'node'):
                #if "PERSON" == node.node:
                    #print(node)
                    #p = ' '.join([part_ne[0] for part_ne in node.leaves()])
                    #person_dist[p] += 1
                #elif "GPE" == node.node:
                    #print(node)
                    #l = ' '.join([part_ne[0] for part_ne in node.leaves()])
                    #location_dist[l] += 1
        #print(ne_tree)
