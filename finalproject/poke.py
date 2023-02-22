#!/user/bin/python3

import requests
from io import BytesIO

def convertImageToAscii(cols, scale, moreLevels):
    """
    Download a random Pokémon sprite and convert it to ASCII art.
    """
    # declare globals
    global gscale1, gscale2

    # get a random Pokémon
    pokemon_id = random.randint(1, 151)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to get Pokémon.")
        return

    # get the sprite URL
    sprite_url = response.json()["sprites"]["front_default"]

    # download the sprite
    response = requests.get(sprite_url)
    if response.status_code != 200:
        print("Failed to download sprite.")
        return

    # open image from the downloaded sprite
    image = Image.open(BytesIO(response.content)).convert('L')

    # store dimensions
    W, H = image.size[0], image.size[1]
    print("input image dims: %d x %d" % (W, H))

    # compute width of tile
    w = W/cols

    # compute tile height based on aspect ratio and scale
    h = w/scale

    # compute number of rows
    rows = int(H/h)
    
    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))

    # ascii image is a list of character strings
    aimg = []
    # generate list of dimensions
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)

        # correct last tile
        if j == rows-1:
            y2 = H

        # append an empty string
        aimg.append("")

        for i in range(cols):

            # crop image to tile
            x1 = int(i*w)
            x2 = int((i+1)*w)

            # correct last tile
            if i == cols-1:
                x2 = W

            # crop image to extract tile
            img = image.crop((x1, y1, x2, y2))

            # get average luminance
            avg = int(getAverageL(img))

            # look up ascii char
            if moreLevels:
                gsval = gscale1[int((avg*69)/255)]
            else:
                gsval = gscale2[int((avg*9)/255)]

            # append ascii char to string
            aimg[j] += gsval
    
    # print txt image to console
    for row in aimg:
        print(row)

