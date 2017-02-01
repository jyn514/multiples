def Descending_Order(num):
    order = list(str(num))
    order.sort()
    order.reverse()
    num = ''.join(order)
    return int(num)
