#!/usr/bin/python3
from DSPW215 import SmartPlug
from Meteo import get_meteodata
import os
import Adafruit_DHT
import sys
import time
from datetime import datetime

BASEPATH = os.path.dirname(os.path.abspath(__file__))
HEADER = "#Time;Power[W];RoomTemp[C];RoomHumid[%];EnvTemp[C];EnvHumid[%];EnvRadiation[W/m2];Setpoint[C]"


def get_filepath():
    foldname = datetime.strftime(datetime.now(), "%b%Y").upper()
    filename = datetime.strftime(datetime.now(), "%Y-%m-%d.csv")
    folderpath = os.path.join(BASEPATH, foldname)
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
    filepath = os.path.join(BASEPATH, foldname, filename)
    if not os.path.exists(filepath):
        f = open(filepath, 'w+')
        print(HEADER, file=f)
        f.close()
    return filepath


def append_data(data):
    f = open(get_filepath(), 'a+')
    print(data, file=f)
    f.close()
    return 1


def main():
    SAMPLE_TIME = 5  # Sample time of the monitor (seconds)
    SETPOINT = 27

# Define sensor
    sensor = Adafruit_DHT.DHT22
    dht_pin = 2

# Plug Identity
    ip = '192.168.1.189'
    pin = '859631'

# Connect to the Plug
    print('Connecting with SmartPlut...', end='')
    plug = SmartPlug(ip, password=pin)
    if not plug.auth():
        print('FAIL')
        sys.exit()
    plug.state = 'ON'
    print('OK')

# Monitoring loop
    try:
        while True:
            try:
                meteo = get_meteodata()
            except:
                print('[E] Unable to access meteo data')
                meteo['Temperature'] = 'NaN'
                meteo['Humidity'] = 'NaN'
                meteo['Solar Radiation'] = 'NaN'

            try:
                measure = Adafruit_DHT.read_retry(sensor, dht_pin, retries=3,
                                                  delay_seconds=0.5)
                H,T = tuple(map(lambda x: round(x, 2), measure))
            except Exception as e:
                print(e)
                print('[E] Unable to access DHT sensor')
                H, T = 'NaN', 'NaN'

            try:
                P = plug.current_consumption
            except:
                print('[E] Unable to access SmartPlug')
                P = 'NaN'

            now = datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")
            data = [now, str(P), str(T), str(H),
                    str(meteo['Temperature']), str(meteo['Humidity']), str(meteo['Solar Radiation']),
                    str(SETPOINT)] 
            print('\t'.join(data))
            append_data(';'.join(data))

            time.sleep(SAMPLE_TIME)

    except KeyboardInterrupt:
        print('Manually interrupted!')

if __name__ == '__main__':
    main()
