# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Sheldon", color="#FF0020")


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
    pause 2.0
    return
    