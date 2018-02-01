import smbus
import time

class I2C_Device:
   ''' I2C device object '''
   def __init__(self, addr, port=1):
      self.addr = addr
      self.bus = smbus.SMBus(port)

   def write_cmd(self, cmd):
      '''Write a single command'''
      self.bus.write_byte(self.addr, cmd)
      time.sleep(0.0001)
               
   def write_cmd_arg(self, cmd, data):
      '''Write a command and argument'''
      self.bus.write_byte_data(self.addr, cmd, data)
      time.sleep(0.0001)

   def write_block_data(self, cmd, data):
      '''Write a block of data'''
      self.bus.write_block_data(self.addr, cmd, data)
      time.sleep(0.0001)

   def read(self):
      '''Read a single byte'''
      return self.bus.read_byte(self.addr)

   def read_data(self, cmd):
      '''Read a byte of data'''
      return self.bus.read_byte_data(self.addr, cmd)

   def read_block_data(self, cmd):
      '''Read a block of data'''
      return self.bus.read_block_data(self.addr, cmd)
