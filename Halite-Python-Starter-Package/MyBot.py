from hlt import *
from networking import *

myID, gameMap = getInit()
sendInit("MyPythonBot")

while True:
    moves = []
    gameMap = getFrame()
    for y in range(gameMap.height):
        
        for x in range(gameMap.width):
            
            if gameMap.getSite(Location(x, y)).owner == myID:
                movedPiece = False
                
                for d in CARDINALS:
                    if gameMap.getsite(Location(x,y),d).owner !=myID and gameMap.getSite(Location(x,y),d).strength < gameMap.getSite(Location(x,y)).strength:
                        moves.append(Move(Location(x,y),d)
                        movedPiece = TRUE
                        break
               if not movedPiece and gameMap.getSite(Location(y,x)).strength == 0: #to make pieces of 0 strength stay still
                      moves.append(Move(Location(x, y), STILL))
                      movedPiece = True;
               if not movedPiece:
                      moves.append(Move(Location(x,y),SOUTH if bool(int(random.random()*2)) else EAST)
                      movedPiece = True
    sendFrame(moves)
