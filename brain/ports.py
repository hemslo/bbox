#! /usr/bin/env python2.7

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
if __name__ == '__main__':
    print enabledports()
