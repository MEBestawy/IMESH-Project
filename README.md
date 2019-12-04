<!--
Connect2^2 project README documentation. Connect2^2 is 
a digital take of the classic Connect4 game. This project
is open-source, feel free to contribute as you see best fit.

Developed by iMesh.
-->

<!-- Beginning of document -->
# Connect 2<sup>2</sup>
<p align="center">
  <img src="https://i.imgur.com/FqoDAmg.png"></img>
</p>

A digital remake of the beloved Connect 4 game.

<!-- Document navigation menu -->
## Contents
1. [Game Description](#intro) 
    - [Screenshots](#screenshot)
2. [Installation](#install)
3. [Game Features & How to Play](#howToPlay)
4. [Repository Structure](#repoStructure)
5. [Code Documentation](#codeDocument)
6. [Contributors](#contributors)
7. [Notes & Credits](#credits)
8. [License](#license)

<!-- Game Description section -->
## <a name="intro"></a>Game Description
Connect 2^2 is a game in which two players stack their discs on top of other discs, aiming to make a Connect 2^2, that is to say align four discs of the same colour horizontally, vertically, or diagonally. A player, upon his or her turn, drops his or her disc into one of the seven columns, given that the said column is not completely filled with discs. If this new disc makes a Connect 2^2, the game ends with the player winning. Otherwise, the game continues with the other player. If a board becomes full with no Connect 2^2, the game ends as a tie.

<!-- Screenshots of the game -->
## <a name="screenshot"></a>Screenshots

| ![Screen 1](https://i.imgur.com/I4ctcW9.png) | ![Screen 2](https://i.imgur.com/SESJ0HG.png) |
|---------------------------------------------|---------------------------------------------|
| ![Screen 3](https://i.imgur.com/phT2gt4.png) | ![Screen 4](https://i.imgur.com/CVn7r3k.png) |

<!-- Installation section -->
## <a name="install"></a>Installation

These instructions will help you get a copy of the project up and running on your local device for development and testing purposes.

### Prerequisites

To be able to run our game, you are going to have to download our game's dependencies.
- Python 3 or newer
    - Connect 2<sup>2</sup> is written in Python, so without it, you cannot play our game :(
    - If you do not already have Python installed, you can download it from [here](https://www.python.org/downloads/). Make sure the version of Python you are downloading is Python 3 or higher.
    - **Note:** When installing Python, make sure to select the add to path option so the next few steps are easier to follow.

- Pygame
    - Connect 2<sup>2</sup> uses pygame to act ********************
    - You can download pyGame by opening up your respective command line. For Mac and Linux users, this is your terminal. For Windows users this is your command prompt.
    - Next you need to enter in the following into your command line. This will download pygame for you.
    - ```pip install pygame```
    - Alternatively, you can download pygame from [here](https://www.pygame.org/download.shtml)

- numPy module
    - Similar to installing pygame, you have to enter the following in to your command line to install the numpy module.
    - ```pip install numpy```

### Downloading our game

Now that you have all of our game dependencies installed, you can now download our game by either cloning the repo or downloading the game as a zip file.

- Cloning the repo
    - To clone the repo, simply open up your terminal(Mac/Linux) or command prompt(Windows) and enter the following.
    - ```git clone https://github.com/MEBestawy/IMESH-Project.git```
    - **Note:** To do this, you must have git installed on your device. If you do not have git installed [this](https://gist.github.com/derhuerst/1b15ff4652a867391f03#file-linux-md) will help you get git running.

- Downloading the game as a zip file
    - [Download Connect 2<sup>2</sup> here](https://github.com/MEBestawy/IMESH-Project/archive/master.zip)

### Running our game
To run our game, simply navigate to Game.py in the IMESH-Project directory and run it with the IDE of your choice.
**Note:**: If you downloaded our game as a zip file, make sure to unzip and then proceed with the above step.
     
<!-- How to Play section -->
## <a name="howToPlay"></a> Game Features & How to Play
First of all, get a friend to play against! Note, Connect 2^2 can only handle mouse input so keyboard input(s) won't do anything.

### Features
Title Screen: 
- "Play": Goes to the game screen to play the game.
- "Option": Goes to the option screen to pick a soundtrack, adjust BGM & SFX volume, or to read the game rules.
- "Quit": Exits the game. 

Option Screen: 
- "Select BGM": Selects a song from a selection of copyright-free music.
- "BGM Volume": Toggle BGM volume.
- "SFX Volume": Toggle SFX volume.
- Displays instructions on how to win the game. 

### How to Play
The game screen contains a 6 by 7 board, be the first to connect 2^2 discs to win the game. 
- Click on the circles on the board to drop a disc. 
- Click on the "Back" button to return to the menu. The board will be unaltered until the game ends or the user exits the game.
- **Note:** A disc will only be dropped on the board if a circle is clicked and if the top most row is unoccupied. 

The game ends if someone wins or if there is a tie, and proceeds to the end screen. 

<!-- Repo Structure section -->
## <a name="repoStructure"></a>Repository Structure

<!-- Code Documentation section -->
## <a name="codeDocument"></a>Code Documentation
The documentation for our project can be found in the wiki page of our 
repository. You can access it 
[here](https://github.com/MEBestawy/IMESH-Project/wiki).

<!-- Contributors section -->
## <a name="contributors"></a>Contributors

<!-- Mahmoud's addendum -->
- **Mahmoud El Bestawy**
    - PUT YOUR CONTRIBUTION HERE
     
<!-- Elysia's addendum -->
- **Elysia Yong**
    - I created the Game class that brought the backend and frontend components of the game together, and I am responsible for most the GUI components of the game such as the different screens. I set up the main Game, Menu, State, and Button classes that are currently utilised for this version of the game. I also added other unused classes such as Handler and GameObject for future implementations whereby these two classes handle object animation in the game. I am also responsible for creating most of the graphical assets such as the game's background and logo, but the music and sound effect are from copyright-free producers and a friend. In this README, I added images in "Game Description" and "Screenshots" sections, and populated the "Game Features & How to Play" and "Notes & Credits" sections. 

<!-- Shivam's addendum -->
- **Shivam Bhatoolaul**
    - PUT YOUR CONTRIBUTION HERE
     
<!-- Ivan's addendum -->
- **Ivan Kim**
    - PUT YOUR CONTRIBUTION HERE
    
<!-- Herjot's addendum -->
- **Herjot Dhaliwal**
    - My responsibility was to help design the Board class and implement some of the methods used in it. I further helped design and implement
    the unused Player class. This class is left unused for future implementations where someone may want to make AI opponents or redesign the 
    way we made the game. In addition to this, I am responsible for creating the test board class where I test the functionality of our 
    Connect 2<sup>2</sup> board. I ensured that moves were made correctly, meaning only moves that are valid are made, whether the correct
    winner is found if the game has ended and more. Within this README file, I was responsible for walking potential users through the process
    of installing and running our game without difficulty and provided them with resources that they might find useful.

<!-- Credits section --> 
## <a name="credits"></a>Notes & Credits 
First of all, iMesh gives thanks to [fengthefern] for composing "Rainfall", one of the background music for Connect 2^2. 

On another note, more content for the Connect 2^2 game will be available in the coming future. 

[fengthefern]: https://www.instagram.com/feng_the_fern/
     
<!-- Liecense section -->
## <a name="license"></a>License
MIT License (MIT)

Copyright © 2019 iMesh Group

You can find a copy of the licence at https://mit-license.org/


