# FiledBackendTask


## How to use?

1. Use "requirements.txt" to install all the dependencies. |  > pip install -r requirements.txt
2. Run the app locally using run.py. | > python run.py
3. Run the test cases by using test_ProcessPayment.py | > python test_ProcessPayment.py

#### Note : To get request code 200, please add {"test": true} to the POST.

## /ProcessPayment

### Inputs
  - CreditCardNumber : string | mandatory | valid Credit card number.
  - CardHolder : string | mandatory | NIL
  - ExpirationDate : DateTime | mandatory | greater than current date.
  - SecurityCode : string | optional | NIL
  - Amount : float | mandatory | positive value.
  
Eg. 
For successful processing. Response 200.

{
   "CreditCardNumber" : "4539148803436467",
   "CardHolder" : "Test Card",
   "ExpirationDate" : "2022-03-23T21:12:32.425",
   "SecurityCode" : "242",
   "Amount" : 20.48,
   "test" : true
}

For Response 400 [invaild input]

{
   "CreditCardNumber" : "4539148803436467",
   "CardHolder" : "Test Card",
   "ExpirationDate" : "2022-03-23T21:12:32.425",
   "SecurityCode" : "242",
   "Amount" : -20.48,
}

For Response 500 [if the payment failed.]

{
   "CreditCardNumber" : "4539148803436467",
   "CardHolder" : "Test Card",
   "ExpirationDate" : "2022-03-23T21:12:32.425",
   "SecurityCode" : "242",
   "Amount" : 20.48,
}
