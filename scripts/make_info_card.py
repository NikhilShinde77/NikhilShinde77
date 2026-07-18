from pathlib import Path


OUTPUT = Path("info-card.svg")


NAME = "NIKHIL SHINDE"


INFO = [
    ("ROLE", "Software Engineer"),
    ("EDU", "Integrated M.Sc IT"),
    ("STACK", "Python | React | Node"),
    ("BACKEND", "Redis | Docker"),
    ("CLOUD", "AWS"),
    ("DSA", "FAANG Preparation"),
    ("GOAL", "40 LPA Engineer"),
]


WIDTH = 490
HEIGHT = 360


def generate():

    rows = ""

    y = 110


    for i, (key, value) in enumerate(INFO):

        delay = i * 0.3

        rows += f"""

<g style="
opacity:0;
animation:show 0.8s forwards;
animation-delay:{delay}s;
">

<text
x="40"
y="{y}"
fill="#00ff99"
font-size="17"
font-family="monospace">

{key}

</text>


<text
x="170"
y="{y}"
fill="#ffffff"
font-size="17"
font-family="monospace">

{value}

</text>


</g>

"""

        y += 32



    svg = f"""

<svg width="{WIDTH}"
height="{HEIGHT}"
xmlns="http://www.w3.org/2000/svg">


<style>

@keyframes show {{

from {{
opacity:0;
transform:translateY(15px);
}}

to {{
opacity:1;
transform:translateY(0);
}}

}}

</style>



<rect

x="5"
y="5"

width="480"
height="350"

rx="15"

fill="#0d1117"

stroke="#30363d"

/>



<text

x="40"
y="55"

fill="#58a6ff"

font-size="26"

font-family="monospace"

font-weight="bold">

{NAME}

</text>



<line

x1="40"
y1="75"

x2="450"
y2="75"

stroke="#30363d"

/>



{rows}


</svg>

"""


    OUTPUT.write_text(svg)



if __name__ == "__main__":

    generate()

    print("✅ info-card.svg created")