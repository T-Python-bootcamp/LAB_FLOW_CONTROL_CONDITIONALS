
movies = "me before you" 
evaluation = 3
evaluation_peoples = 72.65

if evaluation > 4 and evaluation_peoples > 80 :
    print ("Highly recommended")
elif evaluation <= 3 and evaluation_peoples > 70 :
    print ("I recommended it. it is good")
elif evaluation <= 2 and evaluation_peoples < 60 : 
    print ("You should check it out!")
else: 
    print ("You don't watch it. It's a waste of time")

