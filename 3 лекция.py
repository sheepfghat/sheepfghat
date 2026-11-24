#3 лекция
#Find maximum and minimum of values in list
def minimum(arr):
    return min(arr)
def maximum(arr):
    return max(arr)
#Word values
def name_value(my_list):
    result=[]
    for i, s in enumerate(my_list,1):
        total=0
        for c in s:
            if c.isalpha():
                total += ord(c) - ord('a') + 1
        result.append(total*i)
    return result
#Remove all marked elements of list
class List:
    def remove_(self, integer_list, values_list):
        return [x for x in integer_list if x not in values_list]
#Remove duplicate words
def remove_duplicate_words(s):
    result = []
    for word in s.split():
        if word not in result:
            result.append(word)
    return ' '.join(result)