#!/usr/bin/env python3.5
import blinkt
import signal

blinkt.set_clear_on_exit(False)
blinkt.set_all(0, 255, 0)
blinkt.show()
signal.pause()
