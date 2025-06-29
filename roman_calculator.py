operators = ('+', '-', '*','/')
roman_numerals =('I','V','X','L','C','D','M')

def console_ps1(func):
    def wrapper(self,):
        print(">>> ", end="")
        res = func(self)
        return res
    return wrapper

class Calculator():
    def __init__(self):
        self.instruction = str()
        self.part_instruction = list()
        self.is_valid = False

    @console_ps1
    def __user_input(self):
        self.instruction = input().strip()
    
    def __check_instruction_validity(self):
        self.is_valid = True
        instruction = self.instruction.replace(" ", "")
        # Check if the expression is empty
        if not instruction:
            return False
        # Check if the first or last character is an operator
        if (instruction[0] in operators or instruction[-1] in operators ):
            self.is_valid = False
        # Check for valid characters and operator placement
        # work becausse instruction[-1] is not an operator
        previous_operator_position =  -1
        for i, car in enumerate(instruction):
            if not (car in operators or car.isnumeric()):
                self.is_valid =  False
                break
            if car in operators:
                if i-previous_operator_position == 1:
                    self.is_valid =  False
                    break
                previous_operator_position = i
        if self.is_valid == False:
            print("Invalid character in expression.")
    
    def __compute(self):
        pass

        
    
    def __console(self): 
        self.__user_input()
        while not (self.instruction.lower() == "q" or self.instruction.lower() == "exit"):
            self.__user_input()
            self.__check_instruction_validity()
            if self.is_valid == True:
                pass
                #self.__compute()
        return 0

    def start(self):
        print("################")
        print("## CALCULATOR ##")
        print("################")
        return self.__console()


if '__main__' == __name__:
    myCalculator = Calculator()
    myCalculator.start()
