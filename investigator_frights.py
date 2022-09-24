from random import sample
listoffrights = ["shadows", "holes", "cockroaches", "cats", "small spaces",
"blood", "darkness", "rainbows", "shakespeare", "forks",
"water/depths", "large men", "angry shouting", "spiders", "hostage situation",
"clowns", "sharp objects", "ghostly children laughter", "screams", "static noise",
"silence", "insects", "mirrors", "fire", "apocalypse", "inevitability of death",
"flying cockroaches", "beans", "birds", "unmoisturized hands", "holes",
"superstitions", "old people", "hospitals", "loss of senses", "large empty spaces",
"missed deadlines"]
frights = sample(listoffrights, (int(input("Number of investigators? ")) * 5))
print(frights)
