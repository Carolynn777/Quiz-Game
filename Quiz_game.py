print("Welcome to my computer quiz!")
playing=input("Do you want to play? ")

if playing!="Yes":
    quit()

print("Okay let's play:)")  
score=0

answer=input("What is the meaning of GUI? ")
if answer== "Graphic User Interface":
    print("Correct!")
    
    score +=1
else: 
    print("Incorrect!")   

    answer=input("What does RAM stand for? ")
if answer== "Random Access Memory":
    print("Correct!")
    score +=1
else: 
    print("Incorrect!") 

answer=input("What does PSU stand for? ")
if answer== "Power Supply unit":
    print("Correct!")
    score +=1
else: 
    print("Incorrect!") 

answer=input("What do you call a baby Lion? ")
if answer== "Cub":
    print("Correct!")
    score +=1
else: 
    print("Incorrect!") 

print("You got "+ str(score) + "questions correct!")
print("You got "+ str((score/4)*100) + "%.")



