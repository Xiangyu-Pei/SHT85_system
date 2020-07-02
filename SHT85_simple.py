import smbus
import time
import math
#Get I2C bus
bus = smbus.SMBus(1)
#SHT85 address,0x44(68)
addr =0x44
#Send Temperature measurement command
SHT85_ADDR       = 0x44 # Device Adress
SHT85_SS         = 0x24 # Single Shot Data Acquisition Mode
SHT85_SS_2       = {'HIGH' : 0x00, 'MEDIUM' : 0x0B, 'LOW' : 0x16} # Repeatability: (HIGH, MEDIUM, LOW)

SHT85_READ       = 0x00 # Read output

rep='HIGH'

bus.write_i2c_block_data(SHT85_ADDR,SHT85_SS,[SHT85_SS_2[rep]])
time.sleep(0.5)
data = bus.read_i2c_block_data(SHT85_ADDR,SHT85_READ,6)
t_data = data[0] << 8 | data[1]
h_data = data[3] << 8 | data[4]
temp = -45. + 175. * t_data / (2**16-1.)
relh = 100. * h_data / (2**16-1.)
T = round(temp,1)
RH = round(relh,1)
print ('Temperature =', T)
print ('Relative Humidity =', RH)
