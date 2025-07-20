from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def get_products_from_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except Exception:
        return None

def get_products_from_csv():
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    except Exception:
        return None

def get_products_from_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        conn.close()
        return products
    except Exception:
        return None

@app.route('/products')
def display_products():
    source = request.args.get('source')
    if source == 'json':
        products = get_products_from_json()
    elif source == 'csv':
        products = get_products_from_csv()
    elif source == 'sql':
        products = get_products_from_sql()
    else:
        return render_template('product_display.html', products=None, error="Wrong source")
    if products is None:
        return render_template('product_display.html', products=None, error="Erreur lors de la récupération des données")
    return render_template('product_display.html', products=products, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
