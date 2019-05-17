import random
num = []

for i in range(100):
    num.append(random.randint(1,100))
print("List of random number:\n\t",num)

print("\t\tPress 1 to find minimum number and its index")
print("\t\tPress 2 to find maximum number & its index")
print("\t\tPress 3 to find mean\n")
select = int(input("Enter your choice: "))

if select == 1:
    print("\n\t\t ***** MINIMUM NUMBER *****")
    min = num[0]
    for j in num:
        if min > j:
            swap = min
            min = j
            j = swap
    print("Minimum number of the list is: ",min)  
    print("Index: ",num.index(min))  

elif select == 2 :
    print("\n\t\t ***** MAXIMUM NUMBER *****")
    max = num[0]
    for j in num:
        if max < j:
            swap = max
            max = j
            j = swap
    print("Maximum number of the list is: ",max)  
    print("Index: ",num.index(max))  

elif select == 3:
    print("\n\t\t ***** MEAN *****")
    sum = 0     
    for j in num:
        sum += j
    mean  = sum / len(num) 
    print("Mean of the list is: ",mean)    

else:
    print("Invalid choice :(")

