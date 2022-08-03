def countdown(num):
    arr = []
    for x in range(num,-1,-1):
        arr.append(x)
    return arr
print(countdown(5))

def pandr(values):
    print(values[0])
    return values[1]

print(pandr([1,2]))

def firstpluslen(list1):
    return list1[0] + len(list1)
print(firstpluslen([1,2,3,4,5]))


def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))


def length_and_value(size,value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output

print(length_and_value(4,7))
print(length_and_value(6,2))