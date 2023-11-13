from lib.password_checker import *
import pytest 

"""Check a password of correct length of 8 or more
returns True"""
def test_correct_password_length_equal():
    p = PasswordChecker()
    assert p.check('hello123') == True# len 8 True

def test_correct_password_length_greater():
    p = PasswordChecker()
    assert p.check('helloqwerty') == True # len > 8 True

"""Check a password less that 8 chars long raises expection
with correct error message"""
def test_password_too_short():
    p = PasswordChecker()
    with pytest.raises(Exception) as e:
        p.check('hello') # len 5
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

"""test with zero length password should rasie expection"""
def test_password_of_zero_length():
    p = PasswordChecker()
    with pytest.raises(Exception) as e:
        p.check('')
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

"""test with int instead of sting which will fail before if
statement as number has no length"""
def test_password_is_an_int():
    p = PasswordChecker()
    with pytest.raises(Exception) as e:
        p.check(55)
    error_message = str(e.value)
    assert error_message.endswith("has no len()")

"""same as above , but test pass as float. Use ends with so
catches errors that end 'object of type <type> has no len()"""
def test_password_is_a_float():
    p = PasswordChecker()
    with pytest.raises(Exception) as e:
        p.check(5.54)
    error_message = str(e.value)
    assert error_message.endswith("has no len()")
