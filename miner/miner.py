#!/usr/bin/python

import random, math, time, cProfile
from tkinter import *

class Brain():
   def __init__(self):
      pass

class Material():

   def __init__(self, colour='grey50', weight=20, shape='rect', value=1):
      self.colour = colour
      self.weight = weight
      self.shape = shape
      self.value = value

      self.IsMined = False
      self.ShowMined = True
      return

   def mine(self):
      result = self.value
      if self.IsMined is False:
         self.IsMined = True
         self.value = 0
         self.weight = 0
         self.colour = 'black'
      return result

class Stone(Material):
   pass

class Ore(Material):

   def __init__(self, colour='light blue', weight=50, shape='rect', value=20):
      self.colour = colour
      self.weight = weight
      self.shape = shape
      self.value = value

      self.IsMined = False
      self.ShowMined = True
      return



class Miner():

   def __init__(self, x, y, colour='blue'):
      self.x = x
      self.y = y
      self.colour = colour
      self.bad_count = 0
      self.bad_max = 5
      self.last_move = (0,0)
      return

   def got_ore (self, value):
      if value == 1 or value == 0:
         self.bad_count += 1
      else:
         self.bad_count = 0
      return

   def move(self, x, y):
      self.x = x
      self.y = y
      return

   def choose (self, values):
      around_miner = [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
      maxValue = max(values)
      index = [j for j, value in enumerate(values) if value == maxValue]

      if self.bad_count > self.bad_max:
         x, y = around_miner[random.choice(index)]
      else:
         if self.last_move != (0,0) and self.bad_count != 1:
            x, y = self.last_move
         else:
            x, y = around_miner[random.choice(index)]

      self.last_move = (x, y)
      x = self.x + x
      maxx = 99
      if x < 0 or x > maxx:
         x = self.x

      y = self.y + y
      if y < 0 or y > maxx:
         y = self.y
      self.move(x,y)
      return x, y


class Land():

   def __init__(self, x, y):
      self.x = x
      self.y = y
      self.maxx = x - 1
      self.maxy = y - 1
      self.land = [[Stone() for j in range(x)] for i in range(y)]
      return

   def place_material(self, material, x, y):
      tmp = self.land[y]
      tmp[x] = material
      self.land[y] = tmp
      return

   def whats_here(self, x, y):
      if x < 0 or x > l.maxx:
         x = miner.x
      if y < 0 or y > l.maxy:
         y = miner.y

      tmp = self.land[y]
      return tmp[x]

   def mine_here(self, x, y):
      return self.land[y][x].mine()

class Window():

   def __init__(self, miner, land, pixelwidth=10):
      self.miner = miner
      self.land = land
      self.mineditem = []
      self.pixelwidth = pixelwidth
      padding = 3*pixelwidth

      winx = (land.x*self.pixelwidth)+padding
      winy = (land.y*self.pixelwidth)+padding

      master = Tk()
      self.win = Canvas(master, width=winx, height=winy)
      self.win.pack()
      self.generate_land()
      self.refresh()
      return

   def place_miner(self):
      firstx = self.miner.x*self.pixelwidth
      firsty = self.miner.y*self.pixelwidth
      seconx = firstx+self.pixelwidth
      secony = firsty+self.pixelwidth

      self.win.create_rectangle(firstx, firsty, seconx, secony,\
                                        fill=miner.colour, width=0, tags='miner')
      return

   def generate_land(self):
      xpos = 0
      ypos = 0
      for y in self.land.land:
         tmp = y
         for x in tmp:
            firstx = xpos*self.pixelwidth
            firsty = ypos*self.pixelwidth
            seconx = firstx+self.pixelwidth
            secony = firsty+self.pixelwidth

            self.win.create_rectangle(firstx, firsty, seconx, secony,\
                                      fill=x.colour, width=0)

            xpos += 1
         xpos = 0
         ypos += 1
      return

   def update_land(self):
      xpos = 0
      ypos = 0
      item = 1
      for tmpy in self.land.land:
         for tmpx in tmpy:
            if tmpx.IsMined and tmpx.ShowMined:
               self.win.itemconfig(item, fill=tmpx.colour)
               tmpx.ShowMined = False
            item += 1
            xpos += 1
         xpos = 0
         ypos += 1

      return

   def refresh(self):
      self.update_land()
      self.win.delete(self.win.find_withtag('miner'))
      self.place_miner()
      self.win.update()
      return


around_miner = [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
miner = Miner(50,50)
l = Land(101, 101)
direction = [-1,1,0]
count = 0
for i in range(1000):
   if count > 0 and count < 100:
      lastx += random.choice(direction)
      lasty += random.choice(direction)
      for x in lastx, lasty:
         if x < 0:
            x = 0
         if x > 99:
            x = 99
      l.place_material(Ore(), lastx, lasty)
   else:
      count = 0
      lastx = random.randint(0,99)
      lasty = random.randint(0,99)
      l.place_material(Ore(), lastx, lasty)
   count += 1

win = Window(miner=miner, land=l, pixelwidth=5)


while(True):
   values = []

   for x, y in around_miner:
      x = miner.x + x
      y = miner.y + y

      values.append(l.whats_here(x, y).value)


   x, y = miner.choose(values)
   value = l.mine_here(x, y)
   miner.got_ore(value)
   win.refresh()
