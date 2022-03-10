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
# 키값 중복시 벨류 합치기
# 정해진 품목 외에 값 들어오면 에러 반환
    def get_inventory():
        warehouse_list =[]
        while True :
            name = input('이름 : ')
            key = input('품목 : ')
            val = int(input('수량 : '))
            order = {}
            order[key] = val
            warehouse = {
                '이름' : name,
                '재고' : order
                }
            answer = input('q를 누르면 종료, 계속 입력하고 싶으면 아무 키나 누르세요')
            if answer =='q' :
                break
            else :
                warehouse_list.append(warehouse)
        return warehouse_list
    print (get_inventory())
# # [ { 이름: owd, 재고: { 사과: 5, 주황색: 10 } }, { 이름: dm:, 재고: { 바나나: 5, 주황색: 10 } } ]
# 키값 중복시 벨류 합치기 
# 에러 반환
# 와 마지막 입력은 씹히는지 
