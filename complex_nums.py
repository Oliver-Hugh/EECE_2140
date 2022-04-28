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
        term = 0, * and /: 2, + and -: 1, p: 3
        :param exp: the string to iterate through
        :return: the list of lists discussed above
        """
        #a list of lists (of length 2): term or operator, integer indicating order of operation, as discussed
        # in docstrings
        exp_lst = []
        answer = ""
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
            elif exp[i] in "eijp":
                if last_element_term or in_parenthesis:
                    exp_lst[-1][0] += exp[i]
                else:
                    val = exp[i], 0
                    exp_lst.append(list(val))
                    last_element_term = True

            elif exp[i] == "^":
                #make sure exp_lst has at least one element in it
                if i > 0:
                    #if last digit/character of last term
                    if exp_lst[-1][-1] in "+-/*^" or not last_element_term:
                        raise ValueError("Operator cannot precede '^'. Must be a term")
                    exp_lst[-1][0] += "^"
            elif exp[i] == "(":
                if last_element_term:
                    #add multiplication automatically
                    val = "*", 2
                    exp_lst.append(list(val))
                val = "(", 3
                exp_lst.append(list(val))
                in_parenthesis = True
            #check to make sure it has been properly opened and then close the parenthesis or raise an error
            elif exp[i] == ")":
                #first character of the term must be the start of the parenthesis
                if exp_lst[-1][0][0] == "(":
                    exp_lst[-1][0] += ")"
                    in_parenthesis = False
                else:
                    print(exp_lst[-1][0][0])
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

            new_lst.append(self.expr_lst[i])

    @staticmethod
    def mult_or_division(term_1, term_2, operation):
        print(term_1)
        print(term_2)
        print(operation)
        return 1

    @staticmethod
    def add_or_subtract(term_1, term_2, operation):
        print(term_1)
        print(term_2)
        print(operation)
        return 2

    @staticmethod
    def convert_to_polar(term):
        print(term)
        return 3

    @staticmethod
    def convert_to_rect(term):
        print(term)
        return 4
