import pytest
from lib.present import *

"""Create present and wrap it passing in present string
no error should be raised and nothing returned"""
def test_wrap_present():
    pres = Present()
    assert pres.wrap('book') == None

"""Test correct running of class where present is wrapped
and then unwrapped. Should return present contents"""
def test_wrap_present_and_unwrap():
    pres = Present()
    pres.wrap('book')
    assert pres.unwrap() == 'book'

"""Try to call the unwrap method before the present has been
wrapped should raise expection"""
def test_unwrap_present_before_anything_has_been_wrapped():
    pres = Present()
    with pytest.raises(Exception) as e:
        pres.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

"""Calling the wrap method when the present has already been 
wrapped should rasie an expection"""
def test_wrap_when_present_already_wrapped():
    pres = Present()
    pres.wrap('book')
    with pytest.raises(Exception) as e:
        pres.wrap('chocolate')
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

"""Calling the wrap method when the present has already been 
wrapped and expection is rasied should preserve value already wrapped"""
def test_wrap_when_present_already_wrapped_peserves_value_already_wrapped():
    pres = Present()
    pres.wrap('book')
    with pytest.raises(Exception) as e:
        pres.wrap('chocolate')
    assert pres.unwrap() == "book"  # not chocolate

"""creating a present with an empty string, wrapping it and 
unwrapping it shouldn't raise an error message and instead returns
an empty string because '' != None """
def test_empty_str_present():
    pres = Present()
    pres.wrap('')
    assert pres.unwrap() == ''