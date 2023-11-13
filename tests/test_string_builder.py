from lib.string_builder import *

"""Initially the output string is empty string"""
def test_with_zero_string_output():
    s = StringBuilder()
    assert s.output() == ''

"""Initially the string length is 0"""
def test_with_zero_string_size():
    s = StringBuilder()
    assert s.size() == 0

"""test adding single string and the output is that single string"""
def test_string_output():
    s = StringBuilder()
    s.add('Hello')
    assert s.output() == 'Hello'

"""
test adding single string and the size is the len of
that single string
"""
def test_string_length():
    s = StringBuilder()
    s.add('Hello')
    assert s.size() == 5


"""
Add multiple strings and the output should be all the added
strings concatanated together
"""
def test_output_with_multiple_adds():
    s = StringBuilder()
    s.add('hello')
    s.add(' ')
    s.add("Joe")
    s.add('!')
    assert s.output() == 'hello Joe!'

"""
Add multiple strings and the length should be the length of all
strings concatanated together
"""
def test_length_with_multiple_adds():
    s = StringBuilder()
    s.add('hello') # len 5
    s.add(' ') # len 6
    s.add("Joe") # len 9
    s.add('!') # len 10
    assert s.size() == 10