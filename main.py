#!/usr/bin/python3
# https://atcoder.jp/contests/abc137/tasks/abc137_a
import sys
str=input()
str2=str.split()
A=int(str2[0])
B=int((str2[1]))
AplusB=A+B
AminusB=A-B
AxB=A*B
print(max(AplusB,AminusB,AxB))
