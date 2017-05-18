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

# n = 23927411014020695772934916764953661641310148480977056645255098192491740356525240675906285700516357578929940114553700976167969964364149615226568689224228028461686617293534115788779955597877965044570493457567420874741357186596425753667455266870402154552439899664446413632716747644854897551940777512522044907132864905644212655387223302410896871080751768224091760934209917984213585513510597619708797688705876805464880105797829380326559399723048092175492203894468752718008631464599810632513162129223356467602508095356584405555329096159917957389834381018137378015593755767450675441331998683799788355179363368220408879117131
# e1 = 12900676191620430360427117641859547516838813596331616166760756921115466932766990479475373384324634210232168544745677888398849094363202992662466063289599443
# e2 = 7718975159402389617924543100113967512280131630286624078102368166185443466262861344357647019797762407935675150925250503475336639811981984126529557679881059
# c1 = 21050269275063947324803736152108894960122834143453871907171889706069292182017441714340845630199726901695235325331162743215493028971840698886694652237493693233562510612601511933544385719792087669184188577257426314936474401349404047895204434845607471209321070641238142431886829644762263880353945176747824295861773784296485143574724157411701384084642412647460092918280364241325796565550082230981630789430160325171428941325164099673663196407439039250584955677662418429817961970120515321431370774024177287738150427369478834235920832376988907441000788444734564377426364934553237120525037142991363604288054944470726414900627
# c2 = 6450984114106657233418272201667817010768003811756575350064243420877391894365353747069532492005631706505537625725185847890305749446294465596475368239792417224814540364037312829242769458491279070913902496186534058889668940647382402026752270529611203130010362248980055145615851893813096026876153582356477939111070601783786491932490927153302914437902634211112496671182359706019466893672546770021703829360700572739573729669067501821556528672020020952478557547749543804975103585024833805220345272127706528601277722403999642507250963456431679257566679612247350741121349306893059826143033437954988365464143578911826517264933
# print RSA_Commod(e1,e2,c1,c2,n)
