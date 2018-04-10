import tiles as Tiles   #Tiles class code
import maps as Maps     #Map class code
import random
import sys
import signal
import time
import string
import winsound

#winsound.PlaySound('eventlanding_popup_reward_won.wav', winsound.SND_FILENAME)
#winsound.PlaySound('SoundHelix-Song-8.mp3', winsound.SND_FILENAME)

#ToDo on everyone's code:
#ToDo "Scavenger hunt" in welcome()
#ToDo leaderboard bugx2 (name three times and too many lines)
#ToDo checkwatch bug (under a minute)
#ToDo: Infinite loop ...???
#ToDo: MasterListofItems bug
#Delete everyone's timespent variables.
#Check and see if everyone has "while CheckTimer()":
#MasterListOfItems+=RiverMap.GetItems() to everyones "map/tile area
#Move map setup and inventory population outside everyone's functions
#ToDo:
#Add "storyline" in the "nebulus starting area."

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
        print("\nYour 30 minute timer has expired!\n")
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
    #ToDo: I don't like how the text is scrolling.  Work on newlines and other BS ...
    #Get access to the global variables
    global MasterListOfItems
    global Inventory
    global GulfMap

    #Special variables to handle some "gulf events"
    WaveCounter=0
    DisplayEvent=False
    EventText=""

    CurrentTile=MyGulfMap.GetCurrentTile()

    delay_print("\nYou decide to take a trip out to the Gulf of Mexico.")
    
    while CheckTimer():
        #Each scenario needs to keep track of time and curfew busts!!!
       
        #"Wave event! (delayed explosion after the user finds the fisherman
        if WaveCounter>0:
            WaveCounter -=1
            if WaveCounter==0:
                print("""
****:***:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.::::::::::::::.:.::.::::::::::::::.:::::::::::::::::::::::::
****:::::::::::::::::::::::::::::::::::::::::::::::::::::..:::::::..:....::.::......:.::::...:::::..:..:..:..::.:::::::..:.:::::
***::::::::::::::::::::::::::::::...:::::.:::..:.:..........::::::.::...:.:.:..:.....::.:.........................:::::::...::::
**:::::I***I:::::::::::::::::::::::::::...:.::...:::....:.:.:My::::...:.....:............::......:::......:...:::...:::::::.::..::
*:::::::*I:*:::::::::::::::::::::::::::::**IV......I*:::::::::::::.::..::...:::.::::..:.........::::....::.....::.::::::.:::::::
**::::::IF:*:::::::::::::::::::::::I:............:::*:..*...:.:::...::..:.......:............:..:.....:.::.....:....:::..:::..::
***:*::::V.::::::::::::.........I...............:::...::I..I:::::.::..:................................:.:..:...:::....:::::.:::
*::::*:*:*:*:::::::::.......I...............II:I:II:...:.*...:.*..:..::..................................:.:::::::.:::::::::::::
*:::I:::.:.*::::.:::::...::........*:.:...I*.:I:*IIV:.::***I:I:::.::.::::................................:::::::::::::::::::::::
********::*::*::::::...I.........:**:*III:IIIFVFNF:*I..**::.:*.I*:::::...........................::::..:::::::::::::::.:::::::::
***VF*:****:*::::::::V.........**:*:.::NFFFIIFNNNNF..::*I:*.:.::::::.............:..............:::.::::::::::::::::::::::::::::
***IV***I:::*:::::V..........::.::*NF*FNNFFNNVFFFNNNV:::.I.*..:.....I:.**...................:....:::::::::::::::::::::::::::::::
*******I::****::::...........INFFN*FNNNVNNNNVFFNNVFIFV:II*::*:*..**I:*:.::......................::.:::::::::::::::::::::::::::::
****I***********.............INFFNFNNNVNNFNVNNNNVFNNNNN:..::.:*.::..I....*:........................:::::::::::::::::::::::::::::
*************V:...............:FNNVFNFVFNNINNFVFNNVNNFF*...I*.*II..::..:.I.I:............................:.:...:.....:::::::::::
II********VI:.:....................:I::NNFFFVFFNNFNIFVF:*.:*::::.::..*:II:..:::.:.:....................................:.:.:.:.:
FFFFFFVFV:::.:::....::I*......I...:II:VFNVNIFV:NFNFFF:......:.:*:I:..I:**I..:..................................................:
*IVV*::.:.:...::I:::I*:...:..::::V:..FNI.V*INFIFFFFF:.........:I..::*.*.::*:::..:..............................................:
:::::::::*:...:*::.:I::*I.:*.*I::II.:.:.:VFF*FFNNVFF...:...........*I****...:.....................................:..........*..
:::*I***I*V:*FFV*::.***:I.*:.****I:::*::.:.*I*:NNVFI:................:.:..:::::..::.........:......................:.:.....*....
:::::*V**I*:.NFNIFNV:::*IV*.::FNVNVFIN**:I*FVFNFNFV::...:..:.::.::.::..:::.::...:...............:.....:.................:*.....:
::I***::I*:*:IVFVNFVV.:I**:*...VF*:FVFIVVVVF:NFINNFI........::.....::...............................::........:......:........:*
:V****INF*:*V*V*FINNF:**I*::I:*.IIIFNFNFNVVIFNFFNNFV........:.........................::...:.............:.:.:::......I........:
::*:IV::FNVVNNIFFFF:*IV::*VFN*II..*INNFNFFFNVVFVNNNVI::::::.:::::..:::...:....:.:...::.:........:::..:::::::::::.I..I......I*:*:
I:*NVNV:*V*VNFFFFFVV*:FFFIFFFI*:*N**VVNFNNN**NFIINNF.V:::::::::::::.:.:.:::.::::.::.:::::::::::::::::::::::::::*:.*I.......:.VV*
I::::::I:I**VFFI*NIFF*FVNVV:FNFFVIFFFFFVN*......*VFFNFF:::*::::::::::::::::::::::::::::::::::*:::***********IIFFI*......II*::VVN
**::*II:::..*:IINNFFFFFFVFFNFFFNFVVFF*FF:...........N*NVI*I************.************************IIIIIIIIII*FVVFI.........I..IFFF
****I*:I*:*I**I:*IVINFFFFNVFFNFVFVFIIF...............IVNFIII:IIII**IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIVVVIIIIIFV*FV.......**:F:VFVFFF
*I****I:::I*V*:F:I:**IIVIVFN*IFNVVIF........I:.......***FFFVIVIIVVVIVIVVIIIVVVIII:*IIIIIIIVIVVVVVVVVVVVFFVVV....*.:.:VIFFFFFNNN*
***NNNVNF*NFIII*I**I:I::I*I*::*VF*.........***I:.......:..*NFIIVVVVVVVVVVVVVVVV.....IIIVVVVVVVVVVVVIVVII:*...*:.:..VFVFFFFF::::.
:::FNVFVNIVFFFI*II*I**IIFFF*F:..........:**I:*..........::.....VVVVVVVVIVVVVI......:..*VVVVVVVVVFF*::*I........VVFINFFF:.:VF....
:::FFNFNFFFFNIFI*:I*V*::V:.........:::.I:.*:I*.**..:....:*.V:.:.VVVVVVVV**:*IFFN.IFFVI.:VFF*:*::*V...**.I*.VI*IVV:.:.:VVV..:.::
:::::::*FFNFVI:..........:..........I:..:**.I...::*..:::....II*.....IFNNNNNNNN*VVVVVFVVFVVFFVV:.....**VVVVVV*..:....*VV:.:::::::
:::.:::::..:....::......:V::::..II.I*II::::.I:I..*.*:VV.::..IIVF.:VI:.*...*:.:*II***::.......*I.FIF***..:::::.:VFFVII.::::::IVFF
::::*****:......I::.....:*I::::..::::*:......:::..FVVF*F*:*F..IVFV:V**:FF*::.........:............:::..FFFFFFFFFFF..:::::FFVVFFV
::::::I***I*.I.*:::.I..*I*:.*.I.......*.I*:..*::..*:F*:*I:*:V...*FFIFFFV*FFV::.....:..::...*.:..::**:.VVVFVVVVVI....:IFNNNNNNFI*
:::::::::.**::::::.*NV.I:.I*:*:..:V.:::::..::I.**..FNFVNI**FFV:V...*FNNFFIINFF::::.:I*::.:::::VFVVVVI*:*VNNFF*..:::::::::*VVFFFN
::::::*V:I*VF*IFV*NVFFI:**::.VI::::*.::I.:*.:.I:*:..FNFFFFV*IIV:*FVVIV.INFFFIFFNFI::..FFFFI::VNNFFI:*IIVFFV..:::::::VNNNNFVFNV**
::::FVVFF*NNFFNNNNFFV::I::.I*I::.....:*::VF.FF*::*:..:VNFFNFF***III:II:*V*::IFNFFNNFFF*:.IFNFFFFFFFFFFVI......:.:::*I::..:VFFFFF
:::NNVFVFNNFNFNFVV::*V*F.FNVN:I:::*IV:::.IFFNVIVI.:::..NNFFFNVN*II**IIVIVIV***********IIIV:FVIF*VFIV.....:*VFFFFFFFFFNNNFFFFFFFF
::NFVNFVIN*VFN*NNIIFINVFNNINVNN:.::..........FNN:VVF.....:NFFFNNVF*I:::::*IIIIIV***********:**I*...::::**I:IFNNFNNNNNNF*::IIVFNN
::NVFFNVNFNVNNVNNNVNNIFNFVNFNN**:::IVNN.I.FN*IIINIVNNI:V:...VNNFNFNFNV**::::::::::::::*II*....:FNFFNNNFFFNNNNNF:.......:::::::..
.:NINNVFFFNIFNVNFNVNFVNNNVNVNNF:::IN:*V**NI:V::VFIFNNNFV***I:...:VFFFNNFFFNNNNNNNV:.......:::......::::....:::::::::YRREBRAP*NAI""")
                delay_print("\nOut of nowhere, a rogue wave capsizes your boat!")
        #Where the real code is ... Tells the user what they see at every tile.
        delay_print("******\nYou see {}.\n".format(CurrentTile.GetDescription()))

        #Ran into a problem ... I needed my event code to print AFTER the "tile code"
        if DisplayEvent:
            print EventText
            DisplayEvent=False
        #User options
        delay_print("(I)nventory, (L)ook around, (F)ish, (C)heck watch, move (N)orth, (S)outh, (E)ast or (W)est, e(X)it")
        #get user options and shift to uppercase
        UserSelection=raw_input("What would you like to do next?: ").upper()
