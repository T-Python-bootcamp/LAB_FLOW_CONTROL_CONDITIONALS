#  Create a variable for the movie (choose any movie you like)
movie = "RUN"

# - Create a variable of type int to hold the rating of the movie out of 5 . Give this movie 3
rate: int = 3

# - Create a popularity score of type float , let it be 72.65
score: float = 72.65

# - Using an if statement 
if rate >= 4 and score > 80 :
    print("Highly recommended")
elif rate >= 3 and score > 70:
    print("I recommended it . It is good")
elif rate <= 2 and score > 60:
    print("You should check it out!")
else:
    print("Don't watch it. It is a waste of time")
