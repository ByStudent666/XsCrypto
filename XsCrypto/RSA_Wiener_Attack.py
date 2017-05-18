#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ByStudent'
import RSA_Wiener_ContinuedFractions, RSA_Wiener_Arithmetic
import sys
sys.setrecursionlimit(1000000)
def RSA_Wiener(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = RSA_Wiener_ContinuedFractions.rational_to_contfrac(e, n)
    convergents = RSA_Wiener_ContinuedFractions.convergents_from_contfrac(frac)

    for (k,d) in convergents:

        # check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            discr = s*s - 4*n
            if(discr >= 0):
                t = RSA_Wiener_Arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    return "d = " + str(d)


# n = 310417953704722170730847224402877983815425243802949146921747155554873214220856824312098961643471840575991636613043700912852694476430642621109657293199766030858364981594359341335457943511388291654144608627164424697545853589150385759857708455254761227678476750080293606809444462895661894497915336651794981901683
# e = 180160219817657029643391514538629205160228298622505654076129556003630962924040643558658232436259668646427759588151297967578950689360985724312726411880635697242206899247553123368979139238838216404056134080086977722515560207477455248034027633490880147280702252198966243510960816978036425871522668587833586334027
# print RSA_Wiener(e,n)





