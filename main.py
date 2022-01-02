game_over = """    
    
       ______                           ____                        
      / ____/____ _ ____ ___   ___     / __ \ _   __ ___   _____    
     / / __ / __ `// __ `__ \ / _ \   / / / /| | / // _ \ / ___/    
    / /_/ // /_/ // / / / / //  __/  / /_/ / | |/ //  __// /_  _  _ 
    \____/ \__,_//_/ /_/ /_/ \___/   \____/  |___/ \___//_/(_)(_)(_)



"""


#----------------------------------------------------------------------------------------------------------------------

print("""

   ______                __   __  ___                 _                __  ___           __        __
  / ____/___  ____  ____/ /  /  |/  /___  _________  (_)___  ____ _   /  |/  /___  _____/ /___  __/ /
 / / __/ __ \/ __ \/ __  /  / /|_/ / __ \/ ___/ __ \/ / __ \/ __ `/  / /|_/ / __ \/ ___/ __/ / / / / 
/ /_/ / /_/ / /_/ / /_/ /  / /  / / /_/ / /  / / / / / / / / /_/ /  / /  / / /_/ / /  / /_/ /_/ /_/  
\____/\____/\____/\__,_/  /_/  /_/\____/_/  /_/ /_/_/_/ /_/\__, /  /_/  /_/\____/_/   \__/\__, (_)   
                                                          /____/                         /____/      

It seems Rick got a bit drunk and bored last night, a dangerous combination for you!
looks like this time he pulled your brain out and hooked you up to his computer, all you can do is type in 'yes' or 'no'
or select one of the answers offered to you like 1, 2, or 3
and you can ONLY use lowercase letters! if you manage to mess up with your answers, you will have to start over!

Type 'yes' to continue...


                                                                                       
""")
answer1 = input()
task1 = False
while task1 == False:
    if answer1 == "yes":
        print("""
        
        ok, lets get going...
        
        """)
        task1 = True
    elif answer1 == "no":
        print("boring little shit... Try again!")
    else:
        print("really, you couldnt follow those simple instructions?? Try Again")
print("""



Rick left you a note, the note says:
"Hey, you dumb shit, remember when you said how a 1980's robot could do what you do when you're with me on adventures adn that i should
let you get back to math class? Well we're about to see won't we?
Solve this challenge or you stay like this! Aaaand you will pass butter...
Aaaand... i don't know... your dad's face will turn into... Spiders!... who eat his ears.. or something.. :Buuurp:"

-type 'yes' if you want to flip the page over, or type 'no if you want to continue:

""")
answer2 = input("So?   ")
task2 = False
while task2 != True:
    if answer2 == 'yes':
        print("""
        
                ___          
    . -^   `--,      
   /# =========`-_   
  /# (--====___====\ 
 /#   .- --.  . --.| 
/##   |  * ) (   * ),
|##   \    /\ \   / |
|###   ---   \ ---  |
|####      ___)    #|
|######           ##|
 \##### ---------- / 
  \####           (  
   `\###          |  
     \###         |  
      \##        |   
       \###.    .)   
        `======/     
        
    Looks like he is just trolling you!
    
    Lets go on...
        
        """)
        task2 == True
        break
    elif answer2 == "no":
        print("Well someone is a party pooper.. ok, lets go on...")
        task2 == True
        break
    else:
        print("Try again...")
        break
print("""


You are alone in a wooden box! 

The only light is eminating from a small LCD display, that seems to be connected to the door...
you try to open the door but its locked! 
On the display you see 3 options for a password, it says "You only get 1 try"

choices are: 

(1)EatMyShorts123 
(2)RespectMyAuthoritah321 
(3)WabaLabaDubDuuuub525

answer with 1, 2 or 3 to continue...



""")
task3 = False
answer3 = input("what is your answer?   ")
while task3 != True:
    if answer3 != "3":
        print("""
        
        
        

You are a dissapointment Morty.. guess who is passing the butter tonight! and every night...
        

        """)
        print(game_over)
        break
    else:
        task3 = True
        break
print("""




You made it! you are out of the box!

Not just that, you see rick is passed out sleeping next to you, and for some reason he is dressed as the indian from the Village people...
and he is butt naked from the waist down...

next to him is a remote control with a "Revert morty" button, Looks like your lucky day!

Type 'yes' to continue...


""")
answer4 = input("""

Answer:   """)
task4 = False
if answer4 != "yes":
    print("""




    You are a dissapointment Morty.. guess who is passing the butter tonight! and every night...

    
            """)
    print(game_over)
print("""



You Turned Back into yourself! Now its time for payback!

Rick is starting to wake up so you don't have a lot of time, by your guess you only have time for 1 prank to get back to him.. 

will you:   

            (1) Call the whole family to quickly come into the garage and laugh their ass off when they see ricks impressive outfit!

            (2) Replace the bottle of beer in ricks hand with a bottle of his own pee he has sitting on the floor, because the bathroom next door was too far away apparently...
            
            (3) Use Rick's portal gun, open a portal to the version of the wild west where everybody is gay, make rick remember not to fall asleep with no pants again...

""")
answer4 = input("What option do you go for?, 1, 2, or 3:   ")
if answer4 == "1":
    print("""
    
    
    
    Everybody ran once you called them, Beck is facepalming, with a dissapointed look in her face... 
    Jerry and Summer are rolling on the floor, laughing their asses off, sounds like Jerry pooped his pants a little!
    Rick wakes up, looks around, and whispers: "ill turn you into a pickle next time, you little shit..."
    
    
                         

    """)
    print(game_over)
if answer4 == "2":
    print("""

    
    
    You replace the bottles, then run behind a counter and hide.
    Rick slowly wakes up, and right away he drinks the entire bottle of pee you placed in his hand
    he burps slowly and says: "goddamn, these craft beers get flat really fast..."
    
    

        """)
    print(game_over)
if answer4 == "3":
    print("""

    
    
    You open the portal right next to rick and push him inside, he falls in screaming. 
    The moment before the portal closes you hear him yelling:
                "God Damnit not the gay cowboys agaaain..!"
    
    


        """)
    print(game_over)


