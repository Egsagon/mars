import json
from os import popen, system

keys = ['glyph', 'header', 'temp', 'wind']
glyhps = ['盛', '', '', '殺', '', '']


res = popen('curl wttr.in/paris?format="%c|%C|%t|%w"').read().split('|')

# TODO: convert emoji to iosveka glyph

s = res[0].lower()

if 'sun' in s: res[0] = glyhps[0]
elif 'rain' in s: res[0] = glyhps[-1]
elif 'cloud' in s: res[0] = glyhps[3]
else: res[0] = glyhps[1]

print(json.dumps(dict(zip(keys, res))))