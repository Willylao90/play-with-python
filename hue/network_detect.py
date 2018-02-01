#!/usr/bin/python

import nmap
import pprint

''' A module for detecting a particular device on a network '''

class Detector(object):
   ''' Class to detect a device on a network '''

   def __init__(self, mac, ip_range='192.168.1.0-255'):
      ''' Initialisation method

      mac - mac address of device as string
      '''

      self.mac = mac
      self.ip_range = ip_range
      self.net_map = nmap.PortScanner()
      return

   def is_present(self):
      ''' Returns whether the device is present on the network '''

      present = False

      net_dict = self.net_map.scan(self.ip_range, arguments='-sn')
      if 'scan' in net_dict:
         for add in net_dict['scan']:
            pprint.pprint(add)
            if 'mac' in net_dict['scan'][add]['addresses']:
               if net_dict['scan'][add]['addresses']['mac'] == self.mac:
                  present = True
                  print('Match!')
                  break
               else:
                  print('No Match - {} - {}'.format(self.mac,
                                                    net_dict['scan'][add]['addresses']['mac']))
            else:
               print('No MAC here!')
      else:
         print('Failed to scan!!')
      return present
