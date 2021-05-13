from random import randrange
import random
from datetime import timedelta
from datetime import datetime
# 模擬顧客ID
import uuid
import csv
# 自訂資料結構
# 時間 購買商品 主食選擇 數量 該商品總價 附餐選擇 附餐冷熱
class consumptionRecord:
    def __init__(self, time, item, quantity, price, staple, side, heat):
        self.time = time
        self.item = item   
        self.quantity = quantity
        self.price = price
        self.staple=staple
        self.side=side
        self.heat=heat


# 販售的商品及其價格
item_price = {
    "牛肉粉絲鍋":320,
    "破布子苦瓜蒸肉":300,
    "韓國泡菜土雞":310,
    "泰式蒜香炒辣雞":300,
    "時魚":320,
    "杜仲牛南":300,
    "脆皮雞腿":300,
    "紅麴豬排":300,
    "椒鹽魚排":300,
    "橙汁魚排":300,
    "酸菜白肉鍋":300,
    "薄鹽烤鯖魚":300,
}

#飯類的選擇
item_rice={
    "白飯",
    "紫米"
}

#附餐選擇 
item_sides={
    "咖啡":["熱","冷"],
    "紅茶":["熱","冷"],
    "奶茶":["熱","冷"],
    "柚子茶":["熱"],
    "巧克力":["熱"],
    "甜湯":["熱"],
    "綠茶":["熱","冷"],
    "檸檬汁":["冷"],
    "蔓越莓醋":["冷"]
}

# 儲存顧客購買行為
customer_purchase_behavior = {}

# 隨機產生購買的時間點
def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

# 用來計算目前有幾筆資料
i = 0

while (i <= 500):
    # 產生顧客ID
    customer_id = str(uuid.uuid4())[:8]

    # 產生該顧客會來該商家幾次
    random_customer_purchase_days = random.randint(1, 10)

    for j in range(random_customer_purchase_days):

        # 產生每次來店家的日期
        d1 = datetime.strptime('1/1/2020  8:30 AM', '%m/%d/%Y %I:%M %p')
        d2 = datetime.strptime('12/31/2020 11:00 PM', '%m/%d/%Y %I:%M %p')
        random_dat = random_date(d1, d2)

        # 隨機產生顧客會購買幾項商品
        random_quantity = random.randint(1, 5)
        
        # 複製販售商品
        item_price_copy = item_price.copy()

        for k in range(random_quantity):
            # 從販售商品中隨機挑選一個項目
            random_item = random.choice(list(item_price_copy))

            # 刪除選擇的商品, 不重複選擇商品
            del item_price_copy[random_item]

            # 隨機產生該商品被購買的數量
            random_item_quantity = random.randint(1, 5)

            price = random_item_quantity * item_price[random_item]
            
            #隨機產生的主食選擇
            random_item_staple=random.choice(list(item_rice))

            #隨機產生的附餐選擇
            random_item_side=random.choice(list(item_sides))
            
            #隨機產生附餐冷熱選擇
            random_item_heat=random.choice(item_sides[random_item_side])
            
            
            customer_purchase_behavior.setdefault(customer_id, []).append(consumptionRecord(random_dat, random_item, random_item_quantity, price, random_item_staple, random_item_side, random_item_heat))
    
    # 該顧客的交易次數
    times =  random_customer_purchase_days * random_quantity
    
    #總交易次數
    i = i + times

def print_item_price(item_price):
    print("販售中的商品")
    for i in item_price:
        print(i +" "+ str(item_price[i]))

def print_customer_purchase_behavior(customer_purchase_behavior):
    for j in customer_purchase_behavior:
        for k in range(len(customer_purchase_behavior[j])):
            print(j+" "+str(customer_purchase_behavior[j][k].time)+" "+str(customer_purchase_behavior[j][k].item)+" "+str(customer_purchase_behavior[j][k].quantity)+" "+str(customer_purchase_behavior[j][k].price)+" "+str(customer_purchase_behavior[j][k].staple)+" "+str(customer_purchase_behavior[j][k].side)+" "+str(customer_purchase_behavior[j][k].heat))

print_item_price(item_price)
print_customer_purchase_behavior(customer_purchase_behavior)

with open('generator_database.csv', 'w', newline='') as csv_file:  
    writer = csv.writer(csv_file)
    writer.writerow(["顧客ID", "購買時間", "購買商品","購買數量", "商品小計","主食選擇","附餐選擇","附餐冷熱"])
    for j in customer_purchase_behavior:
        for k in range(len(customer_purchase_behavior[j])):
            writer.writerow( [j, str(customer_purchase_behavior[j][k].time), str(customer_purchase_behavior[j][k].item), str(customer_purchase_behavior[j][k].quantity), str(customer_purchase_behavior[j][k].price), str(customer_purchase_behavior[j][k].staple), str(customer_purchase_behavior[j][k].side), str(customer_purchase_behavior[j][k].heat)] )
