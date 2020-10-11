import pytest


class TestASimpleTest:
    """Test: A simple test..."""

    @pytest.mark.this
    def test_should_work_a(self):
        """It should work a"""
        assert True
    
    def test_should_work_b(self):
        """It should work b"""
        assert True
    
    def test_should_work_c(self):
        """It should work c"""
        assert True