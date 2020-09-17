import pygame
from network import Network

pygame.init()
width = 1000
height = 500

#               R    G    B
WHITE       = (255, 255, 255)
BLACK       = (  0,   0,   0)
RED         = (255,   0,   0)
GREEN       = (  0, 255,   0)
DARKGREEN   = (  0, 155,   0)
DARKGRAY    = ( 40,  40,  40)
GRAY        = (110, 110, 110)
LIGHT_GREEN = (  0, 120,   0)
LIGHT_RED   = (120,   0,   0)

# Basic bg screen info
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Poker')
clock = pygame.time.Clock()
bg_img = pygame.image.load("poker_table.png").convert()

# Scaling the bg image to the full screen
screen.blit(pygame.transform.scale(bg_img, (width, height)), (0, 0))
pygame.display.flip()
clock.tick(10)

# Card class definition
class Card:
    def __init__(self, suit_type, value):
        self.suit_type = suit_type
        self.value = value
'''
def read_num(str):
    # Obtaining value of numbers as a tuple
    # And splitting them into two numbers and returning them in the format of a tuple
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_num(tup):
    return str(tup[0]) + "," + str(tup[1])
'''

def main():
    global screen
    # Creating the Network object and connecting to the server
    n = Network()
    pot_card = n.recv(2048)
    print("The pot card is: ", pot_card)
    #startNum = read_num(n.getNum())

    # The type of suit
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    # The type of card
    cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
    # The card value
    cards_values = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "11": 11, "12": 12, "13": 13}
    # The deck of cards - List of Objects
    deck = []
    # Adding each card to the deck
    for suit in suits:
        for card in cards:
            deck.append(Card(suit, card))

    # Types of fonts used
    small_font = pygame.font.Font(None, 32)
    large_font = pygame.font.Font(None, 50)

    # Start and Stop Game Buttons

    start_button = large_font.render("START", True, WHITE)
    # Gets_rectangular covering of text
    start_button_rect = start_button.get_rect()
    # Places the text
    start_button_rect.center = (280, 400)

    stop_button = large_font.render("STOP", True, WHITE)
    stop_button_rect = stop_button.get_rect()
    stop_button_rect.center = (520, 400)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
            # Allowing the image to be scaled to various screen sizes
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(event.dict['size'], pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
                screen.blit(pygame.transform.scale(bg_img, event.dict['size']), (0, 0))
                pygame.display.flip()



        # Used to stop game functioning, if True
        over = False

        # The GAME LOOP
        while True:
            # Tracking the mouse movements
            mouse = pygame.mouse.get_pos()

            # Manage the button hovering animation
            if 220 <= mouse[0] <= 220 + 125 and 370 <= mouse[1] <= 370 + 60:
                pygame.draw.rect(screen, LIGHT_GREEN, [220, 370, 125, 60])
            else:
                pygame.draw.rect(screen, GREEN, [220, 370, 125, 60])

            if 460 <= mouse[0] <= 460 + 120 and 370 <= mouse[1] <= 370 + 60:
                pygame.draw.rect(screen, LIGHT_RED, [460, 370, 120, 60])
            else:
                pygame.draw.rect(screen, RED, [460, 370, 120, 60])

            # Loop events occurring inside the game window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # Left-mouse clicked event
                if not over and event.type == pygame.MOUSEBUTTONDOWN:
                    choice = -1

                    # Clicked on the Start Button
                    if 220 <= mouse[0] <= 220 + 125 and 370 <= mouse[1] <= 370 + 60:
                        choice = 1
                    # Clicked on the Stop Button
                    if 460 <= mouse[0] <= 460 + 120 and 370 <= mouse[1] <= 370 + 60:
                        choice = 0
                        quit()

                    # If a valid choice, the game logic
                    if choice == 1:
                        print(pot_card)

                        # Loading and scaling the pot card image
                        p_card = pygame.image.load(pot_card + '.PNG')
                        p_card = pygame.transform.scale(p_card, (100, 160))
                        screen.blit(p_card, (200, 100))

            # Setting up all the buttons, images and texts on the screen
            screen.blit(start_button, start_button_rect)
            screen.blit(stop_button, stop_button_rect)

            # Receiving the dealt cards
            while True:
                dealt_cards = n.recv(2048)
                print("The dealt card is: ", dealt_cards)
                print("\n")

                # Choosing and sending a card with value less than the pot card
                card = input(str("Enter: "))
                n.send(card)


                new_pot = n.recv(2048)
                new_pot = pygame.image.load(data + '.PNG')
                new_pot = pygame.transform.scale(new_pot(100, 160))
                screen.blit(new_pot, (200, 100))

        pygame.display.update()


if __name__ == '__main__':
    main()

