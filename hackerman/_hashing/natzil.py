# https://repl.it/@21natzil/BadHash

from sympy import divisors

collides = set()


def badhash(number: int, rounds=15, size: int = 0xFFFFFFFFFF):
    if not (rounds % 2):
        rounds += 1

    for i in range(rounds):
        d = divisors(number)
        for e, div in enumerate(d):
            number ^= (div ^ (number // div)) * e
        number *= sum(d)
        number ^= size
        number &= size
    return number >> 4


class BadHash:

    def __init__(self):
        self._hashed = 0

    def update(self, data: bytes):
        for byte in data:
            self._hashed = badhash(data[0] + self._hashed)
    
    def hexdigest(self):
        return hex(self._hashed)[2:]
