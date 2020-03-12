#task 1

arr = []
print("Please enter five numbers:\n")

for i in range(5):
    num = int(input("-: "))
    arr.append(num)

min,max = arr[1],arr[1]

for i in arr:
    if i>max:
        max=i
    elif i<min:
        min=i

print("\nThe maximum number was - %d and the minimum - %d\n" % (max,min))
input("Press enter to continue to task 2\n\n")

#task 2

del arr
arr = []
print("enter any number of non-negative floating-point values. The user terminates the input list with any negative value.\n")

import sys
min,max=float(sys.float_info.max),0 

while(True):
    inp=float(input("-: "))
    if inp<0:
        print("---------------------\n")
        break
    if inp>max:
        max=inp
    elif inp<min:
        min=inp
    arr.append(inp)

def calculate_sum(arr):
    sum = 0
    for i in arr:
        sum+=i
    return sum

def calculate_average(arr):
    return float(calculate_sum(arr))/len(arr)

print("\nThe sum = %f\nThe AMedian =%f \nThe max = %f\nAnd the ugly = %f\n" % (calculate_sum(arr),calculate_average(arr),max,min  ))
