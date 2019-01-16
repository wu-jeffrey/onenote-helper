# import win32gui
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

# TODO: Refactor in to general method
def keypress(event):
    """Simulate keys"""
    keyboard.press('a')
    print(event)

def alttab():
  keyboard.press(Key.alt)
  keyboard.press(Key.tab)
  keyboard.release(Key.alt)
  keyboard.release(Key.tab)
  time.sleep(0.2)

def copy(event):
  alttab()
  with keyboard.pressed(Key.ctrl.value):
    keyboard.press('c')
    time.sleep(0.2)
    keyboard.release('c')

def paste(event):
  alttab()
  with keyboard.pressed(Key.ctrl.value):
    keyboard.press('v')
    time.sleep(0.2)
    keyboard.release('v')

def cut(event):
  alttab()
  with keyboard.pressed(Key.ctrl.value):
    keyboard.press('x')
    time.sleep(0.2)
    keyboard.release('x')

def undo(event):
  alttab()
  with keyboard.pressed(Key.ctrl.value):
    keyboard.press('z')
    time.sleep(0.2)
    keyboard.release('z')

def redo(event):
  alttab()
  with keyboard.pressed(Key.ctrl.value):
    keyboard.press('y')
    time.sleep(0.2)
    keyboard.release('y')