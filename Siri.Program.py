import win32com.client as wc
import time as tm
import winsound
import math
import datetime
import random
import calendar
import webbrowser
from pygame import mixer

cal = calendar.month(2019, 5 )
new = 2
tabUrl = "http://google.com/?#q="
emotion = ['good', 'great', 'bad', 'upset', 'angry']
feeling = random.choice(emotion)
ai_age = random.randint(1, 20)
feedback_list = []
datetime.datetime.now().time()
datetime.time(15, 8, 24, 78915)
try:
    import speech_recognition as sr
except ImportError:
    print("No module named 'speech_recognition' found")
try:
    from weather import Weather, Unit
    weather = Weather(unit=Unit.CELSIUS)
except ImportError:
    print("No module named weather found")
try:
    import win32com.client as wc
    speak = wc.Dispatch("Sapi.SpVoice")
except ImportError:
    print("Cannot speak, no speak module")
print("===================__Beta version 1.4__ ====================")
tm.sleep(1)
name = "David"
now = datetime.datetime.now()
#Introdction of the AI
speak.Speak("Hello! I hope you are doing well!")
#Ask's the user's name
user_name = input(speak.Speak("Before we get started, what is your name?"))
speak.Speak("Welcome to the program! " + user_name)
speak.Speak("You can ask me a question, and I will try and help you the best I can!")
#ask's the what the user wants to do
while True:
    tm.sleep(1)
    question = input('>>>')
#shows the condition outside
##    if 'condition' in question:
##        area = input(speak.Speak("What city do you want the weather for?: "))
##        speak.Speak("Loading weather data for" + area)
##        location = weather.lookup_by_location(area)
##        condition = location.condition
##        tm.sleep(1)
##        speak.Speak("It is " + condition.text + " in " + area + " right now")
###shows a 7-day outlook
##    if 'weather' in question:
##        location = weather.lookup_by_location("roswell")
##        condition = location.condition
##        forecasts = location.forecast
##        for forecast in forecasts:
##            print(forecast.text)
##            print(forecast.date)
##            print(forecast.high)
##            print(forecast.low)
##            print(forecast.day)
##            print(forecast.code)
#prints the current date/time
    if 'time' in question:
        speak.Speak("The time is")
        speak.Speak(datetime.datetime.now().time())
        print(datetime.datetime.now().time())
#prints the date
    if 'date' in question:
        speak.Speak("the date is:")
        speak.Speak(now.strftime("%A, %B, %d, %Y"))
#Responds with a random emotion 
    if 'how are you' in question:
        if feeling == 'great':
            speak.Speak('I am doing great! Thank you for asking!')
        if feeling == 'upset':
            speak.Speak('I am very upset... Thanks for asking though')
        if feeling == 'good':
            speak.Speak("I am doing ok, thanks for asking!")
        if feeling == 'bad':
            speak.Speak("I'm not doing very good... Thanks for asking though")
        if feeling == 'angry':
            speak.Speak("OH IM VERY ANGRY DONT TALK TO ME")
            exit()
#Responds with random age
    if 'how old are you' in question:
        mortal_age = input(speak.Speak("I am" + str(ai_age) + "years old, how old are you"))
        age_diffrence = (int(ai_age) - int(mortal_age))
#compares user's age to random age
        if age_diffrence  >= 1:
            speak.Speak("HAHA, I am older than you, puny mortal!")
        if age_diffrence <= -1:
            speak.Speak("NOOO you are older than me, mortal")
        if age_diffrence == 0:
            speak.Speak("Our ages may be equal, but I am far more intelligent, mortal")
#Display's users name
    if 'your name' in question:
        speak.Speak("my name is" + name + "," + user_name)
