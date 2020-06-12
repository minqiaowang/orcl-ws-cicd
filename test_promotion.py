"""
Unit tests for simple Python application
"""

import promotion


class TestPromotion:

    def test_addition(self):
        assert 1200 == promotion.addition(1150, 50)

    def test_increment(self):
        assert 1250 == promotion.increment(1000, 25)
