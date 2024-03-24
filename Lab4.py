# Chelsea Rowe Python Programming II
from functools import reduce
from Fraction import *
from decimal import *

pi50 = Decimal('3.14159265358979323846264338327950288419716939937510')
iterations = 100000


# Part I
class LeibnizPiIterator:
    def __init__(self):
        pass

    def __iter__(self):
        self.fraction = Fraction(0, 1)
        self.n = 1
        self.add_next = True
        return self

    def __next__(self):
        # I kept getting an attribute error, so I added self.__iter__() since __iter__ returns self.
        # I don't think this is right, but I wasn't sure what else to do to get it to work.
        # I tried making other variables, I tried to replicate the Custom Iterators video.. I'm sure when the
        # solution code comes out, it will seem really obvious to me then! (*hopefully*)
        # Clearly this section is the problem since it only returns 4.
        self.__iter__()
        if self.add_next:
            self.fraction += Fraction(4, self.n)
        else:
            self.fraction -= Fraction(4, self.n)
        # making add_next opposite
        self.add_next = not self.add_next
        self.n += 2
        return self.fraction.value


pi_iterator = LeibnizPiIterator()
for i in range(iterations):
    leibPi = next(pi_iterator)

counter = 0
for x in LeibnizPiIterator():
    counter += 1
    if counter >= iterations:
        break
print(f"Pi after {iterations} iterations: {leibPi:.50f}")
diff = pi50 - leibPi
print(f"Difference: {diff:0.50f}")

iterations2 = 10000000
pi_iterator_10m = LeibnizPiIterator()
for i in range(iterations2):
    leibPi = next(pi_iterator_10m)

counter = 0
for x in pi_iterator_10m:
    counter += 1
    if counter >= iterations2:
        break
print(f"Pi after {iterations2} iterations: {leibPi:.50f}")
diff = pi50 - leibPi
print(f"Difference: {diff:0.50f}")


# PART II
def NilakanthaPiGenerator():
    fraction = Fraction(3, 1)
    num = 2
    add_next = True

    while True:
        operand = Fraction(4, (num * (num + 1) * (num + 2)))
        if add_next:
            fraction += operand
        else:
            fraction -= operand
        # making add_next opposite
        add_next = not add_next
        num += 2
        yield fraction.value


gen = NilakanthaPiGenerator()
for i in range(iterations):
    nilaPi = next(gen)
print(f"Pi after {iterations} iterations through the Nilakantha Generator: {nilaPi}")
diff2 = pi50 - nilaPi
print(nilaPi)
print(f"Difference: {diff2}")

iterations = 10000000
for i in range(iterations):
    nilaPi = next(gen)
print(f"Pi after {iterations} iterations through the Nilakantha Generator: {nilaPi}")
diff2 = pi50 - nilaPi
print(nilaPi)
print(f"Difference: {diff2}")


# PART III
def compose(*functions):
    return reduce(lambda f, g: lambda x: g(f(x)), functions)


def milesToYards(value):
    return value * 1760


def yardsToMiles(value):
    return value * .0005681818181818


def yardsToFeet(value):
    return value * 3


def feetToYards(value):
    return value * 0.3333333333333333


def feetToInches(value):
    return value * 12


def inchesToFeet(value):
    return value * .0833333333333333


def inchesToCm(value):
    return value * 2.54


def cmToInches(value):
    return value * .3937007874015748


def cmToMeters(value):
    return value * 0.01


def metersToCm(value):
    return value * 100


def metersToKm(value):
    return value * 0.001


def kmToMeters(value):
    return value * 1000


def kmToAu(value):
    return value * .000000006684587122268445


def auToKm(value):
    return value * 149597870.700


def auToLy(value):
    return value * .00001581250740982065847572


def lyToAu(value):
    return value * 63241.07708426628026865358


# extra credit conversions
def cmToMm(value):
    return value * 10


def mmToCm(value):
    return value * .1


def mmtoMM(value):
    return value * 1000


def MMTomm(value):
    return value * .001


def MMToAng(value):
    return value * 10000


def AngToMM(value):
    return value * .00001


milesToInches = compose(milesToYards, yardsToFeet, feetToInches)
feetToMeters = compose(feetToInches, inchesToCm, cmToMeters)
metersToInches = compose(metersToCm, cmToInches)
milesToKM = compose(milesToYards, yardsToFeet, feetToInches, inchesToCm, cmToMeters, metersToKm)
kmToMiles = compose(kmToMeters, metersToInches, inchesToFeet, feetToYards, yardsToMiles)
kmToInches = compose(kmToMeters, metersToInches)
inchesToKm = compose(inchesToCm, cmToMeters, metersToKm)
metersToLightYears = compose(metersToKm, kmToAu, auToLy)

# extra credit
mmToYards = compose(mmToCm, cmToInches, inchesToFeet, feetToYards)
cmToAng = compose(cmToMm, mmtoMM, MMToAng)

print(milesToInches(2))
print(feetToMeters(5))
print(metersToInches(1))
print(milesToKM(10))
print(kmToMiles(1))
print(kmToInches(12.7))
print(inchesToKm(500000))
print(metersToLightYears(9460730472580800))
# extra credit
print('Extra credit:', mmToYards(198530), ',', cmToAng(2))
