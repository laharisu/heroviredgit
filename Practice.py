names =[]
feedbacks =[]
average=0
for i in range (4):
    name = input("ener the name")
    feedback = int(input("enter the feebdbackscore "))
    names.append(name)
    feedbacks.append(feedback)
    length =len(names)
    
    average +=feedback
    averages=average/len(names)    
    print(averages)
