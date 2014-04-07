import urllib2
import sys
from bs4 import BeautifulSoup

def getHoroscope(sign, horoscope_type):
    """
    Retrieves horoscope from site according to SIGN and HOROSCOPE_TYPE.
    """
    url = "http://www.elle.com/horoscopes/daily/" + sign + "-" + horoscope_type + "-horoscope"
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page)
    soup.prettify()
    horoscope = soup.find('div', {'class': "body bodySign"}).get_text()
    print(horoscope.encode(sys.stdout.encoding, errors='replace'))

def getUserInput(seed = None):
    """
    Requests user input for horoscope media queries.
    For simplicity of testing, optional parameter of seed which can retrieve queries. 
    Run doctest using "python -m doctest -v example.py"
    >>> wrong_entry = ["nothoroscope", "nottype"]
    >>> getUserInput(seed = wrong_entry)
    Invalid sign
    Invalid horoscope type
    >>> right_entry = ["cancer","daily"]
    >>> getUserInput(seed = right_entry)
    Success
    
    """
    signs = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn",
    "aquarius", "pisces"]
    types = ["daily", "weekly", "monthly"]
    if seed is None:
        sign = raw_input("Enter your horoscope sign: ").lower()
        horoscope_type = raw_input("Daily, weekly, or monthly?: ").lower()
    else:
        sign = seed[0]
        horoscope_type = seed[1]
    if sign not in signs:
        print("Invalid sign")
    if horoscope_type not in types:
        print("Invalid horoscope type")
    else:
        if seed is None:
            getHoroscope(sign, horoscope_type)
        else:
            print("Success")
if __name__ == '__main__':
    getUserInput()