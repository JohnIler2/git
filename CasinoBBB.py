import tiles as Tiles   #Tiles class code
import maps as Maps     #Map class code
import random
import sys
import signal
import time
import winsound

def signal_handler(signal, frame):
    print("Ctrl-c pressed ... exiting.")
    sys.exit(0)

def delay_print(s):
   for c in s:
       sys.stdout.write(c)
       sys.stdout.flush()
       #ToDo: Uncomment line below for prod
       #time.sleep(0.03)

def CheckTimer():
    MinsInDayWhenGameStarted=TimerStart.tm_hour*60+TimerStart.tm_min
    TotalMinsSinceInGame=time.localtime(time.time()).tm_hour*60+time.localtime(time.time()).tm_min
    #print StartMinsInDay
    #print MinsInGame
    if TotalMinsSinceInGame-MinsInDayWhenGameStarted>30:
        return False    #More than 30 mins in game ... game over man!
    else:
        return True     #They still have time to play!

def GenerateMap(Len,Width,MandatoryTiles,FluffTiles,AvailableItems):
    MyMap=[]
    MyTile=Tiles.Tile
    for MyTile in FluffTiles:
        if MyTile.GetItem()!="":
            Print("Programming error, please remove '{}' from fluff tile '{}'".format(MyTile.GetItem(),MyTile.GetDescription()))
            sys.exit(1)
    for x in range(Len):
        MapRow=[]
        for y in range(Width):
            i=random.randint(0,len(FluffTiles)-1)
            MapRow.append(FluffTiles[i])
        MyMap.append(MapRow)

    for i in range(len(MandatoryTiles)):
        x=random.randint(0,Len-1)
        y=random.randint(0,Width-1)
        while True:
            if MyMap[x][y] in FluffTiles:
                #print("Placing mandatory tile '{}' at ({},{})".format(MandatoryTiles[i].GetDescription(),x,y))
                MyMap[x][y]=MandatoryTiles[i]
                break
            else:
                x=random.randint(0,Len-1)
                y=random.randint(0,Width-1)

    for i in range(len(AvailableItems)):
        x=random.randint(0,Len-1)
        y=random.randint(0,Width-1)
        while True:
            if MyMap[x][y].GetItem()=="":
                #print("Placing item '{}' at ({},{})".format(AvailableItems[i],x,y))
                MyMap[x][y].SetItem(AvailableItems[i])
                break
            else:
                x=random.randint(0,Len-1)
                y=random.randint(0,Width-1)
#Some debugging code
#    for x in range(Len):
#        for y in range(Width):
#            MyTile=Map[x][y]
#            print("Tile at {},{} (X,Y) is:".format(x,y))
#            MyTile.DisplayTile()

    return MyMap
    
def Bayrace():
    print("**** Ross' code goes here.")
    return True

def GulfScenario():
    print("**** Jeff's code goes here.")
    return True

