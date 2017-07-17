#!/usr/bin/python3
import sys
import os
import argparse

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

BASEPATH = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASEPATH, 'JUN2017/2017-06-23.csv')


def get_data(fileName):
    readopt = {'sep': ';',
               'index_col': 0,
               'parse_dates': True,
               'skiprows': 1,
               'names': ['power', 'temp', 'humid',
                         'envtemp', 'envhumid', 'envrad',
                         'setpoit']}
    df = pd.read_csv(fileName, **readopt)
    df = df.resample('30S').mean()
    return df


def plot_consumption():
    fileName = sys.argv[1]
    df = get_data(fileName)
    # df['time'] = pd.to_datetime(df['time'])
    time = df.index.to_series()

    # Process data
    mean_pow = df['power'].mean()
    dt = (time.iloc[-1] - time.iloc[0]).seconds
    energy = mean_pow * dt / 3600 / 1000
    cost = energy*0.16
    print('Mean power[W]:', mean_pow)
    print('Energy[kWh]:', energy)
    print('Mean temperature [C]', df['temp'].mean())
    print('cost[€]', cost)

    # Show current state conditions:
    print('\nCurrent Weather:')
    print('Room Temperature:', df['temp'].iloc[-1], 'ºC')
    print('Room Humidity:', df['humid'].iloc[-1], '%')
    print('Env Temperature:', df['envtemp'].iloc[-1], 'ºC')
    print('Env Humidity:', df['envhumid'].iloc[-1], '%')
    print('Env Radiation:', df['envrad'].iloc[-1], 'W/m2')

    # Plotting
    plt.plot(time, df['power'])
    ax = plt.gca()
    lines, = ax.lines
    t = lines.get_xydata()[:, 0]
    ax.fill_between(t, 0, df['power'], facecolor='lightblue')
    ax.xaxis.set_major_formatter(DateFormatter("%H:%M"))
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.xlabel('Time [s]')
    plt.ylabel('Power [W]')

    ax2 = ax.twinx()
    ax2.plot(time, df['temp'], color='red')
    ax2.plot(time, df['envtemp'], color='orange')
    ax2.set_ylabel('Temperature [C]')
    # ax2.set_ylim(30, 43)

    plt.show()


def plot_meteo():
    fileName = sys.argv[1]
    df = get_data(fileName)
    time = df.index.to_series()

    # Plotting
    plt.plot(time, df['envrad'], color='#ffcc00')
    ax = plt.gca()
    lines, = ax.lines
    t = lines.get_xydata()[:, 0]
    ax.fill_between(t, 0, df['envrad'], facecolor='#ffeeaa')
    ax.set_ylabel('Radiation [W/m2]')
    ax.set_ylim([0,1200])
    ax.xaxis.set_major_formatter(DateFormatter("%H:%M"))
    plt.grid(True)
    plt.xticks(rotation=45)

    ax2 = ax.twinx()
    ax2.plot(time, df['envtemp'], color='#ff0000')
    ax2.plot(time, df['temp'], color='#ff8080')
    ax2.set_ylabel('Temperature [ºC]')


    plt.show()

if __name__ == '__main__':
    plot_consumption()
    # plot_meteo()
