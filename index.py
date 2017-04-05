def odd_even(start, end):
    message1 = "odd"
    message2 = "even"
    message =""
    for num_count in range(1,200):
        if num_count % 2 == 0:
            message += "Number is " +str(num_count) + "." + " This is " + message2 + " number. "
        else:
            message += "Number is " + str(num_count) + "." + " This is " + message1 +" number. "
    #print message

#odd_even(1,200)

def multiply (arr,value):
    new_arr = []
    for num_count in arr:
        new_arr.append(num_count * value)
    #print new_arr
#multiply([2,4,10,16], 8)

# def layered_multiples(arr):
#     new_arr = []
#     for x in arr:
#         val_arr = []
#         for one in range(0,xt):
#             val_arr.append(1)
#         new_arr.append(val_arr)
#     return new_arr
# x = layered_multiples(multiply([2,4,5],3))
# print arr
def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
