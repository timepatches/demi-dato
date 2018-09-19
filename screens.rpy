Okay! So here's the sitch:
I designed the game menu and the in-game menu to be very different visually (which sounded like a great idea at the time). I was trying to implement them as two separate menus - as opposed to how renpy usually uses one with a few if statements for the main menu - with two separate navigation screens that they draw from, but this proved to be a lot harder than I anticipated :sweat_smile: 
I'm uploading thumbnails of what the menus are supposed to look like, and here's what my code looks like so far (throws up a lot of exceptions obviously):

Let me know what you think! I honestly have no idea where this ranges on a scale of "really dumb and probably impossible" and "actually pretty easy but i don't know what mistakes i'm making" lol
screen main_menu:
    tag menu
    add "gui/main_menu.png"
    imagebutton auto "gui/ib_new_%s.png" action Start() xpos 0 ypos 0 focus_mask True
    imagebutton auto "gui/ib_load_%s.png" xpos 0 ypos 0 focus_mask True action ShowMenu('mm_load')
    imagebutton auto "gui/ib_settings_%s.png" xpos 0 ypos 0 focus_mask True action ShowMenu('mm_settings')
    imagebutton auto "gui/ib_gallery_%s.png" xpos 0 ypos 0 focus_mask True action ShowMenu('mm_gallery')
    imagebutton auto "gui/ib_quit_%s.png" xpos 0 ypos 0 focus_mask True action Quit(confirm=False)
      ## this all works fine, but as soon as it goes to navigate to mm_settings (for example) ren'py crashes
            my hunch is that "settings" as a label (ditto for the other menu labels) does something special and that ren'py doesn't
            know what to do with a customised version but i don't really know what i'm talking about lmao
  #mm_navigation & qm_navigation: my plan was to have ren'py draw its navigation from these two separate screens, instead of screen_navigation
    like it does in vanilla ren'py code, but i don't know how to do that
  
  
screen mm_navigation():
    add "gui/mm_nav_full.png"
    imagebutton auto "gui/ib_new_%s.png" action Start() xpos -181 ypos 0 focus_mask true
    imagebutton auto "gui/ib_load_%s.png" xpos -181 ypos 0 focus_mask True action ShowMenu('mm_load')
    imagebutton auto "gui/ib_settings_%s.png" xpos -181 ypos 0 focus_mask True action ShowMenu('mm_settings')
    imagebutton auto "gui/ib_gallery_%s.png" xpos -181 ypos 0 focus_mask True action ShowMenu('mm_gallery')
    imagebutton auto "gui/ib_quit_%s.png" xpos -181 ypos 0 focus_mask True action Quit(confirm=False)
        ##possibly mess with xpos?? to achieve proper horizontal positions

screen mm_settings():
    tag menu
    add "gui/mm_settings_headers.png" ##ADD TRANSITION LATER
    use mm_navigation
    #imagebuttons

#screen mm_load:
    #tag menu
    #use mm_navigation
    #probably a "file_slot" screen inserted in here like in vanilla renp'y

##    >the elements on the right hand side of the screen for loading and stuff
    #(borrow from vanilla code here)
        #>save MM and QM are actually laid out exactly the same so i'll copy the code over
        #    (differing xpos and ypos tho so either change this or alter the image files depending on how this code actually works)
            #*this is actually true for all the screens in mm vs qm, the layout is the same it's just in a different position
