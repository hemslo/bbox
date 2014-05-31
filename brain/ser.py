#! /usr/bin/env python2.7
import sys, os, serial, threading
from string import strip
from time import time
try:
    from serial.tools.list_ports import ports
except ImportError:
    comports = None

cache = []


class serers(object):

    def __init__(self,port='/dev/tty.submodem1411', baudrate=115200):
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
        global cahce
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
            while self.alive and self._start_reader:
                self.text = self.ser.readline()
                cache.append(str(time())+'#'+self.text)
        except serial.SerialException, KeyboardInterrupt:
            raise

    def get(self):
        global cache
        try:
            return cache.pop()
        except Exception:
            return '0'

