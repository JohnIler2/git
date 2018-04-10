#This is almost ready (To be utilized with the walk through document)s
import tiles as Tiles   #Tiles class code
import maps as Maps     #Map class code
import random
import sys
import signal
import time

#ToDo:
#Remove stub code
#Delete everyone's timespent variables.
#Check and see if everyone has "while CheckTimer()":
#MasterListOfItems+=RiverMap.GetItems() to everyones "map/tile area
#Move map setup and inventory population outside everyone's functions
#Leader board (in file?)  #of Turns, # of items found show top turns, show top items found?
#Welcome()
#Allow user to see items they can find "Bent fishing hook" might lead someone to go back into the bay until it is found?
#Graphics?/Images?
#Replace raw_input with a getch function?
#Sound?
#Make a "Must have" list for the guys???

#Ideas:
#Allow areas to be reentered (test)

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
           print("Programming error, please remove '{}' from fluff tile '{}'".format(MyTile.GetItem(),MyTile.GetDescription()))
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
            #MyMap[x][y].DisplayTile()
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
    
def BayraceScenario():
    #Get access to the global variables
    global Inventory
    global BayMap
    global MasterListOfItems
  

   
    #Setup the default map
    #BayraceScenario=Maps.Map(BayMap,5,5,"The bay water is choppy today.")
    CurrentTile=BayMap.GetCurrentTile()

    print("\nA You are looking forward to a day in the bay hunting alligators to make alligator jerky.\n\n")
    print("You also have a reputation as the fastest cajun in the bayou and have heard that local legend Swamp Racer is looking to race.\n\n")
    if Inventory.count("rifle")==0 and Inventory.count("lucky hat")==0:
        Inventory.append("rifle")
        Inventory.append("lucky hat")
        
    print ("You gather up your lucky hat and rifle from under the boat seat and head out to the bay for a day of alligator hunting.\n\n")
    while CheckTimer():
                     
        #Where the real code is ... Tells the user what they see at every tile.
        print(CurrentTile.GetDescription())

        if CurrentTile.GetItem()!= "":
            Inventory.append(CurrentTile.GetItem())
            print "You just picked up {}\n\n".format(CurrentTile.GetItem())
            #Clear the item out of the tile
            CurrentTile.SetItem("")

        #User options
        print("(I)nventory, (C)heck watch, move (N)orth, (S)outh, (E)ast or (W)est, (Q)uit")
        
        #get user options and shift to uppercase
        UserSelection=raw_input("What would you like to do next?: ").upper()
        if CurrentTile.GetEvent()== "race":
            if Inventory.count("prop") >0 and Inventory.count("moon shine")>0 and Inventory.count("lucky hat")>0:
                #If user has turbo prop & moon shine & lucky hat then user wins the race
                print "With all available items you win the Bayou Classic boat race"
            else:
                print "Without the turbo prop, moon shine, and lucky hat you head back to the docks in utter failure.\n\n"
        elif CurrentTile.GetEvent()== "marina":
            if Inventory.count("rifle") >0 and Inventory.count("lucky hat")>0:
                print "You have verified that your rifle and lucky hat are on-board the boat. You are ready to head out to the bay,\n\n"
            else:
                print "Without your rifle and lucky hat you will not be successful in hunting alligators.\n\n"
        elif CurrentTile.GetEvent()== "prop":
            if Inventory.count("prop") >0:
                print "You have found and collected a turbo prop.\n\n"
        elif CurrentTile.GetEvent()== "moon shine":
            if Inventory.count("moon shine") >0:
                print "You have found and collected a full bottle of moon shine.\n\n"
        elif CurrentTile.GetEvent()== "alligator":
            if Inventory.count("rifle") >0:
                print "With your rifle you are able to kill the alligator.\n\n"
###### START EVENT CODE!!!!
                #Special BayraceScenario code.  Only allow user to kill alligator if rifle is available
            if CurrentTile.GetEvent()=="alligator":
                        if Inventory.count("rifle")==1:
                            print("You shoot the alligator with your rifle.\n\n")
                            CurrentTile.SetDescription("Can't wait to make alligator jerky this weekend")
                        else:
                            #ToDo?: Make it random to see if they get bit?   For now ... BITE EM! =)
                            print("Without a rifle you get bit by the alligator and need to go to the hospital!\n\n")
                            return False
                    #Net event
        elif CurrentTile.GetEvent()=="race":
                        #Soon as they get the arm drop the race begins
                        CurrentTile.SetDescription("race start")
