'''Given two non-negative integers low and high.
   Return the count of odd numbers between low and high (inclusive).'''

low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))

count_low = (low + 1) // 2
count_high = (high + 1) // 2
count = count_high - count_low

print("The count of odd numbers between", low, "and", high, "is", count)
