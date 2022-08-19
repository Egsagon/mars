# ======================================== #
# Script that parses the output of xdotool #
# to get the current number of workspaces. #
# ======================================== #

from os import popen
from json import dumps

empty = ''

# Fetch
wks = [(n + 1, popen(f'xdotool search --desktop {n} --class ".*"').readlines()) for n in range(10)]
cur = str(int(popen('xdotool get_desktop').read().strip()) + 1)


# Crop
res = [n if len(wk) else empty for n, wk in wks]
if not cur in res: res[int(cur) - 1] = cur
while res[-1] == empty: res.pop(-1)


# Send
res = [{'name': wk, 'focused': wk == cur} for wk in res]
print(dumps(res))