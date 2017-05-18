#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ByStudent'
from Crypto.Cipher import AES
def de_AES(c,key,mode,iv=0):
    """
    :param c: 密文
    :param key: 密钥
    :param mode: 加密方式（ecb/cbc）
    :param iv: iv
    :return: 明文
    """
    if mode == 'ecb':
        cipher = AES.new(key, AES.MODE_ECB)
        m = cipher.decrypt(c)
        return m
    else:
        cipher = AES.new(key, AES.MODE_CBC,iv)
        m = cipher.decrypt(c)
        return m
def en_AES(m,key,mode,iv):
    """
    :param m: 明文
    :param key: 密钥
    :param mode: 加密方式（ecb/cbc）
    :param iv: iv
    :return: 密文
    """
    if mode == 'ecb':
        message = AES.new(key, AES.MODE_ECB)
        c = message.encrypt(m)
        return c
    else:
        message = AES.new(key, AES.MODE_CBC,iv)
        c = message.encrypt(m)
        return c

# m = "The answer is no"
# key = "This is a key123"
# iv = "This is an IV456"
# c = en_AES(m,key,'cbc',iv)
# print c
# m = de_AES(c,key,'cbc',iv)
# print m
# #



import base64
s = 'mbZoEMrhAO0WWeugNjqNw3U6Tt2C+rwpgpbdWRZgfQI3MAh0sZ9qjnziUKkV90XhAOkIs/OXoYVw5uQDjVvgNA=='
iv = base64.b64decode(s)[:16]
c = base64.b64decode(s)
key = 'Qq4wdrhhyEWe4qBF'
print de_AES(c,key,mode='cbc',iv=iv)







