#! /usr/bin/env python2.7
import serial

def enabledports():
    import os
    if os.uname()[0] == 'Darwin':
        print('the system is Darwin\n')
        prefixes = ['cu.','tty.']
    else:
        print('the system is Linux\n')
        prefixes = ['ttyACM','ttyUSB']
    port_lists = []
    devs_lists = os.listdir('/dev')
    for devs_name in devs_lists:
        for prefix in prefixes:
            if prefix in devs_name:
                path = os.path.join('/dev', devs_name)
                port_lists.append(path)
    return port_lists

def abledports(ports_lists):
    abledports_lists = []
    for port in ports_lists:
        _ser = serial.Serial()
        _ser.port = port
        try:
            _ser.open()
            if _ser.isOpen():
                abledports_lists.append(port)
        except Exception:
            pass
    return abledports_lists

if __name__ == '__main__':
    print abledports(enabledports())
