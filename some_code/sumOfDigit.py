num = int(input("Enter a number:"))
sum_of_Digit = 0
while num != 0:
    sum_of_Digit += num % 10
    num = num // 10
    if sum_of_Digit>=10 and num == 0:
        num = sum_of_Digit
        sum_of_Digit = 0
print(f"Sum of digit of the given number, {sum_of_Digit}")


#------------------------------------------------------------------------------------------------------------------------------------------------->


num1 = 8.1
num2 = 7.2
sum = num1 + num2
print(f"The sum of {num1} and {num2} is , {sum}")
print("The sum of {0} and {1} is {2}".format(num1, num2, sum))