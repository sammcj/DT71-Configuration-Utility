# DT71-Configuration-Utility

Configuration utility for your digital tweezers

```shell
pip3 install -r requirements.txt
pyuic6 main.ui -o ui_main.py
python3 main.py
```

## CAL.ini

SLEEP_TIME:
A number between 30 and 999 that defines the number of seconds the measuring tweezers remain active after waking up from sleep mode.

DISPLY_DIRECTION:
The number 0, 3 or 4 that defines whether you will hold the device exclusively in your right hand, exclusively in your left hand or alternately in both hands. In the latter case, the sensor will be activated so that the processor will reverse the data in the display if you are working with the left hand.

OLED_BRIGHTNESS:
A number between 0 and 10 that allows you to set the brightness of the display.

SINE_FREQ_OPT:
A number from 0 to 5 that allows you to set the frequency of the sine wave generator from 200 Hz (5) to 10 kHz (0).

NOISE_FREQ_OPT:
Defines the frequency of the noise generator. Can in this version of the firmware, be set only to 1, which corresponds to a frequency of 100 kHz.

USER_FREQ_OPT:
A number from 0 to 5 that allows you to set the frequency of the self-defining signal from 200 Hz (5) to 10 kHz (0).

PULSE_FREQ_OPT:
A number from 0 to 8 that allows you to set the frequency of the pulse generator from 100 Hz (8) to 100 kHz (0).

USER_WAVEFORM:
A sequence of hexadecimal numbers that allows you to define the shape of the user defined signal.
