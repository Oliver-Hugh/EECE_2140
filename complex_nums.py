#Oliver Hugh 4/27/2022
import math


class ComplexExpression:
    def __init__(self, orig_string):
        self.orig_string = orig_string
        self.expr_lst = self.process(self.orig_string)
        print("the list is ", self.expr_lst)

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
        last_element_term = False
        #this for loop separates the string into individual terms and operators
        in_parenthesis = False
        for i in range(len(exp)):
            #if an operator
            if exp[i] in "*/":
                last_element_term = False
                val = exp[i], 2
                exp_lst.append(list(val))
            elif exp[i] in "+-":
                last_element_term = False
                val = exp[i], 1
                exp_lst.append(list(val))
            if exp[i].isdigit() or exp[i] == ".":
                #if it's the start of a number
                if not last_element_term and not in_parenthesis:
                    val = exp[i], 0
                    exp_lst.append(list(val))
                    last_element_term = True
                #if this character is continuing a number
                else:
                    #update the last element in the list of terms/numbers
                    exp_lst[-1][0] += exp[i]
            #check if imaginary component, e, pi, or parenthesis
            elif exp[i] in "ijp":
                if last_element_term or in_parenthesis:
                    exp_lst[-1][0] += exp[i]
                else:
                    val = exp[i], 0
                    exp_lst.append(list(val))
                    last_element_term = True

            elif exp[i] == u"\u2220":
                #make sure exp_lst has at least one element in it
                if i > 0:
                    #if last digit/character of last term is an operator
                    if not last_element_term:
                        raise ValueError("Number must precede ", u"\u2220")
                    exp_lst[-1][0] += u"\u2220"
            elif exp[i] == "(":
                if i > 0 and exp[i] == u"\u2220":
                    exp_lst[-1] += "("
                if last_element_term:
                    #add multiplication automatically
                    val = "*", 2
                    exp_lst.append(list(val))
                val = "(", 3
                exp_lst.append(list(val))
                in_parenthesis = True
            #check to make sure it has been properly opened and then close the parenthesis or raise an error
            elif exp[i] == ")":
                # term must already have the start of the parenthesis
                if "(" in exp_lst[-1][0]:
                    exp_lst[-1][0] += ")"
                    in_parenthesis = False
                else:
                    raise ValueError("Invalid Parenthesis order")
        return exp_lst

    def reduce_parenthesis(self):
        new_lst = []
        max_index = len(self.expr_lst)-1
        for i in range(max_index+1):
            #if there are parenthesis
            if self.expr_lst[i][0] == 3:
                #if operator to the left and right
                if i < max_index:
                    """for all comparisons under this if statement, we need to use the new list (which is updated for 
                    what is left in the list) when comparing to the left, and use self.expr_lst when comparing to 
                    terms to the right"""
                    #check if multiplication/division for first term
                    if self.expr_lst[i-1][1] == 2:
                        new_term = ComplexExpression.mult_or_division(term_1=self.expr_lst[i-2][0],
                                                                      term_2=self.expr_lst[i][0],
                                                                      operation=self.expr_lst[i][0])
                        new_lst.append(new_term)
                        #delete the 2 terms already in the list that were just operated on because they are now
                        # accounted for in the new term.
                        del new_lst[-1]
                        del new_lst[-1]
                        continue

                    #check if multiplication/division for next term
                    if self.expr_lst[i+1][1] == 2:
                        new_term = ComplexExpression.mult_or_division(term_1=self.expr_lst[i][0],
                                                                      term_2=self.expr_lst[i+2][0],
                                                                      operation=self.expr_lst[i+1][0])
                        new_lst.append(new_term)
                        #move to next iteration but skip two ahead to account for already operated terms
                        i -= 2
                        continue
                    #check if addition or subtraction for previous term
                    if self.expr_lst[i-1][1] == 1:
                        new_term = ComplexExpression.add_or_subtract(term_1=self.expr_lst[i-2][0],
                                                                     term_2=self.expr_lst[i][0],
                                                                     operation=self.expr_lst[i][0])
                        new_lst.append(new_term)
                        #delete the 2 terms already in the list that were just operated on because they are now
                        # accounted for in the new term.
                        del new_lst[-1]
                        del new_lst[-1]
                        continue
                    # check if add/sub for next term
                    if self.expr_lst[i + 1][1] == 1:
                        new_term = ComplexExpression.add_or_subtract(term_1=self.expr_lst[i][0],
                                                                     term_2=self.expr_lst[i + 2][0],
                                                                     operation=self.expr_lst[i + 1][0])
                        new_lst.append(new_term)
                        # move to next iteration but skip two ahead to account for already operated terms
                        i -= 2
                        continue
            new_lst.append(self.expr_lst[i])

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
        if u"\u2220" in term_1:
            term_1 = ComplexExpression.convert_to_rect(term_1)
        if u"\u2220" in term_2:
            term_2 = ComplexExpression.convert_to_rect(term_2)
        #now we have 2 rectangular numbers
        term_1_split = term_1.split("+")
        term_2_split = term_2.split("+")
        #from the convert to rect method, we get the numbers in the form a + bi or (-bi) or just a or just bj
        real_part = float(term_1_split[0]) + float(term_2_split[0])
        im_coefficient = float(term_1_split[:-1]) + float(term_2_split[:-1])
        string_answer = "{:.3f}".format(real_part) + "+" + "{:.3f}".format(im_coefficient) + "i"
        return string_answer

    @staticmethod
    def convert_to_polar(term):
        """
        Takes a string representation of a complex number in RECTANGULAR FORM and converts it to POLAR FORM
        :param term: string of a complex number
        :return: a string of the term in polar form
        """
        lst = []
        last_term_num = False
        im_in_last = False
        for ind in range(len(term)):
            if term[ind].isdigit() or term[ind] == ".":
                if last_term_num or im_in_last:
                    lst[-1] += term[ind]
                else:
                    lst.append(term[ind])
                    last_term_num = True
                    im_in_last = False
            elif term[ind] == "+":
                continue
            elif term[ind] == "-":
                last_term_num = True
                im_in_last = False
                lst.append(term[ind])

        return 3

    @staticmethod
    def convert_to_rect(term):
        #will return a+-bj if there is a negative (will always include the +)
        print(term)
        return 4