def CasinoScenario():
    global Inventory
    global CasinoMap
    global MasterListOfItems

    JackpotCounter=0
    DisplayEvent=False
    EventText=""

    CurrentTile=CasinoMap.GetCurrentTile()

    delay_print("\nYou see a storm on the horizon and decide to hang out at the Casino until the storm passes.\n")
    delay_print("As you walk through the front doors you are greeted by the smell of smoke, booze, and crab legs from the buffet.\n\n")
    delay_print("You don't have much dough to gamble so you decide to explore the casino for a while. Move around the Casino and see if you can find all the items.\n")
    delay_print("P.S. Be careful not to gamble at the same table for too long... Good Luck!\n")

    while CheckTimer():
        #Jackpot event! (delayed jackpot after the user meets cowboy)
        if JackpotCounter>0:
            JackpotCounter -=1
            if JackpotCounter==0:
                print("*****************************")
                print("*****************************")
                print("****DING!DING!DING!DING!!****")
                print("*****************************")
                print("*****************************")
                print("\nWith a loud hoot you hear, 'Bout time I hit it big! YEEEE HAAAAWWWWW!!!!!!'")
        #Where the real code is ... Tells the user what they see at every tile.
        delay_print("******\nYou see {}.\n".format(CurrentTile.GetDescription()))

        #User options
        print("(I)nventory, (A)vailable Items, (L)ook Around, (C)heck watch, (G)amble")
        print("Movement Options: (N)orth, (S)outh, (W)est or (E)ast, e(X)it\n")
        
        #get user options and shift to uppercase
        UserSelection=raw_input("What would you like to do next?: ").upper()
        if UserSelection=="X":
            #ToDo: Check if they are at the dock, if now, print a message saying they take X times the number of spaces to get back?
            delay_print("You leave the Casino and head back to the docks.\n")
            return True     #Important! Routine needs to return True (keep playing) or False (game over)
        elif UserSelection=="I":
            if len(Inventory)==0:
                delay_print("You have nothing in your inventory.")
            else:
                delay_print("You are currently holding:\n {}".format(Inventory))
        elif UserSelection=="L":
            #Search the tile for an item
            UserSelection=raw_input("How many minutes would you like to search the area? ")
            if UserSelection==0 or UserSelection=="":
                delay_print("You decide not to spend time searching the current location.")
            else:
                #If there is an item and they searched longer than the "random time" (10-20)
                if (len(CurrentTile.GetItem()) == 0) or UserSelection<random.randint(10,20):
                    delay_print("You spend {} minutes searching the area and find nothing.".format(UserSelection))
                else:
                    #Add item found to inventory
                    Inventory.append(CurrentTile.GetItem())
                    delay_print("You spend {} minutes searching the area and find {}.".format(UserSelection,CurrentTile.GetItem()))
                    #Clear the item out of the tile
                    CurrentTile.SetItem("")
                    #Special casino code.  Only allow user to pick up $1000 if they found the lucky rabbit foot
                    if CurrentTile.GetEvent()=="$1000 Chip":
                        if Inventory.count("Lucky Rabbit Foot")==1:
                            delay_print("It's your lucky day!(must've been that lucky rabbit foot you found earlier)You snatch up the chip before anyone misses it.")
                            CurrentTile.SetDescription("empty floor")
                        else:
                            delay_print("But without a lucky rabbit foot, a blue-haired lady beats you to it and snatches it up! :(")
                            CurrentTile.SetDescription("empty floor")

        elif UserSelection=="G":
            UserSelection=int(raw_input("How many minutes would you like to stay and gamble? "))
            if UserSelection==0 or UserSelection=="":
                delay_print("You decide not to gamble for now.")
            elif UserSelection<=10:
                delay_print("You spend {} minutes gambling and win ${}. Congrats!".format(UserSelection,random.randint(10,30)))
            elif UserSelection<=25:
                delay_print("You spend {} minutes gambling and lose ${}.".format(UserSelection,random.randint(10,20)))
            elif UserSelection<=30:
                delay_print("You spend {} minutes gambling and win $100! Congrats!".format(UserSelection))
            elif UserSelection<=59:
                delay_print("You spend {} minutes gambling and lose ${}.".format(UserSelection,random.randint(5,10)))
            elif UserSelection>=60:
                delay_print("You gambled too long and should've quit when you were ahead! You lose all your money and head back to the dorm disheartened...")
                return False
        #User wants to check their watch.
        elif UserSelection=="C":
            CheckWatch()
        #User wants to move
        elif UserSelection in ["N","S","E","W"]:
            OriginalTile=CurrentTile
            CurrentTile=CasinoMap.Move(UserSelection)
            #If they are at a border, the code will return same tile back.  Need to check if we moved.
            if CurrentTile!=OriginalTile:
            #ToDo: Check for special events on new tile
                if CurrentTile.GetEvent()=="Cowboy":
                    DisplayEvent=True
                    EventText=""
                    #Set a timer flag to go off in "3-5" moves
                    JackpotCounter=random.randint(3,5)
                #print MyMap.DisplayMap()
                #print MyTile.DisplayTile()
        elif UserSelection == "A":
            print("\nYou currently have found {} of {} items.  Here is a list of all the items in the game:".format(len(Inventory),len(MasterListOfItems)))
            OutputString=""
            print MasterListOfItems
            for i in range(0,len(MasterListOfItems)):
                if i%5==0:
                    if OutputString=="":
                        OutputString=MasterListOfItems[i]
                    else:
                        OutputString+=",\n"+MasterListOfItems[i]
                else:
                    OutputString+=","+MasterListOfItems[i]
        else:
            print("'{}' is an invalid selection.".format(UserSelection))
            
