import configparser

def get(section,option):
    cf = configparser.ConfigParser()
    cf.read("D:\ProgramFiles\JetBrains\PyCharm 2019.1.1\projects\music\config.ini")
    return cf.get(section,option)