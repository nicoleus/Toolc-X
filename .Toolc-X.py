# Tool Name :- Tool Kit
# Author :- Ijen Sinaga
# Date :- 22/09/2019
# Powered By :- Nicoleus F Sitorus

import sys
import os
from modules.logo import exit
from modules.menu import ToolcX

class chk(object):
  def chos(self):
    if "linux" in sys.platform:
      # Running Toolc-X on linux ....
      pass
    elif "darwin" in sys.platform:
      pass
      # print("Sorry, its not available for mac right now...")
      ex()
    elif "win" in sys.platform:
      print("Sorry, its not available for windows right now...")
      ex()
    else:
      print("If Tool-X not support for \'%s\' right now !!!" %sys.platform)

def Tool_X():
  try:
	chk().chos()
	ToolcX()

  except KeyboardInterrupt:
	exit()
Toolc_X()
