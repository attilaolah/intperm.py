"""Permutation tests."""
import unittest


class PermutationTest(unittest.TestCase):
    """Permutation tests."""

    def setUp(self):
        """Set up a permutation instance."""
        import permutation
        self.perm = permutation.Permutation(42, (13, 7, 17))

    def test_unmap(self):
        """Test the unmap method."""
        self.assertEqual(self.perm.unmap(3333656047352411619), 42)
