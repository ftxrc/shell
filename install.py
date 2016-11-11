#!/usr/bin/env python3
from sys import argv

SHELLS = ['zsh', 'bash']

# Check which shell to configure.
if len(argv) == 2:
    # Shell given in argument.
    shell = argv[1]
else:
    # No shell given. Ask.
    shell = input("Shell (bash/zsh): ")

if shell not in SHELLS:
    print("Shell not found.")
    exit()

# Import that shell folder
setup = getattr(__import__(shell, fromlist=['setup']), 'setup')
setup.do()
