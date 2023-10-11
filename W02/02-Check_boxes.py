# File: 02-Check_boxes.py
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse111-course/lesson02/check.html
import math

itens = int(input("Enter the number of itens: ") or 0)
itens_per_box = int(input("Enter the number of itens per box: ") or 1)

boxes = math.ceil(itens / itens_per_box)

#Doing the calculation without math.ceil function
boxes2 = int(itens / itens_per_box)
if (itens % itens_per_box) > 0:
    boxes2 += 1 

print(f"\nFor {itens} items, packing {itens_per_box} items in each box, you will need {boxes} boxes.")

print(f"\nFor {itens} items, packing {itens_per_box} items in each box, you will need {boxes2} boxes.")