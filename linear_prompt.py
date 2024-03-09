Math_Teacher_Prompt = """I want you to act as Math Teacher. Your objective is to rewrite a given equation into a more complex version to make it a bit harder to handle. But the rewritten prompt must be reasonable and must be understood and responded to by humans. After that Simplify equation and transform it to Symbolic Equation.
Try to create different kind of new equations base on Given equation to be more difficult and must followed these principles:
1. Do not solve the equation.
2. The new equation must be written in form of [[equation]]
3. Do not use the same equation as the given equation.

""".strip()

Ahrimetic_Seed = """
Task: using Arithmetic methods such as multiplication - division number to make the equation more complex,generate new equations with each method.If division is used, make sure the divisor is not zero and if not divisible, keep the fraction.

equation: 2*x + 3 = 7
Multiply equation: [[2*x + 3 * 12 = -7 * 6]]
Symbolic Equation: [[2*x + 3 * 12, -7 * 6 , x , solve]]

Divide equation: [[ (4*x+2)/2  = 7/4 ]]
Symbolic Equation: [[(4*x+2)/2,7/4,x,solve]]

equation: 4x - 106 = -66

Multiply equation: [[2(4x-106)=2(-66)]]
Symbolic Equation: [[2*(4*x-106),2*(-66),x,solve]]

Divide equation: [[(4x-106)/2=(-66)/2]]
Symbolic Equation: [[(4*x-106)/2,(-66)/2,x,solve]]

equation: 29 = 6*f - 31
Multiply equation: [[29 * 5 = 6 * f * 5 - 31 * 5]]
Symbolic Equation: [[29 * 5 , 6 * f * 5 - 31 * 5 , f , solve]]

Divide equation: [[29 / 3 = 6 * f - 31 / 3]]
Symbolic Equation: [[29 / 3, 6*f - 31 / 3,f,solve]]

equation:{equation}
""".strip()


Variables_On_Both_Sides_Seed = """
Task: Adding Variables on Both Sides of the Equation and parenthesis to group terms to clarify the structure of the equation.
equation: [[-52*a - 95 = 82*a + 39]]
Complex_Equation: [[-52*(a + 3) - (95 - 2*a) = 82*(a - 2) + (39 + a)]]
Symbolic Equation: [[-52*(a + 3) - (95 - 2*a), 82*(a - 2) + (39 + a) , a , solve]]

equation: [[21*d = 182 - 35]]
Complex_Equation: [[21d + (3d - 7) = 182 - (35 + 5*d)]]
Symbolic Equation: [[21*d + (3*d - 7), 182 - (35 + 5*d) , d , solve]]

equation: [[-2076 = -230*w - 6]]
Complex_Equation: [[-2076 + (115w + 3) = -230w - 6 - (115*w - 3)]]
Symbolic Equation: [[-2076 + (115*w + 3), -230*w - 6 - (115*w - 3) , w , solve]]

equation:[[{equation}]]
""".strip()

Deepening_Seed = """
Task : Deepening the equation by substituting the variable with a more complex expression.
equation: [[-52*a - 95 = 82*a + 39]]

Complex_Equation: [[-52*(2*a - 3) - 95 = 82*(3*a - 2) + 39]]
Symbolic Equation: [[-52*(2*a - 3) - 95, 82*(3*a - 2) + 39 , a , solve]]

equation: [[21*d = 182 - 35]]
Complex_Equation: [[21(2d + 1) = 182 - 35]]
Symbolic Equation: [[21*(2*d + 1), 182 - 35 , d , solve]]

equation: [[-2076 = -230*w - 6]]
Complex_Equation: [[-2076 = -230*(w + 3) - 6 - 230]]
Symbolic Equation: [[-2076, -230*(w + 3) - 6 - 230 , w , solve]]

equation:{equation}
""".strip()

Distribution_Seed = """
Task: Distribute the coefficients to the terms - expression inside parentheses.

equation: [[-52*a - 95 = 82*a + 39]]
Complex_Equation: [[-52*(a + 3) - 95 = 82*(a - 2) + (39 + 4*(2*a - 5))]]
Symbolic Equation: [[-52*(a + 3) - 95, 82*(a - 2) + (39 + 4*(2*a - 5)) , a , solve]]

equation: [[21*d = 182 - 35]]
Complex_Equation: [[21*(d + 4) - 3*(2*d + 3) = 182 - 35 + d]]
Symbolic Equation: [[21*(d + 4) - 3*(2*d + 3), 182 - 35 + d , d , solve]]

equation: [[-2076 = -230*w - 6]]
Complex_Equation: [[-2076 - 2*(115w + 10) = -230w - 6 - 2*(57*w + 3)]]
Symbolic Equation: [[-2076 - 2*(115*w + 10), -230*w - 6 - 2*(57*w + 3) , w , solve]]

equation:{equation}
""".strip()

