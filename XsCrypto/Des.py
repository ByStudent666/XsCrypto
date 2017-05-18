#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ByStudent'
from Crypto.Cipher import DES
def de_DES(c,key,mode,iv=0):
    """
    :param c: 密文
    :param key: 密钥(8byte)
    :param mode: 加密方式（ecb/cbc）
    :param iv: iv
    :return: 明文
    """
    if mode == 'ecb':
        cipher = DES.new(key, DES.MODE_ECB)
        m = cipher.decrypt(c)
        return m
    else:
        cipher = DES.new(key, DES.MODE_CBC,iv)
        m = cipher.decrypt(c)
        return m
def de_DES_baopo(c,key1=0,key2_l=0):
    """
    在已知部分key或不知key的情况下爆破key解密DES
    :param c: 密文
    :param key1: 已知key
    :param key2_l: 未知key长度
    :return: 明文
    """
    if key2_l == 1:
        for x1 in range(256):
            key = str(key1) + chr(x1)
            cipher = DES.new(key, DES.MODE_ECB)
            m = cipher.decrypt(c)
            return "key="+str(key)+'\n'+"m="+m
    elif key2_l == 2:
        for x1 in range(256):
            for x2 in range(256):
                key = str(key1) + chr(x1) + chr(x2)
                cipher = DES.new(key, DES.MODE_ECB)
                m = cipher.decrypt(c)
                return "key=" + str(key) + '\n' + "m=" + m
    elif key2_l == 3:
        for x1 in range(256):
            for x2 in range(256):
                for x3 in range(256):
                    key = str(key1) + chr(x1) + chr(x2) + chr(x3)
                    cipher = DES.new(key, DES.MODE_ECB)
                    m = cipher.decrypt(c)
                    return "key=" + str(key) + '\n' + "m=" + m
    elif key2_l == 4:
        for x1 in range(256):
            for x2 in range(256):
                for x3 in range(256):
                    for x4 in range(256):
                        key = str(key1) + chr(x1) + chr(x2) + chr(x3) + chr(x4)
                        cipher = DES.new(key, DES.MODE_ECB)
                        m = cipher.decrypt(c)
                        return "key=" + str(key) + '\n' + "m=" + m
    elif key2_l == 5:
        for x1 in range(256):
            for x2 in range(256):
                for x3 in range(256):
                    for x4 in range(256):
                        for x5 in range(256):
                            key = str(key1) + chr(x1) + chr(x2) + chr(x3) + chr(x4) + chr(x5)
                            cipher = DES.new(key, DES.MODE_ECB)
                            m = cipher.decrypt(c)
                            return "key=" + str(key) + '\n' + "m=" + m
    elif key2_l == 6:
        for x1 in range(256):
            for x2 in range(256):
                for x3 in range(256):
                    for x4 in range(256):
                        for x5 in range(256):
                            for x6 in range(256):
                                key = str(key1) + chr(x1) + chr(x2) + chr(x3) + chr(x4) + chr(x5) + chr(x6)
                                cipher = DES.new(key, DES.MODE_ECB)
                                m = cipher.decrypt(c)
                                return "key=" + str(key) + '\n' + "m=" + m
    elif key2_l == 7:
        for x1 in range(256):
            for x2 in range(256):
                for x3 in range(256):
                    for x4 in range(256):
                        for x5 in range(256):
                            for x6 in range(256):
                                for x7 in range(256):
                                    key = str(key1) + chr(x1) + chr(x2) + chr(x3) + chr(x4) + chr(x5) + chr(x6) +chr(x7)
                                    cipher = DES.new(key, DES.MODE_ECB)
                                    m = cipher.decrypt(c)
                                    return "key=" + str(key) + '\n' + "m=" + m
    else:
        for x1 in range(256):
            for x2 in range(256):
                for x3 in range(256):
                    for x4 in range(256):
                        for x5 in range(256):
                            for x6 in range(256):
                                for x7 in range(256):
                                    for x8 in range(256):
                                        key = str(key1) + chr(x1) + chr(x2) + chr(x3) + chr(x4) + chr(x5) + chr(x6) +chr(x7) + chr(x8)
                                        cipher = DES.new(key, DES.MODE_ECB)
                                        m = cipher.decrypt(c)
                                        return "key=" + str(key) + '\n' + "m=" + m

def en_DES(m,key,mode,iv=0):
    """
    :param m: 明文
    :param key: 密钥(8byte)
    :param mode: 加密方式（ecb/cbc）
    :param iv: iv
    :return: 密文
    """
    if mode == 'ecb':
        message = DES.new(key, DES.MODE_ECB)
        c = message.encrypt(m)
        return c
    else:
        message = DES.new(key, DES.MODE_CBC,iv)
        c = message.encrypt(m)
        return c






