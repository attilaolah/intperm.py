# Permutation

[![Bitdeli](https://d2weczhvl823v0.cloudfront.net/attilaolah/intperm.py/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
[![Build Status](https://travis-ci.org/attilaolah/intperm.py.png?branch=master)](https://travis-ci.org/attilaolah/intperm.py)
[![Coverage Status](https://coveralls.io/repos/attilaolah/intperm.py/badge.png)](https://coveralls.io/r/attilaolah/intperm.py)

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

Create a new `Permutation` instance by passing in an optional seed.

```python
>>> fromo intperm import Permutation
>>> perm = Permutation(42)
>>> perm.map_to(37)
13750393542137160527L
>>> perm.map_from(13750393542137160527)
37
```

Not providing a seed will create a random permutation:

```python
>>> perm = Permutation()
>>> perm.map_from(perm.map_to(37)) == 37
True
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

This library is also implemented in [Ruby][7] and [Go][6].

[6]: //github.com/attilaolah/intperm.go
[7]: //github.com/attilaolah/intperm.rb

## License

[Public domain][3].

[3]: //github.com/attilaolah/intperm.py/blob/master/LICENSE
