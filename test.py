import json


def set_basket(key: str):
    try:
        with open("Basket/medvede.kfx@gmail.com", encoding='utf-8') as f:
            file_content = f.read()
            basket = json.loads(file_content)
    except FileNotFoundError:
        basket_new = []
        with open("Basket/medvede.kfx@gmail.com", "w", encoding="utf-8") as file:
            json.dump(basket_new, file)

        with open("Basket/medvede.kfx@gmail.com", encoding='utf-8') as f:
            file_content = f.read()
            basket = json.loads(file_content)

    with open('sample.json', encoding='utf-8') as f:
        file_content = f.read()
        templates = json.loads(file_content)
    for detal in templates:

        if detal["key"] ==key:
            detal["quantity"] = 1
            for basket_detal in basket:
                if basket_detal["key"] == key:
                    basket_detal["quantity"] += 1
                    with open("Basket/medvede.kfx@gmail.com", "w", encoding="utf-8") as file:
                        json.dump(basket, file, ensure_ascii=False, indent=4)
                    return
            basket.append(detal)
            with open("Basket/medvede.kfx@gmail.com", "w", encoding="utf-8") as file:
                json.dump(basket, file, ensure_ascii=False, indent=4 )


    return detal
set_basket("7")