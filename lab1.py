movie = "decstar"
movieRating : int = 3
moviePopularityScore : float = 72.65
if movieRating>=4 and moviePopularityScore>80 :
    print("Highly recommended")
elif movieRating>=3 and moviePopularityScore>70 :
    print("I recommended it . It is good")
elif movieRating<=2 and moviePopularityScore>60 :
    print( "You should check it out!")
else:
    print( "Don't watch it. It is a waste of time")
