from lib.gratitudes import *

"""
Initially gratitudes is empty so second part of formatted
where gratitudes are joined with ', ' should be an empty string
"""
def test_gratitudes_empty_format():
    grat = Gratitudes()
    assert grat.format() == "Be grateful for: "

""" Add one graditude and test the output. Should be
1 gratitude without any extra ',' from join method"""
def test_gratitudes_format_with_one_add():
    grat = Gratitudes()
    grat.add('Health')
    assert grat.format() == "Be grateful for: Health"

""" Add multiple gratitudes and format output should show then
joined by a comma"""
def test_gratitudes_format_with_multiple_adds():
    grat = Gratitudes()
    grat.add('Health')
    grat.add('Love')
    grat.add('Animals')
    assert grat.format() == "Be grateful for: Health, Love, Animals"

"""add an empty gratitude"""
def test_gratitude_add_empty_string():
    grat = Gratitudes()
    grat.add('')
    assert grat.format() == "Be grateful for: "