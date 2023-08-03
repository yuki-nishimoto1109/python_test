# カート内の商品の有無に合わせてメッセージを返す処理を作成してください
def get_cart_message(cart_items):
  if len(cart_items) == 0:
    return 'カートに商品がありません。お買い物をお楽しみください。'
  else:
     return '購入手続きを進めるか、引き続きお買い物をお楽しみください。'

# ここから下は触らないでください
# 利用するデータ
cart_items = [
    {'name': 'Tシャツ', 'type': 'clothes', 'price': 2000},
    {'name': 'キャップ', 'type': 'cap', 'price': 8000}
]
# 関数の呼び出し
message = get_cart_message(cart_items)
print('入力1：カートに商品がある場合')
print(message)

print('-----------------------------')

# 利用するデータ
cart_items = []
# 関数の呼び出し
message = get_cart_message(cart_items)
print('入力2：カートに商品がない場合')
print(message)

# 購入金額に対する付与ポイントを返す処理を作成してください
def calculate_points(total_price, user):
  if user['status'] == 'premium':
    return round(total_price * 0.02)
  else:
    return round(total_price * 0.01)

# ここから下は触らないでください
# 利用するデータ
total_price = 10000

user = {'user_id': 1, 'status': 'basic'}
# 関数の呼び出し
points = calculate_points(total_price, user)
print('入力1：会員ステータスがbasicの場合')
print(points)

print('-----------------------------')

# 利用するデータ
user = {'user_id': 2, 'status': 'premium'}
# 関数の呼び出し
points = calculate_points(total_price, user)
print('入力1：会員ステータスがpremiumの場合')
print(points)

# カート内の商品の税込合計金額を返す処理を作成してください
def calculate_total_with_tax(cart_items, tax_rate):
  total = 0
  for item in cart_items:
    total += round(item['price'] * (1+tax_rate))
  return total
# ここから下は触らないでください
# 利用するデータ
cart_items = [
    {'name': 'Tシャツ', 'type': 'clothes', 'price': 2000},
    {'name': 'キャップ', 'type': 'cap', 'price': 8000}
]
tax_rate = 0.1
# 関数の呼び出し
total_with_tax = calculate_total_with_tax(cart_items, tax_rate)
print(total_with_tax)

# 対象ユーザーの注文履歴を返す処理を作成してください
def get_order_history(user, orders):
  result = []
  for order in orders:
    if user['user_id'] == order['user_id']: result.append(order)
  return result
  
# ここから下は触らないでください
# 利用するデータ
orders = [
    {
        'order_id': 1,
        'user_id': 1,
        'items': [
            {'name': 'キャップ', 'type': 'cap', 'price': 8000},
            {'name': 'Tシャツ', 'type': 'clothes', 'price': 2000}
        ]
    },
    {
        'order_id': 2,
        'user_id': 2,
        'items': [
            {'name': 'ランニングシューズ', 'type': 'shoes', 'price': 15000},
        ]
    },
    {
        'order_id': 3,
        'user_id': 1,
        'items': [
            {'name': 'スポーツドリンク', 'type': 'food', 'price': 150}
        ]
    },
    {
        'order_id': 4,
        'user_id': 3,
        'items': [
            {'name': 'アンダーウェア', 'type': 'clothes', 'price': 4500},
            {'name': 'テニスラケット', 'type': 'sports goods', 'price': 8000}          
        ]
    }
]

user = {'user_id': 1, 'status': 'basic'}
# 関数の呼び出し
user_orders = get_order_history(user, orders)
for order in user_orders:
    print(order)

# 各商品と各色の組み合わせを全て出力する処理を作成してください
def display_product_and_color(items, colors):
  for item in items:
    for color in colors:
      print(item['name'] + ':' + color)

# ここから下は触らないでください
# 利用するデータ
items = [
    {'name': 'Tシャツ', 'type': 'clothes', 'price': 2000},
    {'name': 'キャップ', 'type': 'cap', 'price': 8000}
]
colors = ['Red', 'Blue', 'Black']
# 関数の呼び出し
display_product_and_color(items, colors)

# カート内の合計金額を返す処理を作成してください
def calculate_total_price(cart_items):
  total = 0
  for item in cart_items:
    if item['type'] == 'food':
      total += round(item['price'] * 0.9)
    elif item['type'] == 'clothes':
      total += item['price'] - 1000
    else:
      total += item['price']
  return total
  
# ここから下は触らないでください
# 利用するデータ
cart_items = [
    {'name': 'Tシャツ', 'type': 'clothes', 'price': 2000},
    {'name': 'キャップ', 'type': 'cap', 'price': 8000},
    {'name': 'ランニングシューズ', 'type': 'shoes', 'price': 15000},
    {'name': 'アンダーウェア', 'type': 'clothes', 'price': 4500},
    {'name': 'テニスラケット', 'type': 'sports goods', 'price': 8000},
    {'name': 'スポーツドリンク', 'type': 'food', 'price': 150}
]
# 関数の呼び出し
total_price = calculate_total_price(cart_items)
print(total_price)