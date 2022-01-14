import os

commands = ["ipconfig /release", "ipconfig /renew", "netsh winsock reset", "netsh int ip reset", "ipconfig /flushdns"]

for command in commands:
    os.system(command)
