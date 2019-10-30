def func_task2(a=-1, b=-6, c=-12, d=-7):
    result = []
    for x in range(-100, 100):
        if (a * (x ** 3) + b * (x ** 2) + (c * x) + d) == 0:
            result.append(x)
            return result


if __name__ == "__main__":

    a, b, c, d = [int(i) for i in input().split()]
    func_task2(a, b, c, d)
