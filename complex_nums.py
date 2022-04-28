#Oliver Hugh 4/27/2022
import math


class ComplexExpression:
    def __init__(self, orig_string, answer_format):
        self.answer_format = answer_format
        self.orig_string = orig_string
        self.answer = ComplexExpression.process(self.orig_string)
        self.answer = self.final_answer()

    @staticmethod
    def process(exp):
        """
        This method iterates through a string and creates a list of lists of length 2. The first element
        is either a term or operator, and the second is a number corresponding to the order of operation based on the
        numbers below:
        term = 0, * and /: 2, + and -: 1, parenthesis: 3   (NOT including terms after the angle symbol)
        :param exp: the string to iterate through
        :return: the list of lists discussed above
        """
        #a list of lists (of length 2): term or operator, integer indicating order of operation, as discussed
        # in docstrings
        exp_lst = []
        #elements will be either a term or operator in the list +-*/
        last_term_op = True
        skip_to = 0
        for ind in range(len(exp)):
            print("at the beginning of hte loop, exp list is  ", exp_lst)
            #if skip_to:
            ind += skip_to
            #now that we've skipped ahead in the previous if statement, we might be done:
            if ind > len(exp) - 1:
                break
            print("ind is ", ind)
            #there should never be 2 operators in a row (excluding -)
            if exp[ind] == "*" or exp[ind] == "/" or exp[ind] == "+":
                if exp[ind-1] == ")":
                    exp_lst.append(exp[ind])
                    last_term_op = True
                elif last_term_op:
                    #print("ERROR: the last term was ", exp[ind-1], " and the current is ", exp[ind])
                    #raise ValueError("Cannot have 2 operators in a row")
                    pass
                else:
                    last_term_op = True
                    exp_lst.append(exp[ind])
            #see if the - denotes a negative number or subtraction
            elif exp[ind] == "-":
                if last_term_op:
                    exp_lst.append(exp[ind])
                    last_term_op = False
                else:
                    last_term_op = False
                    exp_lst.append("+")
                    exp_lst.append("-")
            elif exp[ind] == "(":
                intermediate_parenthesis = ""
                #move to the next character (first character inside the parenthesis)
                orig_ind = ind
                ind += 1
                while ind < len(exp) and exp[ind] != ")":
                    intermediate_parenthesis += exp[ind]
                    ind += 1
                skip_to = ind - orig_ind
                #now we have a separate string of all the characters inside the () while not including ()
                #we need to convert this list into a string of one simplified term in polar form so that if
                #there is multiplication or division on either side, we don't have to worry about errors where only
                #1 term of many actually undergoes the operation
                term_to_add = ComplexExpression.process(intermediate_parenthesis)
                print("lst to add", term_to_add)
                exp_lst.append(term_to_add)
                #last_term_op = False
            elif last_term_op:
                exp_lst.append(exp[ind])
                last_term_op = False
            #if the last term was not an operator
            else:
                exp_lst[-1] += exp[ind]
        print("exp list is ", exp_lst)
        answer_string = ComplexExpression.simplify_to_one_term(exp_lst)
        return answer_string

    @staticmethod
    def simplify_to_one_term(lst):
        print("list to simplify, ", lst)
        if len(lst) == 1:
            return ComplexExpression.convert_to_polar(lst[0])
        new_lst = []
        max_index = len(lst)-1
        #due to order of operations, we need to iterate through the list once and see if there are any * or / before
        #we can check for + or -
        for i in range(max_index+1):
            #check if there is an operator to the left and right:
            if i < max_index:
                """for all comparisons under this if statement, we need to use the new list (which is updated for 
                what is left in the list) when comparing to the left, and use self.expr_lst when comparing to 
                terms to the right"""
                if lst[i] == '*' or lst[i] == "/":
                    new_term = ComplexExpression.mult_or_division(term_1=new_lst[-1],
                                                                  term_2=lst[i+1],
                                                                  operation=lst[i])
                    # delete the term already in the list that was just operated on because it is now
                    # accounted for in the new term.
                    del new_lst[-1]
                    new_lst.append(new_term)
                    #now skip one iteration and move onto the next one to skip over the term we just assessed
                    i += 1
                    continue
            new_lst.append(lst[i])

        #now we can iterate through again and see if there is + or -
        #the new_lst has the thus far updated terms, so we will iterate through it
        lst = new_lst
        #and we also need to create a new list to put the even more updated terms into
        newer_lst = []
        if len(lst) == 1:
            newer_lst.append(lst[0])
        skip = False
        for i in range(len(lst)):
            if skip:
                i += 1
            #print(newer_lst)
            if i < len(lst) - 1:
                #check if addition or subtraction
                if lst[i] == "+" or lst[i] == "-":
                    new_term = ComplexExpression.add_or_subtract(term_1=newer_lst[-1],
                                                                 term_2=lst[i+1])
                    new_term = ComplexExpression.convert_to_polar(new_term)
                    # delete the term already in the list that was just operated on because it is now
                    # accounted for in the new term.
                    del newer_lst[-1]
                    newer_lst.append(new_term)
                    # now skip one iteration and move onto the next one to skip over the term we just assessed
                    skip = True
                    continue
                newer_lst.append(lst[i])
        return newer_lst[0]

    @staticmethod
    def mult_or_division(term_1, term_2, operation):
        if u"\u2220" not in term_1:
            term_1 = ComplexExpression.convert_to_polar(term_1)
        if u"\u2220" not in term_2:
            term_2 = ComplexExpression.convert_to_polar(term_2)
        #now we have 2 polar numbers
        lst_coefficients = []
        lst_angles = []
        #find where the polar symbol is and partition
        ind_1 = term_1.index(u"\u2220")
        lst_coefficients.append(term_1[:ind_1])
        lst_angles.append(term_1[ind_1 + 1:])
        ind_2 = term_2.index(u"\u2220")
        lst_coefficients.append(term_2[:ind_2])
        lst_angles.append(term_2[ind_2 + 1:])
        if operation == "*":
            new_coefficient = float(lst_coefficients[0]) * float(lst_coefficients[1])
            new_angle = float(lst_angles[0]) + float(lst_angles[1])
        #if operation is division
        else:
            new_coefficient = float(lst_coefficients[0]) / float(lst_coefficients[1])
            new_angle = float(lst_angles[0]) - float(lst_angles[1])
        resulting_term = str(new_coefficient) + u"\u2220" + str(new_angle)
        return resulting_term

    @staticmethod
    def add_or_subtract(term_1, term_2):
        #if u"\u2220" in term_1:
        print("term 1 and term 2 before adding or subtracting: ", term_1, term_2)
        term_1 = ComplexExpression.convert_to_rect(term_1)
        #if u"\u2220" in term_2:
        term_2 = ComplexExpression.convert_to_rect(term_2)
        #now we have 2 rectangular numbers
        term_1_split = term_1.split("+")
        term_2_split = term_2.split("+")
        #print("term 1:", term_1_split)
        #print("term 2", term_2_split)
        #from the convert to rect method, we get the numbers in the form a + bi or (-bi) or just a or just bj
        real_part = float(term_1_split[0]) + float(term_2_split[0])
        im_coefficient = float(str(term_1_split[1][:-1])) + float(str(term_2_split[1][:-1]))
        string_answer = "{:.3f}".format(real_part) + "+" + "{:.3f}".format(im_coefficient) + "i"
        #print("string_answer is ", string_answer)
        return string_answer

    @staticmethod
    def convert_to_polar(term):
        """
        Takes a string representation of a complex number in RECTANGULAR FORM  (in the form: a + -bj; it can use i
        instead and might not have a negative sign, or may even be ONE of the terms) and converts it to POLAR FORM
        :param term: string of a complex number
        :return: a string of the term in polar form
        """
        #if it is already in polar form
        if u"\u2220" in term:
            return term
        term_lst = term.split("+")
        #if only one term
        if len(term_lst) == 1:
            im_index = term_lst[0].find("i")
            if im_index == -1:
                im_index = term_lst[0].find("j")
            # if there is definitively no imaginary component
            if im_index == -1:
                real_part = float(term_lst[0])
                im_coefficient = 0
            else:
                #if it's at beginning
                if im_index == 0:
                    im_coefficient = float(term_lst[0][1:])
                    real_part = 0
                #if at end
                else:
                    im_coefficient = float(term_lst[0][:-1])
                    real_part = 0
        #if there are 2 numbers, then there will be an imaginary component in term_lst[1]
        else:  # If len(term_lst) == 2:
            im_index = term_lst[1].find("i")
            if im_index == -1:
                im_index = term_lst[1].find("j")
            # if it's at the beginning
            if im_index == 0:
                im_coefficient = float(term_lst[1][1:])
            # if at end
            else:
                im_coefficient = float(term_lst[1][:-1])
            real_part = float(term_lst[0])
        magnitude = math.sqrt(math.pow(real_part, 2) + math.pow(im_coefficient, 2))
        if real_part != 0:
            angle = math.atan(im_coefficient / real_part)
            if real_part < 0 < im_coefficient:
                angle += math.pi
            if im_coefficient < 0 > real_part:
                angle -= math.pi
        else:
            angle = math.pi / 2
        answer_string = "{:.3f}".format(magnitude) + u"\u2220" + "{:.3f}".format(angle)
        return answer_string

    @staticmethod
    def convert_to_rect(term):
        """
        Takes a string representation of a number in polar form in the format 'number u"\u2220" number' and converts
        it to rectangular form
        :param term: string representation of a number in polar form
        :return: string representation of a number in polar form
        """
        #will return a+-bj if there is a negative (will always include the +)
        term_lst = term.split(u"\u2220")
        print(term_lst, "is term list")
        #make sure that it was polar in the first place
        if len(term_lst) == 2:
            magnitude = float(term_lst[0])
            angle = float(term_lst[1])
            real_part = magnitude * math.cos(angle)
            im_part = magnitude * math.sin(angle)
        #if it was rectangular but not in the right format for our processing:
        if len(term_lst) == 1:
            ind = term_lst[0].find("i")
            if ind == -1:
                ind = term_lst[0].find("j")
            #if there is no imaginary part
            if ind == -1:
                real_part = float(term_lst[0])
                im_part = 0
            else:
                real_part = 0
                #if it's just i or just j
                if len(term_lst[0]) == 1:
                    im_part = 1
                # if it's at the beginning
                elif ind == len(term_lst[0]) - 1:
                    im_part = float(term_lst[0][:-1])
                #if it's at the beginning of the number
                elif ind == 0:
                    im_part = float(term_lst[0][1:])
                else:
                    raise ValueError("i or j in imaginary component must be at the beginning or end of the number")
        answer_string = "{:.3f}".format(real_part) + "+" + "{:.3f}".format(im_part) + "i"
        return answer_string

    def final_answer(self):
        if self.answer_format == "po":
            return ComplexExpression.convert_to_polar(self.answer)
        elif self.answer_format == "r":
            return ComplexExpression.convert_to_rect(self.answer)
