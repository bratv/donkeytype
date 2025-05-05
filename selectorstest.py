# Utility method for cli tools where user input does'nt get echoed back
# to user on a newline. Instead the program reads letter typed right
# away, without any reaction or change to the terminal.

import sys
import termios
import tty

def mygetch():
    orig = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin)
    result = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, orig)
    return result

