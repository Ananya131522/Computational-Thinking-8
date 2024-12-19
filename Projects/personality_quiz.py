#Beginning
kaz_points = 0
inej_points = 0
nina_points = 0
jesper_points = 0
matthias_points = 0
wylan_points = 0

#Middle
answer = input("In a group project, are you: A.) the leader, B.) the peacemaker, C.) the comedic relief, D.) the confused one who's just going along with everything, E.) the one who's sick of everything?   ")
if answer == "A":
    kaz_points += 1
elif answer == "B":
    inej_points += 1
elif answer == "C":
    nina_points += 1
    jesper_points += 1
elif answer == "D":
    wylan_points += 1
elif answer == "E":
    matthias_points += 1

print("    ")
answer= input("Which pet would you want? A.) A rottweiler, B.) A black cat, C.) A pomeranian, D.) A golden retriever, E.) A ginger cat, F.) A husky    ")
if answer == "A":
    kaz_points += 1
elif answer == "B":
    inej_points += 1
elif answer == "C":
    nina_points += 1
elif answer == "D":
    jesper_points += 1
elif answer == "E":
    wylan_points += 1
elif answer == "F":
    matthias_points += 1

print ("    ")
answer = input("Are you A.) a cat person or B.) a dog person?   ")
if answer == "A":
    inej_points += 1
    wylan_points += 1
elif answer == "B":
    kaz_points += 1
    jesper_points += 1
    nina_points += 1
    matthias_points += 1

print ("    ")
answer = input("Which of these things do you want most in life? A.) To be loved and forgiven, B.) Acceptance for all of my flaws and things I did wrong, C.) Freedom to do what I wish and to help those around me, D.) Admiration, I want to make people proud, E.) Vengeance (you emo brother, you know you mean A), F.) Personal growth, I want to become a better person.   ")
if answer == "A":
    jesper_points += 1
elif answer == "B":
    wylan_points += 1
elif answer == "C":
    inej_points += 1
elif answer == "D":
    nina_points += 1
elif answer == "E":
    kaz_points += 1
elif answer == "F":
    matthias_points += 1

print ("    ")
answer = input("Where would you like to live? A.) Paris, romantic and decadent Paris, filled with sweet and delicious food, B.) Los Angeles, with the bright lights and brighter stars of Hollywood, and thrilling Universal and Disneyland rides, C.) Hawaii, with open sea for miles and shining reefs, D.) New York, rainsoaked, sparkling-the city that is your oyster E.) Norway, cold, beautiful, harsh, and quiet Norway, F.) Ravello (in Italy), with its lush greenery, refreshing every time you look at it.  ")

if answer == "A":
    nina_points += 1
elif answer == "B":
    jesper_points += 1
elif answer == "C":
    inej_points += 1
elif answer == "D":
    kaz_points += 1
elif answer == "E":
    matthias_points += 1
elif answer == "F":
    wylan_points += 1

#Ending
print ("    ")
print (f"Kaz Brekker = {kaz_points}")
print (f"Inej Ghafa ={inej_points}")
print (f"Jesper Fahey = {jesper_points}")
print (f"Nina Zenik = {nina_points}")
print (f"Wylan Van Eck/Hendriks ={wylan_points}")
print (f"Matthias Helvar ={matthias_points}")

max_number = kaz_points
max_name = "kaz"

if inej_points > max_number:
    max_number = inej_points
    max_name = "inej"
if jesper_points > max_number:
    max_number = jesper_points
    max_name = "jesper"
if nina_points > max_number:
    max_number = nina_points
    max_name = "nina"
if wylan_points > max_number:
    max_number = wylan_points
    max_name = "wylan"
if matthias_points > max_number:
    max_number = matthias_points
    max_name = "matthias"


if max_name == "kaz":
    print("You're like Kaz! You're cunning, and you might come off a little cold. But deep down, you care for those around you and would do whatever it takes to help them. You're a little emo bastard, and we love you for it.")
elif max_name == "inej":
    print("You're like Inej! Biggest icon ever. You're kind and brave and you're hard on yourself. But you don't need to be-you are incredible and talented and perfect. You might feel like you're past the point of no return, but there is no point of no return.")
elif max_name == "jesper":
    print("You're like Jesper! You're a silly little guy with a lot of flaws and self doubt. You laugh off your negative feelings and run away from them, because you don't want to face the self doubt that's your biggest obstacle. But you can't change without confronting. I believe in you. You're great. And you also don't need to be so hard on yourself.")
elif max_name == "nina":
    print("You're like Nina! You are a self confident inspiration, and everyone absolutely adores you. You may get told that you're 'too much', but I promise you're not. You are absolutely perfect and you're incredible.")
elif max_name == "wylan":
    print("You're like Wylan! You're a quiet, introverted, unhinged soul. You seem super chill, but you do blow stuff up all the time, so you're a little enigma. What you aren't is a burden. You are perfect and amazing. And ADORABLE.")
elif max_name == "matthias":
    print("You're like Matthias! You're loyal and hold yourself to high moral standards. Which is admirable, but please remember to forgive yourself once in a while. You're also too hard on yourself.")