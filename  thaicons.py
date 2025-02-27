import tkinter as tk
import random

# List of Thai consonants and their names
thai_consonants = [
    ("ก", "Gor Gai (กอ ไก่)"),
    ("\u0E02", "Khor Khai (ขอ ไข่)"),
    ("\u0E04", "Kor Kwai (คอ ควาย)"),
    ("\u0E07", "Ngor Ngu (งอ งู)"),
    ("\u0E08", "Jor Jaan (จอ จาน)"),
]

class FlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.current_card = None
        
        self.card_label = tk.Label(root, text="", font=("Arial", 100))
        self.card_label.pack(pady=50)
        
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card)
        self.flip_button.pack()
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack()
        
        self.next_card()

    def next_card(self):
        self.current_card = random.choice(thai_consonants)
        self.card_label.config(text=self.current_card[0])
        self.flipped = False

    def flip_card(self):
        if not self.flipped:
            self.card_label.config(text=self.current_card[1])
            self.flipped = True
        else:
            self.card_label.config(text=self.current_card[0])
            self.flipped = False

root = tk.Tk()
app = FlashcardGame(root)
root.mainloop()