###### END EVENT CODE!!!!

			
        if UserSelection=="Q":
            #ToDo: Check if they are at the dock, if now, print a message saying they take X times the number of spaces to get back?
                print("You return to the dock and are safely back on shore.\n")
                
            #Important! Routine needs to return True (keep playing) or False (game over)
                return True     
        elif UserSelection=="I":
            if len(Inventory)==0:
                print("You have nothing in your inventory.\n")
            else:
                print("You are currently holding:\n {}\n".format(Inventory))

        #User wants to check their watch.
        elif UserSelection=="C":
            CheckWatch()
            
        #User wants to move
        elif UserSelection in ["N","S","E","W"]:
            OriginalTile=CurrentTile
            CurrentTile=BayMap.Move(UserSelection)
            
            #If they are at a border, the code will return same tile back.  Need to check if we moved.
            if CurrentTile!=OriginalTile:               
                #CurrentTile.SetDescription("New tile description.")  #good line to keep!!! (changes tile description)
                
                
                #ToDo: Check for special events on new tile
                if CurrentTile.GetEvent()=="Fisherman":
                    DisplayEvent=True
                    EventText="You better have the right bait if you want to catch fish in this river!'\n"
                    
                    #Set a timer flag to go off in "3-10" moves
                    DynamiteCounter=random.randint(3,10)
                    
                #print MyMap.DisplayMap()
                #print MyTile.DisplayTile()

        else:
            print("'{}' is an invalid selection.".format(UserSelection))

    return True

def GulfScenario():
    print("**** Jeff's code goes here.")
    return True

def CasinoScenario():
    print("**** Ethan's code goes here.")
    return True

def RiverScenario():

        print("'{}' is an invalid selection.")
            
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
    else:ilableItems=["Turbo Prop","Moon Shine","Wrench"]   #Available items which can be placed randomly over the map.
#These are the important scenario tiles.  Put your items and events here.
#Usage:Tiles.Tile("Tile description"
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

    print("Leaderboard code")
    
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
RiverFluffTiles.append(Tiles.Tile("clear, open water",0,"",""))
#Generate the scenario map!
RiverMap=GenerateMap(5,5,RiverTiles,RiverFluffTiles,RiverAvailableItems)
#ToDo:Need this in everyone's code!
#Setup the default map
RiverMap=Maps.Map(RiverMap,5,5,"The river bank is too steep to exit here!")
MasterListOfItems+=RiverMap.GetItems()

#    **************************  River specific code end  **************************
#    ************************** Bay specific code start **************************
#shell code (or copy the above river code to start your scenario)
BayMap=[]
BayTiles=[]
BayFluffTiles=[]
BayAvailableItems=["buoy"]   #Available items which can be placed randomly over the map.

#These are the important scenario tiles.  Put your items and events here.
#Usage:Tiles.Tile("Tile description",ignore this field, pass a number,"name of an event you can test for and act on","name of item which can be found on tile"

BayTiles.append(Tiles.Tile("You see Swamp Racer appear. With your luck hat and turbo prop you can win the race",5,"race",""))
#BayTiles.append(Tiles.Tile("You board your boat at the marina",5,"discover your rifle and lucky hat on-board","marina"))
BayTiles.append(Tiles.Tile("You see something shimmering in the water. It's a turbo prop",5,"pick up turbo prop","prop"))
BayTiles.append(Tiles.Tile("You see a floating trot line in the water with a moon shine bottle. Liquor is quicker",5,"collect moon shine bottle attached to trot line","moon shine"))
BayTiles.append(Tiles.Tile("You see an alligator near the shore line",5,"you shoot alligator with rifle and load into boat","alligator"))

#These are the filler scenario tiles.  Don't put items here.  You can do it separately when the GenerateMap() code is called  You can put events here.
BayFluffTiles.append(Tiles.Tile("You are in clear water",5,"",""))
BayFluffTiles.append(Tiles.Tile("You are in choppy water",5,"",""))

#Generate the scenario map!
BayMap=GenerateMap(5,5,BayTiles,BayFluffTiles,BayAvailableItems)
#Setup the default map
BayMap=Maps.Map(BayMap,5,5,"\nWARNING: You have reached the end of the bay map!!!! You are still in the same tile!!!!\n")
MasterListOfItems+=BayMap.GetItems()


#    **************************  Bay specific code end  ***********************


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
        StillPlaying=BayraceScenario()
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
        delay_print("That option isn't availabe ... yet!\n")

DisplayLeaderBoard()



