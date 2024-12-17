def calcular_total(products, discount=False):
    total = 0
    dis = 0
    for product in products:
        total += product['price']
        if discount:
            dis += product['price'] * product['discount'] / 100
    total = total - dis
    return total

def test_calculate_total_with_empty_list():
    assert calcular_total([]) == 0

def test_calculate_total_with_single_product():
    products = [
        {
            'name': 'Notebook', 'price': 5 
        }
    ]
    assert calcular_total(products) == 5

def test_calculate_total_with_multiple_product():
    products = [
        {
            'name': 'Notebook', 'price': 5 
        },
        {
            'name': 'Iphone', 'price': 50 
        },
        {
            'name': 'Book', 'price': 15 
        }
    ]
    assert calcular_total(products) == 70

def test_calculate_total_with_multiple_product_with_discount(discount):
    products = [
        {
            'name': 'Notebook', 'price': 5, 'discount': 1
        },
        {
            'name': 'Iphone', 'price': 50, 'discount': 10
        },
        {
            'name': 'Book', 'price': 15, 'discount': 20
        }
    ]
    assert calcular_total(products, discount) == 61.95



