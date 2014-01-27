"""A simple permutation for arbitrary length integers.

This file also includes a simple XORShift-based PRNG for expanding the seed.
Example code from http://www.jstatsoft.org/v08/i14/paper (public domain).
"""


class Permutation(object):
    """Simple permutation object."""

    def __init__(self, seed, params, bit_length=64):
        """Set up the permutation object.

        The first argument, `seed`, can be any random number.
        The other three should be one of the 275 available triplets from the
        paper (page 3). For unpredictable permutations, choose different values
        from http://www.jstatsoft.org/v08/i14/paper.
        """
        self.bit_length = bit_length
        self._mask = (1 << bit_length)-1
        xorshift = _XORShift(seed, params, self._mask)
        self._masks = tuple(xorshift() & ((1 << (i >> 1)) ^ self._mask)
                            for i in range(bit_length*2))

    def map(self, num):
        """Map a number to another random one."""
        return self._map(num, range(self.bit_length))

    def unmap(self, num):
        """The reverse of map. Ino ther words, perm.unmap(perm.map(x)) == x."""
        return self._map(num, range(self.bit_length-1, -1, -1))

    def _map(self, num, rng):
        """Logic used by both `map` and `unmap`."""
        for i in rng:
            bit = 1 << i
            if (bit & num) >> i == 0:
                num ^= self._mask ^ (self._masks[(i << 1)+((bit & num) >> i)] |
                                     (bit ^ bit & num))
            else:
                num ^= self._mask ^ (self._masks[(i << 1)+((bit & num) >> i)] |
                                     (bit & num))
        return num


class _XORShift(object):
    """XOR Shift implementation."""

    def __init__(self, seed, params, bitmask):
        self._seed = seed
        self._p_a, self._p_b, self._p_c = params
        self._bitmask = bitmask

    def __call__(self):
        self._seed ^= self._bitmask & (self._seed << self._p_a)
        self._seed ^= self._bitmask & (self._seed >> self._p_b)
        self._seed ^= self._bitmask & (self._seed << self._p_c)
        return self._seed