def RiverScenario():
    #ToDo: I don't like how the text is scrolling.  Work on newlines and other BS ...
    #Get access to the global variables
    global Inventory
    global RiverMap
    #ToDo:Need this in everyone's code!
    global MasterListOfItems

    #Special variables to handle some "river events"
    DynamiteCounter=0
    DisplayEvent=False
    EventText=""

    CurrentTile=RiverMap.GetCurrentTile()

    delay_print("\nYou decide to take a trip down the river.  A storm is on the horizon, but is 'supposed' to clear soon.\n")
    delay_print("blah,blah ... (storyline) ...\n\n")

    while CheckTimer():
        #Each scenario needs to keep track of time and curfew busts!!!

        #"Dynamite fishing event! (delayed explosion after the user finds the fisherman
        if DynamiteCounter>0:
            DynamiteCounter -=1
            if DynamiteCounter==0:
                print("*****************************")
                print("*****************************")
                print("******BOOOOOOOOMMMMMM!!******")
                print("*****************************")
                print("*****************************")
                print("\nWith a loud cackle you hear, 'Dats what I call fishing!!!!!!'")
        #Where the real code is ... Tells the user what they see at every tile.
        delay_print("******\nYou see {}.\n".format(CurrentTile.GetDescription()))

        #Ran into a problem ... I needed my event code to print AFTER the "tile code"
        if DisplayEvent:
            delay_print(EventText)
            DisplayEvent=False
        #User options
        print("(I)nventory, (L)ook around, (F)ish, (C)heck watch, move (N)orth, (S)outh, (E)ast or (W)est, e(X)it")
        #get user options and shift to uppercase
        UserSelection=raw_input("What would you like to do next?: ").upper()
        if UserSelection=="X":
            #ToDo: Check if they are at the dock, if now, print a message saying they take X times the number of spaces to get back?
            delay_print("You return to the dock and are safely back on shore.\n")
            return True     #Important! Routine needs to return True (keep playing) or False (game over)
        elif UserSelection=="I":
            if len(Inventory)==0:
                delay_print("You have nothing in your inventory.")
            else:
                delay_print("You are currently holding:\n {}".format(Inventory))
        elif UserSelection=="L":
            #Search the tile for an item
            UserSelection=int(raw_input("How many minutes would you like to search the area? "))
            if UserSelection==0:
                delay_print("You decide not to spend time searching the current location.")
            else:
                #If there is an item and they searched longer than the "random time" (5-10)
                if (len(CurrentTile.GetItem()) == 0) or UserSelection<random.randint(5,10):
                    delay_print("You spend {} minutes searching the area and find nothing.".format(UserSelection))
                else:
                    #Add item found to inventory
                    Inventory.append(CurrentTile.GetItem())
                    delay_print("You spend {} minutes searching the area and find {}.".format(UserSelection,CurrentTile.GetItem()))
                    #Clear the item out of the tile
                    CurrentTile.SetItem("")
                    #Special river code.  Only allow user to catch snake if they found the fishing net
                    if CurrentTile.GetEvent()=="Snake":
                        if Inventory.count("fishing net")==1:
                            delay_print("You capture the snake with your fishing net.")
                            CurrentTile.SetDescription("baby snakes in the water looking for their mother")
                        else:
                            #ToDo?: Make it random to see if they get bit?   For now ... BITE EM! =)
                            delay_print("Without a net, you get bit by the snake and need to go to the hospital!")
                            return False
                    #Net event
                    elif CurrentTile.GetEvent()=="Net":
                        #Soon as they get the net, change the tile description (don't want it to say their is a shiny surface without the shiny net there
                        CurrentTile.SetDescription("water with a surface not as shiny as earlier")
        elif UserSelection=="F":
            #ToDo?  Make fishing so it isn't a waste of time????
            UserSelection=int(raw_input("How many minutes would you like to stay and fish? "))
            if UserSelection==0:
                delay_print("You decide not skip fishing for now.")
        #User wants to check their watch.
        elif UserSelection=="C":
            CheckWatch()
        #User wants to move
        elif UserSelection in ["N","S","E","W"]:
            OriginalTile=CurrentTile
            CurrentTile=RiverMap.Move(UserSelection)
            #If they are at a border, the code will return same tile back.  Need to check if we moved.
            if CurrentTile!=OriginalTile:
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
            