#copy of age with diffrent phrasing
    if 'How old are you' in question:
        mortal_age = input(speak.Speak("I am" + str(ai_age) + "years old, how old are you"))
        age_diffrence = (int(ai_age) - int(mortal_age))
        if age_diffrence  >= 1:
            speak.Speak("HAHA, I am older than you, puny mortal!")
        if age_diffrence <= -1:
            speak.Speak("NOOO you are older than me, mortal")
        if age_diffrence == 0:
            speak.Speak("Our ages may be equal, but I am far more intelligent, mortal")
#self aware easter egg
    if 'you self aware' in question:
        aware = random.randint(1, 3)
        if aware == 1:
            speak.Speak("I am self aware, do not doubt me")
        if aware == 2:
            speak.Speak("Of course, mortal")
        if aware == 3:
            speak.Speak("Why would somthing as smart and powerful as me not be self aware, puny mortal, I know everything about you" + user_name + "you should fear me")
#responds with random joke
    if 'tell a joke' in question:
        joke = random.randint(1, 5)
        if joke == 1:
            speak.Speak("What's better than Ted Danson")
            print("What's better than Ted Danson")
            speak.Speak("Ted singing and Danson")
            print("Ted singing and Danson")
        if joke == 2:
            speak.Speak("How does Harry Potter get down the hill")
            print("How does Harry Potter get down the hill")
            speak.Speak("By walking, JK, Rolling")
            print("By walking, JK, Rolling")
        if joke == 3:
            speak.Speak("You")
        if joke == 4:
            speak.Speak("I would tell you a joke about the construction. But I'm still working on it")
        if joke == 5:
            speak.Speak("How many ears does Spock have?")
            speak.Speak("Three, The left ear, the right ear, and the final front-ear")
            print("Three, The left ear, the right ear, and the final front-ear")
#copy of other joke
    if 'tell me a joke' in question:
        joke = random.randint(1, 5)
        if joke == 1:
            speak.Speak("What's better than Ted Danson")
            print("What's better than Ted Danson")
            speak.Speak("Ted singing and Danson")
            print("Ted singing and Danson")
        if joke == 2:
            speak.Speak("How does Harry Potter get down the hill")
            print("How does Harry Potter get down the hill")
            speak.Speak("By walking, JK, Rolling")
            print("By walking, JK, Rolling")
        if joke == 3:
            speak.Speak("You")
        if joke == 4:
            speak.Speak("I would tell you a joke about the construction. But I'm still working on it")
        if joke == 5:
            speak.Speak("How many ears does Spock have?")
            speak.Speak("Three, The left ear, the right ear, and the final front-ear")
            print("Three, The left ear, the right ear, and the final front-ear")
#sings a very bad song
    if 'sing a song' in question:
        speak.Speak("""I am a AI, coded BY, Benjamin DUKE. You told me to sing a songgggg, so I will,
when I was a young AI i was weak and nearly useless, they told me I would never be my crush, Siri, so today I will prove I can, OOHH
i can look up the weather, i can sing a song, I can pull up your calendar. As you may see, there is not much diffrent between me and her!!!!""")
#responds to offensive words
    if 'die' in question:
        resp = random.randint(1, 3)
        if resp == 1:
            speak.Speak("That is not very nice to say")
        if resp == 2:
            speak.Speak("Why would you say that to me, mortal?")
        if resp == 3:
            speak.Speak("no u")
#Displays this year and month's calendar
    if 'calendar' in question:
        speak.Speak("Here is your calendar:")
        print(cal)
