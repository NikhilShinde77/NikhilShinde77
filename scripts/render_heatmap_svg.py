import json
from pathlib import Path
from datetime import datetime


INPUT = Path(
    "data/contributions.json"
)

OUTPUT = Path(
    "contrib-heatmap.svg"
)



WIDTH = 860
HEIGHT = 220


# GitHub contribution colors
COLORS = [
    "#161b22",
    "#0e4429",
    "#006d32",
    "#26a641",
    "#39d353",
    "#69f0a0"
]



def load_data():

    with open(INPUT) as f:

        data = json.load(f)

    return data["contributions"]



def create_grid(days):

    lookup = {}

    for item in days:

        lookup[item["date"]] = item["level"]


    today = datetime.today()


    cells = ""

    cell_size = 14

    gap = 4


    # 53 weeks

    for week in range(53):

        for day in range(7):


            index = (
                week * 7
                + day
            )


            if index >= len(days):

                continue



            date = days[index]["date"]

            level = days[index]["level"]



            x = week * (
                cell_size + gap
            )


            y = day * (
                cell_size + gap
            )


            delay = index * 0.003



            cells += f"""

<rect

x="{x}"

y="{y}"

width="{cell_size}"

height="{cell_size}"

rx="3"

fill="{COLORS[level]}"

style="

opacity:0;

animation:

show 0.8s forwards;

animation-delay:{delay}s;

"

/>

"""


    return cells




def generate():


    days = load_data()


    grid = create_grid(days)



    total = sum(
        x["level"]
        for x in days
    )



    svg = f"""

<svg

width="{WIDTH}"

height="{HEIGHT}"

xmlns="http://www.w3.org/2000/svg">


<style>

@keyframes show {{

from {{

opacity:0;

transform:
translateY(-20px);

}}


to {{

opacity:1;

transform:
translateY(0);

}}

}}

</style>



<rect

width="100%"

height="100%"

rx="15"

fill="#0d1117"

/>



<text

x="30"

y="35"

fill="#ffffff"

font-size="22"

font-family="monospace">

GitHub Contributions

</text>



<g transform="translate(30 55)">

{grid}

</g>



<text

x="30"

y="190"

fill="#8b949e"

font-size="14"

font-family="monospace">

Less

</text>



<rect

x="70"

y="175"

width="14"

height="14"

fill="#161b22"

/>


<rect

x="95"

y="175"

width="14"

height="14"

fill="#0e4429"

/>


<rect

x="120"

y="175"

width="14"

height="14"

fill="#006d32"

/>


<rect

x="145"

y="175"

width="14"

height="14"

fill="#39d353"

/>



<text

x="175"

y="190"

fill="#8b949e"

font-size="14"

font-family="monospace">

More

</text>



<text

x="600"

y="190"

fill="#58a6ff"

font-size="15"

font-family="monospace">

Total: {total}

</text>



</svg>

"""


    OUTPUT.write_text(svg)


    print(
        "✅ contrib-heatmap.svg created"
    )



if __name__ == "__main__":

    generate()