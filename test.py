import json

from basket import del_basket_json, basket_json

basket = basket_json("medvede.kfx@gmail.com")
del_basket_json(basket, 'medvede.kfx@gmail.com', '10')