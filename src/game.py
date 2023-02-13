from random import shuffle

number_of_players = 3

class Game:
    def __init__(self):
        self.STATUS = True
        self.field = [0]
        self.level = 0
        self.lives = number_of_players - 1
        self.shurikens = 1
        self.players = []
        self.deck = []
        self.shuffleDeck()

    # def __del__(self):
    #     game.field = []
    #     for each_player in self.players:
    #         each_player.hand = []
    #     del self
    #     print("============ GAME DESTROYED ============")
        
    def shuffleDeck(self):
        self.deck = [x for x in range(1,101)]
        print("============= DECK SHUFFLED ============")
        shuffle(self.deck)
        print(self.deck)

    def getDeck(self):
        return self.deck

    def printDeck(self):
        print("============= CURRENT DECK =============")
        print(self.deck)

    def populateGame(self):
        for _ in range(number_of_players):
            _ = Player()
            self.players.append(_)

    def skipCard(self, card):
        pass

    def playerHands(self):
        print("Player hands: ", [every_player.hand for every_player in self.players])
        return [each_player.hand for each_player in self.players]

    def evalCards(self):
        if (len(all(self.playerHands[x])) for x in self.playerHands() ) == 1:
            print("Congratulations, you played yourself. :/")
            
        
    def evalHands(self):
        print("========= EVALUATING HANDS =======")
        if all(p.readyState == True for p in self.players):
            self.nextRound()
        if all(p.voteStop == True for p in self.players):
            pass
        if all(p.voteShuriken == True for p in self.players):
            pass

        
    def eval(self):
        print("============ GAME EVALUED ==========")
        for player in self.players:             #for every player
            for c in player.hand:               #for each card in player's hand
                if c < self.field[-1]:          #if card lower than deck
                    print("MISTAKE! A Player has a ", c)
                    player.hand.pop(player.hand.index(c)) #remove card from hand 
                    self.lives -= 1
                    continue
        if self.lives <= 0:
            print("=========== NO MORE LIVES ===========")
            self.__del__()
        if all(p.hand == [] for p in self.players):
            self.nextRound()


    def dealCards(self):
        for _ in range(self.level):    
            for player in self.players:
                if self.deck == []:
                    print("======= DECK EMPTY =========")
                    self.shuffleDeck()
                player.drawCard(self)
                        

            
    def nextRound(self):
        self.field = []                         #clear field
        self.level += 1                         #increase game level
        for p in self.players:
            p.hand = []                         #reset player's hand & stats
            p.readyState = False
            p.voteStop = False
            p.voteShuriken = False
        print("======= NEXT LEVEL =======")
        if self.level == 3:
            print("You get a new life!")
            self.lives += 1
        self.dealCards()
        self.playerHands()
        
            
                


class Player(Game):
    def __init__(self):
        self.hand = []
        self.readyState = False
        self.voteStop = False
        self.voteShuriken = False

    def getReady(self, game):
        self.readyState = True
        game.evalHands()

    def voteStop(self):
        self.voteStop = True

    def voteShuriken(self):
        self.voteShuriken = True

    def drawCard(self, game):
        print("You drew: ", game.deck[-1])
        self.hand.append( game.deck[-1])
        game.deck.pop()


    def throwCard(self, game):
        self.hand.sort()
        lowest_card = self.hand[0]
        if len(self.hand) == 0:
            return "You don't have a card, please draw."
        else:
            if len(game.field) >= 0:
                game.field.append(lowest_card)
                self.discardCard(lowest_card)
            else:
                try:
                    if game.field[-1] > lowest_card:
                        game.lives -= 1
                        self.discardCard(lowest_card)
                except Exception as e:
                    print(e)
                    print("Mistake! You have a", lowest_card)
                    return "ERROR!!"


    # def throwCard(self, game):
    #     self.hand.sort()                         #sort before throwing
    #     if self.hand == []:                      #not needed to sort every throw
    #         print("You don't have a card")       #move to eval or drawCards
    #     else:
    #         lowest_card = self.hand[0]              #always sorted
    #         if game.field == []:
    #             pass
    #         if game.field[-1] > lowest_card:
    #             print("Mistake! You have a", lowest_card)
    #             game.lives -= 1
    #             self.discardCard(lowest_card)
    #         try:    
    #             if self.hand[1] - 1 == self.hand[0]:
    #                 game.field.append(lowest_card)
    #                 del self.hand[0]
    #                 game.field.append(self.hand[0])
    #                 del self.hand[0]
    #         except IndexError:
    #             pass
    #         game.field.append(self.hand[0])         #throwing after conditions
    #         del self.hand[0]                        # ERROR!!!!!!!!!!!!!!! FLAW
    #         game.eval()



    def discardCard(self, card):
        if card in self.hand:
            self.hand.pop(self.hand.index(card))
        



    
game = Game()
game.populateGame()




print("============= GAME INITIALIZED ============= \n"
      "Players: ", number_of_players)


p1 = game.players[0]
print(p1.hand)
p2 = game.players[1]
print(p2.hand)
p3 = game.players[2]
print(p3.hand)

for p in game.players:
    p.getReady(game)


game.printDeck()    
            
