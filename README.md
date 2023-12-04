# Final-Project-3W2
Repository for my final project assigment. ANGM 2305 Sec: 3W2
<https://github.com/neonoguchi/Final-Project-3W2>

## Demo
Demo Video: <URL>

## GitHub Repository
GitHub Repo: <https://github.com/neonoguchi/Final-Project-3W2>

## Credit for Tutroials
Links to youtube tutorials that helped me create this final project!

<https://youtu.be/5-WGGYLT8E8?si=WRkDpY2n08_Zeaok> by World of Python
<https://youtu.be/UIq3VUzICPU?si=JI8P71CSULvlN5rM> by buildwithpython
<https://youtu.be/1_H7InPMjaY?si=1XN4Wh-dYFU0Vt9e> by Clear Code
<https://youtu.be/hDu8mcAlY4E?si=2tgAIwekfo8NFhDw> by Clear Code
<https://youtu.be/z0aOffHrTac?si=FDLeNal1NKljR82F> by DaFluffyPotato

## Credit for Assets
Links to all the 3rd-party assets used in this project!

Sprites:
<https://opengameart.org/content/pixel-robot> by David Harrington
<https://opengameart.org/content/key-icons> by BizmasterStudios
<https://opengameart.org/content/heart-6> by Mapachana

Sounds:
<https://freesound.org/people/InspectorJ/sounds/431118/>
<https://freesound.org/people/MasterSuite/sounds/667392/>
<https://freesound.org/people/MATRIXXX_/sounds/402766/>
<https://freesound.org/people/EminYILDIRIM/sounds/563662/>

## Description
For this final project, I wanted to be able to say that I had created a game... so that was the goal! I didn't want to this project to be too intimidating and overbearing so I kept the standards low and wanted to face the many problems I faced one step at a time. There were many things that I wanted to implement into this final project that I just could not figure out (such as a main menu, pause menu, quit button, retry button, multiple hostiles depending on the level, different variants of the hostile, etc.), but I think the overall result was a success in and of itself.
The actual game is not very complicated, but I hope you enjoy it none the less. After this project, I have gained a new found respect for game devs!

This project is a 2D infinite game (like many mobile/ arcade games) where youre main goal is to survive as long as possible and surpass as many levels as possible. You play as a robot and move around (using WASD) and are challenged to avoid the 'Hostile' which is a big red square. The hostile follows you and respawns at every new level. Be wary however... as the hostile, although slow, can consume you quickly.. If the hostile comes in contact with the player, you will lose HP! You may regain your HP by collecting hearts! 1 Heart spawns per level so collect them wisely.To continue to the next level, you must interact with the door (a red rectangle that can be found on the sides of the screen) by pressing the E key. However, the door will always be locked at the beginning of each level. To unlock the door, you must first collect the key! Once the key is collected, you may go back to the door to open it, and continue to the next level.

Now let me point out some things in this final project that I simply want to point out haha.
- Lvl count is displayed on the bottom left of the screen and goes up every time you enter a door.
- Every time you enter a door, a new level is generated!
    - The door's location is randomly picked between the 4 walls, and then randomly placed upon the chosen wall.
    - The heart and key items' locations are randomly generated within the screen.
    - When entering a door, the player's coordinates for the next level are based off of the previous door to create the effect of entering a new room.
    - The hostile's spawn location is based off of the player's new location, it will be on the other side of the screen.

- The player has 100 HP! There is a healthbar over their head and a bigger healthbar displayed on the bottom of the screen(though no numbers are displayed).
- The hostile's speed goes up little by little every 5 levels until level 20.
- The hostile's movement is based off of its center coordinates and the player's center coordinates. The hostile's goal is to place its center at the same location of the player, which creates this chase function!
- The hostile also turns blue as feedback, for when it collides with the player. You take 5 damage per tick and the game runs at 60fps, so you can die fairly quickly... be careful!
- The player and hostile's movements are restricted within the same playable display rectangle.
- The door will be locked at the beginning of every level. If your player's rect collides with the door rect, it will be a darker red, implying that it cannot be accessed/ it is locked.
- After collecting the key, the player can go to the door where it will now be highlighted yellow. Pressing the e_key will allow for the player to pass.
- Sprites were implemented for the player, key item, and heart item.
- There are sound effects implemented! The door will have a different interact sound for when it is locked and unlocked. The heart and key also have sounds when collected by the player.

Other Notes:
- 'images' folder for imported sprite assets
- 'sounds' folder for imported sound assets