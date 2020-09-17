#Write a program that:

#Takes an integer n as input
#Adds n doubled to n tripled and prints out the result
#Examples:

#If the input is 2, the result is 10
#If the input is 3, the result is 15
#If the input is 4, the result is 20

n_str = input('Input n: ')
n_int=int(n_str)
result=n_int*2+n_int*3
print(result)
