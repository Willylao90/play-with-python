#!/usr/bin/python

from os import system
import curses

def get_param(prompt_string):
   screen.clear()
   screen.border(0)
   screen.addstr(2,2, prompt_string)
   screen.refresh()
   input = screen.getstr(10,10,60)
   return input

def execute_cmd(cmd_string):
   system("clear")
   a = system(cmd_string)
   print("")
   if a == 0:
      print("Command executed correctly")
   else:
      print("Command failed")
   input("Press enter")
   print("")

x = 0
screen = curses.initscr()

while x != ord('4'):

   screen.border(0)
   screen.addstr(2,2,"Please enter a number...")
   screen.addstr(4,4,"1 - Add a user",curses.A_BLINK)
   screen.addstr(5,4,"2 - Restart Apache",curses.A_STANDOUT)
   screen.addstr(6,4,"3 - Show disk space",curses.A_BOLD)
   screen.addstr(7,4,"4 - Exit",curses.A_DIM)
   screen.refresh()

   x = screen.getch()

   if x == ord('1'):
      username = get_param("Enter the username")
      homedir = get_param("Enter the home dir, eg /home/name")
      groups = get_param("Enter commawoifdjoiwdf")
      shell = get_param("Enter shellwodfinwdfo")
      curses.endwin()
      execute_cmd("echo hello")
   if x == ord('2'):
      curses.endwin()
      execute_cmd("echo hello2")
   if x == ord('3'):
      curses.endwin()
      execute_cmd("df -h")

   screen.clear()

curses.endwin()
