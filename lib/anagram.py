# your code goes here!
class Anagram:
  def __init__(self, word):
    self.word_letters = sorted([letter for letter in word])

  def match(self, anagram_list):
    match_anagram_list = []

    for word in anagram_list:
      if sorted([letter for letter in word]) == self.word_letters:
        match_anagram_list.append(word)
    
    return match_anagram_list