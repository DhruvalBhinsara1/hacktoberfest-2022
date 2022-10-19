num1=int(input("Enter a number:-   "))

rev=0

while(num1>0):
   remain=num1%10

   num1//=10

   rev=(rev*10)+remain

print(rev)
