# test_proofpool.py
"""
Tests for ProofPool module.
"""

import unittest
from proofpool import ProofPool

class TestProofPool(unittest.TestCase):
    """Test cases for ProofPool class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ProofPool()
        self.assertIsInstance(instance, ProofPool)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ProofPool()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
