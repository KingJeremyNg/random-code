import random

# players = ["Jeremy", "Nicholas", "Morgan", "Daniel", "Trev", "Dominic"]
# team1 = []
# team2 = []

# while (players != []) :
#     rand = random.randrange(len(players))
#     team1.append(players[rand])
#     players.pop(rand)

#     if players == [] :
#         break

#     rand = random.randrange(len(players))
#     team2.append(players[rand])
#     players.pop(rand)

people = ["Miguel","Jeremy","Elijah","Christian","Adam","Linh"]

def makeTeams(arr):
    team1=[]
    team2=[]
    for i in range(len(arr)):
        if i == 5:
            team2.append(arr.pop())
            break
        num=random.randrange(0,len(arr)-1)
        if i%2==0:
            team1.append(arr.pop(num))
        else:
            team2.append(arr.pop(num))
    return ("Team 1 :" +str(team1)+"\nTeam 2 :"+str(team2))

print(makeTeams(people))