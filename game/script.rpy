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
    s "Perfect for my pla-"
    scene huge
    play sound "winter-breeze-404248.mp3" volume 2.5
    pause 2.5
    show no at smallright with dissolve
    play sound "preview.mp3" volume 2.0
    s "Huh?! What...What just happened?"
    s "Why's there so much snow all of a sudden?"
    s "Oh no... I can't go outside in a snowstorm like this..."
    s "Will... I can't let this snowstorm ruin my day!"
    s "Although this is a REALLY huge snowstorm..."
    s "But I, Sheldon, will not fear and will follow through with the exact same plans I had for today!"
    s "Yes! I will go dress up warm and go to Macdonalds for breakfast!"
    return
    