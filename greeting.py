def hitung_total(harga, qty, diskon_persen=0):

    total = harga * qty

    return total - (total * diskon_persen / 100)
def greet(name):
    message = "Hello, amanda branch edit 2" + name + "!"  # ← you and your partner will both edit this line
    return message

def farewell(name):
    return "Goodbye, amanda branchedit 2" + name + "!"

 

# contoh pakai

print(hitung_total(50000, 3, 10))  # 135000.0