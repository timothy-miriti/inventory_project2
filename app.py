from flask import Flask, jsonify, request
from inventory import inventory
from external_api import fetch_product

app = Flask(__name__)


#  GET all items
@app.route('/inventory', methods=['GET'])
def get_all():
    return jsonify(inventory), 200


# GET one item by id 
@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_one(item_id):
    item = next((i for i in inventory if i['id'] == item_id), None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify(item), 200


# POST add a new item 
@app.route('/inventory', methods=['POST'])
def add_item():
    data = request.get_json()
    if not data or 'product_name' not in data:
        return jsonify({'error': 'product_name is required'}), 400

    new_item = {
        'id':           inventory[-1]['id'] + 1 if inventory else 1,
        'product_name': data.get('product_name'),
        'brands':       data.get('brands', 'Unknown'),
        'price':        data.get('price', 0.0),
        'stock':        data.get('stock', 0),
        'barcode':      data.get('barcode', ''),
        'ingredients':  data.get('ingredients', '')
    }
    inventory.append(new_item)
    return jsonify(new_item), 201


# PATCH update an item 
@app.route('/inventory/<int:item_id>', methods=['PATCH'])
def update_item(item_id):
    item = next((i for i in inventory if i['id'] == item_id), None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404

    data = request.get_json()
    for key in ['product_name', 'brands', 'price', 'stock', 'ingredients']:
        if key in data:
            item[key] = data[key]

    return jsonify(item), 200


# DELETE remove an item 
@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = next((i for i in inventory if i['id'] == item_id), None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404

    inventory.remove(item)
    return jsonify({'message': f'Item {item_id} deleted'}), 200


#  GET fetch from OpenFoodFacts and save 
@app.route('/inventory/fetch/<barcode>', methods=['GET'])
def fetch_and_save(barcode):
    product = fetch_product(barcode)
    if not product:
        return jsonify({'error': 'Product not found on OpenFoodFacts'}), 404

    new_item = {
        'id':           inventory[-1]['id'] + 1 if inventory else 1,
        'product_name': product.get('product_name', 'Unknown'),
        'brands':       product.get('brands', 'Unknown'),
        'price':        0.0,
        'stock':        0,
        'barcode':      barcode,
        'ingredients':  product.get('ingredients_text', '')
    }
    inventory.append(new_item)
    return jsonify(new_item), 201


if __name__ == '__main__':
    app.run(debug=True)