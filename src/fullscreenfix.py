import os
import pygame

pygame.init()

# find out & store desktopSize
pgdi=pygame.display.Info()
desktopSize=(pgdi.current_w, pgdi.current_h)

FPS = 100
clock = pygame.time.Clock()

screenWidth=800 # initial screen width when windowed
screenHeight=600

hor=0 # ball position on screen 
ver=0

# will make the first intance of the window appear in the middle of the screen.
# (consecutive instances will appear in the upper most left corner)
os.environ['SDL_VIDEO_CENTERED'] = '1' 

# flag to keep track of the question: is the window maximized or not
# should remain False at startup
maximized=False 

# choose to startup fullscreen or not.
# both options will work fine
isFullScreen=True 

# set up initial display:

# always make the non-fullscreen screen first, 
# so the fullscreen has something to toggle back to that is placed properly (as in not at 0,0 )
screen = pygame.display.set_mode((screenWidth,screenHeight), pygame.RESIZABLE) 

if isFullScreen:
    # set size to desktop 
    # not doing this takes much longer (about 4 seconds)
    # but doing this is near instantanious
    pygame.display.set_mode(desktopSize, pygame.RESIZABLE) 
    
    pygame.display.toggle_fullscreen() # now toggle fullscreen


done=False
while not done:
    for event in pygame.event.get():        
        if event.type == pygame.QUIT: 
            # like ctrl-break or the cross in the title bar
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q: 
            # pressing q will also quit the program
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            # pressing f will toggle fullscreen
            
            isFullScreen=not isFullScreen # toggle fullscreen flag
            if isFullScreen: #toggling from not fullscreen to fullscreen
                if maximized: # abort 
                    # toggling from maximized to fullscreen gives a warning:
                    # Warning: re-creating window in toggle_fullscreen      
                    # then fail to function properly, giving back a large window that cannot be resized. 
                    # so, we abort this (till we know a better solution)
                    print('cannot toggle from maximized to fullscreen?')
                    isFullScreen=not isFullScreen # restore fullscreen flag
                else:
                    # store size of windowed screen 
                    # so we can reset it when toggling back
                    screenWidth=screen.get_width()
                    screenHeight=screen.get_height()

                    #print("Correct")

                    # set the number of pixels to desktop size
                    pygame.display.set_mode(desktopSize, pygame.RESIZABLE) 
                    # then toggle that to fullscreen                
                    pygame.display.toggle_fullscreen()                    
                    
            else: # toggling from fullscreen to not fullscreen
                pygame.display.toggle_fullscreen() 
                # restore to old size
                pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)
                
        # this is done to keep track of the question: 'is the window maximized or not':
        elif event.type ==pygame.WINDOWEVENT:
            if event.event == pygame.WINDOWEVENT_MAXIMIZED:
                maximized=True 
            elif event.event == pygame.WINDOWEVENT_MINIMIZED:
                maximized=False
            elif event.event == pygame.WINDOWEVENT_RESTORED:
                maximized=False
    
    # show some things on screen:        
    
    # paint background
    screen.fill((255, 0, 255))

    # slide ball position
    hor += 1
    hor = hor % screen.get_width()
    ver += hor % 2
    ver = ver % screen.get_height()
    
    # paint ball
    pygame.draw.circle(screen, (255, 255, 255), (hor, ver), 5)
        
    pygame.display.flip()
    clock.tick(FPS)