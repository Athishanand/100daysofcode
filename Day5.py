#For even or odd and add them
#Python program to print Even numbers from 1 to n
max=int(input("Please Enter the maximum value: "))

for num in range(2, max+1, 2):
    print("{0}".format(num))

    #Python program to print odd numbers from 1 to n
max=int(input("Please Enter the maximum value: "))

for num in range(1, max+1, 2):
    print("{0}".format(num))

#Python program to add even and odd numbers from 1 to n
max = int(input("Please Enter the maximum value: "))
even_total = 0
odd_total = 0
for number in range(1, max + 1):
    if(number % 2 ==0):
        even_total = even_total + number
    else:
        odd_total = odd_total + number

print("The sum of even number from 1 to {0} = {1}".format(number,even_total))
print("The sum of odd number from 1 to {0} = {1}".format(number,odd_total))
