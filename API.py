from flask import Flask, jsonify, request

app = Flask(__name__)


items = {}


@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = items.get(item_id)
    if item is not None:
        return jsonify(item), 200
    else:
        return jsonify({'error': 'Item not found'}), 404


@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    item_id = len(items) + 1
    items[item_id] = data
    return jsonify({'id': item_id, 'item': data}), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    if item_id in items:
        items[item_id] = data
        return jsonify({'id': item_id, 'item': data}), 200
    else:
        return jsonify({'error': 'Item not found'}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id in items:
        del items[item_id]
        return jsonify({'message': 'Item deleted'}), 200
    else:
        return jsonify({'error': 'Item not found'}), 404




if __name__ == '_main_':
    app.run(debug=True)



