#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ByStudent'
from zhanzhuanxc import zhanzhuanxc
def RSA(p,q,e,n):
    phi = (p-1) * (q-1)
    d = zhanzhuanxc(p,q,e)
    c = 0xdc2eeeb2782c
    m = pow(c,d,n)
    return "d=" + str(d) + "\n" + "m=" + str(m)
n = 322831561921859
e = 65537
p=3487583947589437589237958723892346254777
q=8767867843568934765983476584376578389
print RSA(p,q,e,n)