#--------------------------------------------------------------------------------------------
        if UserSelection=="X":
            #ToDo: Check if they are at the dock, if now, print a message saying they take X times the number of spaces to get back?
            delay_print("You return to the dock and are safely back on shore.\n")
            return True     #Important! Routine needs to return True (keep playing) or False (game over)
#--------------------------------------------------------------------------------------------
        elif UserSelection=="I":
            if len(Inventory)==0:
                delay_print("You have nothing in your inventory.")
            else:
                delay_print("You are currently holding:\n {}".format(Inventory))
#--------------------------------------------------------------------------------------------
        elif UserSelection=="L":
            #Search the tile for an item
            UserSelection=(raw_input("How many minutes would you like to search the area? "))
            if UserSelection==0 or UserSelection=="":
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
                    #Special gulf code.  Only allow user to catch snake if they found the fishing net
                    if CurrentTile.GetEvent()=="Shark!":
                        if Inventory.count("harpoon")==1:
                            delay_print("You hit the shark between the eyes!")
                            CurrentTile.SetDescription("You pull the giant shark in your boat.")
                        else:
                            #ToDo?: Make it random to see if they get bit?   For now ... BITE EM! =)
                            print"""
                     ^`.                     o
     ^_              \  \                  o  o
     \ \             {   \                 o
     {  \           /     `~~~--__
     {   \___----~~'              `~~-_                     _____
      \                         /// a  `~._________________/___
      / /~~~~-, ,__.    ,      ///  __,,,,)      o  ______/    \
      \/      \/    `~~~;   ,---~~-_`~= \ \------o-'            \
                       /   /            / /
                      '._.'           _/_/
                                      ';|\
                                      """
                            delay_print("You don't have a weapon! You get eaten by the shark!")
                            return False
                    #Net event
                    elif CurrentTile.GetEvent()=="Harpoon":
                        #Soon as they get the harpoon, change the tile description (don't want it to say their is a shiny surface without the shiny net there
                        CurrentTile.SetDescription("Nothing in the water")
