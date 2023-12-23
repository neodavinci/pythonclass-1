price = int(input('물건 가격:'))
num = int(input('구매 개수:'))
pay = int(input('지불 금액:'))
wh = pay - price * num

print(wh)