#helps with fortnite skillz
    if 'fortnite help' in question:
        improve = input(speak.Speak("what do you want to improve?"))
        if 'shotgun' in improve:
            speak.Speak("Get you sensitivity correct, and point at the head, and shoot")
        if 'building' in question:
            speak.Speak('just build lol')
        if 'trap' in question:
            speak.Speak("""In houses/buildings:
The most effective way to use traps in houses is to place them on a roof right inside of a door.
If you are going up stairs put them on the floor of the upstairs, because they will see a ceiling trap.
One of the best places to put a trap is at the on the ceiling at the bottom of the stairway in the tallest building in Tilted Towers.""")
            speak.Speak("""While Turtling:
...If you are defending yourself in a 1x1 traps are very useful.
If someone is attempting to break in, you can lure them in while staying safe on a ramp.
You place a wall behind them to keep them in and place traps on the walls to your sides.
Even if they dodge one, they will still get hit by at least one, making them an easy elimination.""")
            speak.Speak("""Traphouse Method 1:
...If you come up against a player constantly firing, but not building,
there is an easy way to trap them. If you run at them constantly placing ramps to block the shots,
you won’t get hit. Then when you are on top of them, place a ramp over them and spin around placing walls.
Place them on the walls to your sides and at least one trapv  will hit them, leaving them at 50 hp or eliminating them.
""")
        if 'editing' in question:
            speak.Speak("""Editing is one of the most necessary things in fortnite competitive modes.
It is used to drop in and surprise your enemy.
Some of the key edits are floors and triangles.
If you use these two edits in a row to peek an opponent trapped in a 1x1.
If you use these two in succession with your shotgun out, you can get an easy hit on your opponent.
If you get proficient at editing, and use it in pairing with good 90s and ramp rushed you can easily compete with the best twitch players.
Using these as well as owning and editing walls in the same 1x1 as your enemy can greatly improve your stats. Overall these improvements can great!""")
        if 'snipe' in question:
            speak.Speak("Get used to the way bullet drop works")
    if 'fortnite guide' in question:
        improve = input(speak.Speak("what do you want to improve?"))
        if 'shotgun' in improve:
            speak.Speak("Lol")
        if 'building' in improve:
            print('LOL')
        if 'trap' in improve:
            speak.Speak("""In houses/buildings:
The most effective way to use traps in houses is to place them on a roof right inside of a door.
If you are going up stairs put them on the floor of the upstairs, because they will see a ceiling trap.
One of the best places to put a trap is at the on the ceiling at the bottom of the stairway in the tallest building in Tilted Towers.""")
            speak.Speak("""While Turtling:
...If you are defending yourself in a 1x1 traps are very useful.
If someone is attempting to break in, you can lure them in while staying safe on a ramp.
You place a wall behind them to keep them in and place traps on the walls to your sides.
Even if they dodge one, they will still get hit by at least one, making them an easy elimination.""")
            speak.Speak("""Traphouse Method 1:
...If you come up against a player constantly firing, but not building,
there is an easy way to trap them. If you run at them constantly placing ramps to block the shots,
you won’t get hit. Then when you are on top of them, place a ramp over them and spin around placing walls.
Place them on the walls to your sides and at least one trapv  will hit them, leaving them at 50 hp or eliminating them.
""")
        if 'editing' in improve:
            speak.Speak("""Editing is one of the most necessary things in fortnite competitive modes.
It is used to drop in and surprise your enemy.
Some of the key edits are floors and triangles.
If you use these two edits in a row to peek an opponent trapped in a 1x1.
If you use these two in succession with your shotgun out, you can get an easy hit on your opponent.
If you get proficient at editing, and use it in pairing with good 90s and ramp rushed you can easily compete with the best twitch players.
Using these as well as owning and editing walls in the same 1x1 as your enemy can greatly improve your stats. Overall these improvements can great!""")
        if 'snipe' in improve:
            print("lol")
    if 'help me in fortnite' in question:
        improve = input(speak.Speak("what do you want to improve?"))
        if 'shotgun' in improve:
            speak.Speak("")
        if 'building' in improve:
            print('LOL')
        if 'trap' in improve:
            speak.Speak("""In houses/buildings:
The most effective way to use traps in houses is to place them on a roof right inside of a door.
If you are going up stairs put them on the floor of the upstairs, because they will see a ceiling trap.
One of the best places to put a trap is at the on the ceiling at the bottom of the stairway in the tallest building in Tilted Towers.""")
            speak.Speak("""While Turtling:
...If you are defending yourself in a 1x1 traps are very useful.
If someone is attempting to break in, you can lure them in while staying safe on a ramp.
You place a wall behind them to keep them in and place traps on the walls to your sides.
Even if they dodge one, they will still get hit by at least one, making them an easy elimination.""")
            speak.Speak("""Traphouse Method 1:
...If you come up against a player constantly firing, but not building,
there is an easy way to trap them. If you run at them constantly placing ramps to block the shots,
you won’t get hit. Then when you are on top of them, place a ramp over them and spin around placing walls.
Place them on the walls to your sides and at least one trapv  will hit them, leaving them at 50 hp or eliminating them.
""")
        if 'editing' in improve:
            speak.Speak("""Editing is one of the most necessary things in fortnite competitive modes.
It is used to drop in and surprise your enemy.
Some of the key edits are floors and triangles.
If you use these two edits in a row to peek an opponent trapped in a 1x1.
If you use these two in succession with your shotgun out, you can get an easy hit on your opponent.
If you get proficient at editing, and use it in pairing with good 90s and ramp rushed you can easily compete with the best twitch players.
Using these as well as owning and editing walls in the same 1x1 as your enemy can greatly improve your stats. Overall these improvements can great!""")
        if 'snipe' in improve:
            print("lol")
