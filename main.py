# Counting numbers
num = 2365789
count = 0
while num != 0:
    num = num // 10
    count =count+1

print("Total digits are: ",count)

#Fibonacci Sequence
num_1=0
num_2=1
print("Fibonacci Sequence: ")
for i in range(20):
    print(num_1)
    result = num_1+num_2
    num_1 = num_2
    num_2 = result







