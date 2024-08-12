from project import random_cat_fact, make_your_own_cat, cat_information
import pytest

def test_random_cat_fact():
    result =  random_cat_fact()
    assert isinstance(result, str)

def test_make_your_own_cat():
    assert make_your_own_cat

def test_cat_information():
    assert cat_information
