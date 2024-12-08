import json


def basket_json(email: str):
    try:
        with open(f"Basket/{email}.json", encoding='utf-8') as f:
            file_content = f.read()
            basket = json.loads(file_content)
    except FileNotFoundError:
        basket_new = []
        with open(f"Basket/{email}.json", "w", encoding="utf-8") as file:
            json.dump(basket_new, file)

        with open(f"Basket/{email}.json", encoding='utf-8') as f:
            file_content = f.read()
            basket = json.loads(file_content)
    return basket

def set_basket_json(basket, email, key):
    with open('sample.json', encoding='utf-8') as f:
        file_content = f.read()
        templates = json.loads(file_content)
    for detal in templates:
        detal["quantity"] = 1
        if detal["key"] == key:
            for basket_detal in basket:
                if basket_detal["key"] == key:
                    basket_detal["quantity"] += 1
                    with open(f"Basket/{email}.json", "w", encoding="utf-8") as file:
                        json.dump(basket, file, ensure_ascii=False, indent=4)
                    return
            basket.append(detal)
            with open(f"Basket/{email}.json", "w", encoding="utf-8") as file:
                json.dump(basket, file, ensure_ascii=False, indent=4)

def del_basket_json(basket, email, key):
        for basket_detal in basket:
            if basket_detal["key"] == key:
                    if basket_detal["quantity"] <= 0:
                        break
               

                    basket_detal["quantity"] -= 1
                    with open(f"Basket/{email}.json", "w", encoding="utf-8") as file:
                        json.dump(basket, file, ensure_ascii=False, indent=4)
                    return

        with open(f"Basket/{email}.json", "w", encoding="utf-8") as file:
                json.dump(basket, file, ensure_ascii=False, indent=4)