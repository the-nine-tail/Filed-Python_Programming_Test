# Filed - Python Programing Test

## Steps to run program:
* Install all the dependencies using requirement.txt file
* Run main.py file and place card_validation.py in the same directory

## Test Cases
There are total eight test cases for all possible scenarios.

| INPUT | EXPECTED OUTPUT | ACTUAL OUTPUT | RESULT | PASS/FAIL |
| :---: | :---:           | :---:         | :---:  | :---:     |
| Wrong Card Number | 400 Bad Request | 400 Bad Request | Transaction Failed | Pass |
| Wrong Holder Name | 400 Bad Request | 400 Bad Request | Transaction Failed | Pass |
| Past Expiration Date | 400 Bad Request | 400 Bad Request | Transaction Failed | Pass |
| Negative or Zero Amount | 400 Bad Request | 400 Bad Request | Transaction Failed | Pass |
| Amount < £21 | CheapPaymentGateway | Redirected to CheapPaymentGateway | Transaction Sucessful | Pass |
| Amount > £21 < £500 | ExpensivePaymentGateway | Redirected to ExpensivePaymentGateway | Transaction Sucessful | Pass |
| Amount > £500 | PremiumPaymentGateway | Redirected to PremiumPaymentGateway | Transaction Successful | Pass |
| Wrong attempt in PremiumPaymentGateway | Retry for 3 times | Retry for 3 times | Transaction Successful | Pass |
| Any Other Error | 500 Server Error | 500 Server Error | Transaction Failed | Pass |
