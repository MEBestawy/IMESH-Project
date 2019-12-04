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

<img src="https://i.imgur.com/fWS9FRi.png"></img>

In this section, we provide a general overview of what each file in our repository contains. Make sure to refer to the [Code Documentation](#codeDocument) for further details about the classes and methods in each file.

We divided our repository into 2 sections: assets and code.

The folder `Assets` contains every component we used in `pygame` for Connect 2^2. This is where you would add any extra image file or sound file to use in our game. 

Now, here are the Python source code files in our repository: 

- `Board.py`: contains information on how to create, move and check for a winner on a Connect 2^2 board.

- `Button.py`: contains information on how to create the different buttons in our game.
	
- `DisplayBoard.py`: contains information on how the board is displayed in our Connect 2^2 game and how the game screen is updated after every turn. 

- `Game.py`: contains all the information about how to start the game, how to change game screens and how to modify the music. 

- `Menu.py`: contains information about what is displayed in the menu screen of Connect 2^2.

- `State.py`: contains every state or screen possible in the game.

Please note that are other Python source code files in our repository that we used for testing or that we started working on to extend the game in the future. That being said, the files mentioned above are all that are needed to run and modify Connect 2^2. 

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
    - In our code,
    I worked on the class ``DisplayBoard``, which displays the Connect 2^2 board where our users play our game (see the bottom-left screen in [Screenshots](#screenshot)). This was done by first initializing a ``Board`` class in ``DisplayBoard``. From there, I created a method that continuously renders the current representation of the ``Board`` with sprites on the game screen. Finally, I created methods in ``DisplayBoard`` that update the ``Board`` according to what was clicked on screen. 
    I also worked on the class ``GameProtoype``, which was originally used to display our game in ``pygame``, before Elysia found a more efficient way to structure our code. 
    Lastly, I created the class ``PlayGameInConsole``, which can be used to test out new features in the ``Board`` class, if someone decides to extend Connect 2^2.

  - In the README file, I worked on the description of our [Repository Structure](#repoStructure).
     
<!-- Ivan's addendum -->
- **Ivan Kim**
    - PUT YOUR CONTRIBUTION HERE
    
<!-- Herjot's addendum -->
- **Herjot Dhaliwal**
    - PUT YOUR CONTRIBUTION HERE

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


