import pygame
from pygame import freetype
import sys
from treys import Card
from treys import Evaluator
from treys import Deck
from events import Events
from tkinter import *
from pynput.mouse import Button, Controller, Listener
import main


card = Card.new('Qh')
evaluator = Evaluator()
deck = Deck()
pygame.init()

cardName1 = ''
cardName11 = ''
cardName2 = ''
cardName22 = ''
cardName3 = ''
cardName33 = ''
cardName4 = ''
cardName44 = ''
cardName5 = ''
cardName55 = ''
cardName6 = ''
cardName66 = ''
cardName7 = ''
cardName77 = ''
cardName8 = ''
cardName88 = ''
cardName9 = ''
cardName99 = ''
cardName10 = ''
cardName1010 = ''
deckCard = 0
deckPick = 0
handPick = 0
board = []
hand = []
pScore = 0
pClass = 0
pScoreText = ''
pClassText = ''
percent = ''


cardCheck1 = cardName11+cardName22




print("'"+cardName77+cardName88+"'")






screen = pygame.display.set_mode((1600, 800))
pygame.display.set_caption("Automat do pokera")
icon = pygame.image.load('assets/icon.jpg')
pygame.display.set_icon(icon)

# background_image
bg = pygame.image.load('assets/table.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (1600,800))

# cards
cardX = 21          # 1st row
cardY = 30
shiftX = 121
card2X = 480        # 2nd row
card2Y = 181
shift2X = 180
shift_card = 100     # for mouse event

# cards import and scale
card2 = pygame.image.load("assets/2.png").convert_alpha()
card2 = pygame.transform.scale(card2, (100, 138))
card2_position = pygame.Rect(21, 30, 100, 138)
card3 = pygame.image.load("assets/3.png")
card3 = pygame.transform.scale(card3, (100, 138))
card4 = pygame.image.load("assets/4.png")
card4 = pygame.transform.scale(card4, (100, 138))
card5 = pygame.image.load("assets/5.png")
card5 = pygame.transform.scale(card5, (100, 138))
card6 = pygame.image.load("assets/6.png")
card6 = pygame.transform.scale(card6, (100, 138))
card7 = pygame.image.load("assets/7.png")
card7 = pygame.transform.scale(card7, (100, 138))
card8 = pygame.image.load("assets/8.png")
card8 = pygame.transform.scale(card8, (100, 138))
card9 = pygame.image.load("assets/9.png")
card9 = pygame.transform.scale(card9, (100, 138))
card10 = pygame.image.load("assets/10.png")
card10 = pygame.transform.scale(card10, (100, 138))
cardJ = pygame.image.load("assets/J.png")
cardJ = pygame.transform.scale(cardJ, (100, 138))
cardQ = pygame.image.load("assets/Q.png")
cardQ = pygame.transform.scale(cardQ, (100, 138))
cardK = pygame.image.load("assets/K.png")
cardK = pygame.transform.scale(cardK, (100, 138))
cardA = pygame.image.load("assets/A.png")
cardA = pygame.transform.scale(cardA, (100, 138))
cardKier = pygame.image.load("assets/kier.png")
cardKier = pygame.transform.scale(cardKier, (100, 138))
cardPik = pygame.image.load("assets/pik.png")
cardPik = pygame.transform.scale(cardPik, (100, 138))
cardKaro = pygame.image.load("assets/karo.png")
cardKaro = pygame.transform.scale(cardKaro, (100, 138))
cardTrefl = pygame.image.load("assets/trefl.png")
cardTrefl = pygame.transform.scale(cardTrefl, (100, 138))
deckCard1 = pygame.image.load("assets/blank.png")
deckCard1 = pygame.transform.scale(deckCard1, (100, 138))
deckCard2 = pygame.image.load("assets/blank.png")
deckCard2 = pygame.transform.scale(deckCard2, (100, 138))
deckCard3 = pygame.image.load("assets/blank.png")
deckCard3 = pygame.transform.scale(deckCard3, (100, 138))
handCard1 = pygame.image.load("assets/blank.png")
handCard1 = pygame.transform.scale(handCard1, (100, 138))
handCard2 = pygame.image.load("assets/blank.png")
handCard2 = pygame.transform.scale(handCard2, (100, 138))
reset = pygame.image.load("assets/reset.png")
resetDeck = pygame.image.load("assets/resetStol.png")
check = pygame.image.load("assets/sprawdz.png")




# cards initialization
def card_func():
    screen.blit(bg, (0,0))
    screen.blit(cardA, (cardX, cardY))
    screen.blit(card2, (cardX+shiftX, cardY))
    screen.blit(card3, (cardX+shiftX*2, cardY))
    screen.blit(card4, (cardX+shiftX*3, cardY))
    screen.blit(card5, (cardX+shiftX*4, cardY))
    screen.blit(card6, (cardX+shiftX*5, cardY))
    screen.blit(card7, (cardX+shiftX*6, cardY))
    screen.blit(card8, (cardX+shiftX*7, cardY))
    screen.blit(card9, (cardX+shiftX*8, cardY))
    screen.blit(card10, (cardX+shiftX*9, cardY))
    screen.blit(cardJ, (cardX+shiftX*10, cardY))
    screen.blit(cardQ, (cardX+shiftX*11, cardY))
    screen.blit(cardK, (cardX+shiftX*12, cardY))
    screen.blit(cardKier, (card2X, card2Y))
    screen.blit(cardKaro, (card2X+shift2X, card2Y))
    screen.blit(cardTrefl, (card2X+shift2X*2, card2Y))
    screen.blit(cardPik, (card2X+shift2X*3, card2Y))
    screen.blit(deckCard1, (600, 400))
    screen.blit(deckCard2, (750, 400))
    screen.blit(deckCard3, (900, 400))
    screen.blit(handCard1, (660, 600))
    screen.blit(handCard2, (840, 600))
    screen.blit(reset, (50, 450))
    screen.blit(resetDeck, (50, 550))
    screen.blit(check, (50, 650))


text_text = ''
text_text2 = ''
# mouse events controller

# card 1 row pick
def click_pos(pos):
    mouseX = pos[0]
    mouseY = pos[1]
    if 30 < mouseY < 151:
        if cardX < mouseX < (cardX+shift_card):
            if main.deckPick == 1:
                main.cardName1 = 'A'
                main.cardName11 = 'A'
            if main.deckPick == 2:
                main.cardName3 = 'A'
                main.cardName33 = 'A'
            if main.deckPick == 3:
                main.cardName5 = 'A'
                main.cardName55 = 'A'
            if main.deckPick == 4:
                main.cardName7 = 'A'
                main.cardName77 = 'A'
            if main.deckPick == 5:
                main.cardName9 = 'A'
                main.cardName99 = 'A'
        if cardX+shiftX < mouseX < (cardX+shiftX+shift_card):
            if main.deckPick == 1:
                main.cardName1 = '2'
                main.cardName11 = '2'
            if main.deckPick == 2:
                main.cardName3 = '2'
                main.cardName33 = '2'
            if main.deckPick == 3:
                main.cardName5 = '2'
                main.cardName55 = '2'
            if main.deckPick == 4:
                main.cardName7 = '2'
                main.cardName77 = '2'
            if main.deckPick == 5:
                main.cardName9 = '2'
                main.cardName99 = '2'
        if cardX+shiftX*2 < mouseX < (cardX+shiftX*2+shift_card):
            if main.deckPick == 1:
                main.cardName1 = '3'
                main.cardName11 = '3'
            if main.deckPick == 2:
                main.cardName3 = '3'
                main.cardName33 = '3'
            if main.deckPick == 3:
                main.cardName5 = '3'
                main.cardName55 = '3'
            if main.deckPick == 4:
                main.cardName7 = '3'
                main.cardName77 = '3'
            if main.deckPick == 5:
                main.cardName9 = '3'
                main.cardName99 = '3'
        if cardX+shiftX*3 < mouseX < (cardX+shiftX*3+shift_card):
            if main.deckPick == 1:
                main.cardName1 = '4'
                main.cardName11 = '4'
            if main.deckPick == 2:
                main.cardName3 = '4'
                main.cardName33 = '4'
            if main.deckPick == 3:
                main.cardName5 = '4'
                main.cardName55 = '4'
            if main.deckPick == 4:
                main.cardName7 = '4'
                main.cardName77 = '4'
            if main.deckPick == 5:
                main.cardName9 = '4'
                main.cardName99 = '4'
        if cardX+shiftX*4 < mouseX < (cardX+shiftX*4+shift_card):
            if main.deckPick == 1:
                main.cardName1 = '5'
                main.cardName11 = '5'
            if main.deckPick == 2:
                main.cardName3 = '5'
                main.cardName33 = '5'
            if main.deckPick == 3:
                main.cardName5 = '5'
                main.cardName55 = '5'
            if main.deckPick == 4:
                main.cardName7 = '5'
                main.cardName77 = '5'
            if main.deckPick == 5:
                main.cardName9 = '5'
                main.cardName99 = '5'
        if cardX+shiftX*5 < mouseX < (cardX+shiftX*5+shift_card):
            if main.deckPick == 1:
                main.cardName1 = '6'
                main.cardName11 = '6'
            if main.deckPick == 2:
                main.cardName3 = '6'
                main.cardName33 = '6'
            if main.deckPick == 3:
                main.cardName5 = '6'
                main.cardName55 = '6'
            if main.deckPick == 4:
                main.cardName7 = '6'
                main.cardName77 = '6'
            if main.deckPick == 5:
                main.cardName9 = '6'
                main.cardName99 = '6'
        if cardX+shiftX*6 < mouseX < (cardX+shiftX*6+shift_card):
            if main.deckPick == 1:
                main.cardName1 = '7'
                main.cardName11 = '7'
            if main.deckPick == 2:
                main.cardName3 = '7'
                main.cardName33 = '7'
            if main.deckPick == 3:
                main.cardName5 = '7'
                main.cardName55 = '7'
            if main.deckPick == 4:
                main.cardName7 = '7'
                main.cardName77 = '7'
            if main.deckPick == 5:
                main.cardName9 = '7'
                main.cardName99 = '7'
        if cardX+shiftX*7 < mouseX < (cardX+shiftX*7+shift_card):
            if main.deckPick == 1:
                main.cardName1 = '8'
                main.cardName11 = '8'
            if main.deckPick == 2:
                main.cardName3 = '8'
                main.cardName33 = '8'
            if main.deckPick == 3:
                main.cardName5 = '8'
                main.cardName55 = '8'
            if main.deckPick == 4:
                main.cardName7 = '8'
                main.cardName77 = '8'
            if main.deckPick == 5:
                main.cardName9 = '8'
                main.cardName99 = '8'
        if cardX+shiftX*8 < mouseX < (cardX+shiftX*8+shift_card):
            if main.deckPick == 1:
                main.cardName1 = '9'
                main.cardName11 = '9'
            if main.deckPick == 2:
                main.cardName3 = '9'
                main.cardName33 = '9'
            if main.deckPick == 3:
                main.cardName5 = '9'
                main.cardName55 = '9'
            if main.deckPick == 4:
                main.cardName7 = '9'
                main.cardName77 = '9'
            if main.deckPick == 5:
                main.cardName9 = '9'
                main.cardName99 = '9'
        if cardX+shiftX*9 < mouseX < (cardX+shiftX*9+shift_card):
            if main.deckPick == 1:
                main.cardName1 = '10'
                main.cardName11 = 'T'
            if main.deckPick == 2:
                main.cardName3 = '10'
                main.cardName33 = 'T'
            if main.deckPick == 3:
                main.cardName5 = '10'
                main.cardName55 = 'T'
            if main.deckPick == 4:
                main.cardName7 = '10'
                main.cardName77 = 'T'
            if main.deckPick == 5:
                main.cardName9 = '10'
                main.cardName99 = 'T'
        if cardX+shiftX*10 < mouseX < (cardX+shiftX*10+shift_card):
            if main.deckPick == 1:
                main.cardName1 = 'J'
                main.cardName11 = 'J'
            if main.deckPick == 2:
                main.cardName3 = 'J'
                main.cardName33 = 'J'
            if main.deckPick == 3:
                main.cardName5 = 'J'
                main.cardName55 = 'J'
            if main.deckPick == 4:
                main.cardName7 = 'J'
                main.cardName77 = 'J'
            if main.deckPick == 5:
                main.cardName9 = 'J'
                main.cardName99 = 'J'
        if cardX+shiftX*11 < mouseX < (cardX+shiftX*11+shift_card):
            if main.deckPick == 1:
                main.cardName1 = 'Q'
                main.cardName11 = 'Q'
            if main.deckPick == 2:
                main.cardName3 = 'Q'
                main.cardName33 = 'Q'
            if main.deckPick == 3:
                main.cardName5 = 'Q'
                main.cardName55 = 'Q'
            if main.deckPick == 4:
                main.cardName7 = 'Q'
                main.cardName77 = 'Q'
            if main.deckPick == 5:
                main.cardName9 = 'Q'
                main.cardName99 = 'Q'
        if cardX+shiftX*12 < mouseX < (cardX+shiftX*12+shift_card):
            if main.deckPick == 1:
                main.cardName1 = 'K'
                main.cardName11 = 'K'
            if main.deckPick == 2:
                main.cardName3 = 'K'
                main.cardName33 = 'K'
            if main.deckPick == 3:
                main.cardName5 = 'K'
                main.cardName55 = 'K'
            if main.deckPick == 4:
                main.cardName7 = 'K'
                main.cardName77 = 'K'
            if main.deckPick == 5:
                main.cardName9 = 'K'
                main.cardName99 = 'K'



# card 2nd row pick
def click_pos2(pos):
    mouseX = pos[0]
    mouseY = pos[1]
    if card2Y < mouseY < card2Y+121:
        if card2X < mouseX < card2X+shift_card:
            if main.deckPick == 1:
                main.cardName2 = 'S'
                main.cardName22 = 'h'
            if main.deckPick == 2:
                main.cardName4 = 'S'
                main.cardName44 = 'h'
            if main.deckPick == 3:
                main.cardName6 = 'S'
                main.cardName66 = 'h'
            if main.deckPick == 4:
                main.cardName8 = 'S'
                main.cardName88 = 'h'
            if main.deckPick == 5:
                main.cardName10 = 'S'
                main.cardName1010 = 'h'
        if card2X+shift2X < mouseX < card2X+shift2X+shift_card:
            if main.deckPick == 1:
                main.cardName2 = 'K'
                main.cardName22 = 'd'
            if main.deckPick == 2:
                main.cardName4 = 'K'
                main.cardName44 = 'd'
            if main.deckPick == 3:
                main.cardName6 = 'K'
                main.cardName66 = 'd'
            if main.deckPick == 4:
                main.cardName8 = 'K'
                main.cardName88 = 'd'
            if main.deckPick == 5:
                main.cardName10 = 'K'
                main.cardName1010 = 'd'
        if card2X+shift2X*2 < mouseX < card2X+shift2X*2+shift_card:
            if main.deckPick == 1:
                main.cardName2 = 'T'
                main.cardName22 = 'c'
            if main.deckPick == 2:
                main.cardName4 = 'T'
                main.cardName44 = 'c'
            if main.deckPick == 3:
                main.cardName6 = 'T'
                main.cardName66 = 'c'
            if main.deckPick == 4:
                main.cardName8 = 'T'
                main.cardName88 = 'c'
            if main.deckPick == 5:
                main.cardName10 = 'T'
                main.cardName1010 = 'c'
        if card2X+shift2X*3 < mouseX < card2X+shift2X*3+shift_card:
            if main.deckPick == 1:
                main.cardName2 = 'P'
                main.cardName22 = 's'
            if main.deckPick == 2:
                main.cardName4 = 'P'
                main.cardName44 = 's'
            if main.deckPick == 3:
                main.cardName6 = 'P'
                main.cardName66 = 's'
            if main.deckPick == 4:
                main.cardName8 = 'P'
                main.cardName88 = 's'
            if main.deckPick == 5:
                main.cardName10 = 'P'
                main.cardName1010 = 's'


# deck, hand pick and buttons
def click_pos3(pos):
    mouseX = pos[0]
    mouseY = pos[1]
    if 400 < mouseY < 538:
        if 600 < mouseX < 700:
            main.deckPick = 1
        if 750 < mouseX < 850:
            main.deckPick = 2
        if 900 < mouseX < 1000:
            main.deckPick = 3
    if 600 < mouseY < 738:
        if 660 < mouseX < 760:
            main.deckPick = 4
        if 840 < mouseX < 940:
            main.deckPick = 5

    if 50 < mouseX < 250:
        if 450 < mouseY < 500:
            if main.deckPick == 1:
                main.cardName1 = ''
                main.cardName11 = ''
                main.cardName2 = ''
                main.cardName22 = ''
                main.pScoreText = ''
            if main.deckPick == 2:
                main.cardName3 = ''
                main.cardName33 = ''
                main.cardName4 = ''
                main.cardName44 = ''
                main.pScoreText = ''
            if main.deckPick == 3:
                main.cardName5 = ''
                main.cardName55 = ''
                main.cardName6 = ''
                main.cardName66 = ''
                main.pScoreText = ''
            if main.deckPick == 4:
                main.cardName7 = ''
                main.cardName77 = ''
                main.cardName8 = ''
                main.cardName88 = ''
                main.pScoreText = ''
            if main.deckPick == 5:
                main.cardName9 = ''
                main.cardName99 = ''
                main.cardName10 = ''
                main.cardName1010 = ''
                main.pScoreText = ''
        if 550 < mouseY < 600:
            main.cardName1= ''
            main.cardName2 = ''
            main.cardName3 = ''
            main.cardName4 = ''
            main.cardName5 = ''
            main.cardName6 = ''
            main.cardName7 = ''
            main.cardName8 = ''
            main.cardName9 = ''
            main.cardName10 = ''
            main.cardName11 = ''
            main.cardName22 = ''
            main.cardName33 = ''
            main.cardName44 = ''
            main.cardName55 = ''
            main.cardName66 = ''
            main.cardName77 = ''
            main.cardName88 = ''
            main.cardName99 = ''
            main.cardName1010 = ''
            main.pScoreText = ''


        if 650 < mouseY < 700:
            checkCards()




running = True


def deck_card():
    if not main.cardName1 == '':
        if not main.cardName2 == '':
            cardFull1 = pygame.image.load("./assets/"+cardName2+cardName1+".png")
            cardFull1 = pygame.transform.scale(cardFull1, (100, 138))
            screen.blit(cardFull1, (600, 400))
    if not main.cardName3 == '':
        if not main.cardName4 == '':
            cardFull1 = pygame.image.load("./assets/"+cardName4+cardName3+".png")
            cardFull1 = pygame.transform.scale(cardFull1, (100, 138))
            screen.blit(cardFull1, (750, 400))
    if not main.cardName5 == '':
        if not main.cardName6 == '':
            cardFull1 = pygame.image.load("./assets/"+cardName6+cardName5+".png")
            cardFull1 = pygame.transform.scale(cardFull1, (100, 138))
            screen.blit(cardFull1, (900, 400))



def hand_card():
    if not main.cardName7 == '':
        if not main.cardName8 == '':
            cardFull1 = pygame.image.load("./assets/" + cardName8 + cardName7 + ".png")
            cardFull1 = pygame.transform.scale(cardFull1, (100, 138))
            screen.blit(cardFull1, (660, 600))
        if not main.cardName9 == '':
            if not main.cardName10 == '':
                cardFull1 = pygame.image.load("./assets/" + cardName10 + cardName9 + ".png")
                cardFull1 = pygame.transform.scale(cardFull1, (100, 138))
                screen.blit(cardFull1, (840, 600))

def checkCards():
    if main.cardName11 and main.cardName22 and main.cardName33 and main.cardName44 and main.cardName55 and main.cardName66 and main.cardName77 and main.cardName88 and main.cardName99 and main.cardName1010:
        cardNew1 = (main.cardName11 + main.cardName22)
        print(cardNew1)
        cardNew2 = (main.cardName33 + main.cardName44)
        cardNew3 = (main.cardName55 + main.cardName66)
        cardNew4 = (main.cardName77 + main.cardName88)
        cardNew5 = (main.cardName99 + main.cardName1010)
        main.board = [
            Card.new(cardNew1),
            Card.new(cardNew2),
            Card.new(cardNew3)
        ]
        main.hand = [
            Card.new(cardNew4),
            Card.new(cardNew5)
        ]

        print(Card.print_pretty_cards(main.board + main.hand))
        main.pScore = evaluator.evaluate(main.board, main.hand)
        main.pClass = evaluator.get_rank_class(main.pScore)
        main.pClass = evaluator.get_rank_class(main.pScore)
        print(evaluator.get_rank_class(main.pScore))
        print(main.pScore, evaluator.class_to_string(main.pClass))

        main.pScoreText = (main.pScore, evaluator.class_to_string(main.pClass))
        main.percent = (((7462-main.pScore)/7462)*100)







while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            click_pos3(pos)
            click_pos(pos)
            click_pos2(pos)


    # GAME_FONT.render_to(screen, (40, 350), "Hello World!", (255, 0, 0))
    card_func()
    font = pygame.font.SysFont("Times New Roman, Arial", 30)
    text1 = ("Karty na stole " )
    text2 = ("Karty na ręce ")
    text = font.render((text1), True, (255, 0, 0))
    text2 = font.render((text2), True, (255, 0, 0))
    screen.blit(text, (730, 350))
    screen.blit(text2, (730, 550))
    finalText = ("Punkty, nazwa układu kart:")
    finalText = font.render((finalText), True, (255, 0, 0))

    pScoreClassText = str(pScoreText)
    pScoreClassText = font.render((pScoreClassText), True, (255, 0, 0))
    screen.blit((pScoreClassText), (1100, 600))
    percentText1 = ("Procent: " + str(main.percent) + "%")
    percentText = (percentText1)
    percentText = font.render((percentText), True, (255, 0, 0))
    finalText1 = ("1 to najlepszy wynik, 7462 - najgorszy")
    finalText1 = font.render((finalText1), True, (255, 0, 0))
    if pScoreText:
        screen.blit((finalText), (1100, 550))
        screen.blit((finalText1), (1100, 700))
        screen.blit((percentText), (1100, 650))
    deck_card()
    hand_card()
    pygame.display.flip()

