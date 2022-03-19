from curses import is_term_resized
from lib2to3.pgen2.token import ISTERMINAL


class InventoryAllocator :  
    def inventory_distribution(order, inventory):
        result = []

        for i in range(len(inventory)): # 창고에 있는 품목을 뽑음
            stock = list(inventory[i]['inventory'].keys()) # 재고 (중첩)딕셔너리에서 품목들(키)을 리스트로 받아서 stock에 할당 
            output = {}

            # for item in order and stock : 
            # count = (inventory[i]['inventory'].get(item)) 




# Input: { apple: 10 }, [ { name: owd, inventory: { apple: 5, orange: 10 } }, { name: dm, inventory: { banana: 5, orange: 10 } } ]
# Output: [{ dm: { apple: 5 }}, { owd: { apple: 5 } }]
inventory =   { 'name': 'owd', 'inventory': { 'apple': 5, 'orange': 10 } }, { 'name': 'dm', 'inventory': { 'banana': 5, 'orange': 10 } }
order = { 'apple': 5, 'banana': 5, 'orange': 5 }
output = {}
for i in range (len(inventory)):
    stock = list(inventory[i]['inventory'].keys()) # apple, orange
    for item in stock :
        # if item in stock and order[item] !=0 :
            item_count = inventory[i]['inventory'].get(item) # 창고안의 재고 갯수만 가져오기 
            if item_count   >= order.get(item) : # 주문보다 재고가 더 많을 경우 
                output[item] = order[item]
                # item_count  -= order[item]
                # order[item]  = 0 
                print (output)
