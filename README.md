# Permutation

[![Bitdeli](https://d2weczhvl823v0.cloudfront.net/attilaolah/permutation.py/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
[![Build Status](https://travis-ci.org/attilaolah/permutation.py.png?branch=master)](https://travis-ci.org/attilaolah/permutation.py)
[![Coverage Status](https://coveralls.io/repos/attilaolah/permutation.py/badge.png)](https://coveralls.io/r/attilaolah/permutation.py)

This package implements a simple, configurable permutation on the set of 64-bit
integers.

The permutation is based on a bitmask that maps each bit of the input to a bit
of the output. The bitmask is expanded from a random seed using a [PRNG][1], as
described by *George Marsaglia* in his paper called [Xorshift RNGs][2]. The
permutations are thus believed to be unpredictable, provided provided that the
seed is kept secret.

[1]: //en.wikipedia.org/wiki/Pseudorandom_number_generator
[2]: http://www.jstatsoft.org/v08/i14/paper

## Usage

Create a new `Permutation` instance by passing in two parameters:

* The first parameter is the seed, which can be any random value.
* The next paramer is a triplet of integers used by the XORShift to expand the
  seed. Valid values are listed in [George Marsaglia's paper][2], on *page 3*.

```python
>>> perm = permutation.Permutation(42, (13, 7, 17))
>>> perm.map(42)
3333656047352411619
>>> perm.unmap(3333656047352411619)
42
```

## Use cases

Use cases may vary, but an example that I find useful is generating
[hard][4]-to-guess, random-looking tokens based on IDs stored in a database.
The IDs can be used together with the seed to decode the original ID, but their
[cardinality][5] is the same as that of the IDs themselves. When used smartly,
this can save you from having to index those tokens in the database.

[4]: //en.wikipedia.org/wiki/NP-hard
[5]: //en.wikipedia.org/wiki/Cardinality

## See also

There is currently also a [Go implementation][6] of this library.

[6]: //github.com/attilaolah/permutation.go

## License

[Public domain][3].

[3]: //github.com/attilaolah/permutation.go/blob/master/LICENSE
