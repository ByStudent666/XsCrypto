#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ByStudent'
def convert(c, key, start = 'a', n = 26):
    a = ord(start)
    offset = ((ord(c) - a + key)%n)
    return chr(a + offset)
def en_caesar_26(str, key):
    """
    恺撒加密
    :param str: 待加密字符串
    :param key: 密钥
    :return: 加密后字符串
    """
    o = ""
    for c in str:
        if c.islower():
            o+= convert(c, key, 'a')
        elif c.isupper():
            o+= convert(c, key, 'A')
        else:
            o+= c
    return o
def de_caesar_26(str, key):
    """
    恺撒解密
    :param str: 待解密字符串
    :param key: 密钥
    :return: 解密后字符串
    """
    return En_caesar_26(str, -key)
def de_Caesar_26baopo(s):
    """
    爆破key(26位)
    """
    for key in range(25,-1,-1):
        c = De_caesar_26(s, key)
        print "ROT-" + str(26-key) + ": " + c

def en_Caesar_127(c,k):
    r=""
    for i in c:
        r += chr((ord(i)+k)%128)
    return r
def de_Caesar_127(c,k):
    r=""
    for i in c:
        r += chr((ord(i)-k)%128)
    return r
def de_Caesar_127baopo(c):
    result=[]
    for k in range(128):
        tmp=De_Caesar_127(c,k)
        result.append(tmp)
    return result
def en_Fence(m,k):
    """
    栅栏加密
    :param m: 明文
    :param k: 密钥
    :return: 密文
    """
    chip=[]
    for i in range(0,len(m),k):
        if i+k>=len(m):
            tmp_m=m[i:]
        else:
            tmp_m=m[i:i+k]
        chip.append(tmp_m)
    c=""
    for i in range(k):
        for tmp_m in chip:
            if i < len(tmp_m):
                c+=tmp_m[i]
    return c
def de_Fence(c,k):
    """
    栅栏解密
    :param c: 密文
    :param k: 密钥
    :return: 明文
    """
    l=len(c)
    partnum=l/k
    if l%k!=0:
        partnum+=1
    m=[""]*l
    for i in range(0,l,partnum):
        if i+partnum>=len(c):
            tmp_c=c[i:]
        else:
            tmp_c=c[i:i+partnum]
        for j in range(len(tmp_c)):
            m[j*k+i/partnum]=tmp_c[j]
    return "".join(m)

def de_Fence_baopo(s):
    """
    栅栏解密爆破
    """
    elen = len(s)
    field = []
    for i in range(2, elen):
        if (elen % i == 0):
            field.append(i)
    for f in field:
        b = elen / f
        result = {x: '' for x in range(b)}
        for i in range(elen):
            a = i % b
            result.update({a: result[a] + s[i]})
        d = ''
        for i in range(b):
            d = d + result[i]
        print '分为\t' + str(f) + '\t' + '栏时，解密结果为：  ' + d




