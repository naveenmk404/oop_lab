class FormulaError(Exception):
    pass

def cal(formula):
    try:
        val = formula.split()
        
        if len(val) != 3:
            raise FormulaError("Invalid formula")
        
        n1 = float(val[0])
        op = val[1]
        n2 = float(val[2])
        
        if op not in ['+', '-']:
            raise FormulaError("Invalid Operator")
        
        if op == '+':
            print(n1+n2)
        else :
            print(n1-n2)
        
    except ValueError :
        raise FormulaError("Invalid values")
    
while True:
    user_in = input("Enter formula ")
    
    if user_in.lower() == 'quit':
        break
    
    try:
        cal(user_in)
    except FormulaError as e:
        print(e)
