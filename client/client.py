#!/usr/bin/env python

import pygame
import time
import requests


class Client(object):

    def __init__(self):
        pygame.mixer.init()
        audios = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Si']
        self.musics = [pygame.mixer.Sound(n + '.wav') for n in audios]
        self.session = requests.Session()

    def play(self, index):
        pygame.mixer.find_channel().queue(self.musics[index])

    def fetch(self):
        r = self.session.get('http://192.168.0.157/get')
        return int(r.text)

    def loop(self):
        while True:
            signal = self.fetch()
            if signal:
                self.play(signal - 1)
            time.sleep(0.2)


def main():
    client = Client()
    client.loop()


if __name__ == '__main__':
    main()
