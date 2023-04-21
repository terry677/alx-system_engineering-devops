from fabric.api import *

env.use_ssh_config = True

def connect():
    env.hosts = ['web2']

def copy():
    put('signature.key')

def copy1():
    put('pri_key')
