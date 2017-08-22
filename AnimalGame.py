##
#   Program that imports the Pygame module to have an image of a dog, cat,
#   and some balls move around the frame.
#   
 
# Importing Pygame Module
import pygame
 
# Intilizing Pygame modules
pygame.init()
 
# Defining the colors.
red = (255, 0, 0)
black = (0, 0, 0)
blue = (51, 51, 255)
keylime = (204, 255, 102)

#Defining the screen size, setting the display, and naming display.
output_display = [1000, 600]
screen = pygame.display.set_mode(output_display)
pygame.display.set_caption("Cat Chase")
 
# Setting variables for the images that will be used and loads images into them.
# Converts image pixels to include alpha channels, allowing for the use of "png", "jpeg,
# and other images files.
Cat = pygame.image.load('C:\\Python\\Images\\BouncingGypTiny.png').convert_alpha()
Dog = pygame.image.load('C:\\Python\\Images\\BouncingPupTiny.png').convert_alpha()
Bckgrnd = pygame.image.load('C:\\Python\\Images\\dvdsnvle_ste_prk.jpg').convert_alpha()
 
# Defining event
Bounce = True
 
# Setting clock variable
clock = pygame.time.Clock()
 
# Defining positions
red_pos_x = 0
red_pos_y = 0
key_pos_x = 90
key_pos_y = 30
cat_pos_x = 20
cat_pos_y = 20
dog_pos_x = 186
dog_pos_y = 186
 
# Defining speed and direction
spd_dir_x = 15
spd_dir_y = 10
spd_dir1_x = 15
spd_dir1_y = 10
spd_dir2_x = 20
spd_dir2_y = 15
spd_dir3_x = 23
spd_dir3_y = 12

#Creating a container for all animal sprites using the pygame sprite group class.
Animal_Sprites = pygame.sprite.Group()

#Creating a class for a non-player animal character inheriting from the pygame sprite class.
class Kitty(pygame.sprite.Sprite) :

    #Defining the constructor; Pass an image.
    def __init__(self, image):

        #Initializing the sprite class by calling itself.
        pygame.sprite.Sprite.__init__(self)

        #Creating the image and cropping the rectangular object of the image within the game to better
        #accomdate the screen.
        self.image = image.subsurface(pygame.Rect(0, 0, 135, 130))

        #Retrieving the location of the image(the rectangular object modified previously).
        self.rect = self.image.get_rect()

#Creating a container for the Kitty class.
Feline = Kitty(Cat)

#Adding the Kitty class to animal sprite container.
Animal_Sprites.add(Feline)

#Creating a class for a player animal character inheriting from the pygame sprite class.
class Puppy(pygame.sprite.Sprite) :

    #Defining the constructor; Pass an image.
    def __init__(self, image):

        #Initializing the sprite class by calling itself.
        pygame.sprite.Sprite.__init__(self)

        #Creating the image and cropping the rectangular object of the image within the game to better
        #accomdate the screen.
        self.image = image.subsurface(pygame.Rect(36, 30, 150, 225))

        #Retrieving the location of the image(the rectangular object modified previously).
        self.rect = self.image.get_rect()

#Creating a container for the Puppy class.
Canine = Puppy(Dog)

#Adding Puppy class to animal sprite container.
Animal_Sprites.add(Canine)

#Creating a container for all sprites that would be used within the program
#using the pygame sprite group class.
Sprites_Roster = pygame.sprite.Group()
#Placing animal sprites group container into a group container which holds all sprites.
Sprites_Roster.add(Animal_Sprites)


#----------------Main Game Program---------------------------------------#

# Intializing event with while loop.
while Bounce == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Bounce = False

    # Creating displaying and setting background to black.
    screen.blit(Bckgrnd, [0,0])

    #Retrieves the mouses coordinates and placed in a container.
    pos = pygame.mouse.get_pos()
    #hides the cursor when placed over game windows.
    pygame.mouse.set_visible(False)
 
    # Drawing the images on the screen and setting their position.

    Canine.rect.x = pos[0] # Setting the position of Canine
    Canine.rect.y = pos[1] # to the follow cursor.

    Feline.rect.x = cat_pos_x #Sets the starting location of Feline
    Feline.rect.y = cat_pos_y #to the predefined cat position.

    Sprites_Roster.draw(screen)#Using the draw function every sprite grouped
                               #together and placed in the sprites_roster
                               #container will be drawn.

    #Using the draw circle function; two circles are created defining what surface they will be drawn on,
    #their fill color, position, radius, and width.
    pygame.draw.circle(screen, keylime, (key_pos_x, key_pos_y), 20, 0)
    pygame.draw.circle(screen, red, (red_pos_x, red_pos_y), 20, 0)
 
    # Using the addition assignment operator to update positions.
    cat_pos_x += spd_dir_x
    cat_pos_y += spd_dir_y
    dog_pos_x += spd_dir1_x
    dog_pos_y += spd_dir1_y #All positions are updated by adding the value of spd_dir
    key_pos_x += spd_dir2_x #to the current value of the pos_(x or y).
    key_pos_y += spd_dir2_y
    red_pos_x += spd_dir3_x
    red_pos_y += spd_dir3_y
    
 
    # Using 'if' loop and 'or' operator to invert the speed and
    # direction of the images when they reach the display boundries.

    if cat_pos_y > 550 or cat_pos_y < 0:#Sets the boundry for the "y" axis
        spd_dir_y = spd_dir_y * -1
    if cat_pos_x > 975 or cat_pos_x < 0: 
        spd_dir_x = spd_dir_x * -1 #When reaching the boundries of the display the
                                   #value of spd_dir is multiplied by -1 inverting the value
                                   #and thus begins subtracting from the "_pos" value causing
                                   #a change in direction.
 
    if dog_pos_y > 495 or dog_pos_y < 5:
        spd_dir1_y = spd_dir1_y * -1
    if dog_pos_x > 995 or dog_pos_x < 5:
        spd_dir1_x = spd_dir1_x * -1

    if key_pos_y > 500 or key_pos_y < 0:
        spd_dir2_y = spd_dir2_y * -1
    if key_pos_x > 900 or key_pos_x < 20:
        spd_dir2_x = spd_dir2_x * -1

    if red_pos_y > 500 or red_pos_y < 0:
        spd_dir3_y = spd_dir3_y * -1
    if red_pos_x > 900 or red_pos_x < 20:
        spd_dir3_x = spd_dir3_x * -1

    # Using clock to set frames per second.
    clock.tick(60)
 
    # Updating the cotents of the entire display.
    pygame.display.flip()
 
# Unintializing display module.
pygame.quit()
