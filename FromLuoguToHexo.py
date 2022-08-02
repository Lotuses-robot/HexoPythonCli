cookies = {
    'UM_distinctid' : '',
    '__client_id' : '',
    '_uid' : ''
}
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'
}


import requests
s = requests.session()

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

def find(str, word, index):
    return str.find(word, index)

def getlast(str, index, word):
    if str.find(word, index + 1) == -1:
        return str[index :]
    return str[index : find(str, word, index)]

import os
import utils
import math
import time

l = []

def content(link):
    ret = s.get(link, headers = headers, cookies = cookies)
    while ret.status_code != 200:
        ret = s.get(link, headers = headers, cookies = cookies)
    return ret

ret = content('https://www.luogu.com.cn/blogAdmin/article/list?pageType=list').text
Loca = ret.find('共有') + len('共有')
sz = math.ceil(int(getlast(ret, Loca, '\n')) / 20)

for i in range(1, sz + 1):
    ret = content('https://www.luogu.com.cn/blogAdmin/article/list?pageType=list&page=' + str(i)).text
    lst = findall(ret, '/blogAdmin/article/edit/', add = True)
    for j in lst:
        l.append(getlast(ret, j, '"'))

print(l)
os.system("pause")

for id in l:
    link = 'https://www.luogu.com.cn/blogAdmin/article/edit/' + id
    ret = content(link).text

    Loca1 = ret.find('name="title"')
    Loca2 = ret.find('value="', Loca1) + len('value="')
    Title = getlast(ret, Loca2, '"')
    # print(Title)

    Loca1 = ret.find('name="identifier"')
    Loca2 = ret.find('value="', Loca1) + len('value="')
    id = getlast(ret, Loca2, '"')
    id = id.replace(' ', '-')

    Loca1 = ret.find('var articleContent = "') + len('var articleContent = "')
    details = getlast(ret, Loca1, '\n')
    details = details[:-2]
    details = details.encode('utf8').decode('unicode_escape')
    details = details.replace('\\/', '/')
    details = details.replace('---', '')
    # print(details)

    utils.chdir(True)
    os.system('hexo new post "%s" -p "%s"' % (Title, id))
    f = open(utils.blogLocation + ('source/_posts/%s.md' % id), 'a', encoding = 'utf-8')
    f.write('\n')
    f.write(details)
    f.close()

    print('Create new post <%s>(%s) done.' % (id, Title))
    print('')
    time.sleep(5)

utils.runExt('UploadOnly')