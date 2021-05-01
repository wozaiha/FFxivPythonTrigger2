from sys import platform, version_info
from asyncio import set_event_loop_policy, WindowsSelectorEventLoopPolicy

if platform == "win32" and version_info >= (3, 8, 0):
    set_event_loop_policy(WindowsSelectorEventLoopPolicy())

from FFxivPythonTrigger import *

Logger.print_log_level = Logger.DEBUG
try:
    register_module("SocketLogger")

    # core
    register_modules([
        "HttpApi",
        "ChatLog",
        "XivMemory",
        "XivMagic",
        "Command",
    ])

    # functions
    register_modules([
        "MoPlus",
        "CutsceneSkipper",
        "SuperJump",
        "ActorQuery",
        "Zoom",
        "Teleporter",
        "XivCombo",
        # "ACTLogLines",
        "SendKeys"
    ])

    register_modules([
        "SpeedHack",
        #"DebugExec",
        "SkillAniUnlocker",
        "XivCombat"
    ])
    start()
except Exception:
    pass
finally:
    close()
