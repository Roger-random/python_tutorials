#!/usr/bin/env python

# Display Si7021 temperature value on PIC-drive 7-segment LED
# 2017/09/18 Roger Cheng

class PIC_7Seg:
  """ A class to display information on a 7-segment LED """
  
  def __init__(self, pi, bus=1, addr=0x47):
    """
    Instantiate with the Pi.

    Optionally the I2C bus may be specified, default 1.

    Optionally the I2C address may be specified, default 0x47.
    """
    self.pi = pi
    self._h = pi.i2c_open(bus, addr)
  
  def cancel(self):
    """
    Release I2C resources
    """
    self.pi.i2c_close(self._h)
    
  def displayHex(self, value):
    """
    Display the given value in hexadecimal format
    Any digits beyond 4 (0xFFFF) are truncated.
    """
    print("Want to show {:4x}".format(value))

if __name__ == "__main__":
  import time
  import pigpio
  import Si7021

  pi = pigpio.pi()

  if not pi.connected:
    exit(0)

  # Sensor initialization
  s = Si7021.sensor(pi)

  s.set_resolution(0)
  print("Sensor resolution set to {:x}".format(s.get_resolution()))

  print("Sensor hardware revision={:x} with ID1={:08x} and ID2={:08x}".format(
    s.firmware_revision(),
    s.electronic_id_1(), 
    s.electronic_id_2()))

  # LCD initialization
  led = PIC_7Seg(pi)

  count = 0

  try:
    print("Press Control-C to exit program.")
    while True:
      led.displayHex(count)
      count = count + 1
      time.sleep(0.1)
  except KeyboardInterrupt:
    pass
    
  print ()
  print ("Contro-C pressed, cleaning up and quitting.")

  pi.stop()

