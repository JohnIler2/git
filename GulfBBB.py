def GulfScenario():
    #ToDo: I don't like how the text is scrolling.  Work on newlines and other BS ...
    #Get access to the global variables
    global TimeSpent
    global Inventory
    global GulfMap

    #Special variables to handle some "gulf events"
    DynamiteCounter=0
    DisplayEvent=False
    EventText=""

    #Setup the default map
    GulfMap=Maps.Map(GulfMap,5,5,"The gulf is too deep to exit here!")
    CurrentTile=GulfMap.GetCurrentTile()
    
    print("\nYou decide to take a trip out to the Gulf of Mexico.")
    print("blah,blah ... (storyline) ...\n\n")

    while True:
        #ToDo: Check the time versus curfew.  Busted?
        #Each scenario needs to keep track of time and curfew busts!!!

        #"Dynamite fishing event! (delayed explosion after the user finds the fisherman
        if DynamiteCounter>0:
            DynamiteCounter -=1
            if DynamiteCounter==0:
                print(""" ____/ (  (    )   )  \___
                         /( (  (  )   _    ))  )   )\
                       ((     (   )(    )  )   (   )  )
                     ((/  ( _(   )   (   _) ) (  () )  )
                    ( (  ( (_)   ((    (   )  .((_ ) .  )_
                   ( (  )    (      (  )    )   ) . ) (   )
                  (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
                  ( (  (   ) (  )   (  ))     ) _)(   )  )  )
                 ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )
                  (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
                 ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
                  ((  (   )(    (     _    )   _) _(_ (  (_ )
                   (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
                   ((__)        \\||lll|l||///          \_))
                            (   /(/ (  )  ) )\   )
                          (    ( ( ( | | ) ) )\   )
                           (   /(| / ( )) ) ) )) )
                         (     ( ((((_(|)_)))))     )
                          (      ||\(|(|)|/||     )
                        (        |(||(||)||||        )
                          (     //|/l|||)|\\ \     )
                        (/ / //  /|//||||\\  \ \  \ _)
-------------------------------------------------------------------------------"""
                print("\nWith a loud cackle you hear, 'Dats what I call fishing!!!!!!'")
        #Where the real code is ... Tells the user what they see at every tile.
        print("******\nYou see {}.\n".format(CurrentTile.GetDescription()))

        #Ran into a problem ... I needed my event code to print AFTER the "tile code"
        if DisplayEvent:
            print EventText
            DisplayEvent=False
        #User options
        print("(I)nventory, (L)ook around, (F)ish, (C)heck watch, move (N)orth, (S)outh, (E)ast or (W)est, e(X)it")
        #get user options and shift to uppercase
        UserSelection=raw_input("What would you like to do next?: ").upper()
        if UserSelection=="X":
            #ToDo: Check if they are at the dock, if now, print a message saying they take X times the number of spaces to get back?
            print("You return to the dock and are safely back on shore.\n")
            return True     #Important! Routine needs to return True (keep playing) or False (game over)
        elif UserSelection=="I":
            if len(Inventory)==0:
                print("You have nothing in your inventory.")
            else:
                print("You are currently holding:\n {}".format(Inventory))
        elif UserSelection=="L":
            #Search the tile for an item
            UserSelection=int(raw_input("How many minutes would you like to search the area? "))
            if UserSelection==0:
                print("You decide not to spend time searching the current location.")
            else:
                #Add the number of minutes searching to the curfew clock
                TimeSpent+=UserSelection
                #If there is an item and they searched longer than the "random time" (5-10)
                if (len(CurrentTile.GetItem()) == 0) or UserSelection<random.randint(5,10):
                    print("You spend {} minutes searching the area and find nothing.".format(UserSelection))
                else:
                    #Add item found to inventory
                    Inventory.append(CurrentTile.GetItem())
                    print("You spend {} minutes searching the area and find {}.".format(UserSelection,CurrentTile.GetItem()))
                    #Clear the item out of the tile
                    CurrentTile.SetItem("")
                    #Special river code.  Only allow user to catch snake if they found the fishing net
                    if CurrentTile.GetEvent()=="Shark!":
                        if Inventory.count("fishing net")==1:
                            print("You capture the snake with your fishing net.")
                            CurrentTile.SetDescription("baby snakes in the water looking for their mother")
                        else:
                            #ToDo?: Make it random to see if they get bit?   For now ... BITE EM! =)
                            print("Without a net, you get bit by the snake and need to go to the hospital!")
                            return False
                    #Net event
                    elif CurrentTile.GetEvent()=="Net":
                        #Soon as they get the net, change the tile description (don't want it to say their is a shiny surface without the shiny net there
                        CurrentTile.SetDescription("water with a surface not as shiny as earlier")
        elif UserSelection=="F":
            #ToDo?  Make fishing so it isn't a waste of time????
            UserSelection=int(raw_input("How many minutes would you like to stay and fish? "))
            if UserSelection==0:
                print("You decide not skip fishing for now.")
            else:
                TimeSpent+=UserSelection
        #User wants to check their watch.
        elif UserSelection=="C":
            CheckWatch()
        #User wants to move
        elif UserSelection in ["N","S","E","W"]:
            OriginalTile=CurrentTile
            CurrentTile=GulfMap.Move(UserSelection)
            #If they are at a border, the code will return same tile back.  Need to check if we moved.
            if CurrentTile!=OriginalTile:
                #If they moved tiles, add three minutes to their timer.  Too much?
                TimeSpent+=3
                #ToDo: Check for special events on new tile
                if CurrentTile.GetEvent()=="Fisherman":
                    DisplayEvent=True
                    EventText="She says, 'You better have the right bait if you want to catch fish in this river!'\n"
                    #Set a timer flag to go off in "3-10" moves
                    DynamiteCounter=random.randint(3,10)
                #print MyMap.DisplayMap()
                #print MyTile.DisplayTile()

        else:
            print("'{}' is an invalid selection.".format(UserSelection))
