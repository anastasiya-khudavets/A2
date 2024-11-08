import tkinter as tk
from tkinter import messagebox
import random

window = tk.Tk()
window.title("Blackjack")
window.geometry("800x600")

#Creating card deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

#Shuffle cards
def shuffle_cards():
    global deck, player_hand, dealer_hand
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    player_hand = []
    dealer_hand = []

shuffle_cards()

#Rules
def show_rules():
    rules = (
         "Blackjack Rules:\n"
        "1. Try to get as close to 21 without going over.\n"
        "2. Number cards are worth their face value, face cards are 10, Aces are 1 or 11.\n"
        "3. Dealer will draw until at least 17.\n"
        "4. Bust (over 21) loses the round."
    )
    messagebox.showinfo("Game Rules", rules)
    
rules_button = tk.Button(window, text="View Rules", command=show_rules, font=("Comic Sans MS", 12))
rules_button.pack(pady=10)

#GUI elements

#Hands 
player_label = tk.Label(window, text="Player's Hand: ", font=("Comic Sans MS", 12), fg="red")
player_label.pack()

dealer_label = tk.Label(window, text="Dealer's Hand: ", font=("Comic Sans MS", 12), fg="red")
dealer_label.pack()

#Wallet balance
starting_money = 100
wallet = starting_money
bet = 0

balance_label = tk.Label(window, text=f"Balance: ${wallet}", font=("Comic Sans MS", 12), fg="blue")
balance_label.pack()

result_label = tk.Label(window, text="", font=("Comic Sans MS", 12))
result_label.pack()

#Betting 
bet_label = tk.Label(window, text="Enter your bet:", font=("Comic Sans MS", 12))
bet_label.pack()

bet_entry = tk.Entry(window, font=("Comic Sans MS", 12))
bet_entry.pack()

#Dealing cards
def deal_card(hand):
    card = deck.pop()
    hand.append(card)
    return card

#Calculate value of hand
def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card, suit in hand:
        value += values[card]
        if card == 'A':
            aces += 1
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

#Player hits
def player_hit():
    deal_card(player_hand)
    player_label.config(text=f"Player's Hand: {player_hand} (Value: {calculate_hand_value(player_hand)})")
    
    if calculate_hand_value(player_hand) > 21:
        result_label.config(text="Bust! Dealer wins.")
        update_balance(False)  
        disable_buttons()

#Player stands - dealer's turn
def player_stand():
    while calculate_hand_value(dealer_hand) < 17:
        deal_card(dealer_hand)
    dealer_label.config(text=f"Dealer's Hand: {dealer_hand} (Value: {calculate_hand_value(dealer_hand)})")
    
    determine_winner()

#Determining the winner
def determine_winner():
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21 or player_value > dealer_value:
        result_label.config(text="Yay! You win!")
        update_balance(True)
    elif player_value == dealer_value:
        result_label.config(text="You tied...!")
    else:
        result_label.config(text="No luck... Dealer wins!")
        update_balance(False)
    
    disable_buttons()
    reset_betting_controls()

#Disable buttons when game is over
def disable_buttons():
    hit_button.config(state=tk.DISABLED)
    stand_button.config(state=tk.DISABLED)

#Update wallet
def update_balance(player_won):
    global wallet
    if player_won:
        wallet += bet
    else:
        wallet -= bet
    
    balance_label.config(text=f"Balance: ${wallet}")

#Submit bet
def submit_bet():
    global bet
    try:
        bet = int(bet_entry.get())
        if bet > wallet:
            messagebox.showwarning("Warning", "Oops! You don't have enough money :(")
        else:
            bet_entry.config(state=tk.DISABLED) 
            hide_betting_controls()  
            start_game()
    except ValueError:
        messagebox.showwarning("Warning", "Oops! Something went wrong...")

def hide_betting_controls():
    bet_label.pack_forget()
    bet_entry.pack_forget()
    submit_bet_button.pack_forget()

#Reset bet for new round
def reset_betting_controls():
    bet_entry.config(state=tk.NORMAL)
    bet_label.pack()
    bet_entry.pack()
    submit_bet_button.pack()

#Game starts
def start_game():
    global player_hand, dealer_hand
    shuffle_cards()
    
    #GUI reset
    player_label.config(text="Player's Hand:")
    dealer_label.config(text="Dealer's Hand:")
    result_label.config(text="")
    
    #Deal  cards
    deal_card(player_hand)
    deal_card(player_hand)
    deal_card(dealer_hand)
    deal_card(dealer_hand)
    
    #Update the displayed hands
    player_label.config(text=f"Player's Hand: {player_hand} (Value: {calculate_hand_value(player_hand)})")
    dealer_label.config(text=f"Dealer's Hand: {dealer_hand[0]} and [Hidden]")
    
    hit_button.config(state=tk.NORMAL)
    stand_button.config(state=tk.NORMAL)

#Reset
def restart_game():
    global wallet
    wallet = starting_money
    shuffle_cards()
    balance_label.config(text=f"Balance: ${wallet}")
    reset_betting_controls()
    result_label.config(text="")
    
#Buttons
hit_button = tk.Button(window, text="Hit", command=player_hit, state=tk.DISABLED, font=("Comic Sans MS", 12))
hit_button.pack(side=tk.LEFT, padx=10, pady=10)

stand_button = tk.Button(window, text="Stand", command=player_stand, state=tk.DISABLED, font=("Comic Sans MS", 12))
stand_button.pack(side=tk.RIGHT, padx=10, pady=10)

submit_bet_button = tk.Button(window, text="Submit Bet", command=submit_bet, font=("Comic Sans MS", 12), fg="red")
submit_bet_button.pack()

restart_button = tk.Button(window, text="Restart Game", command=restart_game, font=("Comic Sans MS", 12), fg = "green")
restart_button.pack(pady=20)

window.mainloop()
