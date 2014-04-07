import sys

"""
Dict of how many of [key] do I need for a meter/liter/gram?
"""
unit_dict = {"m": 1, "cm": 100, "mm": 1000, "km": 0.001, "in": 39.3701, "ft": 3.28084, "yd": 1.09361, "mi": 0.000621371,
"L": 1,"mL": 1000,"floz": 33.814,"cup": 4.22675,"pint": 2.11338,"qt": 1.0569,"gal": 0.264172,
"g": 1,"kg": 0.001,"mg": 1000,"oz": 0.035274,"lb": 0.00220462}


def initialPrompt():
    """
    Welcome prompt upon user starting the program.
    """
    print("Welcome to our Python-powered Unit Converter v1.0 by Jenny Peng!")
    print("You can convert Distances, Weights, Volumes & Times to one another, but only")
    print("within units of the same category, which are shown below. E.g.: 1 mi in ft")
    print("")
    print("Distances: ft cm mm mi m yd km in")
    print("Weights: lb mg kg oz g")
    print("Volumes: floz qt cup mL L gal pint")
    print("")
    prompt()


def errorPrompt():
    """
    Friendly prompt printed upon invalid user input.
    """
    print("Opps! You've printed an invalid format. Please try again.")
    prompt()

def prompt():
    """
    Prompt for conversion. Asks for user input. If debug, print out values received.
    """
    print("")
    conversion = raw_input("Convert [AMT SOURCE_UNIT in DEST_UNIT, or (q)uit]:")
    if conversion.lower() == 'q':
        print("Thanks for converting with us. Y'all come back now, y'hear?")
        sys.exit(0)
    else:
        conversion = conversion.split(' ') #split by space
        if len(conversion) != 4:
            errorPrompt()
        try:
            num = float(conversion[0])
            source_unit = conversion[1]
            dest_unit = conversion[3]
            calculate(num, source_unit, dest_unit, False)
        except ValueError:
            errorPrompt()


def calculate(num, src, dst, debug):
    """
    Calculates how many dst are in num src.
    If debug flag is on, then we do not prompt again.
    >>> calculate(10, "mi", "m", True)
    10 mi = 16093.4449789 m
    >>> calculate(1, "lb", "oz", True)
    1 lb = 16.0000362874 oz
    >>> calculate(123.456789, "kg", "mg", True)
    123.456789 kg = 123456789.0 mg
    """
    try:
        base = num / unit_dict[src] # how many base units in num of src
        result = base * unit_dict[dst] # how many of dst in num of src
        print(str(num) + " " + src + " = " + str(result) + " " + dst)
        if not debug:
            prompt()
    except KeyError:
        errorprompt()
if __name__ == '__main__':
    initialPrompt()

