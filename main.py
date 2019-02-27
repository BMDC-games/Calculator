from func import prime
from func import power
from func import devide
from func import times
from func import minus
from func import add
from user import one_num
from user import two_nums
from user import Input
def menu():
    choice  = Input("Welcome to Ruby's Totally awesome calculator\n Please enter the number of the calculation you would like to do. \n 1. Add. X + Y \n 2. Subtract. X - Y \n 3. Multiply. X * Y\n 4. Devide. X / Y \n 5. Power. X in the power of Y\n 6. Prime. Returns if the number is prime \n - ")
    if choice == 1:
        num1,num2 = two_nums()
        print " {} + {} = {}".format(num1,num2,add(num1,num2))
    elif choice == 2:
        num1,num2 = two_nums()
        print " {} - {} = {}".format(num1,num2,minus(num1,num2))
    elif choice == 3:
        num1,num2 = two_nums()
        print " {} * {} = {}".format(num1,num2,times(num1,num2))
    elif choice == 4:
        num1,num2 = two_nums()
        print " {} / {} = {}".format(num1,num2,devide(num1,num2))
    elif choice == 5:
        num1,num2 = two_nums()
        print " {} in the power of {} = {}".format(num1,num2,power(num1,num2))
    elif choice == 6:
        num = one_num()
        if prime(num):
            print " {} is a prime number.".format(num)
        else:
            print " {} is not a prime number".format(num)
    else:
        print "Sorry, the program doesn't support that function yet..."
menu()