import math

diameter = int(input())
sides = list(map(int, input().split()))
if diameter <= min(*sides):
  print("S")
else:
  print("N")

