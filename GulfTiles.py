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
MyGulfTiles.append(Tiles.Tile("Something floating in the water",1,"Water skis","")
MyGulfTiles.append(Tiles.Tile("A shark in the water",1,"Shark","a dead Shark"))
MyGulfTiles.append(Tiles.Tile("water with a shiny surface",1,"Net","casting net"))
MyGulfTiles.append(Tiles.Tile())
#These are the filler scenario tiles.  Don't put items here.  You can do it separately when the GenerateMap() code is called  You can put events here.
MyGulfFluffTiles.append(Tiles.Tile("Clear Deep Water,0,"",""))
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
