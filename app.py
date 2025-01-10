from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Updated Indian Stock List
INDIAN_STOCKS = [
    'Reliance', 'TATA', 'Infosys', 'HDFC', 'ICICI', 'SBI', 
    'Bharti Airtel', 'L&T', 'Tata Motors', 'Wipro'
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stock Mastermind CTF</title>
    <style>
        body {
            background-color: #f0f0f0;
            color: #333;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 30px;
        }
        .container {
            width: 100%;
            max-width: 1000px;
            margin: 0 auto;
        }
        h1 {
            font-size: 2rem;
            color: #333;
            margin-bottom: 20px;
        }
        h3 {
            font-size: 1.5rem;
            color: #666;
            margin-bottom: 20px;
        }
        .stock-card {
            background: #fff;
            border: 1px solid #ccc;
            padding: 20px;
            margin: 20px 0;
            display: inline-block;
            width: 100%;
            max-width: 350px;
            text-align: left;
            border-radius: 5px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        }
        .stock-card h2 {
            font-size: 1.2rem;
            margin-bottom: 15px;
        }
        .stock-card label, .stock-card p {
            font-size: 1rem;
            margin-bottom: 10px;
            color: #555;
        }
        .stock-card input, .stock-card select {
            background: #fff;
            color: #333;
            border: 1px solid #ccc;
            padding: 10px;
            width: 100%;
            margin-bottom: 15px;
            font-size: 1rem;
            border-radius: 5px;
        }
        button {
            padding: 10px 20px;
            background: #0066cc;
            color: white;
            border: none;
            cursor: pointer;
            font-weight: bold;
            border-radius: 5px;
            font-size: 1.1rem;
        }
        button:hover {
            background: #004d99;
        }
        .success {
            display: none;
            margin-top: 20px;
            background-color: #e0ffe0;
            border: 1px solid #99cc99;
            padding: 20px;
            font-size: 1rem;
            color: #4d4d4d;
        }
        img, iframe {
            margin: 10px;
            width: 300px;
            height: auto;
        }
        .typing {
            border-right: 2px solid #0066cc;
            white-space: nowrap;
            overflow: hidden;
        }
        @media (max-width: 768px) {
            .container {
                padding: 15px;
            }
            .stock-card {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Stock Mastermind CTF</h1>
        <div>
            <h3>Greetings, Trader!</h3>
            <p class="typing" id="storyline">Welcome to the world of high-stakes trading. Harshad Mehta is here to guide you, but only the smartest will succeed.</p>
        </div>
        
        <div id="stocks">
            <div class="stock-card">
                <h2>Trade Stocks</h2>
                <label for="stock-select">Choose Stock:</label>
                <select id="stock-select">
                    {% for stock in stocks %}
                        <option value="{{ stock }}">{{ stock }}</option>
                    {% endfor %}
                </select>
                <p>Price: <span id="stock-price">100</span> USD</p>
                <label for="quantity">Quantity:</label>
                <input type="number" id="quantity" value="1">
                <br>
                <button onclick="buyStock()">Trade</button>
            </div>
        </div>
        
        <div class="success" id="success">
            <h2>🎉 Congratulations! Harshad is impressed! 🎉</h2>
            <iframe src="https://c.tenor.com/dN7Lg9K4xFgAAAAd/tenor.gif" frameborder="0"></iframe>
            <img src="https://pbs.twimg.com/media/Ek8ZBBKU8AEsLbs.jpg:large" alt="Harshad Mehta">
            <p>Harshad says: "Well done, trader! You've proven yourself in the market manipulation game."</p>
            <p><code>FLAG: CTF{Reliance_Stock_Manipulation_Master}</code></p>
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
    return render_template_string(HTML_TEMPLATE, stocks=INDIAN_STOCKS)

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
