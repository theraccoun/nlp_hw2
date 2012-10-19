#__author__Steven MacCoun
from LexiconImprovement import LexiconImprover


class BigramParser:

	def __init__(self, bigram_file):
		self.bigram_dict = {}


		#Get the unique words
		keyset = set([])
		for line in bigram_file:
			line = line.lower()
			line = line.replace('\n', '')
			line = line.replace('\t', ' ')
			line = line.split(' ')
			if self.bigram_dict.has_key(line[0]):
				self.bigram_dict[line[0]].append(line)
			else:
				self.bigram_dict[line[0]] = []
				self.bigram_dict[line[0]].append(line)

		print len(self.bigram_dict)




	def parseString(self, test_str):
		lexImprover = LexiconImprover(None)

		test_word = ''
		cur_char_pointer = 0
		while cur_char_pointer < len(test_str):
			self.get_best_bigram_from_cur_char(cur_char_pointer, test_str)
	
	def format_string(self, test_str):
		test_str = test_str.replace('#','')
		test_str = test_str.lower()

		return test_str

	def get_best_bigram_from_cur_char(self, cur_char_pointer, astring):
		test_word = ''
		print astring
		possible_bigrams = []
		while cur_char_pointer < len(astring):
			test_word += astring[cur_char_pointer]
			if self.bigram_dict.has_key(test_word):
				#See which bigrams are possible by checking if they match
				#the characters in the string
				
				for bg in self.bigram_dict[test_word]:
					match_word = True
					cc = 0
					t_point = cur_char_pointer + 1
					while match_word and t_point < len(astring) and cc < len(bg[1]):
						# print bg[1][cc]
						# print astring[t_point]
						# print "cc: " , cc
						# print "t_point: " , t_point
						# raw_input()
						match_word = bg[1][cc] == astring[t_point]
						if match_word and cc == len(bg[1]) - 1:
							possible_bigrams.append(bg)
						
						t_point += 1
						cc += 1

			cur_char_pointer += 1

		#Determine highest count bigram and return that
		biggest_count = 0
		biggest_bigram = []
		for pbg in possible_bigrams:
			if pbg[2] > biggest_count:
				print pbg[2]
				print pbg
				raw_input()
				biggest_bigram = pbg
				biggest_count = pbg[2]

		return biggest_bigram



def main():
	bigram_file = open('count_2w.txt', 'r')
	bparser = BigramParser(bigram_file)
	test_tag = bparser.format_string('#iaskedforit')
	bparser.parseString(test_tag)
	

if __name__ == "__main__":
    main()