#--------------------------------------------------------------------------------------------
        elif UserSelection=="F":
            #ToDo?  Make fishing so it isn't a waste of time????
            UserSelection=int(raw_input("How many minutes would you like to stay and fish? "))
            if UserSelection==0:
                delay_print("You decide not skip fishing for now.")           
#--------------------------------------------------------------------------------------------
        #User wants to check their watch.
        elif UserSelection=="C":
            CheckWatch()
#--------------------------------------------------------------------------------------------
        #User wants to move
        elif UserSelection in ["N","S","E","W"]:
            OriginalTile=CurrentTile
            CurrentTile=MyGulfMap.Move(UserSelection)
            #If they are at a border, the code will return same tile back.  Need to check if we moved.
            if CurrentTile!=OriginalTile:
                #ToDo: Check for special events on new tile
                if CurrentTile.GetEvent()=="Abandoned fishing boat":
                    DisplayEvent=True
                    EventText="You teather your boat to the abandoned boat and step onto the deck!'\n"
                    #Set a timer flag to go off in "3-10" moves
                    WaveCounter=random.randint(3,10)
                #print MyMap.DisplayMap()
                #print MyTile.DisplayTile()
#--------------------------------------------------------------------------------------------
        else:
            print("'{}' is an invalid selection.".format(UserSelection))
    return True

