import json


from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager

router = APIRouter()
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


current_user = fastapi_users.current_user()
@router.get("/user_my")
async def read_me(user: User = Depends(current_user)):
    user_data = {
        "email": user.email,
        "phone": user.phone,
        "id": user.id
    }

    return user_data

@router.get("/del_basket")
def del_basket(user: User = Depends(current_user)):
    basket_new = []
    with open(f"Basket/{user.email}.json", "w", encoding="utf-8") as file:
        json.dump(basket_new, file)
    return []
@router.get("/get_basket")
def get_basket(user: User = Depends(current_user)):
    try:
        with open(f"Basket/{user.email}.json", encoding='utf-8') as f:
            file_content = f.read()
            basket = json.loads(file_content)
    except FileNotFoundError:
        basket_new = []
        with open(f"Basket/{user.email}.json", "w", encoding="utf-8") as file:
            json.dump(basket_new, file)

        with open(f"Basket/{user.email}.json", encoding='utf-8') as f:
            file_content = f.read()
            basket = json.loads(file_content)
    return basket
@router.get("/set_basket/{key}")
def set_basket(key: str, user: User = Depends(current_user)):
    try:
        with open(f"Basket/{user.email}.json", encoding='utf-8') as f:
            file_content = f.read()
            basket = json.loads(file_content)
    except FileNotFoundError:
        basket_new = []
        with open(f"Basket/{user.email}.json", "w", encoding="utf-8") as file:
            json.dump(basket_new, file)

        with open(f"Basket/{user.email}.json", encoding='utf-8') as f:
            file_content = f.read()
            basket = json.loads(file_content)

    with open('sample.json', encoding='utf-8') as f:
        file_content = f.read()
        templates = json.loads(file_content)
    for detal in templates:
        detal["quantity"] = 1
        if detal["key"] == key:
            for basket_detal in basket:
                if basket_detal["key"] == key:
                    basket_detal["quantity"] += 1
                    with open(f"Basket/{user.email}.json", "w", encoding="utf-8") as file:
                        json.dump(basket, file, ensure_ascii=False, indent=4)
                    return
            basket.append(detal)
            with open(f"Basket/{user.email}.json", "w", encoding="utf-8") as file:
                json.dump(basket, file, ensure_ascii=False, indent=4 )


    return detal
@router.get("/Name_without_use/{key}")
def get_detal(key: str):
    with open('sample.json', encoding='utf-8') as f:
        file_content = f.read()
        templates = json.loads(file_content)
    for detal in templates:
        if detal["key"] == key:
            return detal
    return []
@router.get("/brands")
def get_brands():

    with open('sample.json', encoding='utf-8') as f:
        file_content = f.read()
        templates = json.loads(file_content)
        all_brends = [{
            "key": 0,
            "Manufacturer": "",
            "Model": []
        }]

    for brands in templates:

        all_model = []
        for model in all_brends:
            all_model.append(model["Manufacturer"])
        if brands["Manufacturer"] not in all_model:
            all_brends.append({
                "key": brands["key"],
                "Manufacturer": brands["Manufacturer"],
                "Model": []
            })

        for brend in all_brends:
            if brend["Manufacturer"] == brands["Manufacturer"] and brands["Model"] not in brend["Model"]:
                brend["Model"].append(brands["Model"])
    return all_brends
@router.get("/{brend}")
def get_brand(brend: str):
    brend = brend.title()
    print(brend)
    with open('sample.json', encoding='utf-8') as f:
        file_content = f.read()
        templates = json.loads(file_content)
        detail = []

        for brands in templates:

            if brands["Manufacturer"] == brend or brend == 'All':

                detail.append(brands)

    return detail



