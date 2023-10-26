#1.1 implement a recursive function to calculate the factorial of a given number
def recur_factorial(n):
   if n==1;
       return 1
   else :
       return n* recur_factorial(n-1)
#take input from the user
num=int(input(*enter a number:"))
#check is the number is negative
if num<0;
   print("sorry, factorial does not exist for nagative number")
              elif num==0;
              print("the factorial of 0 is 1")
              else:
              print("the factorial of ",num,"is",recur-factorial(num))
              