
# Advent of Code 2025 - Day 6

class MathProblem:
    def __init__(self, operand_one, operand_two, operand_three, operator):
        self.operand_one = operand_one
        self.operand_two = operand_two
        self.operand_three = operand_three
        self.operator = operator

class ComplexMathProblem(MathProblem):
    def __init__(self, operand_one, operand_two, operand_three, operand_four, operator):
        super().__init__(operand_one, operand_two, operand_three, operator)
        self.operand_four = operand_four
        
class PartTwoMathProblem:
    def __init__(self):
        self.operator = ""
        self.operands = []

def parse_input(input, use_sample_input=False):
    sample_input = []
    sample_input.append("123 328  51 64 ")
    sample_input.append(" 45 64  387 23 ")
    sample_input.append("  6 98  215 314")
    sample_input.append("*   +   *   +  ")
    
    math_problems = []
    
    operand_ones = [int(x) for x in " ".join(sample_input[0].split()).split()] if use_sample_input else [int(x) for x in " ".join(input[0].split()).split()]
    operand_twos = [int(x) for x in " ".join(sample_input[1].split()).split()] if use_sample_input else [int(x) for x in " ".join(input[1].split()).split()]
    operand_threes = [int(x) for x in " ".join(sample_input[2].split()).split()] if use_sample_input else [int(x) for x in " ".join(input[2].split()).split()]
    operand_fours = [] if use_sample_input else [int(x) for x in " ".join(input[3].split()).split()]
    operators = [x for x in " ".join(sample_input[3].split()).split()] if use_sample_input else [x for x in " ".join(input[4].split()).split()]
    
    for x in range(0, len(operand_ones)):
        if use_sample_input:
            math_problems.append(MathProblem(operand_ones[x], operand_twos[x], operand_threes[x], operators[x]))
        else:
            math_problems.append(ComplexMathProblem(operand_ones[x], operand_twos[x], operand_threes[x],operand_fours[x], operators[x]))
                
    return math_problems

def parse_input_part_2(input, use_sample_input=False):
    sample_input = []
    sample_input.append("123 328  51 64 ")
    sample_input.append(" 45 64  387 23 ")
    sample_input.append("  6 98  215 314")
    sample_input.append("*   +   *   +  ")
    
    math_problems = []
    row1 = sample_input[0] if use_sample_input else input[0]
    row2 = sample_input[1] if use_sample_input else input[1]
    row3 = sample_input[2] if use_sample_input else input[2]
    row4 = sample_input[3] if use_sample_input else input[3]
    row5 = [] if use_sample_input else input[4]
    
    if use_sample_input:
        pointer = 0
        math_problem = PartTwoMathProblem()
        while pointer < len(row1):
            row1_val = row1[pointer]
            row2_val = row2[pointer]
            row3_val = row3[pointer]
            row4_val = row4[pointer]
            
            if row1_val == ' ' and row2_val == ' ' and row3_val == ' ' and row4_val == ' ':
                math_problems.append(math_problem)
                math_problem = PartTwoMathProblem()
                
            else:
                row1_num = None if row1_val == ' ' else row1_val
                row2_num = None if row2_val == ' ' else row2_val
                row3_num = None if row3_val == ' ' else row3_val
                row4_operator = None if row4_val == ' ' else row4_val
                
                operand = ""
                operand += row1_num if row1_num else ""
                operand += row2_num if row2_num else ""
                operand += row3_num if row3_num else ""
                
                math_problem.operands.append(int(operand))
                if row4_operator:
                    math_problem.operator = row4_operator

            pointer += 1
            
        math_problems.append(math_problem)
        
    else:
        pointer = 0
        math_problem = PartTwoMathProblem()
        while pointer < len(row1):
            row1_val = row1[pointer]
            row2_val = row2[pointer]
            row3_val = row3[pointer]
            row4_val = row4[pointer]
            row5_val = row5[pointer]
            
            if row1_val == ' ' and row2_val == ' ' and row3_val == ' ' and row4_val == ' ' and row5_val == ' ':
                math_problems.append(math_problem)
                math_problem = PartTwoMathProblem()
                
            else:
                row1_num = None if row1_val == ' ' else row1_val
                row2_num = None if row2_val == ' ' else row2_val
                row3_num = None if row3_val == ' ' else row3_val
                row4_num = None if row4_val == ' ' else row4_val
                row5_operator = None if row5_val == ' ' else row5_val
                
                operand = ""
                operand += row1_num if row1_num else ""
                operand += row2_num if row2_num else ""
                operand += row3_num if row3_num else ""
                operand += row4_num if row4_num else ""
                
                math_problem.operands.append(int(operand))
                if row5_operator:
                    math_problem.operator = row5_operator

            pointer += 1
            
        math_problems.append(math_problem)
                
    return math_problems

def solve_part_one(input):
    math_problems = parse_input(input, False)
    
    sum_of_answers = 0
    
    for math_problem in math_problems:
        if math_problem.operator == '+':
            if hasattr(math_problem, 'operand_four'):
                sum_of_answers += (math_problem.operand_one + math_problem.operand_two + math_problem.operand_three + math_problem.operand_four)
            else:
                sum_of_answers += (math_problem.operand_one + math_problem.operand_two + math_problem.operand_three)
        elif math_problem.operator == '*':
            if hasattr(math_problem, 'operand_four'):
                sum_of_answers += (math_problem.operand_one * math_problem.operand_two * math_problem.operand_three * math_problem.operand_four)
            else:
                sum_of_answers += (math_problem.operand_one * math_problem.operand_two * math_problem.operand_three)
    
    return sum_of_answers

def solve_part_two(input):
    math_problems = parse_input_part_2(input, False)
    
    sum_of_answers = 0
    
    for math_problem in math_problems:
        if math_problem.operator == '+':
            answer = 0
            for operand in math_problem.operands:
                answer += operand
            sum_of_answers += answer
        elif math_problem.operator == '*':
            answer = 1
            for operand in math_problem.operands:
                answer *= operand
            sum_of_answers += answer
    
    return sum_of_answers
