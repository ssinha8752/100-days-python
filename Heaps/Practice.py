def rev(x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        reversed_num = int(str(abs(x))[::-1])
        return sign * reversed_num


print(rev(-120))