"""A simple permutation for 64-bit ints.

This file also includes a simple XORShift-based PRNG for expanding the seed.
Example code from http://www.jstatsoft.org/v08/i14/paper (public domain).
"""

_ONES = 0xffffffffffffffff


class Permutation(object):
    """Simple permutation object."""

    def __init__(self, seed, (p_a, p_b, p_c)):
        """Set up the permutation object.

        The first argument, `seed`, can be any random number.
        The other three should be one of the 275 available triplets from the
        paper (page 3). For unpredictable permutations, choose different values
        from http://www.jstatsoft.org/v08/i14/paper.
        """
        xorshift = _XORShift(seed, p_a, p_b, p_c)
        self._masks = tuple(xorshift() & ((1 << (i >> 1)) ^ _ONES)
                            for i in range(128))

    def map(self, num):
        """Map a number to another random one."""
        raise NotImplementedError()

    def unmap(self, num):
        """The reverse of map. Ino ther words, perm.unmap(perm.map(x)) == x."""
        for i in range(63, -1, -1):
            bit = 1 << i
            if (bit & num) >> i == 0:
                num ^= _ONES ^ (self._masks[(i << 1)+((bit & num) >> i)] |
                                (bit ^ bit & num))
            else:
                num ^= _ONES ^ (self._masks[(i << 1)+((bit & num) >> i)] |
                                (bit & num))
        return num


class _XORShift(object):
    """XOR Shift implementation."""

    def __init__(self, seed, p_a, p_b, p_c):
        self._seed = seed
        self._p_a = p_a
        self._p_b = p_b
        self._p_c = p_c

    def __call__(self):
        self._seed ^= _ONES & (self._seed << self._p_a)
        self._seed ^= _ONES & (self._seed >> self._p_b)
        self._seed ^= _ONES & (self._seed << self._p_c)
        return self._seed
