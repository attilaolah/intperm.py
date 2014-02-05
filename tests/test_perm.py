"""Permutation tests."""
import unittest


RUNS = 256


class PermutationTest(unittest.TestCase):
    """Permutation tests."""

    def setUp(self):
        """Set up a permutation instance."""
        import permutation
        self.perm = permutation.Permutation(42, (13, 7, 17))

    def test_map_to(self):
        """Test the map_to method."""
        self.assertEqual(self.perm.map_to(42), 3333656047352411619)

    def test_map_to_not_self(self):
        """Test the map_to method."""
        for i in range(RUNS):
            self.assertNotEqual(self.perm.map_to(i), i)

    def test_map_from(self):
        """Test the map_from method."""
        self.assertEqual(self.perm.map_from(3333656047352411619), 42)

    def test_map_from_reverse(self):
        """Test the map_from method."""
        for i in range(RUNS):
            self.assertEqual(self.perm.map_from(self.perm.map_to(i)), i)


class Permutation8bitTest(unittest.TestCase):
    """8-bit permutation tests."""

    def setUp(self):
        """Set up an 8-bit permutation instance."""
        import permutation
        self.perm = permutation.Permutation(42, (13, 7, 17), bit_length=8)

    def test_map_to(self):
        """Test the map_to method."""
        self.assertEqual(self.perm.map_to(42), 255)

    def test_map_to_not_self(self):
        """Test the map_to method."""
        for i in range(RUNS):
            self.assertNotEqual(self.perm.map_to(i), i)

    def test_map_from(self):
        """Test the map_from method."""
        self.assertEqual(self.perm.map_from(255), 42)

    def test_map_from_reverse(self):
        """Test the map_from method."""
        for i in range(RUNS):
            self.assertEqual(self.perm.map_from(self.perm.map_to(i)), i)
