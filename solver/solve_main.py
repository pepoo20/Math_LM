import sympy
from sympy import symbols, cos, simplify, trigsimp, factor, solveset, S, Eq, solve, solve_univariate_inequality
import re
from solve_function import Solve,Relation
from utils import Operation, my_igcd, my_ilcm
from trigometry import symplify_trigometry
Relation = Relation
Action = ['solve', 'igcd', 'ilcm', 'divisible', 'simplify']
def isOperator(x):
    return x in ['+', '-', '*', '/']

def isAction(x):
    return x in Action

def doAction(Equation_to_Solve, action):
    if action == 'solve':
        return Solve(Equation_to_Solve)
    elif action == 'igcd':
        return my_igcd(Equation_to_Solve)
    elif action == 'ilcm':
        return my_ilcm(Equation_to_Solve)
    elif action == 'divisible':
        return divisible(Equation_to_Solve[0], Equation_to_Solve[1])
    elif action == 'simplify':
        return symplify_trigometry(Equation_to_Solve)
    

def extract_equation(parse_equation):
    parse_equation = re.findall(r'\[\[(.*?)\]\]', parse_equation)[0].split(',')
    parse_equation = [simplify(item.strip()) if item.strip() not in Action and item.strip() not in Relation else item.strip() for item in parse_equation]
    print(parse_equation)
    Equation_to_Solve = []
    for i in range(len(parse_equation)):
        if isOperator(parse_equation[i]):
            print("Use Operator")
            number = Operation(Equation_to_Solve, parse_equation[i])
            Equation_to_Solve.append(number)
        elif isAction(parse_equation[i]):
            print("Before Action", Equation_to_Solve)
            result = doAction(Equation_to_Solve, parse_equation[i])
            return result
        else:
            Equation_to_Solve.append(parse_equation[i])
            
    return Equation_to_Solve