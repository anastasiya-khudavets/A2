import tkinter as tk
from tkinter import messagebox
import random

window = tk.Tk()
window.title("BLACJKACK")
window.geometry("800x600")

def rules():
    rules = (
    "Blackjack Rules:\n"
        "1. Try to get as close to 21 without going over.\n"
        "2. Number cards are worth their face value, face cards are 10, Aces are 1 or 11.\n"
        "3. Dealer will draw until at least 17.\n"
        "4. Bust (over 21) loses the round."
    )
    messagebox.showinfo("Game Rules", rules)
    
rules_button = tk.Button(window, text="View Rules", command=rules, font=("Comic Sans MS", 12))
rules_button.pack(pady=10)

#Cards
suits = ['spades', 'clubs', 'diamonds', 'clubs']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

def shuffle_cards():
    global deck, player, dealer
    player = []
    dealer = []
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)


#Player and dealer
player_label = tk.Label(window, text="Player's Hand: ", font=("Comic Sans MS", 20), fg="red")
player_label.pack()

dealer_label = tk.Label(window, text="Dealer's Hand: ", font=("Comic Sans MS", 20), fg="red")
dealer_label.pack()

#Wallet
starting_money = 100
wallet = starting_money
bet = 0

balance_label = tk.Label(window, text=f"Balance: ${wallet}", font=("Comic Sans MS", 14), fg="blue")
balance_label.pack()

result_label = tk.Label(window, text="", font=("Comic Sans MS", 14))
result_label.pack()

#Betting 
bet_label = tk.Label(window, text="Enter your bet:", font=("Comic Sans MS", 14))
bet_label.pack()

bet_entry = tk.Entry(window, font=("Comic Sans MS", 14))
bet_entry.pack()

#Card dealt
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

#Pkaying
def hit():
    deal_card(player)
    player_label.config(text=f"Player's Hand: {player} (Value: {calculate_hand_value(player)})")
    
    if calculate_hand_value(player) > 21:
        result_label.config(text="Bust! Dealer wins.")
        update_wallet(False)  
        

def stand():
    while calculate_hand_value(dealer) < 17:
        deal_card(dealer)
    dealer_label.config(text=f"Dealer's Hand: {dealer} (Value: {calculate_hand_value(dealer)})")
    
    
def determine_winner():
    player_value = calculate_hand_value(player)
    dealer_value = calculate_hand_value(dealer)

    if player_value > dealer_value or dealer_value > 21:
        result_label.config(text="Yay! You win!")
        update_wallet(True)
    elif player_value == dealer_value:
        result_label.config(text="You tied...!")
    else:
        result_label.config(text="No luck... Dealer wins!")
        update_wallet(False)
    

def update_wallet(player_won):
    global wallet
    if player_won:
        wallet += bet
    else:
        wallet -= bet
    
    balance_label.config(text=f"Balance: ${wallet}")

#Submit bet
def bet():
    global bet
    try:
        bet = int(bet_entry.get())
        if bet > wallet:
            messagebox.showwarning("Warning", "Oops! You don't have enough money :(")
        else:
            bet_entry.config
            hide_bet()  
            start()  
    except ValueError:
        messagebox.showwarning("Warning", "Oops! Something went wrong...")

def hide_bet():
    bet_label.pack_forget()
    bet_entry.pack_forget()
    submit_bet_button.pack_forget()

def reset_bet():
    bet_entry.config
    bet_label.pack()
    bet_entry.pack()
    submit_bet_button.pack()

#Starting game
def start():
    global player, dealer, hit_button, stand_button
    shuffle_cards()
    
    player_label.config(text="Player's Hand:")
    dealer_label.config(text="Dealer's Hand:")
    result_label.config(text="")
    
    deal_card(player)
    deal_card(player)
    deal_card(dealer)
    deal_card(dealer)
    
    player_label.config(text=f"Player's Hand: {player} (Value: {calculate_hand_value(player)})")
    dealer_label.config(text=f"Dealer's Hand: {dealer[0]} and [Hidden]")
    
    hit_button.config(state=tk.NORMAL)
    stand_button.config(state=tk.NORMAL)

#Reset
def restart():
    global wallet
    wallet = starting_money
    shuffle_cards()
    balance_label.config(text=f"Balance: ${wallet}")
    reset_bet()
    result_label.config(text="")
    
#Buttons
hit_button = tk.Button(window, text="Hit!", command=hit, state=tk.DISABLED, font=("Comic Sans MS", 14)) 
hit_button.pack(side=tk.LEFT, padx=10, pady=10)

stand_button = tk.Button(window, text="Stand", command=stand, state=tk.DISABLED, font=("Comic Sans MS", 14))
stand_button.pack(side=tk.RIGHT, padx=10, pady=10)

submit_bet_button = tk.Button(window, text="Submit Bet", command=bet, font=("Comic Sans MS", 14), fg="red")
submit_bet_button.pack()

restart_button = tk.Button(window, text="Restart", command=restart, font=("Comic Sans MS", 14), fg="green")
restart_button.pack(pady=20)

window.mainloop()
#YAY!!
