import os
import shutil

def path(s):
    p = os.path.dirname(os.path.realpath(__file__))
    return "%s/%s" % (p, s)

# http://stackoverflow.com/questions/1868714/how-do-i-copy-an-entire-directory-of-files-into-an-existing-directory-using-pyth
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def themes():
    if "ZSH" in os.environ:
        zsh_custom = "%s/custom" % os.environ['ZSH']
        zsh_themes = "%s/custom/themes" % os.environ['ZSH']

        print("Copying themes...")
        copytree(path('themes'), zsh_themes)
    else:
        print("$ZSH_CUSTOM not found.")
        print("Are you in bash, or have you installed oh-my-zsh yet?")
        exit()

def rc():
    print("Copying configuration...")
    zshrc = "%s/.zshrc" % os.path.expanduser('~')
    with open(zshrc, "a") as file:
        file.write(open(path('config.sh'), 'r').read())

def do():
    install = input("What to install? (all, themes, rc): ")
    if install == 'all':
        themes()
        rc()
    elif install == 'themes':
        themes()
    elif install == 'rc':
        rc()
    print("Done.")
