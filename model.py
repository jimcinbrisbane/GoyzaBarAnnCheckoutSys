class Model():
    def __init__(self):
        self.result = 0 #stores result
        self.buffer = 0#stores working number
        self.nn = True #new number
        #self.pending = False
        self.op = "" #operation
        self.equals = False #equals flag
        self.dec = 0 #decimal flag& shift
    def calc(self):
        if(self.op == "+"):
            self.result = self.result+self.buffer
        elif(self.op == "-"):
            self.result = self.result-self.buffer
        elif(self.op == "/"):
            self.result = self.result/self.buffer
        elif(self.op == "*"):
            self.result = self.result*self.buffer
        elif(self.op == "="):
            self.result = self.result
        else:
            print("error")

    def number_input(self,num):
        if (self.nn == True): #if the number is new (succeeds operation)
            self.nn = False #
            self.buffer = num #add number to buffer
        elif(self.dec):
            self.buffer = round(self.buffer+(num/(10**self.dec)),self.dec)
            self.dec = self.dec + 1
        else: #self.nn is False
            self.buffer = (self.buffer*10)+num #shift buffered digit and append new digit
    def op_input(self,op):
        self.dec = 0 #reset decimal input
        if(self.op == ""): #placed buffered number in result and select operation
            self.result = self.buffer
            self.op = op
        elif(op in ["-","+","*","/"] and self.equals == True): #no buffered operation on operations initially proceeding equals
            self.equals = False
            self.op = op
        elif(op in ["-","+","*","/"]): #perform calculation
            self.calc()
            self.op = op
        elif(op == "="): #perform buffered calculation
            self.calc()
            self.equals = True
        else:
            print("error")
        self.nn = True #a new number will be entered after an operation

    def input(self, n): #handles all input
        if(len(n) > 1): #inputs longer than one character are invalid
            print("invalid")
        elif (n == "c"): #cancel operations if c
            self.cancel()
        elif (n == "."):
            self.dec = 1
        elif (n in ["-","+","*","/","=",""]): #if input character, perform input operation
            self.op_input(n)
        elif (int(n) in range(10)): #if a number
            self.number_input(int(n)) #handle number input
        else:
            print("invalid")

    def get_info(self): #for debugging
        print("buffer: {} result: {} op: {} nn: {}".format(self.buffer, self.result, self.op, self.nn))

    def get_result(self): #returns result
        return self.result
    def get_buffer(self):
        return self.buffer
    def cancel(self):
        self.result = 0
        self.buffer = 0
        self.nn = True
        self.op = ""
        self.equals = False
        self.dec = 0

"""
instance = Model()
while(1):
    i = input('> ')
    instance.input(i)
    instance.get_info()
"""
