from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def items():
    try:
        with open("items.json", "r") as file:
            data = json.load(file)
            item_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading items.json: {e}")
        item_list = []

    return render_template("items.html", items=item_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
