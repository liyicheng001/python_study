goods_car = { }
# 1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
goods_name = input('请输入商品名称:')
goods_count =  int(input('请输入修改的商品数量:'))
goods_price = int(input('请输入修改的商品价格:'))

def addCar(goods_name,goods_count,goods_price  ):
  goods_car[goods_name] = {'goods_count':goods_count,'goods_price':goods_price}

addCar(goods_name ,goods_count,goods_price  )
# 2.修改购物车:要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
def editCar( ):
   goods_edit_name = input('请输入修改的商品名称:')
   if goods_edit_name in goods_car:
       goods_car[goods_edit_name ]['goods_price'] =  int(input('请输入修改的商品价格:'))
       goods_car[goods_edit_name ]['goods_count'] =  int(input('请输入修改的商品数量:'))
       print(f'修改成功{ goods_car[goods_edit_name]}') 
   else:
        print('请输入有效的商品名称') 
    #    目前正确吗
editCar( )

# 3.删除购物车:要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
def delCar( ):
  goods_edit_name = input('请输入修改的商品名称:')
  if goods_edit_name in goods_car:
    del goods_car[goods_edit_name]
    print('删除成功') 
  else:
        print('请输入有效的商品名称') 
delCar()

# 4.查询购物车:将购物车中的商品信息展示出来，格式为:"商品名称:xxx，商品价格:xxx，商品数量:xxx”。
def selectCar():
  for k in goods_car.keys():
     print(f"商品名称{k},商品价格：{goods_car[k]['goods_price']},商品数量:{goods_car[k]['goods_count']}")
selectCar()
