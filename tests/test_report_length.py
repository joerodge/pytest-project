from lib.report_length import *
from string import ascii_letters as letters
import random

def test_length1():
    result = report_length('Hello')
    assert result == "This string was 5 characters long."

def test_length2():
    result = report_length('joe')
    assert result == "This string was 3 characters long."

def test_zero_length():
    result = report_length('')
    assert result == "This string was 0 characters long."

"ascii_letters is upper and lowercase alphabet so should be len 52 (26*2)"
def test_whole_alphabet():
    result = report_length(letters)
    assert result == "This string was 52 characters long."

def test_random_input():
    rand_text = ''.join(random.sample(letters, random.randint(1,10)))
    func_result = report_length(rand_text)
    assert func_result == f"This string was {len(rand_text)} characters long."