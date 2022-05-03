from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import datetime as dt

to_day = dt.date.today()

d_day = dt.date(year=2022,month=11,day=21)

sum_day = d_day - to_day

from PIL import Image, ImageDraw, ImageFont

# get an image
with Image.open("C:/Users/a24cc/Pictures/c.png").convert("RGBA") as base:

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

    # get a font
    fnt = ImageFont.load_default()
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text((50, 100), "testttttttttt!!1234", font=fnt, fill=(10, 255, 255, 128))
    # draw text, full opacity
    d.text((10, 60), str(sum_day), font=fnt, fill=(255, 255, 255, 255))

    out = Image.alpha_composite(base, txt)

    out.show()