import tcod as libtcod

from input_handlers import handle_keys

###Main loop
def main():
    #define screen size
    screen_width = 80
    screen_height = 50
    
    #track player pos
    player_x = int(screen_width/2)
    player_y = int(screen_height/2)
    
    #define font
    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    
    ##create the screen
    #end argument is if fullscreen
    libtcod.console_init_root(screen_width, screen_height, 'libtcod tutorial revised', False)
    
    #create new console
    con = libtcod.console_new(screen_width, screen_height)
    
    ##player input
    #keyboard input
    key = libtcod.Key()
    #mouse input
    mouse = libtcod.Mouse()
    
    
    #game loop won't end until we close the screen
    while not libtcod.console_is_window_closed():
        
        #capture new events, ie user input
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        
        #colour of our player symbol
        libtcod.console_set_default_foreground(con, libtcod.white)
        
        #player symbol; console, x, y, char, background
        libtcod.console_put_char(con, player_x, player_y, '@', libtcod.BKGND_NONE)
        
        #blit it to console
        libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
        
        #this flushes to screen
        libtcod.console_flush()
        
        libtcod.console_put_char(con, player_x, player_y, ' ', libtcod.BKGND_NONE)
        
        action = handle_keys(key)
        
        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')
        
        if move:
            dx, dy = move
            player_x += dx
            player_y += dy
        
        if exit:
            return True
            
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
    
    
    
if __name__ == '__main__':
    main()
    