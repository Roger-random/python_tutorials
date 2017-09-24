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
    
    # Cap given value at 0xFFFF
    value = value & 0xFFFF
    
    # Goal: Given the hexadecimal value, write out each digit as a
    # byte. So for value of 0xBEEF, we want [0xB, 0xE, 0xE, 0xF]
    # There's probably a really clever Python way to do this I don't
    # know yet. The below feels very hacky.
    
    # Using string.format to get a string of four characters.
    displayString = "{:04x}".format(value)
    
    # Break this string up into a list of four characters.
    displayList = list(displayString)
    
    # Map these four characters to four integer values by using the
    # integer parser (passing in base of 16)
    displayBytes = map(lambda x: int(x, 16), displayList)

    # Send the array of values to the PIC for display.
    self.pi.i2c_write_i2c_block_data(self._h, 0, displayBytes)
    
  def displayFloat2(self, value):
    """
    Display the given decimal values to two decimal places.
    """
    
    # Cap given value at 100
    value = value % 100
    
    # Goal: Given a floating point value, convert each digit into a byte.
    # So "12.34" becomes [1, 2, 3, 4]
    # There's probably a really clever Python way to do this I don't
    # know yet. The below feels very hacky.
    
    # 12.34 -> "12.34"
    displayString = "{:02.2f}".format(value)
    
    # "12.34" -> ["1", "2", ".", "3", "4"]
    displayList = list(displayString)
    
    # TODO: We don't have a way to display decimal point at the moment,
    # so the results are just the tens, ones, tenths, and hundredths
    # digits on the display.
    
    # ["1", "2", ".", "3", "4"] -> ["1", "2", "3", "4"]
    displayList.remove(".")
    
    # ["1", "2", "3", "4"] -> [1, 2, 3, 4]
    displayBytes = map(lambda x: int(x), displayList)
    
    # Send the array of values to the PIC for display.
    self.pi.i2c_write_i2c_block_data(self._h, 0, displayBytes)

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

  try:
    print("Press Control-C to exit program.")
    while True:
      celsius = s.temperature()
      farenheit = celsius * 1.8 + 32
      try:
        led.displayFloat2(farenheit)
      except Exception as err:
        if err.value == "I2C write failed":
          print("PIC has reset, waiting to retry.")
        else:
          raise
      time.sleep(0.25)
  except KeyboardInterrupt:
    pass
    
  print ()
  print ("Contro-C pressed, cleaning up and quitting.")

  pi.stop()

