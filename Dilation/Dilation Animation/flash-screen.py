# import pygame module in this program 
import pygame 
from dilationAnimation import main
from input import getInputs
import time

# activate the pygame library . 
# initiate pygame and give permission 
# to use pygame's functionality. 
pygame.init() 

# define the RGB value 
# for white colour 
white = (255, 255, 255) 

# assigning values to X and Y variable 
X = 1000
Y = 563

# create the display surface object 
# of specific dimension..e(X, Y). 
display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('Dilation')

# create a surface object, image is drawn on it.
image = pygame.image.load(r'Dilation/assets/flash-image1.png')

# white color
color = (255,255,255)

# light shade of the button
color_light = (170,170,170)

# dark shade of the button
color_dark = (100,100,100)

# stores the width of the
# screen into a variable
width = display_surface.get_width()

# stores the height of the
# screen into a variable
height = display_surface.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel',35)

# rendering a text written in
# this font
text = smallfont.render('START' , True , color)

# infinite loop
while True:

	# completely fill the surface object
	# with white colour
    display_surface.fill(white)

	# copying the image surface object
	# to the display surface object at
	# (0, 0) coordinate.
    display_surface.blit(image, (0, 0))

	# iterate over the list of Event objects
	# that was returned by pygame.event.get() method.
    for event in pygame.event.get():
		# if event object type is QUIT
		# then quitting the pygame
		# and program both.
        if event.type == pygame.QUIT:
			# deactivates the pygame library
            pygame.quit()

			# quit the program.
            quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
			#if the mouse is clicked on the
			# button the game is terminated
            if width/2-70 <= mouse[0] <= width/2+70 and height/2+80 <= mouse[1] <= height/2+120:
                # pygame.quit()
                time.sleep(1)
                getInputs()
                # main()

		# # Draws the surface object to the screen.
        # pygame.display.update()
        # fills the screen with a color
        # display_surface.fill((60,25,60))
        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        # if mouse is hovered on a button it
        # changes to lighter shade
        if width/2-70 <= mouse[0] <= width/2+70 and height/2+80 <= mouse[1] <= height/2+120:
            pygame.draw.rect(display_surface,color_light,[width/2-70,height/2+80,140,40])
        else:
            pygame.draw.rect(display_surface,color_dark,[width/2-70,height/2+80,140,40])

        # superimposing the text onto our button
        display_surface.blit(text , (width/2-40,height/2+90))

        # updates the frames of the game
        pygame.display.update()