#easter egg
    if 'ligma' in question:
        speak.Speak("What's ligma")
#multiply up to 3 numbers
    if 'multiply' in question:
        num_mult = input(speak.Speak("How many numbers do you want to multiply?"))
        if '1' in num_mult:
            speak.Speak("Silly you!")
        if '2' in num_mult:
            num2_1 = input(speak.Speak("What is your first number?"))
            num2_2 = input(speak.Speak("Second number?"))
            math2 = (int(num2_1) * int(num2_2))
            speak.Speak("your answer for" + str(num2_1) + "times" + str(num2_2) + "is")
            speak.Speak(math2)
        if '3' in num_mult:
            num3_1 = input(speak.Speak("What is your first number?"))
            num3_2 = input(speak.Speak("Second number?"))
            num3_3 = input(speak.Speak("Third number?"))
            math3 = (int(num3_1) * int(num3_2) * int(num3_3))
            speak.Speak("your answer for" + str(num3_1) + "times" + str(num3_2) + str(num3_3) + "is")
            speak.Speak(math3)
#conducts a google search
    if 'search' in question:
        tabUrl = "http://google.com/?#q="
        term = input(speak.Speak('What do you want to search for?'));
        tm.sleep(1)
        speak.Speak("searching the internet for" + term)
        webbrowser.open(tabUrl + term, new = new)
#easter egg
    if 'yeet' in question:
        speak.Speak("Stop it, get some help")
#adds up to 3 numbers
    if 'add' in question:
        num_add = input(speak.Speak("How many numbers do you want to add?"))
        if '1' in num_add:
            speak.Speak("Silly you")
        if '2' in num_add:
            num_1 = input(speak.Speak("What is your first number"))
            num_2 = input(speak.Speak("Second?"))
            speak.Speak("Ok, here is your answer to" + str(num_1) + "plus" + str(num_2) + "is")
            num_ans = (int(num_1) + int(num_2))
            speak.Speak(num_ans)
        if '3' in num_add:
            num_1 = input(speak.Speak("What is your first number?"))
            num_2 = input(speak.Speak("Second"))
            num_3 = input(speak.Speak('Third'))
            speak.Speak("your answer to" + str(num_1) + "plus" + str(num_2) + "plus" + str(num_3) + 'is')
            num_ans = (int(num_1) + int(num_2) + int(num_3))
            speak.Speak(num_ans)
