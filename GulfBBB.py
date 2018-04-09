# ***Remove before adding code to BBB.py***
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
Today is your Friday off and you decide head down to the marina and rent a boat.""")

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

    #Setup the default map
    MyGulfMap=Maps.Map(MyGulfMap,5,5,"The gulf is too deep to exit here!")
    MasterListOfItems+=MyGulfMap.GetItems()
    
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
                            delay_print("You don't have a weapon! You get eaten by the shark!)
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
