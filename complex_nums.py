#Oliver Hugh 4/27/2022
import math


#This class handles the logic for calculating complex numbers from an expression involving complex numbers
#To help paint a picture of the design and troubleshooting process, comments of print statements used to debug are
#left included
class ComplexExpression:
    def __init__(self, orig_string, answer_format):
        """
        Takes the answer format and original string of the expression and stores the answer as a string to the complex
        equation in self.answer
        :param orig_string: the original string of the complex expression
        :param answer_format: either "r" or "po" depending on if the answer should be polar or rectangular
        """
        self.answer_format = answer_format
        self.orig_string = orig_string
        self.answer = ComplexExpression.process(self.orig_string)
        self.answer = self.final_answer()

    @staticmethod
    def process(exp):
        """
        This method iterates through a string representing an equation and creates a list with the different terms
        and operators in the string separated. If there are parenthesis in the equation, it will handle them by
        recursively calling itself to deal with the parenthesis as its own sub-string. This method will then call
        the simplify_to_one_term function to reduce the list of terms into 1 number in polar form
        :param exp: the string to iterate through
        :return: a string representation of a number in polar form
        """
        #a list of lists (of length 2): term or operator, integer indicating order of operation, as discussed
        # in docstrings
        exp_lst = []
        #elements will be either a term or operator in the list +-*/
        last_term_op = True
        skip_to = 0
        for ind in range(len(exp)):
            #if skip_to:
            ind += skip_to
            #now that we've skipped ahead in the previous if statement, we might be done:
            if ind > len(exp) - 1:
                break
            #there should never be 2 operators in a row (excluding -)
            if exp[ind] == "*" or exp[ind] == "/" or exp[ind] == "+":
                if exp[ind-1] == ")":
                    exp_lst.append(exp[ind])
                    last_term_op = True
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
                exp_lst.append(term_to_add)
                #last_term_op = False
            elif last_term_op:
                exp_lst.append(exp[ind])
                last_term_op = False
            #if the last term was not an operator
            else:
                exp_lst[-1] += exp[ind]
        answer_string = ComplexExpression.simplify_to_one_term(exp_lst)
        return answer_string

    @staticmethod
    def simplify_to_one_term(lst):
        """
        Takes a list of terms and returns what the expression would be evaluated in a string representing a complex
        number in polar form
        :param lst: a list of terms in an expression
        :return: a string of a complex number in POLAR form
        """
        if len(lst) == 1:
            return ComplexExpression.convert_to_polar(lst[0])
        new_lst = []
        max_index = len(lst)-1
        #due to order of operations, we need to iterate through the list once and see if there are any * or / before
        #we can check for + or -
        skip_amount = 0
        skip = False
        print(max_index)
        for i in range(max_index+1):
            if skip:
                i += skip_amount
            #check if there is an operator to the left and right:
            print("max index is ", max_index, " and i is ", i)
            if i < len(lst):
                """for all comparisons under this if statement, we need to use the new list (which is updated for 
                what is left in the list) when comparing to the left, and use self.expr_lst when comparing to 
                terms to the right"""
                print("RIGHT HERE    lst[i] is ", lst[i])
                print("and the i is ", i)
                if lst[i] == '*' or lst[i] == "/":
                    new_term = ComplexExpression.mult_or_division(term_1=new_lst[-1],
                                                                  term_2=lst[i+1],
                                                                  operation=lst[i])
                    # delete the term already in the list that was just operated on because it is now
                    # accounted for in the new term.
                    print("multiplying ", new_lst[-1], "and ", lst[i+1])
                    print("the answer is ", new_term)
                    print("new list before deletion ", new_lst)
                    del new_lst[-1]
                    print("new list after deletion ",  new_lst)
                    new_lst.append(new_term)
                    print("list after appendage", new_lst)
                    #now skip one iteration and move onto the next one to skip over the term we just assessed
                    skip = True
                    skip_amount += 1
                    continue
                print("before adding, i is ", i, "and the max i is ", max_index)
                new_lst.append(lst[i])
                print("new list: ", new_lst)
                print('old list: ', lst)

        #now we can iterate through again and see if there is + or -
        #the new_lst has the thus far updated terms, so we will iterate through it
        lst = new_lst
        #and we also need to create a new list to put the even more updated terms into
        newer_lst = []
        skip_amount = 0
        if len(lst) == 1:
            newer_lst.append(lst[0])
        skip = False
        for i in range(len(lst)):
            if skip:
                i += skip_amount
            if i < len(lst):
                #check if addition or subtraction
                if lst[i] == "+" or lst[i] == "-":
                    new_term = ComplexExpression.add_or_subtract(term_1=newer_lst[-1],
                                                                 term_2=lst[i+1])
                    new_term = ComplexExpression.convert_to_polar(new_term)
                    # delete the term already in the list that was just operated on because it is now
                    # accounted for in the new term.
                    #print("the term going to be deleted is ", newer_lst[-1])
                    #print("the term going to added is ", new_term)
                    del newer_lst[-1]
                    #print("the list after deleting is ", newer_lst)
                    newer_lst.append(new_term)
                    #print("the list after adding is ", newer_lst)
                    #print(len(newer_lst), "is the length of the new list and should be 1")
                    # now skip one iteration and move onto the next one to skip over the term we just assessed
                    skip = True
                    skip_amount += 1
                    continue
                #print("adding at the bottom ", lst[i])
                newer_lst.append(lst[i])
                print("newer list: ", newer_lst)
                print("older list: ", lst)
        return newer_lst[0]

    @staticmethod
    def mult_or_division(term_1, term_2, operation):
        """
        multiplies or divides 2 terms and returns the result in polar form (as a string)
        :param term_1: a (complex?) number as a string
        :param term_2: a (complex?) number as a string
        :param operation: "*" or "/"
        :return: the product/ quotient of the 2 numbers as a polar string
        """
        term_1 = ComplexExpression.convert_to_polar(term_1)
        term_2 = ComplexExpression.convert_to_polar(term_2)
        print("term 1", term_1)
        print("term2 ", term_2)
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
        """
        Adds or subtracts 2 terms and then returns the sum in polar form
        :param term_1: a (complex?) number as a string
        :param term_2: a (complex?) number as a string
        :return: a string of a polar complex number that is the sum or difference of the 2 terms
        """
        term_1 = ComplexExpression.convert_to_rect(term_1)
        term_2 = ComplexExpression.convert_to_rect(term_2)
        #now we have 2 rectangular numbers
        term_1_split = term_1.split("+")
        term_2_split = term_2.split("+")
        #from the convert to rect method, we get the numbers in the form a + bi or (-bi) or just a or just bj
        real_part = float(term_1_split[0]) + float(term_2_split[0])
        im_coefficient = float(str(term_1_split[1][:-1])) + float(str(term_2_split[1][:-1]))
        string_answer = "{:.3f}".format(real_part) + "+" + "{:.3f}".format(im_coefficient) + "i"
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
        real_part = 0
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
                #if it is only i or only j
                if len(term_lst[0]) == 1:
                    im_coefficient = 1
                #if it's at beginning
                elif im_index == 0:
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
        if real_part != 0:
            angle = math.atan(im_coefficient / real_part)
            if real_part < 0 < im_coefficient:
                angle += math.pi
            if im_coefficient < 0 and 0 > real_part:
                angle += math.pi
        else:
            #if there is no real component
            if im_coefficient < 0:
                angle = -1 * math.pi / 2
            else:
                angle = math.pi / 2
        if im_coefficient == 0:
            if real_part < 0:
                angle = math.pi
            else:
                angle = 0
        magnitude = math.sqrt(math.pow(real_part, 2) + math.pow(im_coefficient, 2))
        answer_string = "{:.3f}".format(magnitude) + u"\u2220" + "{:.3f}".format(angle)
        print("polar conversion = ", answer_string)
        return answer_string

    @staticmethod
    def convert_to_rect(term):
        """
        Takes a string representation of a (probably) complex  number and converts it to rectangular form
        :param term: string representation of a complex number
        :return: string representation of a number in polar form
        """
        #will return a+-bj if there is a negative (will always include the +)
        term_lst = term.split(u"\u2220")
        #set to 0 as default so not referenced before assignment (but an error will be thrown if they aren't assigned
        #new values later)
        real_part = 0
        im_part = 0
        # make sure that it was polar in the first place
        if len(term_lst) == 2:
            magnitude = float(term_lst[0])
            angle = float(term_lst[1])
            real_part = magnitude * math.cos(angle)
            im_part = magnitude * math.sin(angle)
        #if it was rectangular but not in the right format for our processing:
        elif len(term_lst) == 1:
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
        """
        returns the final answer, in the correct format and with a reduced angle if it is polar
        :return: a string of the final answer
        """
        if self.answer_format == "po":
            unreduced_polar_coordinates = ComplexExpression.convert_to_polar(self.answer)
            return ComplexExpression.reduce_polar_coordinates(unreduced_polar_coordinates)
        elif self.answer_format == "r":
            return ComplexExpression.convert_to_rect(self.answer)

    @staticmethod
    def reduce_polar_coordinates(polar_string):
        """
        Takes a polar string in the format number angle symbol number and reduces the angle (the second number) so it
        is
        :param polar_string: a string of a polar number. Ex format: 2.344u"\u2220"4.345
        :return: a polar string with the angle reduced
        """
        polar_lst = polar_string.split(u"\u2220")
        angle = float(polar_lst[1])
        print(angle)
        if angle > math.pi:
            while angle > math.pi:
                angle -= 2 * math.pi
        elif angle < -1 * math.pi:
            while angle < math.pi:
                angle += 2 * math.pi
        return polar_lst[0] + u"\u2220" + "{:.3f}".format(angle)
