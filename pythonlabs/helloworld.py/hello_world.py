import random
def function(y):
    x = random.randint(1, 10)
    if x % y == 0:
        print("This number is even")
        print(x / y)
        return x / y
    else:
        print("This number is odd")
        print(x / y)
        return x / y
function(random.randint(1, 10))
function(random.randint(1, 10))
function(random.randint(1, 10))
function(random.randint(1, 10))

#Heads or Tails
print("""This is a game of heads and tails.
Write your answer in all caps.
Answers can only be either HEADS or TAILS""")
def h_t(bet, guess):
    num = random.randint(1, 2)
    if num ==1 and guess == "HEADS":
        print("You chose " + guess + " and bet " + str(bet) + " dollars.")
        print("Your guess was right! It was heads! You won " + str(bet) + " dollars!")
        return bet
    elif num == 2 and guess == "TAILS":
        print("You chose " + guess + " and bet " + str(bet) + " dollars.")
        print("Your guess was right! It was tails! You won " + str(bet) + " dollars!")
        return bet
    elif num == 1 and not guess == "HEADS":
        print("You chose " + guess + " and bet " + str(bet) + " dollars.")
        print("Your guess was wrong! It was Heads! You lost " + str(bet) + " dollars!")
        return -1 * bet
    elif num == 2 and not guess == "TAILS":
        print("You chose " + guess + " and bet " + str(bet) + " dollars.")
        print("Your guess was wrong! It was tails! You lost " + str(bet) + " dollars!")
        return -1 * bet

print(h_t(35, "HEADS"))
print(h_t(15, "TAILS"))
print(h_t(46, "HEADS"))
print(h_t(50, "TAILS"))
print(h_t(22, "HEADS"))
