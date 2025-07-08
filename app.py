from flask import Flask, render_template, jsonify
import razorpay

app = Flask(__name__)

# === Razorpay Test Keys ===
client = razorpay.Client(auth=("rzp_test_um6QaO0Ca35Em1", "ZIpEKzQRH8OudA2CPoclVvZ4"))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create_order')
def create_order():
    data = {
        "amount": 9900,     # ₹99 in paise
        "currency": "INR",
        "payment_capture": 1
    }
    order = client.order.create(data=data)
    return jsonify(order)

if __name__ == '__main__':
    app.run(debug=True)
