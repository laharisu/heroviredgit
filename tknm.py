###we are going to take the 5 input from the users where they will provide the name of the learnr and the feedback
###at the end we will print the average of the feedback
names = []
feedbacks = []
sumFeedback = 0
for i in range(5):
    name = input("Enter the name")
    feedback = int(input("Enter the Feedback"))
    names.append(name)
    feedbacks.append(feedback)
    sumFeedback = sumFeedback+feedback

average = sumFeedback/len(names)
print(average)
print(names)
print(feedbacks)