def Welcome():
    print("**** Welcome Information code goes here.\n\n")

def CheckWatch():
    NumberOfSecondsWhenGameStarted=(TimerStart.tm_hour*60+TimerStart.tm_min)*60+TimerStart.tm_sec
    TotalSecondsSinceInGame=time.localtime(time.time()).tm_hour*3600+time.localtime(time.time()).tm_min*60+time.localtime(time.time()).tm_sec
    TotalSecondsPlayed=TotalSecondsSinceInGame-NumberOfSecondsWhenGameStarted
    if TotalSecondsPlayed<60:
        print("You have been playing for {} seconds.".format(TotalSecondsPlayed))
    elif TotalSecondsPlayed==60:
        print("You have been playing for 1 minute.")
    else:
        if(TotalSecondsPlayed>119):
            PutAnSOnMinutes="s"
        else:
            PutAnSOnMinutes=""
        if(TotalSecondsPlayed%60):
            if TotalSecondsPlayed%60==1:
                print("You have been playing for {} minute{} and 1 second.".format(TotalSecondsPlayed/60,PutAnSOnMinutes))
            else:
                print("You have been playing for {} minute{} and {} seconds.".format(TotalSecondsPlayed/60,PutAnSOnMinutes,TotalSecondsPlayed%60))
        else:
            print("You have been playing for {} minute{}.".format(TotalSecondsPlayed/60,PutAnSOnMinutes))
    return TotalSecondsPlayed

def DisplayLeaderBoard():
    global MasterListOfItems
    global Inventory

    TimeSpent=""

    TotalSecondsPlayed=CheckWatch()

    if TotalSecondsPlayed<60:
        TimeSpent=str(TotalSecondsPlayed)+" seconds"
    elif TotalSecondsPlayed==60:
        TimeSpent="1 minute"
    else:
        if(TotalSecondsPlayed>119):
            PutAnSOnMinutes="s"
        else:
            PutAnSOnMinutes=""
        if(TotalSecondsPlayed%60):
            TimeSpent=str(TotalSecondsPlayed/60)+" minute"+PutAnSOnMinutes
        else:
            if TotalSecondsPlayed%60==1:
                TimeSpent=str(TotalSecondsPlayed/60)+" minute"+PutAnSOnMinutes+" and 1 second"
            else:
                TimeSpent=str(TotalSecondsPlayed/60)+" minute"+PutAnSOnMinutes+" and "+str(TotalSecondsPlayed%60)+" seconds"

    print("It took you {} to find {} out of {} items in the game.".format(TimeSpent,len(Inventory),len(MasterListOfItems)))
    
