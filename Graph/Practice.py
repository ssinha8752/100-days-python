import math


def constructRectangle(area):
    L=math.sqrt(area)
    while L>0:
        if area%L==0:
            W=area//L
            if L>=W:
                return [int(L),int(W)]
        L-=1
    return []

print(constructRectangle(4))