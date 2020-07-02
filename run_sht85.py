import sht85
import os
import time
from datetime import datetime

mps = 1 # accepted intervals 0.5, 1, 2, 4, 10 seconds
rep = 'HIGH' # Repeatability: HIGH, MEDIUM, LOW

#print 'serial number = ', sht85.sn()
time.sleep(0.5e-3)

sht85.periodic(mps,rep)
time.sleep(1)

now = datetime.now()
print(now)
date_s1 = str(now)
date_s = date_s1[0:9]

file = open("/home/pi/Desktop/Instrument/sht85/data/M_"+date_s+".csv","a")

if os.stat("/home/pi/Desktop/Instrument/sht85/data/M_"+date_s+".csv").st_size == 0:
        file.write("Time,T (oC),RH (%)\n")
        
i = 0
while True:
        i=i+1
        t,rh = sht85.read_data()
        dp = sht85.dew_point(t,rh)
        print(i)
        print('Temperature =', t)
        print('Relative Humidity =', rh)
        #print((t,rh,))
        #print('Dew Point =', dp)
        print(' ')
        
        now = datetime.now()
        file.write(str(now)+","+str(t)+","+str(rh)+"\n")
        file.flush()

        time.sleep(mps)

# except(KeyboardInterrupt, SystemExit): #when you press ctrl+c
#     print("Killing Thread...")
#     time.sleep(0.5e-3)
#     sht85.stop()

sht85.stop()
file.close