def largestTriangleArea(points):
    n = len(points)
    max_area = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Shoelace formula to calculate triangle area
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                area = abs((x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)) / 2
                max_area = max(max_area, area)

    return max_area


print(largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))