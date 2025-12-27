# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Sheldon", color="#FF0020")

# Define a small image positioned on the bottom right
transform smallright:
    zoom 0.2  # scale down to 40% of original size
    xalign 1.0  # right edge
    yalign 1.0  # bottom edge


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "just-relax-11157.mp3"
    play sound "yawning-6096.mp3" volume 3.5
    scene wake with dissolve
    s "Ahhh-hahhhh"
    s "What a wonderful sleep!"
    s "I feel refreshed and ready for my wonderful day!"
    s "I think I'll go have breakfast at Macdonalds, do the Christmas shopping with my friends, and then go visit my grandparents!"
    s "Ah! Only thinking about it makes me even more excited!"
    s "Let me go open the curtains to let the sunshine in!"
    scene window with dissolve
    play sound "curtain-82308.mp3"
    play music "snow-dance-288431.mp3"
    pause 2.0
    scene pretty with fade
    pause 3.5
    s "Such a pretty day!"
    s "Look at those cute and gentle snowflakes!"
    s "Perfect for my pla-"
    scene huge
    play sound "winter-breeze-404248.mp3" volume 2.5
    pause 2.5
    show no at smallright with dissolve
    play sound "preview.mp3" volume 2.0
    s "Huh?! What...What just happened?"
    s "Why's there so much snow all of a sudden?"
    s "Oh no... I can't go outside in a snowstorm like this..."
    s "Well... I can't let this snowstorm ruin my day!"
    s "Although this is a REALLY huge snowstorm..."
    s "But I, Sheldon, will not fear and will follow through with the exact same plans I had for today!"
    s "Yes! I will go dress up warm and go to Macdonalds for breakfast!"
    stop music fadeout 1.0
    scene min with fade
    play music "later.mp3"
    pause 2.5
    scene door with fade
    play music "My Project.mp3"
    pause 1.5
    s "What the hecky-hec is happening?!"
    s "Why can't I open this door?"
    s "Am I... snowed in?!"
    play sound "no-96018.mp3" volume 2.2
    s "No!!!"
    s "I can't carry out my plan! I'm stuck at home!"
    s "I'll have to stay in this ugly house for... who knows how many days..."
    s "Oh no! This is the end of my life!!!"
    stop music fadeout 0.5
    scene sad with fade
    play music "old-house-161057.mp3" fadein 1.0
    s "Sorry Pudding, my cute hamster... if I run out of food, I may have to sacrifice you 😭"
    s "Please don't hate your beloved owner!"
    s "I will always remember the lovely times we had together..."
    s "The memories of me cleaning up after you, your little workouts on the hamster wheel, your tiny muscles..."
    s "Oh... I can't continue... 😢"
    s "You will be cherished in my heart, always..."
    stop music fadeout 0.5
    s "But anyway, let me check first to see I much food I have."
    stop music fadeout 2.0
    scene close with dissolve
    play sound "sing.mp3"
    pause 2.0
    play sound "door-open-46756.mp3"
    pause 0.5
    scene open with fade
    pause 0.5
    scene out with dissolve
    play sound "metal-thud-6034.mp3"
    pause 3.5
    play music "funny-cartoon-music-412765.mp3"
    pause 2.3
    scene pudding with fade
    s "Okay Pudding, I have good news."
    s "We have more than enough food, so I'll survive -- and you will too!"
    s "So don't worry, you will live!"
    s "And you know what?"
    s "I get to spend the whole time with you!"
    s "Are you excited, Pudding?"
    s "Let's start by making breakfast and wacting TV together!"
    pause 1.0
    play music "later.mp3"
    scene hour with fade
    pause 2.7
    play music "funny-cartoon-music-412765.mp3"
    scene pudding with dissolve
    s "So, what do you think, Pudding?"
    s "Are you having fun so far?"
    s "Do you think the snow has melt much?"
    s "I'll go try to open the door -- hopefully it works!"
    scene door with fade
    play sound "My Project.mp3"
    pause 4.5
    scene more with fade
    play music "nebula-135416.mp3"
    play sound "walking-in-water-199418.mp3"
    pause 1.0
    scene water with fade
    pause 1.0
    scene form with fade
    pause 1.0 
    scene monster with fade
    play sound "monster-growl-376892.mp3"
    pause 3.5
    play music "funny-music-319843.mp3"
    


    return
    