############################################################
# CIS 521: Homework 1
############################################################
############################################################
# Imports
############################################################
# Include your imports here, if any are used.
import numpy as np
import nltk
from nltk.tag.perceptron import PerceptronTagger
############################################################
student_name = "Ishita Rai"
# This is where your grade report will be sent.
student_email = "ishitar@seas.upenn.edu"
############################################################
# Section 1: Python Concepts
############################################################
python_concepts_question_1 = """
Python being dynamically typed means variable types are assigned
at runtime (like, 
x="2"
x=3
gives no errors).
Python being strongly typed means it won’t implicitly convert
incompatible types (like, "2"+2 gives TypeError).
"""
python_concepts_question_2 = """
Python keys are supposed to be immutable, that lists aren't
We can use tuples instead. 
points_to_names = {
    (0, 0): "home", (1, 2): "school", (-1, 1): "market"
    }
"""
python_concepts_question_3 = """
concatenate2 ("".join) is faster since it builds the
final string in one pass instead of copying it again
and again.
"""
############################################################
# Section 2: Working with Lists
############################################################


def extract_and_apply(lst, p, f):
    return [f(x) for x in lst if p(x)]


def concatenate(seqs):
    return [x for y in seqs for x in y]


def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

############################################################
# Section 3: Sequence Slicing
############################################################


def copy(seq):
    return seq[:]


def all_but_last(seq):
    if len(seq) == 0:
        return seq
    else:
        return seq[:-1]


def every_other(seq):
    return seq[::2]
############################################################
# Section 4: Combinatorial Algorithms
############################################################


def prefixes(seq):
    for i in range(len(seq) + 1):
        yield seq[:i]


def suffixes(seq):
    for i in range(len(seq) + 1):
        yield seq[i:]


def slices(seq):
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            yield seq[i:j]
############################################################
# Section 5: Text Processing
############################################################


def normalize(text):
    return " ".join(text.lower().split())



def no_vowels(text):
    return "".join([t for t in text if t not in "aeiouAEIOU"])


def digits_to_words(text):
    hashmap = {
            "0": "zero",
            "1": "one",
            "2": "two",
            "3": "three",
            "4": "four",
            "5": "five",
            "6": "six",
            "7": "seven",
            "8": "eight",
            "9": "nine",
            }
    return " ".join([hashmap[t] for t in text if t in hashmap.keys()])


def to_mixed_case(name):
    namelist = name.split("_")
    wordlist = [word.title() for word in namelist if word]
    if wordlist:
        wordlist[0] = wordlist[0].lower()
    return "".join(wordlist)

############################################################
# Section 6: Polynomials
############################################################
class Polynomial(object):

    def __init__(self, polynomial):
        self._polynomial = tuple(polynomial)

    def get_polynomial(self):
        return self._polynomial


    def __neg__(self):
        return Polynomial([(-x[0], x[1]) for x in self._polynomial])


    def __add__(self, other):
        return Polynomial(
            list(self._polynomial) +
            list(other.get_polynomial())
        )


    def __sub__(self, other):
        return Polynomial(
            list(self._polynomial) +
            [(-x[0], x[1]) for x in other.get_polynomial()]
        )


    def __mul__(self, other):
        result = []
        for x in self._polynomial:
            for y in other:
                result.append((x[0] * y[0], x[1] + y[1]))
        return Polynomial(result)


    def __call__(self, x):
        return sum([ (y[0] * (x ** y[1])) for y in self._polynomial ])


    def simplify(self):
        hashmap = {}
        for x in self._polynomial:
            if x[1] in hashmap:
                hashmap[x[1]] += x[0]
            else:
                hashmap[x[1]] = x[0]

        return Polynomial([(x, hashmap[x]) for x in hashmap.keys()])


    def __str__(self):
        result = ""
        poly = self._polynomial
        if poly[1][0] < 0:
            result += "-"
        for i in range(len(poly)):
            term = ""
            # add a sign
            if i != 0:
                if poly[i][0] < 0:
                    term += " - "
                else:
                    term += " + "
            # add coeff
            if poly[i][0] != 1:
                if poly[i][1] > 0:
                    term += str(abs(poly[i][0]))
                else:
                    term += "x"
            # add variable
            if poly[i][1] != 0:
                if poly[i][1] == 1:
                    term += "x"
                else:
                    term += "x^"
                    term += str(poly[i][1])
            result += term
        return result

############################################################
# Section 7: Python Packages
############################################################


def sort_array(list_of_matrices):
    flatlist = []
    for matrix in list_of_matrices:
        flatlist.extend(matrix.flatten())
    return np.sort(flatlist)

def POS_tag(sentence):
    tokens = nltk.word_tokenize(sentence.lower())
    stopwords = nltk.corpus.stopwords.words('english')
    tokens2 = [word for word in tokens if word not in stopwords]
    tagger = PerceptronTagger()
    return tagger.tag(tokens2)

############################################################
# Section 8: Feedback
############################################################
# Just an approximation is fine.
feedback_question_1 = """
6
"""
feedback_question_2 = """
Section 6 because I needed to brush up
my Python OOPS
"""
feedback_question_3 = """
I liked how systematic the questions PDF was.
This helped me revise python concepts.
There's nothing I'd change.
"""
