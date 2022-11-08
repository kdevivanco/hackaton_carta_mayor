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
        self.hand = []
    
    def repartir_mano(self,maso,num):
        for numero in range(num):
            self.hand.append(maso.sacar_carta())
        
        return 
    
    def print_hand(self):
        for carta in self.hand:
            print(carta.card_info())
    
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
        
        
        #escalera multisuit
        value_list = []
        for card in self.hand:
            value_list.append(card.point_val) #lista de los numeros en la mano
        
        value_list.sort() #ordena
        value_set = set(value_list) #crea un set de los valores unicos de la lista
        
        if len(value_list) == len(value_set): #hay 5 cartas diferentes en la mano
            #si la diferencia entre el valor anterior vs el valor actual == 1 
            lista_diferencias = []
            for num in range(len(value_list)-1):
                lista_diferencias.append(value_list[num] - value_list[num+1]) #diferencia entre cada carta
                set_diferencias = set(lista_diferencias) #viendo que solo hayan diferencias de -1
                if -1 in lista_diferencias and len(set_diferencias) == 1: #escalera
                    return 4
        
        return 0
        

