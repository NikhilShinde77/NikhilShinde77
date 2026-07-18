from PIL import Image
from pathlib import Path


IMAGE = "source-prepped.png"
OUTPUT = "avi-ascii.svg"

RAMP = "@%#*+=-:. "


def generate_ascii():

    img = Image.open(IMAGE)

    img = img.convert("L")

    img = img.resize((80, 40))


    rows = []


    for y in range(img.height):

        line = ""

        for x in range(img.width):

            pixel = img.getpixel((x, y))

            index = int(
                pixel / 255 * (len(RAMP) - 1)
            )

            line += RAMP[index]


        rows.append(line)


    create_svg(rows)



def create_svg(rows):

    text = ""

    y = 25


    for row in rows:

        text += f"""
<text
x="20"
y="{y}"
fill="#39d353"
font-size="8"
font-family="monospace">
{row}
</text>
"""

        y += 10



    svg = f"""
<svg
xmlns="http://www.w3.org/2000/svg"
width="700"
height="500">


<rect
width="100%"
height="100%"
fill="#0d1117"/>


{text}


</svg>
"""


    Path(OUTPUT).write_text(svg)


    print("✅ avi-ascii.svg created")



if __name__ == "__main__":

    generate_ascii()