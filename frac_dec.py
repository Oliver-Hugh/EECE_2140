#Oliver Hugh 4/4/2022

"""
pseudocode for decimal to fraction:

make it over a multiple of 10
iterate from 2 to 1/2 of the smaller number
once you reach a common product and divide both by it
if you've gone thru all of the numbers and there are none, then the fraction is simplified
"""


def repeating_nums(repeating_seq, static_num, jump=.1):
    """
    Used if repeating numbers are found in a fraction. Returns
    a tuple of the numerator, denominator of what the unsimplified fraction is
    Example if we have .43333
    :param repeating_seq: the part that repeats in the fraction ex: .03
    :param static_num: .4
    :param jump: the number of digits in the repeating sequence ex: 1
    :return:
    """
    #assume it repeats forever and say it is a geometric series
    #sum = a/(1-r)
    r = jump
    a = repeating_seq
    repeating_numerator = a
    repeating_denominator = 1 - r  # Will always be .9
    #Make it so there are no decimal points in either the numerator or denominator
    while repeating_denominator % 10 or repeating_numerator % 10:
        repeating_denominator *= 10
        repeating_numerator *= 10
    #convert the static portion to a fraction with the same denominator
    static_num_numerator = static_num * repeating_denominator
    static_num_denominator = 1 * repeating_denominator
    new_numerator = static_num_numerator + repeating_numerator
    return new_numerator, static_num_denominator


def simplify(numerator, denominator):
    """
    Tries to simplify a fraction given its numerator and denominator
    :param numerator: Numerator of fraction. Should be an int
    :param denominator: Denominator of fraction. Should be an int
    :return: a tuple of the simplified numerator, denominator
    """
    if type(numerator) is not int or type(denominator) is not int:
        raise TypeError("Numerator and Denominator must be integers")
    smaller_num = numerator if numerator < denominator else denominator
    continue_checking = True
    while continue_checking:
        continue_checking = False
        for i in range(1, smaller_num//2+1):
            if numerator % i == 0 and denominator % 10 == 0:
                numerator /= i
                denominator /= i
                continue_checking = True
                break
    return numerator, denominator


