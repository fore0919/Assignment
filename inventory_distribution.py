class Inventory_distribution:
    def order():
        try:
            order_list = {}
            item = ['사과', '배', '오렌지', '바나나']
            while True:
                key = input('품목 : ')
                val = int(input('수량 : '))
                order_list[key] = val
                answer = input('q를 누르면 종료, 계속 주문하고 싶으면 아무 키나 누르세요')
                if answer =='q' :
                    break 
            return order_list
        except ValueError :
            print ('잘못된 정보 입니다.')
    print(order())

    def get_inventory():
