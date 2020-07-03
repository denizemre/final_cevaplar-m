#SORU 1

# d = input("Bir tarih giriniz: ")
# e, n, i = d.split("-")
# z = ["", "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
# n = int(n)
# print(e, z[n], i)


#SORU 2

# x = int(input("Lütfen 0 ile 16 aralığında bir değer giriniz: "))
# carpim = 1
# if x<0 or x>=16:
#     print("Aralıklar dışında bir değer girdiniz. ")
#
# elif x>=9 and x<16:
#     toplam1 = x*(x+1)
#     print("F(x) =" ,toplam1)
# elif x<9 and x>=0:
#     for i in range(x):
#         carpim *= i + 1
#     print("F(x) =" ,carpim*3)


#SORU 3

# sozluk = {"a":1,"b":2,"c":3,"ç":3,"d":4,"e":5,"f":6,"g":7,"ğ":7,"h":8,"ı":9,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,
#           "ö":15,"p":16,"q":17,"r":18,"s":19,"ş":19,"t":20,"u":21,"ü":21,"v":22,"w":23,"x":24,"y":25,"z":26}
# dizi=[]
# ad= 'denizemre'
#
# for d in ad:
#     dizi.append(sozluk[d])
#
# def sifre(dizi):
#     A = [[1, 2, -1], [2, 5, 2], [-1, -2, 2]]
#     e = dizi[:3]
#     n = dizi[3:6]
#     i  = dizi[6:9]
#     z = []
#     m = []
#
#     for j in A:
#         m.append(j[0] * e[0] + j[1] * e[1] + j[2] * e[2])
#
#     z.append(m)
#     m = []
#
#     for k in A:
#         m.append(k[0] * n[0] + k[1] * n[1] + k[2] * n[2])
#
#     z.append(m)
#     m = []
#
#     for l in A:
#         m.append(l[0] * i[0] + l[1] * i[1] + l[2] * i[2])
#
#     z.append(m)
#
#     return z
#
# print(sifre(dizi))

#SORU 4

# numaram = 18041070
#
# list = []
#
# print(1, "den", numaram, "a kadar asal sayılar: ")
#
# for sayi in range(1, numaram + 1):
#     if sayi > 1:
#         for i in range(2, sayi):
#
#             if (sayi % i) == 0:
#                 break
#
#
#         else:
#             print(sayi)
#
#             list.append(sayi)
#
# print(list)


