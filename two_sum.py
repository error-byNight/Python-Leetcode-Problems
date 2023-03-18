def twoSum(num , target):
    for i in range (len(num)):
        for j in range (i + 1 , len(num)):
            if (num[i] + num[j]  == target): 
               return[i , j]
    return -1

     

num = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8]
target = 9
print (twoSum(num , target))
