# TODO: to_roman()
# NOTE: 1- from_roman pass all 2 + 5 test case on codewars
#       2- This was not meant to be OOP, I created the functions as functions,
#           then joined them into a class.


class RomanNaturals:
    symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    @classmethod
    def hasValidRomanLetters(cls, input):
        for letter in input:
            if letter not in cls.symbols:
                return False
        return True

    @classmethod
    def from_roman(cls, input, debug=False):
        if input is None or not cls.hasValidRomanLetters(input):
            return 0

        decimal = 0
        currblock = 0  # symbols[input[0]]

        for index in range(len(input)):
            thisVal = cls.symbols[input[index]]
            currblock += thisVal

            # get nextval
            if index < len(input) - 1:
                nextVal = cls.symbols[input[index+1]]
            else:
                decimal += currblock
                break
            if debug:  # debug if active
                print(thisVal, nextVal, currblock)

            # if next letter is equal
            if thisVal == nextVal:
                pass

            # if next letter value is smaller
            if thisVal > nextVal:
                decimal += currblock
                currblock = 0

            # if next letter value is greater
            if thisVal < nextVal:
                decimal -= currblock
                currblock = 0

            # debug if active
            if debug is True:
                print("curr input analized:", input[:index+1])
                print("currblock:", currblock, " | currVal:", decimal)
                print()

        return decimal

    @classmethod
    def to_roman(cls, num):
        pass


# MAIN
print(RomanNaturals.from_roman("CXII"))
print(RomanNaturals.from_roman("CMXXIV"))
print(RomanNaturals.from_roman("C"))
print(RomanNaturals.from_roman("III"))
