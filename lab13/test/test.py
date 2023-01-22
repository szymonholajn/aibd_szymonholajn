from app import hello
import pytest
from app import extract_sentiment
from app import text_contain_word
from app import bubblesort

def test_hello():
    got = hello("Szymon")
    want = "Hello Szymon"

    assert got == want

testdata = ["I think today will be a great day","I do not think this will turn out well"]

@pytest.mark.parametrize('sample', testdata)

def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)

    assert sentiment >= 0




testdata = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
    ]

@pytest.mark.parametrize('sample, word, expected_output', testdata)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output



testdata = [
    ([8, 7, 6, 5, 4, 3, 2],[2,3,4,5,6,7,8]),
    ([-1, 2, 4, -5, -3, 0, 1],[-5,-3,-1,0,1,2,4]),
    ([1,1,1],[1,1,1]),
    ([5, 3, 8, 6, 7, 2],[2, 3, 5, 6, 7, 8]),
    ([39, 12, 18, 85, 72, 10, 2, 18],[2, 10, 12, 18, 18, 39, 72, 85]),
    ([3,2,1],[1,2,3]),
    ]



@pytest.mark.parametrize("sample, expected_output",testdata)
def test_bubblesort(sample,expected_output):

    assert bubblesort(sample) == expected_output
