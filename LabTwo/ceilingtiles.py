def num_tiles(lenTile, lenWall): 

    inchesWall = lenWall*12
    tiles = inchesWall//lenTile
    remaining = inchesWall%(lenTile*tiles) 

    print(f'Each row needs {tiles} tiles with {remaining:.2f} remaining.')

if __name__ == "__main__": 

    tile = float(input("What is the length of a tile's side in inches? "))
    wall = float(input("What is the length of the wall in feet? "))

    num_tiles(tile, wall)
