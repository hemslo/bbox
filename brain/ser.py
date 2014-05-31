#!/usr/bin/env python2.7
import sys, os, serial, threading
from string import strip
try:
    from serial.tools.list_ports import comports
except ImportError:
    comports = None

DEFAULT_PORT = None
DEFAULT_BAUDRATE = 9600
DEFAULT_RTS = None
DEFAULT_DTR = None


class serers(object):

    def __init__(self, port, baudrate):
        try:
            self.ser = serial.Serial()
            self.ser.port = port
            self.ser.baudrate = baudrate
            if not self.ser.isOpen():
                self.ser.open()
            self.start()
        except serial.SerialException:
            raise

    def start(self):
        self.alive = True
        try:
            self._start_reader()
            #self._start_writer()
        except threading.ThreadError:
            raise

    def _start_reader(self):
        self._reader_alive = True
        self.reader_thread = threading.Thread(target=self.reader,)
        self.reader_thread.setDaemon(False)
        self.reader_thread.start()

    def _start_writer(self):
        self._writer_alive = True
        self._writer_thread = threading.Thread(target=self.writer)
        self._writer_thread.setDaemon(True)
        self.reader_thread.start()

    def reader(self):
        try:
            while self.alive and self._reader_alive:
                self.text = self.ser.readline()
        except serial.SerialException:
            raise


if __name__ == '__main__':
    port = '/dev/tty.usbmodem1411'
    baudrate = 115200
    serers(port,baudrate)