def CasinoScenario():
    print("**** Ethan's code goes here.")
    return True

def HintFromNatives(posses_babble_fish=False):
    rot13 = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    Hints=["asdf","qwer","zxcv","Thursten Howell is at the S.S. Minnow.","Becareful just grabbing a snake.  Might want to find something to help you.",
           "Baby fish hate to lose their mommy ...","Want to see an air show?  Go to the Love Shack!"]
    OutputString=Hints[random.randint(0,len(Hints)-1)]
    if not posses_babble_fish:
        #Oh no ... they don't have a Babble Fish in their ear!!! Can't understand the language!"
        return string.translate(OutputString, rot13)
    else:
        return OutputString

#ToDo test tiles:
#JohnRiverTiles.append(Tiles.Tile("floating wooden duck decoys",1,"DuckDynasty",""))
#JohnRiverTiles.append(Tiles.Tile("a group of locals toobing down the river",1,"YouTubers","Beta video tape"))
#JohnRiverTiles.append(Tiles.Tile("an island surrounded by millions of minnows with seven castaways standing near a broken down boat",1,"SSMinnow","Deed to Thurston Howell's Oil Field"))
#JohnRiverTiles.append(Tiles.Tile("a diner on the shore",1,"PulpFictionRestaurant","a greasy spoon"))


