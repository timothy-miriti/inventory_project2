import requests

OPENFOODFACTS_URL = 'https://world.openfoodfacts.org/api/v0/product'

# OpenFoodFacts requires a User-Agent header or it returns an empty response
HEADERS = {
    'User-Agent': 'InventoryApp/1.0 (your@email.com)'
}

def fetch_product(barcode):
    try:
        response = requests.get(
            f'{OPENFOODFACTS_URL}/{barcode}.json',
            headers=HEADERS,   # ← this is the fix
            timeout=5
        )

        data = response.json()

        if data.get('status') == 1:
            return data.get('product', {})

        return None

    except requests.exceptions.RequestException as e:
        print(f'API error: {e}')
        return None