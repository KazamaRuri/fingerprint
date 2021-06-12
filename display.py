import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

oled.fill(0)
oled.show()

image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

draw.text((0, 0), "Hello!", font=font, fill=255)
draw.text((0, 29), "Hello!", font=font2, fill=255)
draw.text((0, 46), "Hello!", font=font2, fill=255)

oled.image(image)
oled.show()