from flask import Flask, jsonify, abort
from card_validation import *

app = Flask(__name__)
app.config["DEBUG"] = True
retry_count = 0  # Initialising counter to zero for 3 attempt of PremiumPaymentGateway


@app.route('/', methods=['GET'])
def home():
    return '<h1>Kindly check the test cases</h1>'


# Accepting Card details as GET parameter from URL
@app.route('/<string:name>/<string:card_number>/<string:exp_date>/<int:amount>', methods=['GET'])
def ProcessPayment(name, card_number, exp_date, amount):

    global retry_count
    gateway = 'None'
    response = {}
    # if amount is less than or equal to 500 redirect to PaymentGateway
    if amount <= 500:
        if validate_name(name) and validate_card(card_number) and validate_date(exp_date) and validate_amount(amount):
            # Redirecting to desired PaymentGateway if all goes good
            if amount <= 20:  # if amount is less than 21 redirect to CheapPaymentGateway
                gateway = 'CheapPaymentGateway'
            else:  # if amount is less than 21 redirect to ExpensivePaymentGateway
                gateway = 'ExpensivePaymentGateway'
        else:
            abort(400)  # 400 Bad Request: For any incorrect card credentials
    else:
        # if amount is greater than 500 redirect to PremiumPaymentGateway
        if retry_count < 3:
            if validate_name(name) and validate_card(card_number) and validate_date(exp_date) and validate_amount(amount):
                gateway = 'PremiumPaymentGateway'
            else:
                retry_count += 1
        else:
            abort(400, 'Too many wrong attempt!')  # 400 Bad Request: Exceeding limited transaction request

    # Creating response dictionary with all details
    response['Name'] = name
    response['Card Number'] = card_number
    response['Expiration Date'] = exp_date
    response['Amount'] = amount
    response['Payment Gateway'] = gateway

    if gateway != 'None':
        return jsonify(response)

    return abort(500)


app.run()
