# Advent of Code 2023 - Day 1

def solve_part_one(input):
    sum = 0
    
    for line in input:
        leftPointer = 0
        rightPointer = len(line) - 1
        
        leftMostDigit = 0
        rightMostDigit = 0
        
        leftDigitFound = False
        rightDigitFound = False
        
        while rightPointer >= leftPointer and not (leftDigitFound != False and rightDigitFound != False):
            if line[leftPointer].isdigit():
                leftMostDigit = line[leftPointer]
                leftDigitFound = True
            else:
                leftPointer += 1
                
            if line[rightPointer].isdigit():
                rightMostDigit = line[rightPointer]
                rightDigitFound = True
            else:
                rightPointer -= 1
        
        digitSum = (int(leftMostDigit) * 10) + int(rightMostDigit)
        sum += digitSum
        
    return sum

def solve_part_two(input):
    return 0
