import sys, time, matplotlib, threading
from datetime import datetime
from gpiozero import Button
from signal import pause

sys.path.insert(1, "./lib")
import epd2in7_V2
from PIL import Image, ImageDraw, ImageFont

epd = epd2in7_V2.EPD()
epd.init()
print("Initiated")
epd.Clear()

MAXx = 264
MAXy = 176

btn1 = Button(5)
btn2 = Button(6)
btn3 = Button(13)
btn4 = Button(19)

def dispDef(s):
	image = Image.new('1', (epd.height, epd.width), 255)
	draw = ImageDraw.Draw(image)
	draw.text((5, 5), s, font = ImageFont.load_default(), fill = 0)
	epd.display(epd.getbuffer(image))

def printFont(s, px):
	image = Image.new('1', (epd.height, epd.width), 255)
	draw = ImageDraw.Draw(image)
	f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", px)
	draw.text((5, 5), s, font = f,  fill = 0)
	epd.display(epd.getbuffer(image))

def circle():
	image = Image.new('1', (epd.height, epd.width), 255)
	draw = ImageDraw.Draw(image)
	draw.ellipse((54, 10, 210, 166), outline = 0, width = 7) # Outer Ring
	draw.ellipse((117,0,147,30), outline = 0, fill = 0) # Outer Ring Circle
	draw.ellipse((102, 58, 162, 118), outline = 0, fill = 0) # Inner circle
	epd.display(epd.getbuffer(image))

def bigD():
	image = Image.new('1', (epd.height, epd.width), 255)
	draw = ImageDraw.Draw(image)
	draw.ellipse((0, 0, 88, 88), outline = 0, fill = 0) # Top nut
	draw.ellipse((0, 88, 88, 176), outline = 0, fill = 0) # Bottom nut
	draw.ellipse((220, 44, 264, 132), outline = 0, fill = 0) # Head
	draw.rectangle((44, 44, 244, 132), outline = 0, fill = 0) # Rect
	epd.display(epd.getbuffer(image))

def onWake():
	now = datetime.now()
	cdatetime = now.strftime("%A\n%d %B\n%Y")
	image = Image.new('1', (epd.height, epd.width), 255)
	draw = ImageDraw.Draw(image)
	draw.ellipse((108, 20, 264, 176), outline = 0, width = 7)
	draw.ellipse((171, 10, 201, 40), outline = 0, fill = 0)
	draw.ellipse((156, 68, 216, 128), outline = 0, fill = 0)
	f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
	draw.text((1,1),cdatetime, font = f, fill=0)
	epd.display(epd.getbuffer(image))

def timedRefresh(i):
	while True:
		time.sleep(i)
		onWake()

def btnPress(btn):
	pinNum = btn.pin.number
	if (pinNum == 5):
		print("Pressed button 1")
		onWake()
	elif (pinNum == 6):
		print("Pressed button 2")
		bigD()
	elif (pinNum == 13):
		print("Pressed button 3")
		printFont("Hallo\nThis is also a test \nmessage.",24)
	elif (pinNum == 19):
		print("Pressed button 4")
		return
	else:
		print("Unknown error")


print("Good day.")
circle()
time.sleep(1)
onWake()

btn1.when_pressed = btnPress
btn2.when_pressed = btnPress
btn3.when_pressed = btnPress
btn4.when_pressed = btnPress
threading.Thread(target=timedRefresh, args=(720,), daemon=True).start() #Refresh after 12 hours
pause()