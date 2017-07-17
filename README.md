AirMonitor v1.0
===============
This code is intended to monitor the temperature of the HAVC of my house
depending on the external conditions. This proyect has multiple points of
interest.

1. Scrapping of a Meteo Web to detect current environmental conditions
2. Recording de DSP-W215 power consumption
3. Add a temperature sensor attached to the Raspberry.
4. Add an independent temperature sensor attached to a ESP8266
5. Webserver to request the data without interrupting the monitoring

Well, plenty of things to have a lot of fun... I guess...

## Implementation for monitoring whatever you want
There are plenty of question that can be answered with a few numbers. If you
reach the point where you can handle the technology to suit your purposes you
would be much more interesting! 

Also it may be interesting to test how much would your bill be increased by the
aconditioning of your home, the COP of the system or other interesting points.
(I'm interesting in compare the impact of the setpoint over the overall
consumption).

## Implementation procedure.
I think that the first thing to do must the interconection with the raspberry.
I do not think it may be wise to use my laptop 24/7 for that purpose and I may
be interested in moving it from time to time. So the Raspberry must work for
it.

The second point to address is the monitoring of the DSP. This is almost done
and little modification may be required. It is true that all that modification
may be crucial if a multi-process program is to be finally implemented, but is
better than nothing. Isn't it?

The third point of interest is to scrap the meteo webpage in order to obtain
current information of the weather in Seville.

Forth, to implement the temperature attached to the system, this way it may be
possible to monitor the temperature of the room as well as the expected outter
temperature.

Finally the webserver to interact with the raspi recording the data. This may
be interesting for other applications as well. Once this is done, you may focus
your experiments and processing the data to try to obtain some meaningful
answers.

The bonus part is to include a temperature sensor attached to a ESP8266, but
this may be not accomplished in a reasonable time, so it is almos discarded...
