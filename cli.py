import requests

BASE_URL = 'http://127.0.0.1:5000'

# Menu 
def display_menu():
    print('\n===== Inventory Manager =====')
    print('1. View all inventory')
    print('2. View single item')
    print('3. Add new item')
    print('4. Update item')
    print('5. Delete item')
    print('6. Fetch item from OpenFoodFacts by barcode')
    print('0. Exit')
    return input('Choose an option: ')


# View all 
def view_all():
    res = requests.get(f'{BASE_URL}/inventory')
    items = res.json()
    if not items:
        print('No items in inventory.')
        return
    print('\n── All Inventory ──')
    for item in items:
        print(f"[{item['id']}] {item['product_name']} | {item['brands']} | ${item['price']} | Stock: {item['stock']}")


# View one 
def view_one():
    item_id = input('Enter item ID: ')
    res = requests.get(f'{BASE_URL}/inventory/{item_id}')
    if res.status_code == 404:
        print('Item not found.')
        return
    item = res.json()
    print('\n── Item Details ──')
    for key, val in item.items():
        print(f'  {key}: {val}')


#  Add item 
def add_item():
    print('\n── Add New Item ──')
    name    = input('Product name: ')
    brand   = input('Brand: ')
    price   = input('Price: ')
    stock   = input('Stock quantity: ')
    barcode = input('Barcode (optional, press enter to skip): ')

    payload = {
        'product_name': name,
        'brands':       brand,
        'price':        float(price),
        'stock':        int(stock),
        'barcode':      barcode
    }
    res = requests.post(f'{BASE_URL}/inventory', json=payload)
    print(f'Added: {res.json()}')


# Update item 
def update_item():
    item_id = input('Enter item ID to update: ')
    print('Leave blank to skip a field.')
    price = input('New price: ')
    stock = input('New stock: ')

    payload = {}
    if price:
        payload['price'] = float(price)
    if stock:
        payload['stock'] = int(stock)

    if not payload:
        print('Nothing to update.')
        return

    res = requests.patch(f'{BASE_URL}/inventory/{item_id}', json=payload)
    if res.status_code == 404:
        print('Item not found.')
        return
    print(f'Updated: {res.json()}')


#  Delete item 
def delete_item():
    item_id = input('Enter item ID to delete: ')
    res = requests.delete(f'{BASE_URL}/inventory/{item_id}')
    if res.status_code == 404:
        print('Item not found.')
        return
    print(res.json()['message'])


# Fetch from OpenFoodFacts 
def fetch_from_api():
    barcode = input('Enter barcode: ')
    res = requests.get(f'{BASE_URL}/inventory/fetch/{barcode}')
    if res.status_code == 404:
        print('Product not found on OpenFoodFacts.')
        return
    print(f'Fetched and saved: {res.json()}')


# Main loop 
def main():
    while True:
        choice = display_menu()
        if   choice == '1': view_all()
        elif choice == '2': view_one()
        elif choice == '3': add_item()
        elif choice == '4': update_item()
        elif choice == '5': delete_item()
        elif choice == '6': fetch_from_api()
        elif choice == '0':
            print('Goodbye.')
            break
        else:
            print('Invalid option, try again.')

if __name__ == '__main__':
    main()