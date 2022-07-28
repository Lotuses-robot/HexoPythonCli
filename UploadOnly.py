import os
import time
import utils

while True:
    t = input('Now upload? Please input "UPLOAD" to continue, "QUIT" to quit: ')
    if (t == 'UPLOAD') : break
    if (t == 'QUIT') : os._exit(1)

utils.push()
print('Waiting for 5 seconds')
time.sleep(5)
utils.runExt('GithubActionListen')