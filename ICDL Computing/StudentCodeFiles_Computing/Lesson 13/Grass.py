# Import the 'pygame' library
import pygame
import pygame.gfxdraw
from random import randint
 
# Initialize 'pygame'
pygame.init()
 
# Define the colors we will use in RGB format
GREY =  (230, 230, 230)
GREEN = (  0, 180,   0)
# Create a screen that is 400 wide and 300 high
screen = pygame.display.set_mode( [400,300] )

# This procedure plots a dot on the screen.
# The maths for x and y is to scale the positions of points
# so that they fit nicely on the screen.
def plot_point( p ):
    x = (p[0]+4.6)/10 * 400
    y = (9.5-p[1])/10 * 300
    r = pygame.draw.rect(screen,GREEN,(x,y,2,2) )
    pygame.display.update(r)

# This procedure draws a GREEN circular blob on the screen
def draw_blob( p, size ):
    x = int(p[0])
    y = int(p[1])
    pygame.gfxdraw.filled_circle(screen,x,y,size*2+2,GREEN)
    pygame.display.update()
    print( "(",x,",",y,") size ",size )
    pygame.time.wait( 20 )

# apply_transform() is a function that takes a point
# position and gives back a new position.
#   t is one of the 'affine transforms'.
#   p is a point that the transform will be applied to
#   This function returns the position of the point after
#   the transform has been applied.
def apply_transform( t, p ):
    return ( t[0]*p[0]+t[1]*p[1]+t[4],t[2]*p[0]+t[3]*p[1]+t[5])

# Ask pygame if the user has clicked the X to close.
def check_for_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
            pygame.quit()
            return True
    return False

# Keep checking for events
# IF there was a draw_function, keep redrawing the screen.
def do_eventloop( draw_function ) :
    clock = pygame.time.Clock()
    while True:
        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(10)
        if check_for_quit() :
            return
        if( draw_function ) :
            # Clear the screen to grey
            screen.fill(GREY)
            draw_function()
            # Show whatever we've just drawn.
            pygame.display.update()

# Call a draw function just once, and then wait for the user to
# click X to close.
def draw_once( function ):
    print("Starting")
    # Clear the screen to grey
    screen.fill(GREY)
    # Show the grey background.
    pygame.display.update()
    function()
    # Show whatever we've just drawn.
    pygame.display.update()
    print( 'Finished')    
    # Run the event loop, but not drawing anything in it
    draw_nothing = 0
    do_eventloop( draw_nothing )

# This does the same as do_eventloop.
# It keeps drawing the screen repeatedly until user clicks X
# to close.
def draw_repeatedly( draw_function ):
    do_eventloop( draw_function )

#--- End of Boilerplate code


    
# draw blade of grass.
# i is the number of the blade of grass
# s and t are controled by the mouse position
def draw_blade( i, s, t ) :
    x = i * 10 + 50
    # dx will move the tips of the grass left or right.
    # The randint() changes dx by a random number so the grass 'sways in
    # the wind'.
    # The 2*t*(i-15) makes the tops spread apart.
    dx = randint( -10, 10 )/10 + 2*t*(i-15)
    shape = [(x-2,100),(x+2,100),(x+dx+s,50),(x+dx-s,50)]
    pygame.gfxdraw.aapolygon( screen, shape , GREEN)
    pygame.gfxdraw.filled_polygon( screen, shape , GREEN)
    
# iterate for 30 blades of grass
def draw_grass():
    pos = pygame.mouse.get_pos()
    for i in range(30):
        draw_blade(i, pos[0]/200, pos[1]/300 )

draw_repeatedly( draw_grass )


