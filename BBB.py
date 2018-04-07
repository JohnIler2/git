#This is almost ready (To be utilized with the walk through document)s
import tiles as Tiles   #Tiles class code
import maps as Maps     #Map class code
import random
import sys
import signal
import time

#ToDo on everyone's code:
#Delete everyone's timespent variables.
#Check and see if everyone has "while CheckTimer()":
#MasterListOfItems+=RiverMap.GetItems() to everyones "map/tile area
#Move map setup and inventory population outside everyone's functions
#ToDo:
#Add "storyline" in the "nebulus starting area."
#ToDo(Jeff):
#Welcome()

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
    print("**** Ethan's code goes here.")
    return True

def MyRiverScenario():
    #ToDo: I don't like how the text is scrolling.  Work on newlines and other BS ...
    #Get access to the global variables
    global Inventory
    global MyRiverMap
    #ToDo:Need this in everyone's code!
    global MasterListOfItems

    #Special variables to handle some "river events"
    DynamiteCounter=0
    DisplayEvent=False
    EventText=""

    CurrentTile=MyRiverMap.GetCurrentTile()

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
                    delay_print("You spend {} minutes searching the area and find nothing special.".format(UserSelection))
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
            CurrentTile=MyRiverMap.Move(UserSelection)
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
        if TotalSecondsPlayed==1:
            print("\nYou have been playing for 1 second.")
        else:
            print("\nYou have been playing for {} seconds.".format(TotalSecondsPlayed))
    elif TotalSecondsPlayed==60:
        print("\nYou have been playing for 1 minute.")
    else:
        if(TotalSecondsPlayed>119):
            PutAnSOnMinutes="s"
        else:
            PutAnSOnMinutes=""
        if(TotalSecondsPlayed%60):
            if TotalSecondsPlayed%60==1:
                print("\nYou have been playing for {} minute{} and 1 second.".format(TotalSecondsPlayed/60,PutAnSOnMinutes))
            else:
                print("\nYou have been playing for {} minute{} and {} seconds.".format(TotalSecondsPlayed/60,PutAnSOnMinutes,TotalSecondsPlayed%60))
        else:
            print("\nYou have been playing for {} minute{}.".format(TotalSecondsPlayed/60,PutAnSOnMinutes))
    return TotalSecondsPlayed

def GetPlayerName():
    while True:
        PlayerName=raw_input("Please enter your name for the leaderboard: ")
        if PlayerName=="":
            print("Not adding you to the leaderboard ... now")
            sys.exit(0)
        if PlayerName.find(",")!=-1:
            print("No commas in your file name.")
        else:
            break
    return PlayerName

def DisplayLeaderBoard():
    global MasterListOfItems
    global Inventory
    global Leaders
    global LeaderboardFile

    TimeSpent=""

    TotalSecondsPlayed=CheckWatch()

    if TotalSecondsPlayed<60:
        if TotalSecondsPlayed==1:
            TimeSpent="1 second"
        else:
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

    #print("It took you {} to find {} out of {} items in the game.".format(TimeSpent,len(Inventory),len(MasterListOfItems)))

    try:
        FileHandle = open(LeaderboardFile, 'w+')
    except:
        print("Unable to open the leaderboard file '{}'.\nYour score won't be saved.".format(LeaderboardFile))
        sys.exit(1)

    TiedItemsScoreFlag=False
    NewLeaders=[]
    #print("Current Player's Time => '{}'".format(TotalSecondsPlayed))
    for i in range(0,len(Leaders)):
        Player=Leaders[i][0]
        ItemsFound=int(Leaders[i][1])
        TimePlayed=Leaders[i][2]
        SecondsPlayed=int(Leaders[i][3])
        #print("Current Player's Time => '{}' Leader's Time => '{}'".format(TotalSecondsPlayed,SecondsPlayed))
        if len(Inventory)>ItemsFound:
            NewLeaders.append([GetPlayerName(),len(Inventory),TimeSpent,TotalSecondsPlayed])
            if i < 9:     #Don't add the last name back because (s)he dropped off the leader board
                NewLeaders.append(Leaders[i])
        elif len(Inventory)==ItemsFound:
            if (TiedItemsScoreFlag==False and (TotalSecondsPlayed<SecondsPlayed or TotalSecondsPlayed==SecondsPlayed)):
                NewLeaders.append([GetPlayerName(),len(Inventory),TimeSpent,TotalSecondsPlayed])
                TiedItemsScoreFlag=True
            if (i < 10 or (TiedItemsScoreFlag==False and i<9)):     #Don't add the last name back because (s)he dropped off the leader board
                NewLeaders.append(Leaders[i])            
        else:
            if i < 10:     #Don't add the last name back because (s)he dropped off the leader board
                NewLeaders.append(Leaders[i])            
        #print("Player => {}\nItems => {}\nTime => {}".format(Leaders[i][0],Leaders[i][1],Leaders[i][2]))
    if len(NewLeaders)==len(Leaders) and len(NewLeaders)<10:
        NewLeaders.append([GetPlayerName(),len(Inventory),TimeSpent,TotalSecondsPlayed])

    try:
        for i in range(0,len(NewLeaders)):
            FileHandle.writelines(NewLeaders[i][0]+","+str(NewLeaders[i][1])+","+NewLeaders[i][2]+","+str(NewLeaders[i][3])+"\n")
    except:
        print("Unable to write to leaderboard file '{}'.\nYour score won't be saved.".format(LeaderboardFile))
        sys.exit(1)

    FileHandle.close()

    #ToDo: Uncomment line below
    #print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("The Leader board:\n")
    print("{:20s}{:15s}{:25s}".format("Player Name","Items Found","Time Taken"))
    for i in range(0,len(NewLeaders)):
        print("{:20s}     {:10s}{:25s}".format(NewLeaders[i][0],str(NewLeaders[i][1]),str(NewLeaders[i][2])))

    
