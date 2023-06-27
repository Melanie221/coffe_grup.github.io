def main():
    print("")
    print("==========================================================")
    print("====================|||Coffee Group|||====================")
    print("==========================================================")
    print("")
    pembeli=input("Masukkan Nama Pembeli : ")
    pegawai=input("Masukkan Nama Pegawai : ")
    print("")
    print("==========================================================")
    print("===================||MENU COFFEE GROUP||==================")
    print("==========================================================")
    print("|   Minuman Coffee    |  Original  |  Panas   |  Dingin  |")
    print("==========================================================")    
    print("| 1. Espresso         |  Rp13000   |  Rp14000 |  Rp15000 |")
    print("| 2. Americano        |  Rp13000   |  Rp14000 |  Rp15000 |")
    print("| 3. Machiato         |  Rp14000   |  Rp15000 |  Rp16000 |")
    print("| 4. Cappucino        |  Rp14000   |  Rp15000 |  Rp16000 |")
    print("| 5. Flat White       |  Rp15000   |  Rp16000 |  Rp17000 |")
    print("| 6. Mocha            |  Rp15000   |  Rp16000 |  Rp17000 |")
    print("| 7. Affogato         |  Rp16000   |  Rp17000 |  Rp18000 |")
    print("| 8. Latte            |  Rp16000   |  Rp17000 |  Rp18000 |")
    print("| 9. Latte Machiato   |  Rp17000   |  Rp18000 |  Rp19000 |")
    print("==========================================================")

    nomor = int(input("Masukan Pilihan\t:"))
    varian = input("Varian (original/panas/dingin):")
    gelas = int(input("Berapa Gelas\t:"))

    if nomor==1:
        if varian=='original':
            harga=13000
            jenis=("Gelas Espresso original")
        elif varian=='panas':
            harga=14000
            jenis=("Gelas Espresso Panas")
        elif varian=='dingin':
            harga=15000
            jenis=("Gelas Espresso Dingin")
    elif nomor==2:
        if varian=='original':
            harga=13000
            jenis=("Gelas Americano original")
        elif varian=='panas':
            harga=14000
            jenis=("Gelas Americano Panas")
        elif varian=='dingin':
            harga=15000
            jenis=("Gelas Americano Dingin")
    elif nomor==3:
        if varian=='original':
            harga=14000
            jenis=("Gelas Machiato original")
        elif varian=='panas':
            harga=15000
            jenis=("Gelas Machiato Panas")
        elif varian=='dingin':
            harga=16000
            jenis=("Gelas Machiato Dingin")
    elif nomor==4:
        if varian=='original':
            harga=14000
            jenis=("Gelas Cappucino original")
        elif varian=='panas':
            harga=15000
            jenis=("Gelas Cappucino Panas")
        elif varian=='dingin':
            harga=16000
            jenis=("Gelas Cappucino Dingin")
    elif nomor==5:
        if varian=='original':
            harga=15000
            jenis=("Gelas Flat White original")
        elif varian=='panas':
            harga=16000
            jenis=("Gelas Flat White Panas")
        elif varian=='dingin':
            harga=17000
            jenis=("Gelas Flat White Dingin")
    elif nomor==6:
        if varian=='original':
            harga=15000
            jenis=("Gelas Mocha original")
        elif varian=='panas':
            harga=16000
            jenis=("Gelas Mocha Panas")
        elif varian=='dingin':
            harga=17000
            jenis=("Gelas Mocha Dingin")
    elif nomor==7:
        if varian=='original':
            harga=16000
            jenis=("Gelas Affogato original")
        elif varian=='panas':
            harga=17000
            jenis=("Gelas Affogato Panas")
        elif varian=='dingin':
            harga=18000
            jenis=("Gelas Affogato Dingin")
    elif nomor==8:
        if varian=='original':
            harga=16000
            jenis=("Gelas Latte original")
        elif varian=='panas':
            harga=17000
            jenis=("Gelas Latte Panas")
        elif varian=='dingin':
            harga=18000
            jenis=("Gelas Latte Dingin")
    elif nomor==9:
        if varian=='original':
            harga=17000
            jenis=("Gelas Latte Machiato original")
        elif varian=='panas':
            harga=18000
            jenis=("Gelas Latte Machiato Panas")
        elif varian=='dingin':
            harga=19000
            jenis=("Gelas Latte Machiato Dingin")
    else:
        print ("Pilihan tidak ada, silahkan masukkan lagi..!!")
        
    total=gelas*harga
    print ("\nTotal harus dibayar: Rp", total)
    uang=int(input("Uang Tunai Pembeli: Rp"))
    kembalian=int(uang-total)
    print ("Kembalian :", kembalian)
    print ("")

    print("=====================================")
    print("========S T R U K B E L I ===========")
    print("=====================================")
    print("Nama Pembeli\t:",pembeli)
    print("Nama Pegawai\t:",pegawai)
    print("Beli\t\t:",gelas,jenis)
    print("Tagihan\t\t: Rp.",total)
    print("Uang\t\t: Rp.",uang)
    print("Kembalian\t: Rp.",kembalian)
    print("=====================================")
    print("=====================================")

    repeat=input("Apakah ingin melakukan pesanan lagi?(y/t): ").lower()
    if repeat=='y':
        main()
    else:
        print("bye")
        exit()
main()
