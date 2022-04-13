#Oliver Hugh 4/4/2022

def repeating_nums(repeating_seq, static_num, jump=1):
    """
    Used if repeating numbers are found in a fraction. Returns
    a tuple of the numerator, denominator of what the unsimplified fraction is
    Example if we have .43333
    :param repeating_seq: the part that repeats in the fraction ex: .03
    :param static_num: .4
    :param jump: the number of digits in the repeating sequence ex: 1
    :return:
    """
    if repeating_seq != 0:
        #assume it repeats forever and say it is a geometric series
        #sum = a/(1-r)
        r = .1 ** jump
        a = repeating_seq
        repeating_numerator = a
        repeating_denominator = 1 - r
        #Make it so there are no decimal points in either the numerator or denominator
        while repeating_denominator % 10 or repeating_numerator % 10:
            repeating_denominator *= 10
            repeating_numerator *= 10
        #convert the static portion to a fraction with the same denominator
        static_num_numerator = static_num * repeating_denominator
        #make sure it is a whole number
        while static_num_numerator % 10:
            static_num_numerator *= 10
            #We also must make sure we update the repeating number so they have the same denominator
            repeating_numerator *= 10
            repeating_denominator *= 10
        new_numerator = static_num_numerator + repeating_numerator
        print(new_numerator, repeating_denominator)
        return int(new_numerator), int(repeating_denominator)
    else:
        denominator = 1
        while static_num % 10:
            static_num *= 10
            denominator *= 10
        return int(static_num), int(denominator)


def simplify(numerator: int, denominator: int):
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
        #iterate from 2 to 1/2 of the smaller number
        counter = 0
        for i in range(2, int(smaller_num//2)+1):
            #if first iteration, check if
            if i == 2:
                if numerator % denominator == 0:
                    numerator /= denominator
                    denominator /= denominator
                    continue_checking = False
                    break
                elif denominator % numerator == 0:
                    denominator /= numerator
                    numerator /= numerator
                    continue_checking = False
                    break
            if numerator % i == 0 and denominator % i == 0:
                numerator /= i
                denominator /= i
                continue_checking = True
                smaller_num = numerator if numerator < denominator else denominator
                break
    return int(numerator), int(denominator)


def frac_to_dec(numerator: int, denominator: int):
    """
    This function simply converts fractions to decimals
    :return: decimal equivalent of fraction
    """
    decimal = numerator / denominator
    return float("{:.5f}".format(decimal))
