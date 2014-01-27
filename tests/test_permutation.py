"""Permutation tests."""
import unittest


RUNS = 1000


class PermutationTest(unittest.TestCase):
    """Permutation tests."""

    def setUp(self):
        """Set up a permutation instance."""
        import permutation
        self.perm = permutation.Permutation(42, (13, 7, 17))

    def test_map(self):
        """Test the map method."""
        self.assertEqual(self.perm.map(42), 3333656047352411619)

    def test_map_not_self(self):
        """Test the map method."""
        for i in range(RUNS):
            self.assertNotEqual(self.perm.map(i), i)

    def test_unmap(self):
        """Test the unmap method."""
        self.assertEqual(self.perm.unmap(3333656047352411619), 42)

    def test_unmap_reverse(self):
        """Test the unmap method."""
        for i in range(RUNS):
            self.assertEqual(self.perm.unmap(self.perm.map(i)), i)
