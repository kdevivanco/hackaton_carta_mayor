class Card:

    def __init__( self , suit , point_val , string_val ):
        
        self.suit = suit
        self.point_val = point_val
        self.string_val = string_val

    def card_info(self):
        info = (f"{self.string_val} of {self.suit} : {self.point_val} points")
        #print(f"{self.string_val} of {self.suit} : {self.point_val} points")
        return info
        
        
    

class Deck:


    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append(Card( s , i , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()
            
    
    def sacar_carta(self):
        carta_elegida = random.choice(self.cards)
        
        self.cards.remove(carta_elegida)
        return carta_elegida
    
    def comparar_palos(self,carta1,carta2):
        puntos_pintas = {
            "clubs": 1,
            "hearts":2,
            "spades":3,
            "diamonds":4
        }
        puntos1 = puntos_pintas[carta1.suit]
        puntos2 = puntos_pintas[carta2.suit]

        if puntos1 > puntos2:
            return carta1
        return carta2
            
import random 
class Player:
    def __init__(self,name):
        self.name = name
    
    def escoger_carta(self,maso):
        self.carta = maso.sacar_carta()
        return self.carta

def game():
    on_off = True
    while on_off:
        maso = Deck()
        print(' ')
        print('_______________________')
        print(' ')
        
        answer = input('Jugar cara mayor? Si/No:')
        
        print(' ')
        print('_______________________')
        print(' ')
        
        if answer.lower() == 'no':
            on_off = False
        elif answer.lower() == 'si':
            dealer = Player('Dealer')
            nombre_jugador = input('Escribe tu nombre: ')
            jugador= Player(nombre_jugador)
            
            print(' ')
            print('_______________________')
            print(' ') 
            carta_dealer = dealer.escoger_carta(maso)
            carta_jugador = jugador.escoger_carta(maso)
            
            suma_jugador = jugador.carta.point_val
            suma_dealer = dealer.carta.point_val
            
            print(' ')
            print('_______________________')
            print(' ')
            if suma_jugador>suma_dealer:
                print(f'Gano {jugador.name} con {carta_jugador.card_info()}')
                print(f'Perdio {dealer.name} con {carta_dealer.card_info()}')
            
            elif suma_jugador<suma_dealer:
                print(f'Gano {dealer.name} con {carta_dealer.card_info()}')
                print(f'Perdio {jugador.name} con {carta_jugador.card_info()}')

            elif suma_jugador == suma_jugador:
                carta_ganadora = maso.comparar_palos(jugador.carta,dealer.carta)
                if carta_ganadora == jugador.carta:
                    print(f'Gano {jugador.name} con {carta_jugador.card_info()}')
                    print(f'Perdio {dealer.name} con {carta_dealer.card_info()}')
                else:
                    print(f'Gano {dealer.name} con {carta_dealer.card_info()}')
                    print(f'Perdio {jugador.name} con {carta_jugador.card_info()}')