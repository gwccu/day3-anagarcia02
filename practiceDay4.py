mysteryNumber = 42
guess = int(input("Guess a number."))

while guess != mysteryNumber:
    guess = int(input("Sorry! Guess again."))
print("Nice job, you guessed 42.")


#
strength = 5
print('Your strength is at 5.')
strength += 1
while strength < 10:
    print('Your strength has increased to ' + str(strength))
    strength += 1

print("You've grown too strong! You've moved up to a new level of the game.")

#

n = int(input("What is the value of 'n'?"))
m = int(input("What is the value of 'm'?"))

print(n ** m)

p = 1
new = int(p(n * n))

while n ** m != new
    print(p(n * n))
    p += 1