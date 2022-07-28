import os
import utils
Layout = 'post'
Title = input('Title: ')
if Title == 'QUIT':
    os._exit(1)
utils.new(Layout, Title)
Title = Title.replace(' ', '-')
os.system('code source/_posts/%s.md' % Title)
utils.runExt('UploadOnly')