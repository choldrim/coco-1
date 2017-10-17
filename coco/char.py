#!coding: utf-8

BACKSPACE_CHAR = {b'\x08': b'\x08\x1b[K', b'\x7f': b'\x08\x1b[K'}
ENTER_CHAR = [b'\r', b'\n', b'\r\n']
UNSUPPORTED_CHAR = {b'\x15': 'Ctrl-U', b'\x0c': 'Ctrl-L', b'\x05': 'Ctrl-E'}
CLEAR_CHAR = b'\x1b[H\x1b[2J'
BELL_CHAR = b'\x07'
