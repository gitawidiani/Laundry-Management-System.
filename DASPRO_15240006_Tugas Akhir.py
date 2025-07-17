# Tipe Soal 4 #
# Kelompok 2 #
# Deswita Putria #
# Guntur Surawijaya #
# Sad Gita Widiani #
# Surya Abdi #

import pandas as pd

list_servicename=[]     #Cuci Biasa / Kering
list_serviceprice=[]
list_servicecode=[]
list_typename=[]        #Standar / Coin / Express
list_price=[]
list_typecode=[]
list_setrikaname=[]     #Y/N
list_setrikaprice=[]
list_setrikacode=[]
list_qty=[]
list_subtotal=[]
list_total=0

def title():
    print("All You Can Laundry 'GGSD'".center(75))

title()
print(75*("="))
name_cashier=str(input("Nama Kasir".ljust(26) + ": "))
name_customer=str(input("Nama Pembeli".ljust(26) + ": "))
variant=int(input("Jumlah Data".ljust(26) + ": "))

for i in range(variant):
    print("Data Ke - ", i+1)
    list_servicecode.append(str(input("Kode Layanan [B/K]".ljust(26) + ": ")))
    list_typecode.append(str(input("Kode Tipe Layanan [S/C/E]".ljust(26) + ": ")))
    list_qty.append(int(input("Berat".ljust(26) + ": ")))
    if list_servicecode[i]=="B" or list_servicecode[i]=="b" :
        list_servicename.append("Cuci Biasa".ljust(12))
        list_serviceprice.append(4000)
        if list_typecode[i]=="S" or list_typecode[i]=="s" :
            list_typename.append("Standar".ljust(20))
            list_price.append(5000)
        elif list_typecode[i]=="C" or list_typecode[i]=="c" :
            list_typename.append("Coin (Self Service)".ljust(20))
            list_price.append(2000)
        elif list_typecode[i]=="E" or list_typecode[i]=="e" :
            list_typename.append("Express".ljust(20))
            list_price.append(15000)
        else :
            list_price.append(0)
    elif list_servicecode[i]=="K" or list_servicecode[i]=="k" :
        list_servicename.append("Cuci Kering".ljust(12))
        list_serviceprice.append(6000)
        if list_typecode[i]=="S" or list_typecode[i]=="s" :
            list_typename.append("Standar".ljust(20))
            list_price.append(5000)
        elif list_typecode[i]=="C" or list_typecode[i]=="c" :
            list_typename.append("Coin (Self Service)".ljust(20))
            list_price.append(2000)
        elif list_typecode[i]=="E" or list_typecode[i]=="e" :
            list_typename.append("Express".ljust(20))
            list_price.append(20000)
            
        else :
            list_price.append(0)
    else :
        list_servicename.append("Tidak Ada")
        list_serviceprice.append(0)

    list_setrikacode.append(str(input("Kode Setrika [Y/N]".ljust(26) + ": ")))
    if list_setrikacode[i]=="Y" or list_setrikacode[i]=="y" :
        list_setrikaname.append("Ya".ljust(7))
        list_setrikaprice.append(15000)
    elif list_setrikacode[i]=="N" or list_setrikacode[i]=="n" :
        list_setrikaname.append("Tidak".ljust(7))
        list_setrikaprice.append(0)
    else :
        list_setrikaprice.append(0)
 
    list_subtotal.append(list_serviceprice[i] * list_qty[i] + list_price[i] + list_setrikaprice[i])
    list_total = list_total+list_subtotal[i]
    recap = {
         "Nama Layanan".ljust(10) : list_servicename,
         "Jenis Pelayanan".ljust(20) : list_typename,
         "Setrika" : list_setrikaname,
         "Harga" : list_price,
         "Berat (Kg)" : list_qty,
         "Subtotal" : list_subtotal 
    }

print(75*("="))
print("Bukti Struk Laundry".center(75))
title()
print(75*("="))
print("Nama Kasir".ljust(20) + ": ", name_cashier)
print("Nama Pembeli".ljust(20) + ": ", name_customer)
data_recap = pd.DataFrame(recap)
print(75*"=")
print(data_recap)
print(75*"=")
print(75*"=")
print("Total Bayar : ".rjust(68), list_total)