def JohnRiverScenario():
    #ToDo: I don't like how the text is scrolling.  Work on newlines and other BS ...
    #Get access to the global variables
    global Inventory
    global JohnRiverMap
    #ToDo:Need this in everyone's code!
    global MasterListOfItems
    global CheaterModeEnabled
    global BabbleFishEnabled

    #Special variables to handle some "river events"
    DynamiteCounter=0
    DisplayEvent=False
    EventText=""
    CheatModeEnabled=False
    BabbleFishEnabled=False
    TotalExplosions=0

    CurrentTile=JohnRiverMap.GetCurrentTile()

    delay_print("\nYou decide to take a trip down the river.  A storm is on the horizon, but is 'supposed' to clear soon.\n")
    delay_print("As you step off the dock and into your boat, you hear some ominous notes being played. \n\n")
    #ToDo: Uncomment the line below..
    #time.sleep(3)
    delay_print("Undaunted by the erie music, you start your motor and proceed down the river.\nAfter all, what could possibly happen in the backwaters of Mississippi???\n")
    #ToDo: Play Deliverence theme
    #ToDo: Add babblefish to inventory
    #ToDo: Use dynamite to fish with get babble fish
    #ToDo: Jack Rabbit Slim’s restaurant
    #ToDo: squiling pig toy on random tile.
    #ToDo: Account for "Local's tile" having a random item
    #ToDo: "Tiles list"
    #ToDo: "Add hints!"
    while CheckTimer():
        #"Dynamite fishing event! (delayed explosion after the user finds the fisherman
        if DynamiteCounter>0:
            DynamiteCounter -=1
            if DynamiteCounter==0 and TotalExplosions<3:
                TotalExplosions+=1
                print("""\n
                           ____/ (  (    )   )  \___
                         /( (  (  )   _    ))  )   )\\
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
-------------------------------------------------------------------------------""")
                print("\nWith a loud cackle you hear, 'Dats what I call fishing!!!!!!'")
                
        #Where the real code is ... Tells the user what they see at every tile.
        delay_print("\nYou see {}.\n\n".format(CurrentTile.GetDescription()))
        if CheatModeEnabled:
            if CurrentTile.GetItem()!="":
                print("***Cheat: There is a {} on this tile.".format(CurrentTile.GetItem()))
            else:
                print("***Cheat: There is nothing on this tile.")

        #Ran into a problem ... I needed my event code to print AFTER the "tile code"
        if DisplayEvent:
            #if CurrentTile.GetEvent()=="B52":
                #ToDo: B-52 music
            delay_print(EventText)
            DisplayEvent=False
        #User options
        print("Valid options: (I)nventory, (L)ook around, (F)ish, (C)heck watch, move (N)orth, (S)outh, (E)ast or (W)est, (Q)uit")
        #get user options and shift to uppercase

        UserSelection=raw_input("What would you like to do next?: ").upper()
        if UserSelection=="Q":
            #ToDo: Check if they are at the dock, if now, print a message saying they take X times the number of spaces to get back?
            delay_print("\nYou return to the dock and are safely back on shore.\n\n")
            return True     #Important! Routine needs to return True (keep playing) or False (game over)
        elif UserSelection=="I":
            if len(Inventory)==0:
                delay_print("\nYou have nothing in your inventory.\n")
            else:
                delay_print("\nYou are currently holding:\n {}\n".format(Inventory))
        elif UserSelection=="L":
            #Search the tile for an item
            if TotalExplosions>0 and Inventory.count("a Babble Fish")==0 and CurrentTile.GetEvent()=="Fisherman":
                delay_print("\nYou find a Babble Fish.\n\nThe fisherman congratulates you on such a rare find.\nShe tells you to put it in your ear to understand the locals.\nThinking the lady might be a little crazy, you decide it isn't worth it to offend her.  You place the babble fish in your ear!\n")
                Inventory.append("a Babble Fish")
                BabbleFishEnabled=True
                continue
            elif CurrentTile.GetEvent()=="B52":
                delay_print("\nAs you approach the building, you hear some 80s music.  You see a sign on the building.  It reads, 'Love Shack.'\n")
                #ToDo Love Shack music
                continue
            elif CurrentTile.GetEvent()=="BeverlyHills":
                delay_print("\nYou see a few hill billies celebrate seeing oil burst out of the ground where they were shooting.\n")
                delay_print("One of them screams, 'We struck Oil that is, black gold, Texas tea.  We are rich!!!!'\n")
                delay_print("Before they leave, they give you a 'vial of crude oil' and tell you they are off to Beverly Hills!\n")
                Inventory.append("a vial of crude oil")
                CurrentTile.SetDescription("a sign in a pool of oil which reads, 'We moved to the Hills ... Beverly Hills!'")
                continue
            elif CurrentTile.GetEvent()=="California":
                delay_print("\nYou dock your boat next to the hotel and walk inside.\nAs you enter, you smell a warm smell of colitas, rising up through the air.\n")
                delay_print("Next to the pink champagne on ice and mirrors on the ceiling, you see a welcome to the Hotel California sign.\n")
                if Inventory.count("a Queen's tiara")>0:
                    delay_print("As you search around, you see nothing of value.\n")
                else:
                    delay_print("As you search around, the only thing you see of value is 'a Queen's tiara'.\n")
                    Inventory.append("a Queen's tiara")
                    CurrentTile.SetItem("")
                delay_print("You leave the hotel and get back in your boat.\n")
                continue


            UserSelection=raw_input("How many minutes would you like to search the area? ")
            if UserSelection==0 or UserSelection=="":
                delay_print("You decide not to spend time searching the current location.")
            else:
                #If there is an item and they searched longer than the "random time" (5-10)
                if (len(CurrentTile.GetItem()) == 0) or UserSelection<random.randint(5,10):
                    delay_print("\nYou spend {} minutes searching the area and find nothing special.\n".format(UserSelection))
                else:
                    #Add item found to inventory
                    Inventory.append(CurrentTile.GetItem())
                    delay_print("\nYou spend {} minutes searching the area and find '{}'.\n".format(UserSelection,CurrentTile.GetItem()))
                    #Clear the item out of the tile
                    CurrentTile.SetItem("")
                    #Special river code.  Only allow user to catch snake if they found the fishing net
                    if CurrentTile.GetEvent()=="Snake":
                        if Inventory.count("fishing net")==1:
                            delay_print("You capture the snake with your fishing net.")
                            CurrentTile.SetDescription("baby snakes in the water looking for their mother")
                        else:
                            #ToDo?: Make it random to see if they get bit?   For now ... BITE EM! =)
                            delay_print("\nWithout a net, you get bit by the snake and need to go to the hospital!\n")
                            return False       
                    #Net event
                    elif CurrentTile.GetEvent()=="Net":
                        #Soon as they get the net, change the tile description (don't want it to say their is a shiny surface without the shiny net there
                        CurrentTile.SetDescription("water with a surface not as shiny as earlier")
                    elif CurrentTile.GetEvent()=="Banjo":
                        print"asdfasdfasdfasdfasdfsadf"
                        CurrentTile.SetDescription("small pieces of the broken banjo you have, floating in the water")
                        #Todo Delevernce music
                    elif CurrentTile.GetEvent()=="YoYoGadget":
                        delay_print("\nYou recogine the gadget as a YoYo Fishing setup.  Knowing it is illegal in the area, you take it down.\n")
                        CurrentTile.SetDescription("fishing line hanging from a tree limb where the YoYo Gadget once was")


        elif UserSelection=="F":
            #ToDo?  Make fishing so it isn't a waste of time????
            UserSelection=int(raw_input("How many minutes would you like to stay and fish? "))
            if UserSelection==0:
                delay_print("You decide not skip fishing for now.")
        #User wants to check their watch.
        elif UserSelection=="C":
            CheckWatch()
        elif UserSelection=="J":
            if CheatModeEnabled:
                print("*** Cheat mode disabled ***")
                CheatModeEnabled=False
            else:
                print("*** Cheat mode enabled **")
                CheatModeEnabled=True

        elif UserSelection=="B":
            if BabbleFishEnabled:
                print("\n*** Cheat mode: Babble Fish disabled! ***")
                BabbleFishEnabled=False
            else:
                print("\n*** Cheat mode: Babble Fish enabled!***")
                BabbleFishEnabled=True

        #User wants to move
        elif UserSelection in ["N","S","E","W"]:
            OriginalTile=CurrentTile
            CurrentTile=JohnRiverMap.Move(UserSelection)
            #If they are at a border, the code will return same tile back.  Need to check if we moved.
            if CurrentTile!=OriginalTile or CurrentTile.GetEvent()=="Locals":
                #ToDo: Check for special events on new tile
                if CurrentTile.GetEvent()=="Fisherman":

                    if TotalExplosions==3:
                        CurrentTile.SetDescription("a lady picking up dead fish")
                    else:
                        DisplayEvent=True
                        if TotalExplosions==1:
                            EventText="She says, 'I see you haven't found any fish yet ... you are encouraged to (L)ook around my latest batch of fish.'\n\n"
                        else:
                            EventText="She says, 'You better have the right bait if you want to catch fish in this river!'\n\n"
                        #Set a timer flag to go off in "3-10" moves
                        DynamiteCounter=random.randint(3,10)
                    #print MyMap.DisplayMap()
                    #print MyTile.DisplayTile()
                elif CurrentTile.GetEvent()=="B52":
                    DisplayEvent=True
                    EventText="You see a formation of B-52s fly overhead!\n\n"
                elif CurrentTile.GetEvent()=="Locals":
                    DisplayEvent=True
                    EventText="They yell, '"+HintFromNatives(BabbleFishEnabled)+"'.\n\n"

        else:
            print("'{}' is an invalid selection.".format(UserSelection))
            
