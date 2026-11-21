def hitung_total(harga, qty, diskon_persen=0):

    total = harga * qty

    return total - (total * diskon_persen / 100)

 

# contoh pakai

print(hitung_total(50000, 3, 10))  # 135000.0