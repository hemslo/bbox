#! /usr/bin/env python2.7
import sys, os, serial, threading
import string
from string import strip
from time import time
try:
    from serial.tools.list_ports import ports
except ImportError:
    comports = None

cache = str(time()) + '#' + '0'


class serers(object):

    def __init__(self,port='/dev/tty.usbmodem1411', baudrate=115200):
        try:
            self.ser = serial.Serial()
            self.ser.port = port
            self.ser.baudrate = baudrate
            if not self.ser.isOpen():
                self.ser.open()
            self.start()
        except Exception:
            raise

    def start(self):
        self.alive = True
        try:
            self._start_reader()
        except threading.ThreadError:
            raise

    def _start_reader(self):
        global cache
        try:
            self._reader_alive = True
            self.reader_thread = threading.Thread(target = self.reader)
            self.reader_thread.setDaemon(False)
            self.reader_thread.start()
        except KeyboardInterrupt:
            raise

    def reader(self):
        global cache
        try:
            ptime = time()
            while self.alive and self._start_reader:
                self.text = self.ser.readline()
                cache = (str(time())+'#'+self.text)
        except serial.SerialException, KeyboardInterrupt:
            self.alive = False
            raise

    def get(self):
        global cache
        try:
            #cache = str(time())+'#'+'0'
            ptime, sound = cache.split('#')
            if time() - string.atof(ptime) < 1:
                return (string.atoi(sound) + 70000)/20000
            else:
                return '0'
        except Exception:
            raise
