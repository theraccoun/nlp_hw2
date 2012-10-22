#__author__Steven MacCoun
from LexiconImprovement import LexiconImprover
import math


class BigramParser:

	def __init__(self, bigram_file):
		self.lexImprover = LexiconImprover(None)
		self.pos_bigram_combination = []
		self.bigram_dict = {}
		self.best_bigram = []
		self.max_prob = 0

		#Get the unique words
		keyset = set([])
		line_count = 0
		for line in bigram_file:
			line = line.replace('\n', '')
			line = line.replace('\t', ' ')
			line = line.split(' ')
			if self.bigram_dict.has_key(line[0]):
				self.bigram_dict[line[0]].append(line)
			else:
				self.bigram_dict[line[0]] = []
				self.bigram_dict[line[0]].append(line)

			line_count += 1




	def parseString(self, test_str):
		lexImprover = LexiconImprover(None)

		parsed_tag = ''

		test_word = ''
		self.generate_all_possible_bigrams(test_str, 0, [], 1)
		# while cur_char_pointer < len(test_str):
		# 	best_bigram = self.get_best_bigram_from_cur_char(cur_char_pointer, test_str)
		# 	if len(best_bigram) > 0:
		# 		cur_char_pointer += len(best_bigram[0]) + len(best_bigram[1])
		# 		parsed_tag += best_bigram[0] + best_bigram[1]
		# 	else:
		# 		break
		
		print "ANSWER: " , self.best_bigram
	
	def format_string(self, test_str):
		test_str = test_str.replace('#','')
		test_str = test_str.lower()

		return test_str

	def find_argmax_of_counts(self, word, prev_word, total_prob):
		tprob = 0.0001
		is_valid_word_pair = self.lexImprover.checkIfValidWord(word) and self.lexImprover.checkIfValidWord(prev_word)
		if is_valid_word_pair or prev_word == None:
			pos_bigs_from_dict = []

			if prev_word != None:
				if self.bigram_dict.has_key(prev_word):
					pos_bigs_from_dict = self.bigram_dict[prev_word]

					for dictbg in pos_bigs_from_dict:
						if dictbg[1] == word:
							tprob = math.log(float(dictbg[2]), 2)
			else:
				if self.bigram_dict.has_key(word):
					pos_bigs_from_dict = self.bigram_dict[word]
				
					nc = 0
					for dictbg in pos_bigs_from_dict:
						tprob += float(dictbg[2])
						nc += 1

					tprob = math.log(float(tprob)/nc, 2)


		print "Prob of " , word, " given " , prev_word , " = " , tprob					
		return total_prob + tprob


	def generate_all_possible_bigrams(self, astring, cur_char_pointer, prev_bigs, total_prob):
		possible_bigrams = []
		main_pointer = 0

		pos_first_words = self.get_possible_first_words(astring, cur_char_pointer)

		if len(pos_first_words) == 0:
			self.pos_bigram_combination.append(prev_bigs)
			return


		# print "prev_bigs: " , prev_bigs
		# print "pos_new_words: " , pos_first_words
		for word in pos_first_words:
			prev_copy = [b for b in prev_bigs]
			prob = 1
			prev_word = None
			if len(prev_copy) > 0:
				prev_word = prev_copy[len(prev_copy) - 1]
			
			prob = self.find_argmax_of_counts(word, prev_word, total_prob)
			prev_copy.append(word)

			#Get the next pointer
			next_pointer = cur_char_pointer + len(word)

			if next_pointer == len(astring):
				print "at end of string"
				if prob > self.max_prob:
					self.max_prob = prob
					self.best_bigram = [p for p in prev_copy]
					print "new max prob: " , self.max_prob
					print "new best bigram: " , self.best_bigram
			print "prev_copy: " , prev_copy
			print "cur_prob: " , prob
			# if next_pointer > len(astring) - 1:
				# print "total prob: " , total_prob
				# print "max_prob: " , self.max_prob				
				# self.pos_bigram_combination.append(prev_bigs)
				# return
				# if len(prev_bigs) >= 2:
				# 	# prev_bigs.pop()
				# 	# prev_bigs.pop()

				# 	return

			self.generate_all_possible_bigrams(astring, next_pointer, prev_copy, prob)
		
			# return

	def generate_possible_bigrams_at_curpointer(self, index, astring, cur_char_pointer):
		possible_bigrams = []
		pos_first_word = ''
		pos_second_word = ''
		first_word_pointer = cur_char_pointer
		second_word_pointer = first_word_pointer + 1

		while first_word_pointer < len(astring):
			pos_first_word += astring[first_word_pointer]
			pos_second_word = ''

			while second_word_pointer < len(astring):
				pos_second_word += astring[second_word_pointer]
				pos_bigram = [pos_first_word, pos_second_word]
				possible_bigrams.append(pos_bigram)
				second_word_pointer += 1

			first_word_pointer += 1
			second_word_pointer = first_word_pointer + 1

		return possible_bigrams

	def get_possible_first_words(self, astring, cur_char_pointer):
		pos_first_words = []
		pos_first_word = ''
		while cur_char_pointer < len(astring):
			pos_first_word += astring[cur_char_pointer]
			pos_first_words.append(pos_first_word)
			cur_char_pointer += 1

		return pos_first_words



	def get_best_bigram_from_cur_char(self, cur_char_pointer, astring):
		test_word = ''
		print astring
		possible_bigrams = []
		for f in self.bigram_dict['for']:
			if f[1][0] == 'a' and len(f[1]) == 1:
				print f
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
		print "pos: " , possible_bigrams
		raw_input()
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
	test_tag = bparser.format_string('#ilikeyou')
	bparser.parseString(test_tag)
	

if __name__ == "__main__":
    main()