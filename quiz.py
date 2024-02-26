print("welcome to quiz game")

player=input("Do you want to play the game?")
if player.lower() != "yes":
    quit()
print('ok lests start the game')
score=0
question=input("who developed python?")
if question.lower()== "Guido van Rossum":
    print('correct')
    score+=1
else:
    print('incorrect')
    
question=input(" Is Python case sensitive when dealing with identifiers?")
if question.lower()=="yes":
    print('correct')
    score+=1
else:
    print('incorrect')
    
question=input(" Python supports the creation of anonymous functions at runtime, using a construct called?")
if question.lower()== "lambda":
    print('correct')
    score+=1
else:
    print('incorrect')
    
question=input(" What does pip stand for python?")
if question.lower()== "preferred Installer Program":
    print('correct')
    score+=1
else:
    print('incorrect')
    
question=input("oops stand for?")
if question.lower()== "object oriented progamming system":
    print('correct')
    score+=1
else:
    print('incorrect')
    
question=input("Total types of constructors in C++ are?")
if question.lower()== "3":
    print('correct')
    score+=1
else:
    print('incorrect')
    
question=input("What is the number of parameters that a default constructor requires?")
if question.lower()=="0":
    print('correct')
    score+=1
else:
    print('incorrect')
    
question=input("By default, fields in a structure of a C program is?")
if question.lower()== "public":
    print('correct')
    score+=1
else:
    print('incorrect')
    
question=input("Total access specifiers in OOPS for C++ are?")
if question.lower()== "3":
    print('correct')
    score+=1
else:
    print('incorrect')
    
question=input("What type of inheritance does single-level inheritance support?")
if question.lower()== "runtime inheritence":
    print('correct')
    score+=1
else:
    print('incorrect')
    
question=input("Who developed object-oriented programming?")
if question.lower()== "alan kay":
    print('correct')
    score+=1
else:
    print('incorrect')
    
print("your score"+ str(score))