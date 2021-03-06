from unittest import TestCase
from word_count import words

class TestWordCounts(TestCase):

    """
        Counts the occurrences or characters in a word
    """

    def test_word_occurance1(self):
        self.assertDictEqual(
            {'word': 1},
            words('word'),
            msg='should count one word'
        )

    def test_word_occurance2(self):
        self.assertDictEqual(
            {'one': 1, 'of': 1, 'each': 1},
            words("one of each"),
            msg='should count one of each'
        )

    def test_word_occurance3(self):
        self.assertDictEqual(
            {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1},
            words("one fish two fish red fish blue fish"),
            msg='should count multiple occurrences'
        )

    def test_word_occurance4(self):
        self.assertDictEqual(
            {'car': 1,
                ":": 2,
                'carpet': 1,
                'as': 1,
                'java': 1,
                'javascript!!&@$%^&': 1
             },
            words('car : carpet as java : javascript!!&@$%^&'),
            msg='should include punctuation'
        )