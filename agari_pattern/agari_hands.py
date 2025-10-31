hand_tiles = {"hand":["m5", "s7", "white", "p2", "m6", "p4", "white", "s7", "p3", "m4", "white", "east", "east", "east"], "call":[[],]}

tiles = sorted(hand_tiles["hand"])
print(tiles)

count = len(tiles)
head = []
for i, tile1 in enumerate(tiles):
    for j, tile2 in enumerate(tiles, 1):
        print(tile1, tile2)


print(head)

