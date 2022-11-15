#Poker por: 
#Kayla de Vivanco
#Tomas Heilenkotter
#Rodrigo Flores

import random 

class Card:

    def __init__( self , suit , point_val , string_val ):
        
        self.suit = suit
        self.point_val = point_val
        self.string_val = string_val

    def card_info(self):
        info = (f"{self.point_val}     {self.string_val} of {self.suit}")
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



class Player:
    def __init__(self,name):
        self.name = name
        self.hand = []
    
    def repartir_mano(self,maso,num):
        for numero in range(num):
            self.hand.append(maso.sacar_carta())
        
        return 
    
    def print_hand(self):
        for carta in self.hand:
            print(carta.card_info())
            
    def value_list(self):
        value_list = [] 
        for card in self.hand:
            value_list.append(card.point_val) #lista de los numeros en la mano
        return value_list
        
    def hand_points(self):
                
        position_numbers = [0, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        #Verificar tres veces: 
        for card in self.hand:
            position_numbers[card.point_val - 1] += 1
        
        #3 Trios
        trios = [num for num in position_numbers if num == 3]
        if len(trios) > 0:
            return 3
        
        #1 y 2 Pares 
        pares = [num for num in position_numbers if num == 2]
        if len(pares)>1:
            return 2
        elif len(pares)>0:
            return 1 
        
        #6. Full
        if len(trios)>0 and len(pares)>0: #full house
            return 6
        
        #5. Color
        suit_list = [] #lista de palos
        for card in self.hand:
            suit_list.append(card.suit)
        
        if len(set(suit_list)) == 1: #todas son del mismo color
            return 5
        
        
        #4. escalera multisuit
        value_list = [] 
        for card in self.hand:
            value_list.append(card.point_val) #lista de los numeros en la mano

        value_list.sort() #ordena la lista de valores
        value_set = set(value_list) #crea un set de valores unicos
        
        lista_diferencias = []
        for num in range(len(value_list)-1): #para cada num en la lista
            lista_diferencias.append(value_list[num] - value_list[num+1]) #diferencia entre cada carta
            set_diferencias = set(lista_diferencias) #si el set es de len = 1 las cartas tienen una diferencia igual entre si
        if len(set_diferencias)>1: #todas son diferentes y no hay escalera
            return 0
        if len(set_diferencias) == 1 and -1 in set_diferencias: #si la diferencia es -1, hay escalera
            return 4 #cuatro puntos por escalera
        
        
        #7. escalera de un solo palo... 
        if len(set_diferencias) == 1 and -1 in set_diferencias and len(set(suit_list) == 1):
            return 7 
        

def carta_mayor(p1,p2):
    carta_mayor_p1 = max(p1.value_list())
    carta_mayor_p2 = max(p2.value_list())
    
    if carta_mayor_p1>carta_mayor_p2:
        return p1
    elif carta_mayor_p1<carta_mayor_p2:
        return p2
    else:
        print('Es un verdadero empate')


def game():
    on_off = True
    while on_off:
        maso = Deck()
        print(' ')
        print('_______________________')
        print(' ')
        
        answer = input('Quieres jugar poker Si/No:')
        
        print(' ')
        print('_______________________')
        print(' ')
        
        if answer.lower() == 'no':
            on_off = False
        elif answer.lower() == 'si':
            dealer = Player('Dealer')
            nombre_jugador = input('Escribe tu nombre: ')
            player= Player(nombre_jugador)
            
        print(' ')
        print('_______________________')
        print(' ')
        
    
        
        player.repartir_mano(maso,5)
        dealer.repartir_mano(maso,5)
        
        print(f'La mano de {player.name} es..')
        player.print_hand()
        print(' ')
        print(f'La mano de {dealer.name} es..')
        dealer.print_hand()
        
        
        print(' ')
        print('_______________________')
        print(' ')
        
        player_points = player.hand_points()
        dealer_points = dealer.hand_points()
        
        if dealer_points == player_points:
            print('Vamos a jugar carta mayor para resolver el empate...')
            carta_mayor(player,dealer)
        
        elif type(player_points) == tuple and type(dealer_points) != tuple:
            #dealer tiene una mejor mano 
            print(f'Gano {dealer.name} con {dealer.hand_points()} puntos!')
            
        elif type(dealer_points) == tuple and type(player_points) != tuple:
            #dealer tiene una mejor mano 
            print(f'Gano {player.name} con {player.hand_points()} puntos!')
            
        else:
            if dealer_points>player_points:
                print(f'Gano {dealer.name} con {dealer_points} puntos!')
            elif dealer_points<player_points:
                print(f'Gano {player.name} con {player_points} puntos!')


game()
