# Meteo.py
# Date: 21/06/2017 23:43:56
# Author: Carlos Rubio Abujas <crubio.abujas@gmail.com>
# Description:
#   Simple web scrapper to obtain current information about the temeprature in
#   Seville. Use the information of the web: meteosevilla.com
#   Note: The units of the diffetent measurements can be check in the web.

from lxml import html
import re
import requests


def get_meteodata(print_info=False):
    WEBURL = r'http://meteosevilla.com/datosactuales_currentdata.html'

    # Get the structure
    page = requests.get(WEBURL)
    tree = html.fromstring(page.content)

    # Identify the fields
    data_left = tree.xpath("//td[@class='dato_izq']")
    data_right = tree.xpath("//td[@class='dato_der']")

    # Parse the fields
    data = dict()
    for dl, dr in zip(data_left, data_right):
        key = re.match('(.+):', dl.text).groups()[0]
        try:
            val = re.match('^[+-]?\d+\.?\d*', dr.text)
            if val:
                if print_info:
                    print(key, '-', val.group())
                data[key] = float(val.group())
        except:
            continue
    return data


def main():
    get_meteodata(print_info=True)

if __name__ == '__main__':
    main()
