def menghitung_range():
    print("PROGRAM MENGHITUNG JUMLAH RANGE")
    n = input("masukan angka pertama")
    n = int (n)
    input2=int(input('masukkan angka kedua'))
    sum = 0
    for i in range(n, input2+1, 1):
        sum = sum+i
    print("Jumlah range adalah: ", sum )
menghitung_range()