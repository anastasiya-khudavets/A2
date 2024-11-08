# A2 - Blackjack
This project is a game of Blackjack built using Python and employing the tkinter interface. Players can place bets, draw cards (Hit), hold their hand (Stand), and try to beat the dealer by getting as close to 21 as possible without going over. The game includes basic betting functionality, balance updates, and adjustable Ace values.

**Features**
  GUI - Buttons, entry fields and labels
  Betting system - User starts with $100 and then based on their results will lose or accumulate their balance.
  Rules - Rules button outlines the rules of the game
  Reset button - Resets the game and brings user back to $100 balance

**Requirements**
Python 3.6+

**Gameplay**
Start the Game:
  Upon opening the game, you will see a balance, a field to enter your bet, and buttons to submit your bet, hit, stand, and restart the game.

View Rules:
  Click the “View Rules” button to open a pop-up with a summary of Blackjack rules.

Place a Bet:
  Enter your desired bet amount in the text field and click “Submit Bet.” You’ll be notified if the amount is invalid.

Play the Round:
  Choose “Hit” to draw more cards or “Stand” to hold your hand. The goal is to get as close as possible to 21 without going over. The dealer will draw cards until their hand reaches 17 or higher.

Win or Lose:
  If your hand is closer to 21 than the dealer's without going over, you win the round, and your balance is updated accordingly. If the dealer wins or you bust, you lose your bet amount.

Restart the Game:
  Click "Restart Game" to reset your balance and start fresh.

**Acknowledgements**
Some of the concepts of the gameplay (such as initialising the deck and hands, dealing cards, calculating the value of the hands and determining the winner) were inspired by YouTube videos by users Beau Carnes and Code Coach, though much of the code was changed to accomodate for the integrated GUI and the betting system, which the videos did not implement. Some of the other resources used were realpython.com, python.org and geeksforgeeks.org.

**Links**
  Beau Carnes. (2023, March 21). Python for Beginners Tutorial – Learn Programming by Coding a Blackjack Game [Video]. YouTube. https://www.youtube.com/watch?v=aryte85bt_M&t=354s

Code Coach. (2021, June 29). Create Blackjack in Python | Beginner Friendly Tutorial [Video]. YouTube. https://www.youtube.com/watch?v=mpL0Y01v6tY&t=676s 

Python Software Foundation. (n.d.). tkinter.messagebox — Message dialogs. Python.org. https://docs.python.org/3/library/tkinter.messagebox.html

Python Software Foundation. (n.d.). Tkinter — Python interface to Tcl/Tk. Python.org. https://docs.python.org/3/library/tkinter.html

GeeksforGeeks. (2024, August 14). Python - Creating a button in Tkinter. GeeksforGeeks. https://www.geeksforgeeks.org/python-creating-a-button-in-tkinter/ 

Gruppetta, S. (n.d.). Image processing with the Python Pillow library. Real Python. https://realpython.com/image-processing-with-the-python-pillow-library/  
