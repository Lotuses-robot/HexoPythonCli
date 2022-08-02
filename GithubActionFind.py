import requests
import time
import warnings
warnings.filterwarnings("ignore")
s = requests.session()
s.keep_alive = False
link = "https://github.com/***/***/actions/"

headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71"
}

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

raw = s.get(link, headers = headers, verify = False).text 

l = findall(raw, '/Lotuses-robot/lotuses-robot.github.io/actions/runs/', add = True)
id = getlast(raw, l[0], '"')
print(id)