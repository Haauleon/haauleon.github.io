#!/usr/bin/env python
# !-*- coding:utf-8 -*-

class Menu:

    def __init__(self):
        pass

    def updateProject(self):
        pass

    def restartProject(self):
        pass

    def restartTomcat(self):
        pass

    def stopTomcat(self):
        pass

    def startTomcat(self):
        pass

    def methods(self):
        return(list(filter(lambda m: not m.startswith("__") and not m.endswith("__") and callable(getattr(self, m)), dir(self))))

if __name__ == '__main__':
    print(Menu().methods()) 
    # ['methods', 'restartProject', 'restartTomcat', 'startTomcat', 'stopTomcat', 'updateProject']