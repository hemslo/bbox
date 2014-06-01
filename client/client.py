#!/usr/bin/env python

from ws4py.client import WebSocketBaseClient
from ws4py.manager import WebSocketManager
from ws4py import format_addresses, configure_logger
import pygame

logger = configure_logger()

m = WebSocketManager()


class EchoClient(WebSocketBaseClient):

    def __init__(self, url, client):
        super(EchoClient, self).__init__(url)
        self.client = client

    def handshake_ok(self):
        logger.info("Opening %s" % format_addresses(self))
        m.add(self)

    def received_message(self, msg):
        logger.info(str(msg))
        signal = int(str(msg))
        if signal:
            self.client.play(signal - 1)


class Client(object):

    def __init__(self):
        pygame.mixer.init()
        audios = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Si']
        self.musics = [pygame.mixer.Sound(n + '.wav') for n in audios]
        self.session = requests.Session()

    def play(self, index):
        pygame.mixer.find_channel().queue(self.musics[index])

    def loop(self):
        try:
            m.start()
            client = EchoClient('ws://192.168.0.157:8090/ws', self)
            client.connect()

            while True:
                for ws in m.websockets.itervalues():
                    if not ws.terminated:
                        break
                else:
                    break
        except KeyboardInterrupt:
            m.close_all()
            m.stop()
            m.join()


def main():
    client = Client()
    client.loop()


if __name__ == '__main__':
    main()
