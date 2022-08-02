import os
blogLocation = 'D:/Robot/C++/MyBlog/'
cwdLocation = 'D:/Robot/C++/myCode/Python/HexoPythonCli_backup/'

def runExt(Name):
    nowCWD = os.getcwd()
    os.chdir(cwdLocation)
    os.system('python ' + Name + '.py')
    os.chdir(nowCWD)

def chdir(type : int): # true is blogLoca, false is workLoca
    if type == 1:
        os.chdir(blogLocation)
    if type == 0:
        os.chdir(cwdLocation)
    if type == 2:
        os.chdir(blogLocation)
        os.chdir('source/_posts/')

def clean():
    nowCWD = os.getcwd()
    chdir(True)
    os.system('hexo clean')
    os.chdir(nowCWD)

def push():
    nowCWD = os.getcwd()
    chdir(True)
    clean()
    os.system('hexo g -d')
    os.chdir(nowCWD)

def new(Layout, Title):
    nowCWD = os.getcwd()
    chdir(True)
    os.system('hexo new %s "%s"' % (Layout, Title))
    os.chdir(nowCWD)

