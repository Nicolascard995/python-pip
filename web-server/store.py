import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/products')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json()
    for category in categories:
        print(category['name'])


"""
def get_categories():
    categories = store.get("categories")
    if categories:
        for category in categories:
            category_name = category.get("name")
            if category_name:
                print(category_name)
            else:
                print("Name key not found for category:", category)
    else:
        print("No categories found")

# This code checks if the 'categories' key exists in the dictionary first, 
# then safely accesses the 'name' key using the get() method.

"""