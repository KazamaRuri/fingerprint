import time
import Adafruit_PCA9685
import fingerprint
import binascii
import serial
import serial.tools.list_ports
import time
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import RPi.GPIO as GPIO

i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
fp = fingerprint

# pwm = Adafruit_PCA9685.PCA9685()
# pwm.set_pwm_freq(50) 

# def set_servo_angle(channel,angle):
#     angle=4096*((angle*11)+500)/20000
#     pwm.set_pwm(channel,0,int(angle))

def display(mess,user,mark):
    oled.fill(0)
    oled.show()

    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

    draw.text((0, 0), mess, font=font, fill=255)
    draw.text((0, 30), "User:", font=font2, fill=255)
    draw.text((50, 30), user, font=font2, fill=255)
    draw.text((0, 46), "Mark:", font=font2, fill=255)
    draw.text((50, 46), mark, font=font2, fill=255)

    oled.image(image)
    oled.show()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)
pwm = GPIO.PWM(4,50)
pwm.start(0)
pwm.ChangeFrequency(50)

serial = serial.Serial('/dev/ttyUSB0', 57600, timeout=0.5)
if serial.isOpen() :
    print("识别器已开启")
    display("Already","","")
    while True:
        data_GetImage = fp.GetImage(serial)
        if(data_GetImage == '02'):
            print("请按住识别器")
            display("Hold","","")
        elif(data_GetImage == '00'):
            # print("识别成功")
            break
        else:
            print("不成功")
            display("Retry","","")
    data_Identify = fp.Identify(serial)
    if(data_Identify[20:22] == '00'):
        user = data_Identify[22:26]
        mark = data_Identify[26:30]
        print("用户：",data_Identify[22:26])
        print("相似度：",data_Identify[26:30])
        display("Success",user,mark)
        pwm.ChangeDutyCycle(0/18+2)
        time.sleep(3)
        pwm.ChangeDutyCycle(180/18+2)
        # set_servo_angle(15,180)
        # time.sleep(3)
        # set_servo_angle(15,0)
    else:
        print("失败，请重试")
        display("Retry","","")
else :
    print("open failed")

pwm.stop()
GPIO.cleanup()