from lib.greet import *

def test_greet1():
    result = greet('Joe')
    assert result == "Hello, Joe!"

def test_greet2():
    result = greet('Tim')
    assert result == "Hello, Tim!"

def test_greet_no_one():
    result = greet('')
    assert result == "Hello, !"