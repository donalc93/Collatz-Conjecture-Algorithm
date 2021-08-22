# The Collatz Conjecture is an unsolved Mathmatical problem.

# HOW IT WORKS
# Pick a positive integer number (eg 3, 92, 20182, 515). 2 Rules are then applied to your number :
# If your number is even : number / 2
# If your number is odd : number x 3 then + 1

# The outputted number is then applied to these 2 rules again, and again and again.

# THE PROBLEM
# Eventually, no matter how large or specific the number.
# The outputted number will be caught in an endless loop of 3 numbers, forever. (4,2,1)

# THE CHALLENGE is to try and solve why.

def method(num):

    try:
        n = 0
        lastline = 0
        while num > 0: # forever loop
            n = n + 1 # counts every new loop
            if (num % 2) == 0: # even number rule
                num = num / 2
            else: # odd number rule
                num = (num * 3) + 1

            if num > 4: # Checks for start of loop, then logs the line number
                lastline = n + 1

            print(n, ' - ', num)
    except:
        print('\n')
        print("The '4,2,1' loop starts at line ", lastline) # output




input = int(input("Provide a number : "))
method(input)