def Welcome():

    print("""
 ,---.   ,-.,-.    .---.  .-.   .-.,-.  ,---.     .--.    ,--,  ,-. .-.  ,---.     .--..-.   .-.
 | .-.\  |(|| |   / .-. )  ) \_/ / |(|  | .-.\   / /\ \ .' .')  | |/ /   | .-.\   / /\ \\ \_/ )/
 | |-' \ (_)| |   | | |(_)(_)   /  (_)  | |-' \ / /__\ \|  |(_) | | /    | |-' \ / /__\ \\   (_)
 | |--. \| || |   | | | |   / _ \  | |  | |--. \|  __  |\  \    | | \    | |--. \|  __  | ) (   
 | |`-' /| || `--.\ `-' /  / / ) \ | |  | |`-' /| |  |)| \  `-. | |) \   | |`-' /| |  |)| | |   
 /( `--' `-'|( __.')---'  `-' (_)-'`-'  /( `--' |_|  (_)  \____\|((_)-'  /( `--' |_|  (_)/(_|   
(__)        (_)   (_)                  (__)                     (_)     (__)            (__)
            """)
    delay_print("""Welcome to the Biloxi Back Bay!
You are Airmen Boudreaux. You are a technical training student at Keesler AFB.
Today is your Friday off and you decide to head down to the marina and rent a boat for some adventure.""")

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
        if CheaterModeEnabled:
            print("Cheaters aren't allowed on the leaderboard ... now")
            sys.exit(0)
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
CheaterModeEnabled=False

