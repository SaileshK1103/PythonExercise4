from random import randint, random, choice

#Exercise 1
'''
sum = 0
counter = 1
while counter<10:
     sum = sum + counter
     print(f"the counter, {counter}, and  the sum of the counter is {sum}")
     counter = counter + 1
'''


#Exercise 2
'''
i = 1
n = int(input("Enter a limit: "))
while i<=n:
    if i%2==0:
        print(f"the even number is {i}")
    elif i%2!=0:
        print(f"the odd number is {i}")
    i = i+1
'''

#Exercise 3
'''
target_number = randint(1, 10)
counter = 0
while True:
    user_guess = int(input("Guess a number between 1 and 9: "))
    if user_guess == target_number:
        print("Well guessed")
        break
    else:
        print("Try again")
    counter = counter + 1
    print("tried", counter)
'''
#Exercise 4
'''
user_input = ""
while user_input =="":
    user_input = input("press enter to exit or type something to display")
    print("You typed", user_input)
'''

#Exercise 5
'''
#Initialize the result by flipping the coin once
result = choice(["Head","Tail"]).lower()
#flip the coin until we get head
while result != "head":
    print("flipped", result)
    #flip the coin again
    result = choice(["Head","Tail"]).lower()
#Print the final result when 'Heads" is obtained
print("Finally, flipped", result)
'''
