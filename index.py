movie , ratingMovie  = "The fast & Farious" , 3
rating = 5
popularityScore = 72.65

if ratingMovie > 4 or popularityScore > 80 :
    print("Highly recommended")
elif ratingMovie > 3 or popularityScore > 70 :
    print("I recommended it. It is good")
elif ratingMovie < 2 or popularityScore < 60 :
    print("You should check it out!")
else : 
    print("Don't watch it. It is a waste of time")
