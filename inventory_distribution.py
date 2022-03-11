

class Inventory_distribution:
    def order():
        try:
            order_list = {}
            item = ['사과', '오렌지', '바나나']
            while True:
                key = input('품목 : ')
                if key not in item :
                    print ('존재하지 않는 상품 입니다.')
                    break
                val = int(input('수량 : '))
                order_list[key] = val
                answer = input('q를 누르면 종료, 계속 주문하고 싶으면 아무 키나 누르세요.')
                if answer =='q' :
                    break 
            return order_list
        except ValueError :
            print ('잘못된 정보 입니다.')
    print(order())
# 에러 반환
# 딕셔너리 특성 상 같은 key값이 들어올 시 value가 수정됨 


    def get_inventory():
        warehouse_list =[]
        while True :
            name = input('이름 : ')
            while True :
                order = {}
                key = input('품목 : ')
                val = int(input('수량 : '))
                order[key] = val
                answer = input('q를 누르면 종료, 재고를 추가하고 싶으면 아무 키나 누르세요')
                if answer =='q' :
                    break
            warehouse = {
                '이름' : name,
                '재고' : order
                }
            warehouse_list.append(warehouse)
            answer = input('q를 누르면 종료, 새로운 창고를 추가하려면 아무 키나 누르세요')
            if answer =='q' :
                break
        return warehouse_list
    print (get_inventory())
# # [ { 이름: owd, 재고: { 사과: 5, 주황색: 10 } }, { 이름: dm:, 재고: { 바나나: 5, 주황색: 10 } } ]
# 창고이름 중복시 벨류 합치기 
# 에러 반환
# 품목 여러개 추가하기 