import random

# Stage 1
print("Start the game?") 
while True:
     Yorn = input("Yes or No? ")
     if Yorn.lower() == "no":
          print("Okay, see you!")
          quit()
     elif Yorn.lower() == "yes":
          break
     else:
          print("I'm not quite sure what you're saying. May you repeat once more?")
          continue

# Stage 2
Otot = print("Please enter a natural number between 1 to 10")

print("How many digits is the number?")
while True:
     X1 = input("1~10: ")
     X2 = int(X1)
     if X1.isdigit() == True:
          if 1 <= X2 <= 10:
               break
          else:
               print(Otot)
               continue
     if X1.isdigit() == False:
          print(Otot)
          continue

# To generate answer
Sequence_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(Sequence_)
Answer = ""
for x in range(X2):
     Answer += str(Sequence_[x])

# Test errors & Stage 3
A = 0
B = 0

while True: 
     Inputted = input("Enter your guess: ")
     if Inputted.isdigit() == True:
          if len(Inputted) == len(Answer):
               #Stage 3
               if Inputted == Answer:
                    print("Congratulations! The answer is " + Answer + "!")
                    break
               for a in range(X2):
                    for b in range(X2):
                         if Inputted[a] == Answer[b] and a == b:
                              A += 1
                         elif Inputted[a] == Answer[b]:
                              B += 1
                         print("{}A{}B".format(A, B))
                         continue
          else:
               if X2 == 1:
                    print("Please enter 1 digit of number!")
                    continue
               else:
                    print("Please enter {} digits of numbers!".format(X2))
                    continue
     elif Inputted.isdigit() == False:
          print("Please enter the digital number!")
          continue
     else:
          print("Unexpected Error!")
          continue
