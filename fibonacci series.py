no_of_terms=int(input("How Many Terms To Be Printed : "))
#first two terms
n1=0
n2=1
#used for while loop
count=0
#checking if the input is valid
if no_of_terms<=0:
    print("Please Enter A Positive Integer")
else:
    print("Fibonacci Series Upto",no_of_terms,"is : ")
    while count < no_of_terms:
        print(n1)
        n3=n1+n2
        #updating values
        n1=n2
        n2=n3
        count=count+1