#Start Real Program
#Variables everything needs access to
MasterListOfItems=[]    #List of all items in the game
Inventory=[]            #Inventory of items user found
TimerStart=time.localtime(time.time())

#handler code to grab Ctrl-C
signal.signal(signal.SIGINT, signal_handler)

#    ************************** River specific code start **************************
#One time setup of the scenario map variables
MyRiverMap=[]         #This is the scenario map which holds all the tiles
MyRiverTiles=[]       #Important tiles, will be randomized over the map.  (Only placed once)
MyRiverFluffTiles=[]  #"filler tiles" to populate around the "real scenario tiles".  (Can appear multiple times)
MyRiverAvailableItems=["Gold Coin","Fishing Hook","Wrench"]   #Available items which can be placed randomly over the map.
#These are the important scenario tiles.  Put your items and events here.
#Usage:Tiles.Tile("Tile description",ignore this field, pass a number,"name of an event you can test for and act on","name of item which can be found on tile"
MyRiverTiles.append(Tiles.Tile("a pool of floating fish",1,"","a nearly-dead fish"))
MyRiverTiles.append(Tiles.Tile("someone fishing in a boat",1,"Fisherman",""))
MyRiverTiles.append(Tiles.Tile("MyRiver Tile 2",1,"",""))
MyRiverTiles.append(Tiles.Tile("a snake in the water",1,"Snake","a dead snake"))
MyRiverTiles.append(Tiles.Tile("water with a shiny surface",1,"Net","fishing net"))
MyRiverTiles.append(Tiles.Tile("river Tile 4",1,"","old lure"))
MyRiverTiles.append(Tiles.Tile("river Tile 5",1,"","torn shirt")) 
#These are the filler scenario tiles.  Don't put items here.  You can do it separately when the GenerateMap() code is called  You can put events here.
MyRiverFluffTiles.append(Tiles.Tile("clear, open water",0,"",""))
MyRiverFluffTiles.append(Tiles.Tile("blue water",0,"",""))
MyRiverFluffTiles.append(Tiles.Tile("beautiful, blue water",0,"",""))
MyRiverFluffTiles.append(Tiles.Tile("slightly, murky water",0,"",""))
#Generate the scenario map!
MyRiverMap=GenerateMap(5,5,MyRiverTiles,MyRiverFluffTiles,MyRiverAvailableItems)
#ToDo:Need this in everyone's code!
#Setup the default map
MyRiverMap=Maps.Map(MyRiverMap,5,5,"The river bank is too steep to exit here!")
MasterListOfItems+=MyRiverMap.GetItems()
#    **************************  River specific code end  **************************

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

#Leaderboard Setup Code
Leaders=[]
LeaderboardFile=".\\BBBLeaderBoard.lb"
Data=""
try:
    FileHandle = open(LeaderboardFile, 'r')
    print "File opened"
except:
    #File doesn't exist ... setup a "default leaderboard"
    print("Building a Leader board!")
    Leaders=[["Bella De Ball",10,"30 minutes",1800],["Billy Joe Bob",9,"29 minutes and 59 seconds",1799],["Cousin Vinnie",5,"29 minutes and 58 seconds",1798],["Barney Fife",4,"29 minutes and 57 seconds",1797],["Jethro",3,"29 minutes and 56 seconds",1796],["Crusty the Clown",2,"29 minutes and 55 seconds",1795],["Huck Finn",1,"29 minutes and 54 seconds",1794],["Major Tom",0,"29 minutes and 1 second",1741],["Young Tom Sawyer",0,"29 minutes and 53 seconds",1793]]
 
if len(Leaders)==0:
    try:
        while True:
            Data=FileHandle.readline().strip()
            if Data=="":
                break
            SplitData=Data.split(",")
            Leaders.append(SplitData)

        FileHandle.close()
    except:
        print("Unable to read leaderboard file '{}'.".format(LeaderboardFile))
        sys.exit(1)

#print("Leaders => '{}' Type => {}".format(Leaders,type(Leaders)))

#One-time "intro" to tell the player what is going on ...
#ToDo:Get code from Jeff
Welcome()

#Flag to watch in the loop to see if they are still playing
StillPlaying=True

#This is the main driver of the game.
while(StillPlaying and CheckTimer()):
    #All "scenario" adventures must return a "StillPlaying" result.  i.e. If they drowned in the ocean, the BayCode would return False (no longer playing)
    if (len(Inventory)==len(MasterListOfItems)):
        print("Congratulations!!! You found all of the items! GREAT JOB!!!!!")
        break
    delay_print("blah, blah (storyline) ... \n")
    print("Valid Options: (B)ay Race, (C)asino, (G)ulf, (R)iver, (V)isit a bar, show (A)vailable items or (Q)uit")
    UserSelection=raw_input("What would you like to do next? ").upper()
    if UserSelection == "A":
        print("\nYou currently have found {} of {} items.  Here is a list of all the items in the game:".format(len(Inventory),len(MasterListOfItems)))
        OutputString=""
        for i in range(0,len(MasterListOfItems)):
            if i%5==0:
                if OutputString=="":
                    OutputString=MasterListOfItems[i]
                else:
                    OutputString+=",\n"+MasterListOfItems[i]
            else:
                OutputString+=","+MasterListOfItems[i]

        print OutputString+"\n"
    elif UserSelection == "B":
        StillPlaying=Bayrace()
    elif UserSelection == "C":
        StillPlaying=CasinoScenario()
    elif UserSelection == "G":
        StillPlaying=GulfScenario()
    elif UserSelection == "R":
        StillPlaying=MyRiverScenario()
    elif UserSelection == "V":
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




