from PIL import Image, ImageEnhance
import sys


OUTPUT = "source-prepped.png"



def prepare(image_path):

    img = Image.open(image_path)


    # Convert grayscale

    img = img.convert("L")


    # Increase contrast

    enhancer = ImageEnhance.Contrast(img)

    img = enhancer.enhance(2.0)



    # Resize

    img.thumbnail(
        (120,120)
    )


    # White background

    canvas = Image.new(
        "L",
        img.size,
        255
    )


    canvas.paste(
        img
    )


    canvas.save(
        OUTPUT
    )


    print(
        "✅ source-prepped.png created"
    )



if __name__ == "__main__":

    prepare(
        sys.argv[1]
    )
    