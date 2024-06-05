#!/usr/bin/env python3

class MyString:
  '''A class to analyze sentences in a string.'''

  def __init__(self, value=""):
        '''Initialize the MyString object with an optional string value.'''
        self._value = ""
        self.value = value

  @property
  def value(self):
        '''Getter for the value attribute.'''
        return self._value

  @value.setter
  def value(self, new_value):
       '''Setter for the value attribute. Ensures the value is a string.'''
       if not isinstance(new_value, str):
            print("The value must be a string.")
       else:
            self._value = new_value

  def is_sentence(self):
       '''Returns True if the value ends with a period, False otherwise.'''
       return self._value.endswith(".")

  def is_question(self):
        '''Returns True if the value ends with a question mark, False otherwise.'''
        return self._value.endswith("?")

  def is_exclamation(self):
        '''Returns True if the value ends with an exclamation mark, False otherwise.'''
        return self._value.endswith("!")

  def count_sentences(self):
    '''Returns the number of sentences in the value.
    A sentence is defined as any part of the string that ends with a period,
    question mark, or exclamation mark. Consecutive punctuation marks are
    treated as a single sentence ending.'''
    if not self._value:
        return 0

    count = 0
    i = 0
    while i < len(self._value):
        if self._value[i] in ".?!":
            count += 1
            # Skip any consecutive punctuation marks
            while i + 1 < len(self._value) and self._value[i + 1] in ".?!":
                i += 1
        i += 1

    return count
  pass
