from lib.check_codeword import *

"If the codeword is correct, returns 'Correct! Come in.' "
def test_codeword_correct():
    assert check_codeword('horse') == "Correct! Come in."

"""If the codeword is close, i.e. first and last letter are correct
return 'Close, but nope.' """
def test_codeword_close():
    assert check_codeword('house') == "Close, but nope."

""" Should only be close if first AND letter is correct. So test
input where only first letter is correct which should
output wrong"""
def test_codeword_first_letter_only_correct():
    assert check_codeword('hello') == "WRONG!"

def test_codeword_last_letter_only_correct():
    assert check_codeword('shore') == "WRONG!"

"Return 'WRONG' if codeword wrong and isn't close"
def test_codeword_wrong():
    assert check_codeword('open please') == "WRONG!"
