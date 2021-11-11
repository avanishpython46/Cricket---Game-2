import time
import random

valid_hits = [1,2,3,4,6] 

#functions here
def get_your_score(tot_balls,required_score,wick_opp,your_team_name,oppenet_team_name):
    global your_score,your_wick,valid_hits
    if (required_score == 0):
        tot_wickets = random.randrange(0,11)
        wicket_balls = []
        if tot_wickets > 0:
            for i in range(1, tot_wickets + 1):
                wicket_balls.append(random.randrange(1, tot_balls))
        for i in range(1, tot_balls + 1):
            if (your_wick == 10):
                print("Bowled out ")
                break
            if (i not in wicket_balls):
                s = int(input("What do you want to hit [1,2,3,4,6] : "))
                if (s not in valid_hits):
                    while (s not in valid_hits):
                        s = int(input("What do you want to hit [1,2,3,4,6] : "))
                your_score += s
            else:
                your_score += 0
                print("Wicket gone ", your_score, "/", your_wick + 1)
                your_wick += 1
        return
    tot_wickets = random.randrange(0,11)
    wicket_balls = []
    if tot_wickets > 0:
        for i in range(1,tot_wickets+1):
            wicket_balls.append(random.randrange(1,tot_balls))
    for i in range(1,tot_balls+1):
        if (your_wick == 10):
            print("Bowled out ")
            break
        if (your_score > required_score):
            print()
            print(f"{your_team_name} won by {abs(your_wick-10)} wickets ")
            return 
        if (i not in wicket_balls):
            s = int(input("What do you want to hit [1,2,3,4,6] : "))
            if (s not in valid_hits):
                while (s not in valid_hits):
                    s = int(input("What do you want to hit [1,2,3,4,6] : "))
            your_score += s
        else:
            your_score += 0
            print("Wicket gone ",your_score,"/",your_wick+1)
            your_wick += 1
    if your_score < required_score :
        print(f"{oppenet_team_name} won by {abs(required_score - your_score)} runs ")
    else:
        print("Tie")



def get_score(tot_balls):
    global valid_hits

    tot_wickets = random.randrange(0,11)
    wicket_balls = []
    
    if (tot_wickets > 0):
        for i in range(1,tot_wickets+1):
            wicket_balls.append(random.randrange(1,tot_balls+1))
    total_score = 0


    for i in range(1,tot_balls+1):
        if (i not in wicket_balls):
            total_score += random.choice(valid_hits)
        else:
            total_score += 0
            continue
    return total_score,len(wicket_balls)


curr_time = time.asctime()

teams = ["US","SA","ENG","WI","PAK","AUS","NZ"]

your_team = input("What is your team :")
while (your_team not in teams):
    your_team = input("What is your team :")

teams.remove(your_team)

opponent_team = input("Enter opponent team : ")
while (opponent_team not in teams):
    opponent_team = input("Enter opponent team : ")

print(curr_time)

tot_balls_for_ODI = 50
tot_balls_for_T20 = 20

print(your_team+ " " + " V.S " + opponent_team)

print()

ODI = False
T20 = False

typeplay = input("What series you want to play ODI or T20 : ")
if typeplay == "ODI":
    ODI = True
else:
    T20 = True

toss = random.choice(["Tails","Heads"])
opponent_score = 0
wick = 0
your_score = 0
your_wick = 0

#Main Handling
if (toss == "Tails"):
    #here the computer decides to go to chose bat or bowl
    batorbowl = random.choice(["bat","bowl"])
    if (batorbowl == "bat"):
        if (T20):
            opponent_score,wick = get_score(tot_balls_for_T20)
            print(f"{opponent_team} Team scored :",opponent_score,"/",wick,f"{your_team} needs ",opponent_score+1,"to win in",tot_balls_for_T20,"balls")
            time.sleep(5)
            print("Lets Start")
            print()
            get_your_score(tot_balls_for_T20,opponent_score,wick,your_team,opponent_team)
        else:
            opponent_score,wick = get_score(tot_balls_for_ODI)
            print(f"{opponent_team} Team scored :",opponent_score,"/",wick,f"{your_team} needs ",opponent_score+1,"to win in",tot_balls_for_ODI,"balls")
            time.sleep(5)
            print("Lets Start")
            print()
            get_your_score(tot_balls_for_ODI,opponent_score,wick,your_team,opponent_team)
    else:
        if (T20):
            get_your_score(tot_balls_for_T20,opponent_score,wick,your_team,opponent_team)
            print(f"{your_team} scored {your_score} runs {opponent_team} needs {your_score+1} runs to win")
            time.sleep(5)
            print("Lets Start")
            print()
            opponent_score,wick = get_score(tot_balls_for_T20)
            if (opponent_score > your_score):
                print(f"{opponent_team} won by {abs(10-wick)} wickets ")
            else:
                print(f"{your_team} won by {abs(your_score-opponent_score)} runs ")

        else:
            get_your_score(tot_balls_for_ODI,opponent_score,wick,your_team,opponent_team)
            print(f"{your_team} scored {your_score} runs {opponent_team} needs {your_score+1} runs to win")
            time.sleep(5)
            print("Lets Start")
            print()
            opponent_score,wick = get_score(tot_balls_for_ODI)
            if (opponent_score > your_score):
                print(f"{opponent_team} won by {abs(10-wick)} wickets ")
            else:
                print(f"{your_team} won by {abs(your_score-opponent_score)} runs ")
else:
    batorbowl = input("What do you want to chose bat or bowl : ")
    if batorbowl == "bowl":
        if (T20):
            opponent_score,wick = get_score(tot_balls_for_T20)
            print(f"{opponent_team} Team scored :",opponent_score,"/",wick,f"{your_team} needs ",opponent_score+1,"to win in",tot_balls_for_T20,"balls")
            time.sleep(5)
            print("Lets Start")
            print()
            get_your_score(tot_balls_for_T20,opponent_score,wick,your_team,opponent_team)
        else:
            opponent_score,wick = get_score(tot_balls_for_ODI)
            print(f"{opponent_team} Team scored :",opponent_score,"/",wick,f"{your_team} needs ",opponent_score+1,"to win in",tot_balls_for_ODI,"balls")
            time.sleep(5)
            print("Lets Start")
            print()
            get_your_score(tot_balls_for_ODI,opponent_score,wick,your_team,opponent_team)
    else:
        if (T20):
            get_your_score(tot_balls_for_T20,opponent_score,wick,your_team,opponent_team)
            print(f"{your_team} scored {your_score} runs {opponent_team} needs {your_score+1} runs to win")
            time.sleep(5)
            print("Lets Start")
            print()
            opponent_score,wick = get_score(tot_balls_for_T20)
            if (opponent_score > your_score):
                print(f"{opponent_team} won by {abs(10-wick)} wickets ")
            else:
                print(f"{your_team} won by {abs(your_score-opponent_score)} runs ")

        else:
            get_your_score(tot_balls_for_ODI,opponent_score,wick,your_team,opponent_team)
            print(f"{your_team} scored {your_score} runs {opponent_team} needs {your_score+1} runs to win")
            time.sleep(5)
            print("Lets Start")
            print()
            opponent_score,wick = get_score(tot_balls_for_ODI)
            if (opponent_score > your_score):
                print(f"{opponent_team} won by {abs(10-wick)} wickets ")
            else:
                print(f"{your_team} won by {abs(your_score-opponent_score)} runs ")
