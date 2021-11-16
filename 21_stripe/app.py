from flask import Flask, render_template, jsonify
import stripe

app = Flask(__name__)

stripe.api_key = '*******'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'jpy',
                'product_data': {
                    'name': 'T-shirt',
                },
                'unit_amount': 2000,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:5000/thankyou',
        cancel_url='http://127.0.0.1:5000/',
    )
    return jsonify(id=session.id)

if __name__ == '__main__':
    app.run(debug=True)
