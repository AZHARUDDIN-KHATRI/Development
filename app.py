from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for simplicity
expenses = [
    {"id": 1, "title": "Internet Bill", "amount": 1500, "category": "Utilities"},
    {"id": 2, "title": "Groceries", "amount": 2500, "category": "Food"}
]

@app.route('/expenses', methods=['GET'])
def get_expenses():
    return jsonify({"status": "success", "data": expenses}), 200

@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    if not data or 'title' not in data or 'amount' not in data:
        return jsonify({"status": "error", "message": "Missing fields"}), 400
    
    new_expense = {
        "id": len(expenses) + 1,
        "title": data['title'],
        "amount": data['amount'],
        "category": data.get('category', 'General')
    }
    expenses.append(new_expense)
    return jsonify({"status": "success", "message": "Expense added", "data": new_expense}), 201

@app.route('/expenses/<int:id>', methods=['DELETE'])
def delete_expense(id):
    global expenses
    initial_length = len(expenses)
    expenses = [e for e in expenses if e['id'] != id]
    if len(expenses) < initial_length:
        return jsonify({"status": "success", "message": f"Expense {id} deleted"}), 200
    return jsonify({"status": "error", "message": "Expense not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)