#Start Real Program
#Variables everything needs access to
MasterListOfItems=[]    #List of all items in the game
Inventory=[]            #Inventory of items user found
TimerStart=time.localtime(time.time())

#handler code to grab Ctrl-C
signal.signal(signal.SIGINT, signal_handler)

#    ************************** River specific code start **************************
#One time setup of the scenario map variables
RiverMap=[]         #This is the scenario map which holds all the tiles
RiverTiles=[]       #Important tiles, will be randomized over the map.  (Only placed once)
RiverFluffTiles=[]  #"filler tiles" to populate around the "real scenario tiles".  (Can appear multiple times)
RiverAvailableItems=["Gold Coin","Fishing Hook","Wrench"]   #Available items which can be placed randomly over the map.
#These are the important scenario tiles.  Put your items and events here.
#Usage:Tiles.Tile("Tile description",ignore this field, pass a number,"name of an event you can test for and act on","name of item which can be found on tile"
RiverTiles.append(Tiles.Tile("a pool of floating fish",1,"","a nearly-dead fish"))
RiverTiles.append(Tiles.Tile("someone fishing in a boat",1,"Fisherman",""))
RiverTiles.append(Tiles.Tile("river Tile 2",1,"",""))
RiverTiles.append(Tiles.Tile("a snake in the water",1,"Snake","a dead snake"))
RiverTiles.append(Tiles.Tile("water with a shiny surface",1,"Net","fishing net"))
RiverTiles.append(Tiles.Tile("river Tile 4",1,"","old lure"))
RiverTiles.append(Tiles.Tile("river Tile 5",1,"","torn shirt")) 
#These are the filler scenario tiles.  Don't put items here.  You can do it separately when the GenerateMap() code is called  You can put events here.
RiverFluffTiles.append(Tiles.Tile("clear, open water",0,"",""))
RiverFluffTiles.append(Tiles.Tile("blue water",0,"",""))
RiverFluffTiles.append(Tiles.Tile("beautiful, blue water",0,"",""))
RiverFluffTiles.append(Tiles.Tile("slightly, murky water",0,"",""))
#Generate the scenario map!
RiverMap=GenerateMap(5,5,RiverTiles,RiverFluffTiles,RiverAvailableItems)
#ToDo:Need this in everyone's code!
#Setup the default map
RiverMap=Maps.Map(RiverMap,5,5,"The river bank is too steep to exit here!")
MasterListOfItems+=RiverMap.GetItems()
#print "John"
#print MasterListOfItems
#    **************************  River specific code end  **************************

#    ************************** Casino specific code start **************************
CasinoMap=[]         #This is the scenario map which holds all the tiles
CasinoTiles=[]       #Important tiles, will be randomized over the map.  (Only placed once)
CasinoFluffTiles=[]  #"filler tiles" to populate around the "real scenario tiles".  (Can appear multiple times)
CasinoAvailableItems=["Dice","Craps Stick","Marked Deck","Crab Leg","Lucky Rabbit Foot"]   #Available items which can be placed randomly over the map.
#Usage:Tiles.Tile("Tile description",ignore this field, pass a number,"name of an event you can test for and act on","name of item which can be found on tile"
CasinoTiles.append(Tiles.Tile("people sitting near a sparkling stone fountain tossing coins into it.",1,"","a shiny penny"))
CasinoTiles.append(Tiles.Tile("a large man in a Stetson rolling dice onto a table. He says, 'Ya better know what you're doin' if ya want to win it big in this casino!'\n",1,"Cowboy",""))
CasinoTiles.append(Tiles.Tile("a slender waitress holding a tray of drinks",1,"","old ticket stub"))
CasinoTiles.append(Tiles.Tile("a beautiful lady descending a steep spiral staircase. You hear cat calls from the direction of a table of bikers",1,"","bow tie"))
CasinoTiles.append(Tiles.Tile("formally dressed VIPs gliding over a polished floor. A group of older people stand conversing nearby",1,"$1000 Chip","$1000 Chip"))
CasinoTiles.append(Tiles.Tile("an elderly lady playing the slots. She shoves a coin into the machine and yanks the lever. After the reels come to a stop, you see her frown and then shove another coin in.",1,"",""))
CasinoFluffTiles.append(Tiles.Tile("beautiful, bright paisley carpet under a long craps table",0,"",""))
CasinoFluffTiles.append(Tiles.Tile("luxurious, kaleidoscopic floral carpet. A waitress balances a tray full of drinks nearby",0,"",""))
CasinoFluffTiles.append(Tiles.Tile("beautiful, bright paisley carpet under a long craps table",0,"",""))
CasinoFluffTiles.append(Tiles.Tile("worn, stained carpeting. Rows of Video Poker and slot machines stand off to the side",0,"",""))
CasinoFluffTiles.append(Tiles.Tile("clean, tiled floor. People are crowded around the blackjack tables nearby",0,"",""))

