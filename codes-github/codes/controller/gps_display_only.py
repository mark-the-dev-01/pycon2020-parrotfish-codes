from machine import UART, Pin, SPI,PWM
import utime,gc
import nmea
import ili_9225_3
import math

#initial position
lat_ch=8.559266
long_ch=124.525643
lat_org=8.559266
long_org=124.525643
#map bounding box  canitoan area
lat0=8.4877
lat1=8.4657
lon0=124.5974
lon1=124.6150


SW1=Pin(17,Pin.IN)
SW2=Pin(16,Pin.IN)
buz=PWM(Pin(21))
buz.freq(1000)
buz.duty(0)
def beep():
    buz.duty(512)
    utime.sleep(0.1)
    buz.duty(0)
def draw_basemap():
    f=open('map3.mp','rb') #cerritos
    #f=open('map220_176.mp','rb')
    b=bytearray(176*110*2)
    f.readinto(b,176*110*2)
    lcd.DrawImage(0,0,176,110,b)	
    f.readinto(b,176*110*2)
    lcd.DrawImage(0,110,176,110,b)
    #lcd.DrawMarker(50,50) #draw the 8x8 pixel marker at x,y coordinate*176,220 max)
def show_splash():
    lcd.fillRectangle(0,0,lcd.width,lcd.height,0xFFFF)
    f=open('parrotfish_logo.mp','rb')
    b=bytearray(176*110*2)
    f.readinto(b,176*110*2)
    lcd.DrawImage(0,0,176,110,b)	
    f.readinto(b,176*110*2)
    lcd.DrawImage(0,110,176,110,b) 

def Map_info_display(lat,long,dx,dy):
        lcd.text("{:7.4f}".format(lat),0,175,0xFFFF,0x0000)
        lcd.text("{:7.4f}".format(long),0,198,0xFFFF,0x0000)
        # lcd.text(str(time),65,182,0xFFE0, background)
        lcd.text("{:03d}".format(dy),120,175,0xFFE0,0x0000)
        lcd.text("{:03d}".format(dx),120,198,0xFFE0,0x0000)
        
   
spi=SPI(1,baudrate=40000000, mosi=Pin(13), miso=Pin(12), sck=Pin(14))
uart = UART(1, 9600,tx=23,rx=22)
now = utime.ticks_ms()
sentence = ''
state = ''
my_nmea = nmea.nmea(debug=0)
lcd=ili_9225_3.TFT_22_ILI9225(spi)
lcd.init()
lcd.clear()
lcd.fillRectangle(0,0,lcd.width,lcd.height,0xFFFF)
show_splash()
utime.sleep(2)

# f=open('map3.mp','rb')
# b=bytearray(176*110*2)
# f.readinto(b,176*110*2)
# lcd.DrawImage(0,0,176,110,b)	
# f.readinto(b,176*110*2)
# lcd.DrawImage(0,110,176,110,b)
# lcd.DrawMarker(50,50) #draw the 8x8 pixel marker at x,y coordinate*176,220 max)
draw_basemap()
beep()
draw_basemap()
yold=0
xold=0
if SW2.value():

  while 1:
	while uart.any():
		b = uart.read()
		my_nmea.parse(b)
        
        ynew=(math.floor((lat0-my_nmea.latitude)*1000)*2)
        xnew=(math.floor((my_nmea.longitude-lon0)*1000)*5)
        if ynew!=yold and xnew!=xold:
            if ynew<220 and ynew<176:
                draw_basemap()
                lcd.DrawMarker(xnew,ynew)
                beep()
        yold=ynew
        xold=xnew  
        Map_info_display(my_nmea.latitude,my_nmea.longitude,xnew,ynew)
        #time.sleep(5)    
        #beep()
else:
  lcd.StatDisplay()
  beep()

  while 1:
	while uart.any():
		b = uart.read()
		my_nmea.parse(b)
	if SW2.value()==0:
		lat_org=my_nmea.latitude
		long_org=my_nmea.longitude
		beep()
	
	
	if utime.ticks_diff(utime.ticks_ms(), now) > 1000:
		now = utime.ticks_ms()
		d_ch=nmea.get_distance(my_nmea.latitude,my_nmea.longitude,lat_ch,long_ch)
		d_o=nmea.get_distance(my_nmea.latitude,my_nmea.longitude,lat_org,long_org)
		lcd.LocUpdate(my_nmea.latitude,my_nmea.longitude,my_nmea.time_local,my_nmea.satcount,d_ch,d_o)
		#print('d_ch:',d_ch)
		#print('d_o:',d_o)
		print('{} {} {} {} num of sat:{}'.format(my_nmea.time, my_nmea.date, my_nmea.latitude, my_nmea.longitude,my_nmea.satcount))
		#display(my_nmea, margin, d)
	    
