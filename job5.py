def travel_time(x,y):
    
    marche = x
    week=(marche *2)*7
    distance = week * y
    print(f"vous avez parcouru cette semaine {(distance*5)/100} metres")

travel_time(20,30)