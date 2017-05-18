#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ByStudent'
import sys
def RSA_Commod(e1,e2,c1,c2,n):
  def gcd(a, b):
    #求最大公约数
    if a == 0:
      x, y = 0, 1;
      return (b, x, y);
    tup = gcd(b % a, a)
    d = tup[0]
    x1 = tup[1]
    y1 = tup[2]
    x = y1 - (b / a) * x1
    y = x1
    return (d, x, y)
  def find_any_solution(a, b, c):
    # 解决 a*x0 + b*y0 = c
    tup = gcd(abs(a), abs(b))
    g = tup[0]
    x0 = tup[1]
    y0 = tup[2]
    if c % g != 0:
      return (False, x0, y0)
    x0 *= c / g
    y0 *= c / g
    if a < 0:
      x0 *= -1
    if b < 0:
      y0 *= -1
    return (True,x0,y0)
  sys.setrecursionlimit(5000)
  (x, a1, a2) = find_any_solution(e1, e2, 1)
  if a1 < 0:
      # 求逆
      (x, c1, y) = find_any_solution(c1, n, 1)
      a1 = -a1
  if a2 < 0:
      (x, c2, y) = find_any_solution(c2, n, 1)
      a2 = -a2
  m = (pow(c1, a1, n) * pow(c2, a2, n)) % n
  return "M="+str(m)