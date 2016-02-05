from src.common.constants.frontendconstants import *


def createurl(endpoint):
    return "{0}{1}:{2}/{3}/".format(PROTOCOL, HOST, PORT, endpoint)