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



# Define four 'affine transformations'
f1 = [0,0,0,0.22,0,0]
f2 = [0.85,0.04,-0.04,0.85,0,1.6]
f3 = [0.2,-0.26,0.23,0.22,0,1.6]
f4 = [-0.15,0.28,0.26,0.24,0,0.44]
    
# The recursive function which calls itself.
# It calls itself four times
# Each of those in turn calls itself four times, 
def draw_fern( level, p ):
    if level < 1 :
        plot_point( p )
        return
    draw_fern( level-1, apply_transform( f1, p ))
    draw_fern( level-1, apply_transform( f2, p ))
    draw_fern( level-1, apply_transform( f3, p ))
    draw_fern( level-1, apply_transform( f4, p ))

def draw_the_fern():
    draw_fern( 9, (0,0) )    
    
 

def draw_blade( i, s, t ) :
    x = i * 10 + 50
    dx = randint( -10, 10 )/10 + 2*t* (i - 15)
    #pygame.draw.line(screen, GREEN, [x, 100],[x+dx, 50], 3)
    shape = [[x-2,100],[x+2,100],[x+dx+s,50],[x+dx-s,50]]
    pygame.gfxdraw.aapolygon( screen, shape , GREEN)
    pygame.gfxdraw.filled_polygon( screen, shape , GREEN)

def draw_grass():
    # Clear the screen to grey
    screen.fill(GREY)
    pos = pygame.mouse.get_pos()
    for i in range(30):
        draw_blade(i, pos[0]/200,pos[1]/300 )

   
# The recursive function which calls itself.
# It calls itself twice, once for the left, once for the right.
def draw_curve( level, start, end, bend ):
    draw_blob( end, level )
    if level < 1 :
        return
    bend = bend/2
    split = ((start[0]+end[0])/2, (start[1]+end[1]-bend)/2);
    draw_curve( level-1,start,split,bend/2)
    draw_curve( level-1,split,end,bend/2)

def draw_the_curve():
    draw_curve( 6, (10,290), (390,190), 400 )


def intensity( time ):
    value = math.sin( math.radians( (3*time) %360)  )
    value = int(100 * value + 150);
    return value;
    
def colour( time ) :
    R = intensity( time * 1 )
    G = intensity( time * 1.3 )
    B = intensity( time * 1.5 )
    #G=R
    #B=R
    colour = ( R, G, B )
    print( colour )
    return colour


def show_colour( R, G, B ):
    print( "RGB colour values are R=", R, " G=", G, " B=",B )
    screen.fill( (R,G,B) )
    pygame.display.update()
    check_for_quit()
    input( "Press return for next colour..." )
    print()


def draw_all_colours() :
    time=0

    print("Black")
    show_colour( 0,0,0 )
    print("White")
    show_colour( 255,255,255 )
    print("Light Grey")
    show_colour( 200,200,200 )
    print("Dark Grey")
    show_colour( 80,80,80 )
    print("Red")
    show_colour( 200,100,100 )
    print("Green")
    show_colour( 100,200,100 )
    print("Blue")
    show_colour( 100,100,200 )

    print("Now showing lots of colours...")

def draw_colour( RGB ):
    screen.fill( (RGB[0], RGB[1], RGB[2] ))
    pygame.display.update()
    pygame.time.wait( 20 )

def blend_colour( From, To ):
    for i in range(256):
        t = i/255
        RGB = [ From[j] + t * (To[j]-From[j]) for j in range(3)]
        draw_colour( RGB )

Colour = [0,0,0]

def next_colour2( name, RGB ):
    global Colour
    print( "Changing colour to ", name)
    print( " R:", RGB[0]," G:",RGB[1], " B:", RGB[2] )
    blend_colour( Colour, RGB )
    Colour = [ x for x in RGB]
    print( "Colour changed" )
    pygame.time.wait( 2000 )
    
def next_colour( name, RGB ):
    print( "Changing colour to ", name)
    print( " R:", RGB[0]," G:",RGB[1], " B:", RGB[2] )
    draw_colour( RGB )
    pygame.time.wait( 2000 )
        
def draw_the_colours():
    next_colour( "Black", [0,0,0] )
    next_colour( "White", [255,255,255] )
    next_colour( "Light Grey", [200,200,200] )
    next_colour( "DarkGrey", [80,80,80] )

    next_colour( "Red", [255,0,0] )
    next_colour( "Green", [0,255,0] )
    next_colour( "Blue", [0,0,255] )
    

#draw_once( draw_grass )
#draw_repeatedly( draw_grass )
#draw_once( draw_the_curve )
#draw_once( draw_the_fern )
#draw_all_colours()
draw_once(draw_the_colours)
