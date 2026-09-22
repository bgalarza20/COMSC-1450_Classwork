'''
count= 1
while( count<= 10):
    print(count)
    count += 1


c=2
while(c<=20):
    print(c)
    c += 2
    

c = int(input("Enter a number: "))
while(c>=0):
    print(c)
    c -=1


c=2
while(c<=30):
    print(c, c*c)
    c+= 2


x = input("Enter your password: ")
while( x != "rvel0305"):
    print("Incorrect password, try again.")
    x = input("Enter your password: ")



x = int(input("Enter a number: "))
while(x != 46):
    if(x > 46):
        print("Too high!")
    else:
        print("Too low!")
    x = int(input("Enter a number: "))

print("You guessed it! The number is 46.")


x =str(input("Please enter a word: "))
while (x != "x"):
    print(x)
    if(x == "stop"):
        print("Program ended.")
    x = str(input("Please enter a word: "))

n = int(input("Enter a positive integer: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print("The sum is:", total)


sum = 0
x = int(input("Enter a positive number or 0 to stop: "))
while(x != 0):
    sum = sum + x
    x = int(input("Enter a positive number or 0 to stop: "))
print("the total is" , sum)




x = int(input("Enter a positive number or 0 to stop: "))
count_ps=0
count_neg = 0
while( x != 0):
    if(x > 0):
        count_ps +1
    else:
        count_neg +1
    x = int(input("Enter a positive number or 0 to stop: "))
print("The number of positive numbers is:", count_ps)
print("The number of negative numbers is:", count_neg)


total = 0
for i in range(6):
    grade = float(input("Enter grade: "))
    total += grade
average = total / 6
print("Average:", average)


largest_even = 0
n = int(input("Enter an integer (0 to stop): "))
while n != 0:
    if n > 0 and n % 2 == 0:
        if n > largest_even:
            largest_even = n
    n = int(input("Enter an integer (0 to stop): "))
print("Largest positive even number:", largest_even)


n= int(input("Enter a positive number: "))
fact= 1
for i in range(1, n + 1):
    fact= fact * i
    print(fact)

    
for i in range(1, 11):
    print(i)

    
word = input("enter a word: ")
for i in range(5):
    print(word)

    
for i in range(2, 21):
    if i % 2 == 0:
        print(i)


n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("The sum of numbers from 1 to", n, "is:", total)


word=input("Enter a word: ")
letter_count = 0
for letter in word:
    if letter in "a":
        letter_count += 1
print(f"letter 'a' found: {letter_count}")


for i in range(1):
    print("0000")
    for j in range(1):
        print("1111")
        for k in range(1):
            print("2222")
            for l in range(1):
                print("3333")



for i in range(4):
    print("****")
for i in range(1):
    print("0")
    for j in range(1):
        print("0 1 2")
        for k in range(1):
            print("0 1 2 3")
            for l in range(1):
                print("0 1 2 3 4")
                for m in range(1):
                    print("0 1 2 3 4 5")



for i in range(1):
    print("*")
    for j in range(1):
        print("**")
        for k in range(1):
            print("***")
            for l in range(1):
                print("****")
                for m in range(1):
                    print("*****")

'''

for i in range(6):
    for j in range(i):
        print(j, end = "")
        print()