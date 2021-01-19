# app/logic.py


from credit_card_checker import CreditCardChecker

from datetime import datetime

def check_if_request_is_valid(data):
        if not data.get("CreditCardNumber"):
            return False
        if not data.get("CardHolder"):
            return False
        if not data.get("ExpirationDate"):
            return False
        if not data.get("Amount"):
            return False
        return True


def check_if_args_are_vaild(data):
    if not CreditCardChecker(data["CreditCardNumber"]).valid():
        return False
    if len(data["CardHolder"]) < 1:
        return False
    if datetime.utcnow() > datetime.strptime(data["ExpirationDate"], "%Y-%m-%dT%H:%M:%S.%f"):
        return False
    if data["Amount"] < 0:
        return False
    return True 

 
def useCheapPaymentGateway(data):
    # Returns True if payment is processed else False
    if data.get("test") and data.get("test") == True:
        return True
    else:
        return False


def useExpensivePaymentGateway(data):
    # Returns True if payment is processed else False
    if data.get("test") and data.get("test") == True:
        return True
    else:
        return False


def usePremiumPaymentGateway(data):
    # Returns True if payment is processed else False
    if data.get("test") and data.get("test") == True:
        return True
    else:
        return False