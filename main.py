#!/usr/bin/python3
# https://atcoder.jp/contests/abc137/tasks/abc137_a
str=input().split()
A=int(str[0])
B=int(str[1])
print(max(A+B,A-B,A*B))
