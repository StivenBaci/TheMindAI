import string
import tkinter as tk
import game

class GameWindow(tk.Tk):
    def __init__(self, *args, **kwargs):

        self.game = game.Game()
        self.game.populateGame()

        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1200x800")
        self.config(bg="green")

        self.label = tk.Label(self, text="The Mind", bg="green")
        self.label.pack(pady=10)

        self.card_frame = tk.Frame(self, bg="green")
        self.card_frame.pack(pady=10)

        self.throw_card_button = tk.Button(self, text="Throw Card", command=self.throw_card)
        self.throw_card_button.pack(side="bottom", pady=20, anchor="center")

        

    def throw_card(self):
        #Improve code 
        game = self.game

        card = game.players[0].throwCard(game)           #divide in multiple series of function calls
        show_card = str(game.players[0]) + "threw: " + str(game.players[0].hand[-1])    #divide in multiple players each turn
        show_field = str(game.field)

        card_label = tk.Label(self.card_frame, text=show_card, bg="green")
        card_label.pack(side="left", padx=10)

        field_label = tk.Label(self.card_frame, text=show_field, bg="green")
        field_label.pack(side="left", pady=10)
        
    
        

if __name__ == "__main__":
    window = GameWindow()
    window.mainloop()

    game.populateGame()
    p1 = game.players[0]
    p2 = game.players[1]
    p3 = game.players[2]

    

