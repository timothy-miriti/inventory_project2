import requests
from colorama import Fore, Style,init
init(autoreset=True)

BASE_URL = 'http://127.0.0.1:5000'

# Menu 
def display_menu():
    print(f'\n{Fore.CYAN}===== Inventory Manager ====={Style.RESET_ALL}')
    print(f'{Fore.GREEN}1. View all inventory{Style.RESET_ALL}')
    print(f'{Fore.GREEN}2. View single item{Style.RESET_ALL}')
    print(f'{Fore.GREEN}3. Add new item{Style.RESET_ALL}')
    print(f'{Fore.GREEN}4. Update item{Style.RESET_ALL}')
    print(f'{Fore.RED}5. Delete item{Style.RESET_ALL}')
    print(f'{Fore.BLUE}6. Fetch item from OpenFoodFacts by barcode{Style.RESET_ALL}')
    print(f'{Fore.RED}0. Exit{Style.RESET_ALL}')
    return input('Choose an option: ')


# View all 
def view_all():
    res = requests.get(f'{BASE_URL}/inventory')
    items = res.json()
    if not items:
        print('No items in inventory.')
        return
    print(f'\n{Fore.GREEN}── All Inventory ──{Style.RESET_ALL}')
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
    print(f'\n{Fore.GREEN}── Item Details ──{Style.RESET_ALL}')
    for key, val in item.items():
        print(f'  {key}: {val}')


#  Add item 
def add_item():
    print(f'\n{Fore.GREEN}── Add New Item ──{Style.RESET_ALL}')
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
            print(f'{Fore.RED}Invalid option, try again.{Style.RESET_ALL}')

if __name__ == '__main__':
    main()