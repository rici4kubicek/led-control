import spidev
from nightWiring import io
import signal
import time
import binascii

from array import array

# A demo GPIO map for Raspberry Pi with ICA HAT, 'i' means integer.
ledMap = array('i', [6])

io.setup()
io.setupGPIO(ledMap, 1)
io.pinMode(0, io.OUTPUT)
io.digitalWrite(0, io.HIGH)
io.digitalWrite(0, io.LOW)
time.sleep(0.1)
io.digitalWrite(0, io.HIGH)
time.sleep(0.1)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000

to_send = [0x0, 0x0, 0x0, 0x0]
spi.xfer(to_send)

to_send = [0xe1, 0xe1, 0, 0]
spi.xfer(to_send)
to_send = [0xf1, 0x0, 0xe1, 0x0]
spi.xfer(to_send)
to_send = [0xfe, 0x0, 0x0, 0xe1]
spi.xfer(to_send)
to_send = [0xe6, 0, 0x12, 0x32]
spi.xfer(to_send)

to_send = [0xff, 0xff, 0xff, 0xff]
spi.xfer(to_send)