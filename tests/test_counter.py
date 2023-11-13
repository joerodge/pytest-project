from lib.counter import *

"""
Test counter initially reports value of zero
"""
def test_counter_init_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

"""
test adding 1 is inital 0 is 1
"""
def test_counter_1():
    counter = Counter() # 0
    counter.add(1) # 1
    result = counter.report()
    assert result == "Counted to 1 so far."

"""
test adding 5 to inital 0 is 5
"""
def test_counter_2():
    counter = Counter() # 0
    counter.add(5) # 5
    result = counter.report()
    assert result == "Counted to 5 so far."

"""
test adding multiple values and then displaying output
"""
def test_counter_add_multiple():
    counter = Counter() # 0
    counter.add(1) # 1
    counter.add(3) # 4
    counter.add(7) # 11
    result = counter.report()
    assert result == "Counted to 11 so far."

"""
test that if we add 0 to inital 0 it is 0
"""
def test_counter_add_zero():
    counter = Counter() # 0
    counter.add(0) # still 0
    result = counter.report()
    assert result == "Counted to 0 so far."

"""
testing adding a negitive number results in that
number being minused from value of counter
"""
def test_counter_add_negative():
    counter = Counter() # 0
    counter.add(23) # 23
    counter.add(-30) # -7
    result = counter.report()
    assert result == "Counted to -7 so far."    