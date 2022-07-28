# Github_Cookies = {
#     "_octo" : "GH1.1.2111284038.1649572031",
#     "_device_id" : "6f57292fb60f30ee61cf5c0b98e0bdb8",
#     "user_session" : "2n_wEpcFGv0b8r13F9lPAnRA8qvZBL_cLOOO_itFviUftOXx",
#     "__Host-user_session_same_site" : "2n_wEpcFGv0b8r13F9lPAnRA8qvZBL_cLOOO_itFviUftOXx",
#     "logged_in" : "yes",
#     "dotcom_user" : "Lotuses-robot",
#     "has_recent_activity" : "1",
#     "tz" : "Asia/Shanghai",
#     "_gh_sess" : "McIFeS2Ay6ycKY8cR96Y1%2BBvguF5LMZJhbQS%2BM37GhMuEq%2FkMtXFGclHYNqs5Ova24TaX2fMisuxpLBDq%2B11pjv98b0%2BV6q9cP7xJGMO9S4KWFPuM39t5oS%2FecFhsvUgd90QXAmcOLNKMqf4gJdT9aLSxOjBO0y9QRsKuZCszdNwXXQT2cvPcGJLTvnac2l2ajNRxaW2T2VidQhqlEakARAX8xqyXEn3--KLlE3zZmdw%2Bh1qm8--eqjv0YAGrfGALNvpNwCziw%3D%3D"
# }

headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71"
}

import requests
import time
import warnings
import os
warnings.filterwarnings("ignore")
s = requests.session()
s.keep_alive = False

def findall(str, word, bef = -1, add = False):
    # print(bef)
    ans = []
    it = str.find(word)
    while it != -1:
        if add == True:
            ans.append(it + len(word))
        else:
            ans.append(it)
        it = str.find(word, it + 1)
        if bef != -1 and it >= bef:
            break
    return ans

def getlast(str, index, word):
    if str.find(word, index + 1) == -1:
        return str[index :]
    return str[index : str.find(word, index)]

tot = 0
def getNameAndStatus(str, index):
    global tot
    l1 = findall(str, 'This ', index)
    stat = getlast(str, l1[-1], '"')
    name = getlast(str, index, '<')
    if stat.find('successfully') != -1:
        tot += 1
    return '%-25s%s' % (name + ': ', stat)

raw = s.get('https://github.com/Lotuses-robot/lotuses-robot.github.io/actions/', headers = headers, verify = False).text 
ll = findall(raw, '/Lotuses-robot/lotuses-robot.github.io/actions/runs/', add = True)
id = getlast(raw, ll[0], '"')

link = "https://github.com/Lotuses-robot/lotuses-robot.github.io/actions/runs/" + id

bt = time.time()

while True:
    try: 
        ret = s.get(link, headers = headers, timeout = 114514, verify = False).text
    except:
        pass
    # file = open('html', 'r', encoding = 'utf-8')
    # ret = file.read()
    # file.close()
    # print(ret)

    ct = time.time() - bt
    local_time = time.localtime(ct)
    secs = int((ct - int(ct)) * 1000)
    word = "[%s:%03d]" % (time.strftime("%M:%S", local_time), secs)

    os.system('cls')
    print(word)
    l = findall(ret, '<span class="css-truncate css-truncate-overflow">', add = True)
    if len(l) < 1:
        print("Project starting")
    if len(l) >= 1:
        tot = 0
        for loca in l:
            print('-', getNameAndStatus(ret, loca))
        if tot == len(l):
            os._exit(0)
    
    time.sleep(1)