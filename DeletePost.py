import utils
import os
import PostList as pl
List = pl.getRetList()
Title = input('Title: ')
if Title == 'QUIT':
    os._exit(1)
if Title.isdigit():
    Title = List[int(Title)]

while True:
    t = input('Really want to DELETE the post <%s>? Please input "DELETE" to continue, "QUIT" to quit: ' % Title)
    if (t == 'DELETE') : break
    if (t == 'QUIT') : os._exit(1)


utils.chdir(2)
Title = Title.replace(' ', '-')
try:
    os.remove(Title + '.md')
except:
    pass
try:
    os.removedirs(Title)
    os.rmdir(Title)
except:
    pass
utils.runExt('UploadOnly')