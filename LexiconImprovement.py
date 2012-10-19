__author__ = 'theraccoun'

import re

class LexiconImprover:

    validOneLetterWords = ['a', 'i']

    validTwoLetterWords = ['am', 'as',  'at', 'be', 'he', 'hi', 'if', 'in', 'is',  'it', 'me', 'my', 'of', 'on', 'or','to', 'us', 'we', 'yo']

    validThreeLetterWords = ['the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'any', 'can', 'had', 'her', 'was', 'one',
                             'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how', 'man', 'new', 'now', 'old', 'see',
                             'two', 'way', 'who', 'boy', 'did', 'its', 'let', 'put', 'say', 'she', 'too', 'use']

    validFourLetterWords = ['That', 'with', 'have', 'this', 'will', 'your', 'from', 'they', 'know', 'want', 'been',
                            'good', 'much', 'some', 'time', 'very', 'when', 'come', 'here', 'just', 'like', 'long',
                            'make', 'many', 'more', 'only', 'over', 'such', 'take', 'than', 'them', 'well', 'were']

    def __init__(self, lexicon):
        self.lexicon = lexicon

    def checkIfValidWord(self, word):

        if len(word) == 1 and not self.validOneLetterWords.__contains__(word):
            return False
        if len(word) == 2 and not self.validTwoLetterWords.__contains__(word):
            return False
#        if len(word) == 3 and not self.validThreeLetterWords.__contains__(word):
#            return False
#        if len(word) == 4 and not self.validFourLetterWords.__contains__(word):
#            isValidWord = False

        return True

    def improveLexicon(self):

        newLexicon = [word for word in self.lexicon if self.checkIfValidWord(word)]
        return newLexicon