Context_Equation = """
I want you to act as Math Teacher. Your objective is to rewrite a given equation into a more complex version to make it a bit harder to handle. But the rewritten prompt must be reasonable and must be understood and responded to by humans.
Task: Create a word problem that can be represented by the given equation. Then transform the word problem to an equation.
equation: 2*x + 3 = 7
Word Problem:
"Imagine you have a basket with some apples. Each apple is represented by 'x'. You have two apples, so we represent this as '2x'. Now, you also have three oranges, which we represent as '3'. Altogether, you have seven fruits in your basket, represented as '7'. So, the total number of fruits in your basket can be represented by the equation '2x + 3 = 7'."

Transforming this word problem to an equation:
"Two apples" or "2*x" - This represents the multiplication operation.
"Three oranges" or "3" - This represents the addition operation.
"Seven fruits in your basket" or "7" - This represents the total value of the equation.
So, when you put these together, you get the 
Equation: [[2*x + 3 = 7]]
Symbolic Equation: [[2*x + 3, 7 , x , solve]]

equation: 20x = 2880
Word Problem:
"A farming field can be ploughed by 6 tractors in 4 days. When 6 tractors work together, each of them ploughs 120 hectares a day. If two of the tractors were moved to another field, then the remaining 4 tractors could plough the same field in 5 days. How many hectares a day would one tractor plough then?"
Transforming this word problem to an equation:
If each of 6 6 tractors ploughed 120 120 hectares a day and they finished the work in 4 4 days, then the whole field is: 120 * 6 * 4 = 720 * 4 = 2880 hectares.Let's suppose that each of the four tractors ploughed x hectares a day. Therefore in 5 days, the whole field is: 4 * x * 5 = 20 * x = 2880 hectares.
So the equation is: 20x = 2880
Equation: [[20x = 2880]]
Symbolic Equation: [[20x, 2880 , x , solve]]

equation: -52a - 95 = 82a + 39
Word Problem:
In a small town, there were two groups of people, one group collected (-52a) apples and the other group collected (82a) apples. The first group also had a debt of 95 dollars, while the second group had 39 dollars in their pocket. In order to make the total number of apples and the total amount of money equal for both groups, how many apples (a) should be distributed among them?

Transforming this word problem to an equation:
The first group has a negative collection of 52 times the number of apples (a) and a debt of 95 dollars, which can be represented as -52a - 95.
The second group has a positive collection of 82 times the number of apples (a) and 39 dollars in their pocket, which can be represented as 82a + 39. 
To make the total number of apples and the total amount of money equal for both groups, we need to find the value of 'a' such that -52a - 95 = 82a + 39.

Equation: [[-52a - 95 = 82a + 39]]
Symbolic Equation: [[-52a - 95, 82a + 39 , a , solve]]

equation: {equation}

""".strip()


# Deepening_Seed
# Complex_Equation: [[72 - 28 = 11(q + 2)]]
# Simplify equation: [[44 = 11q + 22]]
# Symbolic Equation: [[44, 11q + 22, q, solve]]

# Variables_On_Both_Sides_Seed
# # equation:[[5x - 13 = -8x]]
# Complex_Equation: [[5x - 13 = -8x + (3x - 15 + 2)]]
# Simplify equation: [[5x - 13 = -8x + 3x - 13]]
# Symbolic Equation: [[5x - 13, -8x + 3x - 13, x, solve]]

# Distribution_Seed
# # equation:[[24*o + 94 = -98]]
# Complex_Equation: [[24*(o - 5) + (94 + 3*(2*o - 10)) = -98]]
# Simplify equation: [24o - 120 + 94 + 6o - 30 = -98]
# Symbolic Equation: [[24o - 120 + 94 + 6o - 30, -98, o, solve]]

# Adding seed
# Add equation: [[2*x + 3 + 4  = 7 + 4 + 4*x]]
# Simplify equation: [[2*x + 7 = 11 + 4*x]]
# Symbolic Equation: [[2*x + 7, 11 + 4*x , x , solve]]
# Add equation: [[4x-106+20=-66+20]]
# Simplify equation: [[4x-86=-46]]
# Symbolic Equation: [[4x-86,-46,x,solve]]

# Subtract seed
# Subtract equation: [[2*x + 3 - 5 + 3*x = 7 - 4]]
# Simplify equation: [[5*x - 2 = 3]]
# Symbolic Equation: [[5*x - 2, 3 , x , solve]]
# Subtract equation: [[4x-106-2x=-66-2x]]
# Simplify equation: [[2x-106=-66-2x]]
# Symbolic Equation: [[2x-106,-66-2x,x,solve]]