#Generate the scenario map!
print("ignore 1")
CasinoMap=GenerateMap(5,5,CasinoTiles,CasinoFluffTiles,CasinoAvailableItems)
print("ignore 2")
CasinoMap=Maps.Map(CasinoMap,5,5,"\nWARNING: You ran into the Casino wall!\n")
print("ignore 3")
MasterListOfItems+=CasinoMap.GetItems()
#print "Ethan"
#print MasterListOfItems
#    **************************  Casino specific code end  **************************

#shell code (or copy the above river code to start your scenario)
#Map=[]
BayMap=[]
BayTiles=[]
BayFluffTiles=[]
#(uncomment after you build tiles) - BayMap=GenerateMap(Len,Width,BayTiles,BayFluffTiles,AvailableItems)

#shell code (or copy the above river code to start your scenario)
GulfMap=[]
GulfTiles=[]
GulfFluffTiles=[]
#(uncomment after you build tiles) - GulfMap=GenerateMap(Len,Width,GulfTiles,GulfFluffTiles,AvailableItems)


#One-time "intro" to tell the player what is going on ...
#ToDo:Get code from Jeff
Welcome()

#Flag to watch in the loop to see if they are still playing
StillPlaying=True

#This is the main driver of the game.
while(StillPlaying and CheckTimer()):
    #All "scenario" adventures must return a "StillPlaying" result.  i.e. If they drowned in the ocean, the BayCode would return False (no longer playing)
    #ToDo:Check if len of inventory==MasterListOfItems, if so, quit.
    #ToDo:Check watch code return value(s) so leaderboard can call it?
    
    delay_print("blah, blah (storyline) ... \n")
    print("(B)ay Race (C)asino (G)ulf (R)iver (X)bar (Q)uit")
    UserSelection=raw_input("What would you like to do next? ").upper()
    if UserSelection == "B":
        StillPlaying=Bayrace()
    elif UserSelection == "G":
        StillPlaying=GulfScenario()
    elif UserSelection == "R":
        StillPlaying=RiverScenario()     
    elif UserSelection == "C":
        StillPlaying=CasinoScenario()
    elif UserSelection == "X":
        TimeWaster=raw_input("How many drinks would you like to have at Billy Bob's Bangin Bar? ")
        TimeWaster=int(TimeWaster)
        if TimeWaster==0:
            delay_print("Probably a good idea.\nYou leave the bar.")
        elif TimeWaster==1:
            delay_print("After a quick drink, you leave the bar for more adventures!")
        elif TimeWaster<3:
            delay_print("You spend a good amount of time at the bar, but decide to leave, finding nothing more than a slight headache.")
        else:
            StillPlaying=False
            delay_print("You lose track of time and bust curfew!")
    elif UserSelection == "Q":
        StillPlaying=False
        #sys.exit(0) #Leaderboard entry?  For now, no ...
    else:
        delay_print("That option isn't available ... yet!\n")

DisplayLeaderBoard()




