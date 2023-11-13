import pytest
from lib.reminder import *


def test_given_name():
    reminder = Reminder('Joe')
    reminder.remind_me_to('Complete chapter 2')
    result = reminder.remind()
    assert result == 'Complete chapter 2, Joe!'

"""Test remind without a task being set (still = None)
the should raise expection"""
def test_reminder_no_task_set():
    reminder = Reminder('Joe')
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == "No reminder set!"