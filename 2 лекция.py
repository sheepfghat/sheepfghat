#2 лекция
#Count monkeys
def monkey_count(n):
    return list(range(1,n+1))
# Sum of positive
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
# Basic mathematical operations
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    else:
        return value1 / value2