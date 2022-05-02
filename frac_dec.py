#Oliver Hugh 4/4/2022


#functions in this file deal with the logic of converting fractions to decimals and vice versa
def repeating_nums(repeating_seq, static_num):
    """
    Used if repeating numbers are found in a fraction. Returns
    a tuple of the numerator, denominator of what the unsimplified fraction is
    Example if we have .43333
    :param repeating_seq: the part that repeats in the fraction ex: .03
    :param static_num: .4
    :return: numerator, denominator  (Both ints)
    """
    if repeating_seq != 0:
        """
        #The following commented code works for most decimals, but after some experimentation, I learned it doesn't work
        #for all repeating decimals. For example .415 repeating. It will run an infinite loop because 1 - .001 will not
        #exactly equal .999. This is left in to show my process for this, which took a long time to figure out. Below 
        this comment is the actual code, which works by converting numbers to strings and back so that we can ensure
        the values are exact, like a and 1-r in the geometric series summation formula
        
        #assume it repeats forever and say it is a geometric series
        #sum = a/(1-r)
        r = .1 ** jump
        a = repeating_seq
        repeating_numerator = a
        #the line below is the logic, but we will assign it in a different way due to how python handles floats (it
        #needs to be 1 - r exactly)
        #repeating_denominator = 1 - r"""
        repeating_numerator = str(repeating_seq)
        print("repeating numerator is", repeating_numerator)
        #get all numbers to the right of the decimal place
        repeating_numerator = repeating_numerator.split(".")[1]
        print("no decimal repeating numerator", repeating_numerator)
        #default no jump
        jump = 0
        if "0" in repeating_numerator:
            extra = len(repeating_numerator)
            print("extra is ", extra)
            for num_char_index in range(len(repeating_numerator)):
                if repeating_numerator[num_char_index] == "0":
                    continue
                else:
                    jump = len(repeating_numerator[num_char_index:])
            print("jump is ", jump)
            #number of extra zeros
            extra -= jump
        else:
            jump = len(repeating_numerator)
            extra = 0
        repeating_numerator = int(repeating_numerator)
        repeating_denominator = ""
        for k in range(jump):
            repeating_denominator += "9"
        for m in range(extra):
            repeating_denominator += "0"
        print(repeating_numerator)
        print(repeating_denominator)
        repeating_denominator = int(repeating_denominator)

        #convert the static portion to a fraction with the same denominator
        static_num_numerator = static_num * repeating_denominator
        #make sure it is a whole number
        while static_num_numerator % 10:
            static_num_numerator *= 10
            #We also must make sure we update the repeating number, so they have the same denominator
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
        print("denominator is", denominator)
        if numerator % denominator == 0:
            numerator /= denominator
            denominator /= denominator
            continue_checking = False
        elif denominator % numerator == 0:
            denominator /= numerator
            numerator /= numerator
            continue_checking = False
        for i in range(2, int(smaller_num//2)+1):
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
