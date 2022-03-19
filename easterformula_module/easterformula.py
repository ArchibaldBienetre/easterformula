def calculateEasterSundayDate(year):
    """ See: https://en.wikipedia.org/wiki/Date_of_Easter#Gauss's_Easter_algorithm
    Resp. https://de.wikipedia.org/wiki/Gau%C3%9Fsche_Osterformel#Eine_erg%C3%A4nzte_Osterformel"""
    # secular number
    k = year // 100

    # secular moon switching (?)
    m = 15 + (3 * k + 3) // 4 - (8 * k + 13) // 25

    # secular sun switching (?)
    s = 2 - (3 * k + 3) // 4

    # moon parameter
    a = year % 19

    # seed of the first full moon in spring
    d = (19 * a + m) % 30

    # calendar correction parameter
    r = (d + a // 11) // 29

    # easter threshold
    og = 21 + d - r

    # first sunday in March
    sz = 7 - (year + year // 4 + s) % 7

    # distance of Easter Sunday from easter threshold in days
    oe = 7 - (og - sz) % 7

    # date as number of day in March
    os = og + oe
    if os > 31:
        # maps over to April: 32nd March -> 1st April etc
        day = os - 31
        if day < 10:
            return str(year) + "-04-0" + str(day)
        else:
            return str(year) + "-04-" + str(day)
    else:
        if os < 10:
            return str(year) + "-03-0" + str(os)
        else:
            return str(year) + "-03-" + str(os)
