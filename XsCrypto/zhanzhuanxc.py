#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ByStudent'
def zhanzhuanxc(p,q,e):
    def egcd(a, b):
        x,y, u,v = 0,1, 1,0
        while a != 0:
            q, r = b//a, b%a
            m, n = x-u*q, y-v*q
            b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
        return gcd, x, y
    def modinv(a, m):
        gcd, x, y = egcd(a, m)
        if gcd != 1:
            return None  # modular inverse does not exist
        else:
            return x % m
    phi_n = (p - 1) * (q - 1)
    d = modinv(e, phi_n)
    return int(d)

# print zhanzhuanxc(18443,49891,19)


