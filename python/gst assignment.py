def calcGstShare(price, rate):
    return price * (rate / 2) / 100
def printGstDetail():
    SGST = CGST = calcGstShare(price, rate)
    print("Actual price of the item :", price)
    print("Price after applying CGST :", CGST)
    print("Price after applying SGST :", SGST)
    print("Total price with GST :", price + CGST + SGST)
price = float(input("Price before GST : "))
rate = float(input("GST rate : "))

printGstDetail()