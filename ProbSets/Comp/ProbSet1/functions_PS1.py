from itertools import combinations, permutations

def smallest_factor(n):
    """Return the smallest prime factor of the positive integer n."""
    if n == 1: return 1
    for i in range(2, int(n**.5+1)):
        if n % i == 0: return i
    return n



def month_length(month, leap_year=False):
    """Return the number of days in the given month."""
    if month in {"September", "April", "June", "November"}:
        return 30
    elif month in {"January", "March", "May", "July", "August", "October", "December"}:
        return 31
    if month == "February":
        if not leap_year:
            return 28
        else:
            return 29
    else:
        return None


def operate(a, b, oper):
    """Apply an arithmetic operation to a and b."""
    if type(oper) is not str:
        raise TypeError("oper must be a string")
    elif oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    elif oper == '/':
        if b == 0:
            raise ZeroDivisionError("division by zero is undefined")
        return a / b
    raise ValueError("oper must be one of '+', '/', '-', or '*'")




class Backpack:

    def __init__(self, name, color, max_size=5):

        #name, color, max_size are attributes
        # __init__ is the constructor, which is a method


        self.name=name
        self.contents = []

        self.color = color
        self.max_size = max_size

    def put(self, item): #a method that adds 'item' to contents if possible

        if len(self.contents) >= self.max_size :

            # if the bag is full, 'item' is not added to contents and "No Room!" is printed.
            print("No Room!")

        if len(self.contents) < self.max_size:

            # if there is room for 'item' in the backpack, 'item' is added.

            self.contents.append(item)

    def take(self, item):

        #'item' is removed from the backpack

        self.contents.remove(item)

    def dump(self):

        #removes all contents from the backpack
        self.contents = []


class Fraction(object):
    """Reduced fraction class with integer numerator and denominator."""
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("denominator cannot be zero")

        elif type(numerator) is not int or type(denominator) is not int:
            raise TypeError("numerator and denominator must be integers")
    
        def gcd(a,b):
            while b != 0:
                a, b = b, a % b
            return a

        common_factor = gcd(numerator, denominator)
        self.numer = numerator // common_factor
        self.denom = denominator // common_factor

    def __str__(self):
        if self.denom != 1:
            return "{} / {}".format(self.numer, self.denom)
        
        else:
            return str(self.numer)

    def __float__(self):
        return self.numer / self.denom

    def __eq__(self, other):
        if type(other) is Fraction:
            return self.numer==other.numer and self.denom==other.denom
        else:
            return float(self) == other

    def __add__(self, other):
        return Fraction(self.numer*other.denom + self.denom*other.numer, self.denom*other.denom)

    def __sub__(self, other):
        return Fraction(self.numer*other.denom - self.denom*other.numer, self.denom*other.denom)

    def __mul__(self, other):
        return Fraction(self.numer*other.numer, self.denom*other.denom)

    def __truediv__(self, other):
        if self.denom*other.numer == 0:
            raise ZeroDivisionError("cannot divide by zero")

        return Fraction(self.numer*other.denom, self.denom*other.numer)





def count_sets(cards):
    
    if len(cards) != 12:
        raise ValueError("hand must contain 12 cards")
    if len(cards)>len(set(cards)):
        raise ValueError("all cards must be unique")
    for card in cards:
        if len(card) != 4:
            raise ValueError("each card must be described by 4 numbers")
    for card in cards:
        for num in card:
            if num not in "012":
                raise ValueError("each card must contain only numbers 0, 1, 2")
                
                
    numSets = 0
    combs = list(combinations(cards, 3))
    for potSet in combs:
        if is_set(str(potSet[0]), str(potSet[1]), str(potSet[2])):
            numSets += 1

    return numSets
    
    
def is_set(a,b,c):
    
    firstdigits = True
    seconddigits = True
    thirddigits = True
    fourthdigits = True
    
    set_first = {a[0], b[0], c[0]}
    set_second = {a[1], b[1], c[1]}
    set_third = {a[2], b[2], c[2]}
    set_fourth = {a[3], b[3], c[3]}
    
    A = [1,3]
    
    if len(set_first) not in A:
        firstdigits = False
    if len(set_second) not in A:
        seconddigits = False
    if len(set_third) not in A:
        thirddigits = False
    if len(set_fourth) not in A:
        fourthdigits = False
        
    print(firstdigits)
    print(fourthdigits)
        
    if firstdigits == True and seconddigits == True and thirddigits == True and fouthdigits== True:
        is_set = True
        
    else:
        is_set = False
        
    return is_set
