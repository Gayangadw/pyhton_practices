#Sum of first positive numbers
num = int(input("How many numbers there ? "))
n=0
for n in range(num):
    numbers = float(input("Enter the number: "))
    total_sum =num*(num+1)/2
print("sum is :",total_sum)