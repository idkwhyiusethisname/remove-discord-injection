'''
OG CODE FROM RANDOM DISCORD INJECTION 

MODIFIED BY REGENXY DONT REMOVE THIS CRADIT SKIDDER 

CONTACT : t.me/Notregenxy

'''

import requests, os
from re import search, findall

def urmom():

    def get_core(dir):
        for file in os.listdir(dir):
            if search(r"app-+?", file):
                modules = dir + "\\" + file + "\\modules"
                #print(modules)
                if not os.path.exists(modules):
                    continue
                for file in os.listdir(modules):
                    if search(r"discord_desktop_core-+?", file):
                        core = modules + "\\" + file + "\\" + "discord_desktop_core"
                        if not os.path.exists(core + "\\index.js"):
                            continue
                        return core, file

    appdata = os.getenv("LOCALAPPDATA")
    discord_dirs = [
        appdata + "\\Discord",
        appdata + "\\DiscordCanary",
        appdata + "\\DiscordPTB",
        appdata + "\\DiscordDevelopment",
    ]

    code = "module.exports = require('./core.asar');"

    for dir in discord_dirs:
        if not os.path.exists(dir):
            continue

        if get_core(dir) is not None:
            with open(
                get_core(dir)[0] + "\\index.js", "w", encoding="utf-8"
            ) as f:
                f.write(
                    (code)
                )
            print("done press enter to close")
            os.system('pause')
            os.system('exit')

print(''' 

╔═╗╦ ╦╔═╗╦╔═  ╔╦╗╦╔═╗╔═╗╔═╗╦═╗╔╦╗  ╦╔╗╔ ╦╔═╗╔═╗╔╦╗╦╔═╗╔╗╔
╠╣ ║ ║║  ╠╩╗   ║║║╚═╗║  ║ ║╠╦╝ ║║  ║║║║ ║║╣ ║   ║ ║║ ║║║║
╚  ╚═╝╚═╝╩ ╩  ═╩╝╩╚═╝╚═╝╚═╝╩╚══╩╝  ╩╝╚╝╚╝╚═╝╚═╝ ╩ ╩╚═╝╝╚╝

''')
urmom()