#handler code to grab Ctrl-C
signal.signal(signal.SIGINT, signal_handler)

#    ************************** River specific code start **************************
#One time setup of the scenario map variables
JohnRiverMap=[]         #This is the scenario map which holds all the tiles
JohnRiverTiles=[]       #Important tiles, will be randomized over the map.  (Only placed once)
JohnRiverFluffTiles=[]  #"filler tiles" to populate around the "real scenario tiles".  (Can appear multiple times)
JohnRiverAvailableItems=["Lost Lure","Fishing Hook","Wrench"]   #Available items which can be placed randomly over the map.
#These are the important scenario tiles.  Put your items and events here.
#Usage:Tiles.Tile("Tile description",ignore this field, pass a number,"name of an event you can test for and act on","name of item which can be found on tile"
JohnRiverTiles.append(Tiles.Tile("a pool of floating fish",1,"","a nearly-dead fish"))
JohnRiverTiles.append(Tiles.Tile("someone 'fishing' in a boat",1,"Fisherman",""))
JohnRiverTiles.append(Tiles.Tile("a snake in the water",1,"Snake","one ticked off snake"))
JohnRiverTiles.append(Tiles.Tile("water with a shiny surface",1,"Net","fishing net"))
JohnRiverTiles.append(Tiles.Tile("a diner on the shore",1,"PulpFictionRestaurant","a greasy spoon"))
JohnRiverTiles.append(Tiles.Tile("open waters with an abandon boat",1,"BrokenBoat","spare boat parts"))
JohnRiverTiles.append(Tiles.Tile("shack with a tin roof .... RUSTED..",1,"B52",""))
JohnRiverTiles.append(Tiles.Tile("floating wooden duck decoys",1,"DuckDynasty",""))
JohnRiverTiles.append(Tiles.Tile("worn life boat",1,"",""))
JohnRiverTiles.append(Tiles.Tile("flotsam floating on the water",1,"Flotsam","A ticket to Paradise"))
JohnRiverTiles.append(Tiles.Tile("an abandon hotel",1,"California","a Queen's tiara"))
JohnRiverTiles.append(Tiles.Tile("an interesting contraption",1,"YoYoGadget","a YoYo Fishing Gadget"))
JohnRiverTiles.append(Tiles.Tile("an island surrounded by millions of minnows with seven castaways standing near a broken down boat",1,"SSMinnow","ticket for a three hour cruise"))
JohnRiverTiles.append(Tiles.Tile("absolutely nothing! This is a void",1,"","a piece of the void"))
JohnRiverTiles.append(Tiles.Tile("locals shooting guns at the ground",1,"BeverlyHills",""))
JohnRiverTiles.append(Tiles.Tile("a broken banjo floating on the water",1,"Banjo","broken banjo"))
JohnRiverTiles.append(Tiles.Tile("a group of locals toobing down the river",1,"YouTubers","Beta video tape"))

