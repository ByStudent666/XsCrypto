#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ByStudent'
from zhanzhuanxc import zhanzhuanxc
def RSA(p,q,e,n,c):
    d = zhanzhuanxc(p,q,e)
    m = pow(c,d,n)
    return "d=" + str(d) + "\n" + "m=" + str(m)
