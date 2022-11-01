#so well this is my first atempt at this, I have some knolage of python but honestly, im starting coding in collage soon and I want to brush up on my python so I dont look like a muppet and alos im bored so hey we will see where this goes
#ENJOY!

#This is becoming kida a monologe (defiatly spelt that wrong) but idk who knows maybe ill try make a virus or a game idk ig we see where this goes

Pin=int(input("Enter Your Pin"))
print(Pin)

Counter=("0")

for Counter in range (9999):
    Counter = Counter +1
    if Counter == Pin:
        print(Counter)

#well after like what 15 mins i have made this, yes not much but all it does it go through every number untill it finds the pin the user entered, not much but im woundering if i can tweek this to make this alot better and actualy make this a viable tool to use
#now can i make it do the same wwith leters because if so eventualy it will make words which eventualy will turn into passwords

#now heres ethe first issue I have no idea for first how to make python go though an alpabet and second how i would make python create ever single possible combination of letters in an order

import string
print("Alphabet from a-z:")
for letter in string.ascii_lowercase:
   print(letter, end =" ")

#got to love the internet 
#so now how to i make this create egvery word possible, I mean my first idea is to append all letters to a list and then maybe uuse a math formular to make every possible word
#not sure how im going to find this equasion im after so i have plan b
#plan b is to give each letter a value 1-26 then have 26 lines all strting with a diffrent letter going through every possible combination of word then maybe, maybe append them all to a list
#lets try plan B

alp=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print(alp[2]) # prints c

#well this is going to be harder than expected as This list of all two-letter combinations includes 1352 (2 × 262)
#yeahh...we really do have a projecvt now ahaha

#well 2 weeks later im back still no idea what im doing or how im going to tackle this one ahahahahah 
#okay im going to try look online and see how others make this type of thing ill be back 

