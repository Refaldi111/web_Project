product = {
    "caffe americano": 37000,
    "caramel macchiato": 59000,
    "asian dolce latte": 55000,
    "caramel latte": 52000,
    "vanilla latte": 52000,
    "caffe latte": 48000,
    "cappuccino": 48000,
   "caffe mocha": 55000,
}

def toko():
    print("Selamat datang, selamat berbelanja")
    print("Berikut adalah daftar barang yang tersedia:")
    for barang, harga in product.items():
        print(f"{barang}: Rp{harga} per cup") 
        
    total_belanja = 0
    while True:
        barang_dipilih = input("Masukkan nama barang yang ingin anda beli(atau 'selesai' untuk selesai)").lower()
        if barang_dipilih.lower() == 'selesai':
             break
        if barang_dipilih not in product:
            print("Maaf, barang tersebut tidak tersedia")
            continue
        jumlah = float(input(f"Berapa cup {barang_dipilih} yang anda inginkan?"))
        total_belanja += product[barang_dipilih] * jumlah
    print(f"total Belanja anda adalah: Rp{total_belanja}")

    def pajak_barang(total_belanja, pajak):
        ppn = total_belanja * pajak
        return ppn

    ppn = pajak_barang(total_belanja, 0.1) 

    print ("ppn 10%:", ppn)

    def diskon_barang(total_belanja, diskon):
        diskon = total_belanja * 0.15
        return diskon

    diskon = diskon_barang(total_belanja, 0.15)

    if (total_belanja > 350000):
        print("diskon 15%:", diskon)
    else:
        print("")

    print("total belanja setelah di hitung dengan pajak dan diskon adalah:", total_belanja + ppn - diskon)
         
toko()       