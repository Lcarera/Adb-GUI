import os
import time


ente =r'adb shell input keyevent "KEYCODE_ENTER"'
tab =r'adb shell input keyevent "KEYCODE_TAB"'
cd = r'\Users\QT\Desktop\platform-tools'
path =r'\Users\QT\Desktop\Install'

def tabear(times):
    i=0
    while i != times:
        os.system(tab)
        time.sleep(1)
        i += 1

def enter():
    os.system(ente)
    time.sleep(5)


def open_app(app):
    os.system(f'adb shell monkey -p {app} 1')
    time.sleep(10)


def input_text(text):
    os.system(f'adb shell input text {text}')
    time.sleep(3)


def uninstall(app):
    os.system(f"adb uninstall {app}")


def connect(ip,puerto):
    os.system(f"adb connect 192.168.{ip}.{puerto}")
    time.sleep(1)
    os.system("adb root")
    time.sleep(1)
    os.system("adb remount")
    time.sleep(1)


def reboot():
    os.system("adb reboot")


def install():
    for file in os.listdir(path):
        fullpath=os.path.join(path, file)
        if os.path.isfile(fullpath):
            os.system(f"adb install -r {fullpath}")

def new_pack(pack):
    app = pack
def disconn():
    os.system("adb disconnect")
