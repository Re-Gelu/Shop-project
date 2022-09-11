from Shop.models import *
from art import tprint
import random

def DB_AUTO_FILL(amount, model):
    match model:
        case "Categories":
            print("[+] Model exists...\n")

            for i in range(1, amount + 1):
                category = Categories()
                category.name=f"Категория №{i}"
                
                category.save()
                print(category.name, "\n")

        case "Subcategories":
            print("[+] Model exists...\n")
            
            categories = list()
            for category in Categories.objects.all():
                categories.append(category)
            
            for category in categories:
                for i in range(1, random.randrange(start = 1, stop = amount + 1) + 1):
                    subcategory = Subcategories()
                    subcategory.name = f"Подкатегория №{str(category).removeprefix('Категория №')}.{i}"
                    subcategory.category = category
                    
                    subcategory.save()
                    print(subcategory.name, "\n")
                print("\n")
                
        case "Products":
            print("[+] Model exists...\n")
            
            subcategories = list()
            for subcategory in Subcategories.objects.all():
                subcategories.append(subcategory)

            for i in range(1, amount + 1):
                product = Products()
                product.name = f"Товар №{i}"
                product.price = round(random.random() * 100, 2)
                product.image = "product_images/WIP.png"
                product.subcategory = random.choice(subcategories)
                product.information = f"Товар №{i}\nПодкатегория: {product.subcategory}\nКатегория: {product.subcategory.category}"
                
                product.save()
                print(product.information, "\n")

if __name__ == '__main__':
    tprint("DB auto fill", font="Slant")
    amount = int(input("Кол-во записей: "))
    model = input("Таблица: ")
    DB_AUTO_FILL(amount, model)