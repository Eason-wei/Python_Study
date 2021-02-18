with open('text.txt', 'rb') as f:
    offset = -10
    i = 0
    while True:
        f.seek(offset, 2)
        data = f.readlines()
        print(i, "======>", data)
        if len(data) > 1:
            end_data = data[-1]
            print("最后一行是：", end_data.decode("utf-8"))
            break
        offset *= 2
        i += 1
