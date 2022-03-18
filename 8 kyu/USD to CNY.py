def usdcny(usd):
    yuan = 6.75 * usd
    yuan ="{:.2f}".format(yuan)
    return yuan + " Chinese Yuan"

print(usdcny(2558))
print(usdcny(15))
print(usdcny(465))