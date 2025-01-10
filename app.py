from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stock Mastermind CTF</title>
    <style>
        body {
            background-color: #f4f4f9;
            color: #333;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #2c3e50;
            color: #fff;
            padding: 15px;
            text-align: center;
            font-size: 1.5rem;
            font-weight: bold;
        }

        .container {
            max-width: 1200px;
            margin: 20px auto;
            padding: 20px;
        }

        .card {
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }

        .card h2 {
            margin-top: 0;
            color: #2c3e50;
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        select, input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 1rem;
        }

        button {
            display: inline-block;
            padding: 10px 20px;
            font-size: 1rem;
            background-color: #27ae60;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        button:hover {
            background-color: #219150;
        }

        .success {
            display: none;
            text-align: center;
            background: #ecf0f1;
            border: 2px solid #27ae60;
            padding: 20px;
            border-radius: 8px;
            margin-top: 20px;
        }

        .success h2 {
            color: #27ae60;
        }

        iframe, img {
            margin: 10px 0;
            max-width: 100%;
            height: auto;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <header>Stock Mastermind CTF</header>

    <div class="container">
        <div class="card">
            <h2>Trade Stocks</h2>
            <div class="form-group">
                <label for="stock-select">Choose Stock:</label>
                <select id="stock-select">
                    <option value="HACK">HACK</option>
                    <option value="Reliance">Reliance</option>
                    <option value="TATA">TATA</option>
                </select>
            </div>

            <div class="form-group">
                <label for="quantity">Quantity:</label>
                <input type="number" id="quantity" value="1">
            </div>

            <p>Price: <strong><span id="stock-price">100</span> USD</strong></p>
            <button onclick="buyStock()">Trade</button>
        </div>

        <div class="success" id="success">
            <h2>🎉 Congratulations! Harshad is impressed! 🎉</h2>
            <iframe src="https://c.tenor.com/dN7Lg9K4xFgAAAAd/tenor.gif" frameborder="0"></iframe>
            <img src="https://pbs.twimg.com/media/Ek8ZBBKU8AEsLbs.jpg:large" alt="Harshad Mehta">
            <p>Harshad says: "Well done, trader! You've proven yourself in the market manipulation game."</p>
            <p><code>FLAG: SCIT{Reliance_Stock_Manipulation_Master}</code></p>
        </div>
    </div>

    <script>
        function buyStock() {
            const stock = document.getElementById('stock-select').value;
            const quantity = document.getElementById('quantity').value;
            const price = document.getElementById('stock-price').textContent;

            fetch('/buy-stock', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ stock: stock, price: price, quantity: quantity })
            })
            .then(response => response.json())
            .then(data => {
                if (data.flag) {
                    document.getElementById('success').style.display = 'block';
                    document.getElementById('stocks').style.display = 'none';
                } else {
                    alert(data.message);
                }
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/buy-stock', methods=['POST'])
def buy_stock():
    data = request.json
    stock = data.get('stock')
    price = data.get('price')

    # Hidden logic for flag
    if stock == 'Reliance' and price == '5000':
        return jsonify({"flag": True})
    return jsonify({"flag": False, "message": "Invalid trade! Harshad isn't impressed."})

if __name__ == '__main__':
    app.run(debug=True)
