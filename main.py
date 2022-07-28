import os
import utils

# init

print('Hexo python-cli 1.0.0')
print('Copyright Lotuses-robot (https://github.com/Lotuses-robot)')
print('')
print('https://github.com/Lotuses-robot/HexoPythonCli')

while True:
    cmd = input('Hp> ')
    CmdList = cmd.split()
    if len(CmdList) == 0:
        continue
    if CmdList[0] == 'update' or CmdList[0] == 'u':
        utils.runExt('UploadOnly')
    elif CmdList[0] == 'new' or CmdList[0] == 'n':
        utils.runExt('UploadNewPost')
    elif CmdList[0] == 'list' or CmdList[0] == 'l':
        utils.runExt('PostList')
    elif CmdList[0] == 'listen':
        utils.runExt('GithubActionListen')
    elif CmdList[0] == 'delete' or CmdList[0] == 'd':
        utils.runExt('DeletePost')
    elif CmdList[0] == 'QUIT':
        os._exit(0)
    elif CmdList[0] == 'help' or CmdList[0] == 'h':
        print('%-15s%s' % ('update(u):', 'Upload all the changes.'))
        print('%-15s%s' % ('new(n):', 'Create a new post.'))
        print('%-15s%s' % ('list(l):', 'Show the list of the posts.'))
        print('%-15s%s' % ('listen:', ''))
        print('%-15s%s' % ('delete(d):', 'Delete the post. (Carefully)'))
        print('%-15s%s' % ('help(h):', 'The help of the commands.'))
        print('%-15s%s' % ('QUIT:', "Quit."))
        print('\nAlso, you can always input QUIT to quit in any mode.')
    else:
        print('unknow keywords: ' + CmdList[0])
    
    print('')