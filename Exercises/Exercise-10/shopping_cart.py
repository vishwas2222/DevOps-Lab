from flask import Flask, jsonify, request

app = Flask(__name__)
cart = []

@app.route("/cart", methods=["GET"])
def get_cart():
    return jsonify(cart)

@app.route("/cart", methods=["POST"])
def add_to_cart():
    item = request.get_json(silent=True)

    if not item:
        return jsonify({"error": "JSON request body required"}), 400

    if "id" not in item or "name" not in item or "quantity" not in item:
        return jsonify({"error": "id, name and quantity are required"}), 400

    cart.append(item)
    return jsonify({"message": "Item added", "cart": cart}), 201

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)