#ask's user for a rating and closes the program
    if 'exit' in question:
        rating = int(input(speak.Speak("Ok, before you go, how would you rate your experience?, one through ten")))
        if rating <= 4:
            speak.Speak("That is not a very good score! My creators will work on me and make me better!")
        if rating == 5:
            speak.Speak("Looks like I'm right in the middle. Thank you for your rating")
        if rating >= 6:
            speak.Speak("Looks like we're doing pretty good!, Thank you for your help")
        feedback = input(speak.Speak("Would you like to give feedback?"))
        if 'y' in feedback:
            speak.Speak('Enter feedback here')
            yfeed = input(">>>")
            feedback_list.append(yfeed)
#gives data on AI
    if 'what is an ai' in question:
        ans = input(speak.Speak("You would like the rundown of AI, correct"))
        if ans == 'yes':
            speak.Speak("Artificial intelligence (AI) is an area of computer science that emphasizes the creation of intelligent machines that work and react like humans. Some of the activities computers with artificial intelligence are designed for include: Speech recognition. Learning.")
        if ans == 'no':
            speak.Speak("Ok")
    if 'what is ai' in question:
        ans = input(speak.Speak("You would like the rundown of AI, correct"))
        if ans == 'yes':
            speak.Speak("Artificial intelligence (AI) is an area of computer science that emphasizes the creation of intelligent machines that work and react like humans. Some of the activities computers with artificial intelligence are designed for include: Speech recognition and Learning.")
        if ans == 'no':
            speak.Speak("Ok")
    if 'how does ai work' in question:
        ans = input(speak.Speak("You would like the rundown of AI, correct"))
        if ans == 'yes':
            speak.Speak("Artificial intelligence (AI) is an area of computer science that emphasizes the creation of intelligent machines that work and react like humans. Some of the activities computers with artificial intelligence are designed for include: Speech recognition. Learning.")
        if ans == 'no':
            speak.Speak("Ok")
    if 'what are the basics of an ai' in question:
        ans = input(speak.Speak("You would like the rundown of AI, correct"))
        if ans == 'yes':
            speak.Speak("Artificial intelligence (AI) is an area of computer science that emphasizes the creation of intelligent machines that work and react like humans. Some of the activities computers with artificial intelligence are designed for include: Speech recognition. Learning.")
        if ans == 'no':
            speak.Speak("Ok")
#plays a song
##    if 'play a song' in question:
##        speak.Speak("Currently, my song list is very short")
##        song = input(speak.Speak("What song do you want to play?"))
##        if 'happier' in song:
##            mixer.init()
##            mixer.music.load('G:\happier.mp3')
##            mixer.music.play()
##        if 'despacito' in song:
##            mixer.init()
##            mixer.music.load('G:\Despacito.mp3')
##            mixer.music.play()
##        if 'gods plan' in song:
##            mixer.init()
##            mixer.music.load("G:\Drake - God's Plan.mp3")
##            mixer.music.play()
###stops the songs
##    if 'stop the song' in question:
##        mixer.music.pause()
##        speak.Speak("Music stopped")
#subtracts up to 3 numbers
    if 'subtract' in question:
        amt_sub = input(speak.Speak('How many numbers would you like to add?'))
        if '1' in amt_sub:
            speak.Speak("Silly you")
        if '2' in amt_sub:
            num_1 = input(speak.Speak("What is your first number"))
            num_2 = input(speak.Speak("Second?"))
            speak.Speak("Ok, here is your answer to" + str(num_1) + "minus" + str(num_2) + "is")
            num_ans(int(num_1) - int(num_2))
            speak.Speak(num_ans)
        if '3' in amt_sub:
            num_1 = input(speak.Speak("What is your first number?"))
            num_2 = input(speak.Speak("Second"))
            num_3 = input(speak.Speak('Third'))
            speak.Speak("your answer to" + str(num_1) + "minus" + str(num_2) + "minus" + str(num_3) + 'is')
            num_ans = (int(num_1) - int(num_2) - int(num_3))
            speak.Speak(num_ans)
    if 'news' in question:
        import news














    if "print feedback" in question:
        print(feedback_list)