#These are the filler scenario tiles.  Don't put items here.  You can do it separately when the GenerateMap() code is called  You can put events here.
JohnRiverFluffTiles.append(Tiles.Tile("locals shouting at you from the river's edge",0,"Locals",""))
JohnRiverFluffTiles.append(Tiles.Tile("blue water",0,"",""))
JohnRiverFluffTiles.append(Tiles.Tile("open water",0,"",""))
JohnRiverFluffTiles.append(Tiles.Tile("slightly, murky water",0,"",""))
#Generate the scenario map!
JohnRiverMap=GenerateMap(1,20,JohnRiverTiles,JohnRiverFluffTiles,JohnRiverAvailableItems)
#ToDo:Need this in everyone's code!
#Setup the default map
JohnRiverMap=Maps.Map(JohnRiverMap,1,20,"The river bank is too steep to exit here!")
MasterListOfItems+=JohnRiverMap.GetItems()
#Manually add a few items I will control in the scenario
MasterListOfItems.append("a tasty burger")
MasterListOfItems.append("fried green tomatoes")
MasterListOfItems.append("a Babble Fish")
MasterListOfItems.append("a vial of crude oil")
#    **************************  River specific code end  **************************

#shell code (or copy the above river code to start your scenario)
#Map=[]
BayMap=[]
BayTiles=[]
BayFluffTiles=[]
#(uncomment after you build tiles) - BayMap=GenerateMap(Len,Width,BayTiles,BayFluffTiles,AvailableItems)

#    ************************** Gulf specific code start **************************
#One time setup of the scenario map variables
MyGulfMap=[]         #This is the scenario map which holds all the tiles
MyGulfTiles=[]       #Important tiles, will be randomized over the map.  (Only placed once)
MyGulfFluffTiles=[]  #"filler tiles" to populate around the "real scenario tiles".  (Can appear multiple times)
MyGulfAvailableItems=["Boat keys","Casting net","Water skis","Harpoon"]   #Available items which can be placed randomly over the map.
#These are the important scenario tiles.  Put your items and events here.
#Usage:Tiles.Tile("Tile description",ignore this field, pass a number,"name of an event you can test for and act on","name of item which can be found on tile"
MyGulfTiles.append(Tiles.Tile("a school of Speckled Trout",1,"","a Jack Crevalle bit in half"))
MyGulfTiles.append(Tiles.Tile("abandoned boat",1,"Abandoned fishing boat",""))
MyGulfTiles.append(Tiles.Tile("Something floating in the water",1,"Boat Keys",""))
MyGulfTiles.append(Tiles.Tile("Something floating in the water",1,"Water skis",""))
MyGulfTiles.append(Tiles.Tile("A shark in the water",1,"Shark","a dead Shark"))
MyGulfTiles.append(Tiles.Tile("water with a shiny surface",1,"Net","casting net"))
#These are the filler scenario tiles.  Don't put items here.  You can do it separately when the GenerateMap() code is called  You can put events here.
MyGulfFluffTiles.append(Tiles.Tile("Clear Deep Water",0,"",""))
MyGulfFluffTiles.append(Tiles.Tile("Clear Shallow Water",0,"",""))
MyGulfFluffTiles.append(Tiles.Tile("Dark Shallow Water",0,"",""))
MyGulfFluffTiles.append(Tiles.Tile("Dark Deep water",0,"",""))
MyGulfFluffTiles.append(Tiles.Tile("blue water",0,"",""))
#Generate the scenario map!
MyGulfMap=GenerateMap(5,5,MyGulfTiles,MyGulfFluffTiles,MyGulfAvailableItems)
#ToDo:Need this in everyone's code!
#Setup the default map
MyGulfMap=Maps.Map(MyGulfMap,5,5,"The gulf is too deep to exit here!")
MasterListOfItems+=MyGulfMap.GetItems()
#    **************************  Gulf specific code end  **************************

#Leaderboard Setup Code
Leaders=[]
LeaderboardFile=".\\BBBLeaderBoard.lb"
Data=""
try:
    FileHandle = open(LeaderboardFile, 'r')
except:
    #File doesn't exist ... setup a "default leaderboard"
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
    delay_print("\n\nblah, blah (storyline) ... \n")
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
        StillPlaying=JohnRiverScenario()
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
sys.exit(0)




