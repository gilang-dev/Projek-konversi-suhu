import os
def menu ():
    os.system("cls")
    print ("=====================================================================")
    print ("                  Selamat datang di Koversi suhu :)")
    print ("=====================================================================")
    print ("""    01. Celcius to fahrenheit          02. Fahrenheit to Celcius
    03. Kelvin to Celcius              04. Reamur to Celcius
    05. Celcius to Kelvin              06. Celcius to Reamur
    07. Fahrenheit to Kelvin           08. Fahrenheit to Reamur
    09. Kelvin to Fahrenheit           10. Kelvin to Reamur
    11. Reamur to Fahrenheit           12. Reamur to Kelvin""")
    print ("=====================================================================")
    pilihan=int(input("Masukkan Pilihan menu : "))
    while True:
     try:
        if pilihan ==1:
           nomor1()
        elif pilihan==2:
           nomor2()
        elif pilihan==3:
           nomor3()
        elif pilihan==4:
           nomor4()
        elif pilihan==5:
           nomor5()
        elif pilihan==6:
           nomor6()
        elif pilihan ==7:
           nomor7()
        elif pilihan==8:
           nomor8()
        elif pilihan==9:
           nomor9()
        elif pilihan==10:
           nomor10()
        elif pilihan==11:
           nomor11()
        elif pilihan==12:
           nomor12()
        else:
           print("Pilihan tidak valid. Silakan coba lagi.")
           break
     except ValueError:
        print("Harus berupa angka yaa :)")


def nomor1():
   while True:
      try:
         celcius=float(input("Masukkan suhu CELCIUS dalam bentuk desimal (atau keluar 0.0) : "))
         if celcius==0.0:
            menu()
         else:
            hasil =(celcius *9/5)+32 
            print(f"Jadi Hasil konvertnya adalah :{hasil:.2f} FAHRENHEIT")
         break
      except ValueError:
         print("Data Harus berformat desimal contoh (36,0)")

def nomor2():   
   while True:
      try:
         fahrenheit =float(input("Masukkan suhu fahrenheit dalam bentuk desimal (0.0 untuk exit): "))
         if fahrenheit==0.0:
            menu()
         else:
          hasil =(fahrenheit-32)*5/9
          print(f"Jadi Hasil konvertnya adalah :{hasil:.2f} CELCIUS")
         break
      except ValueError:
         print("Data Harus berformat desimal contoh (36,0)")

def nomor3():   
   while True:
      try:
         kelvin =float(input("Masukkan suhu KELVIN dalam bentuk desimal (0.0 untuk exit): "))
         if kelvin==0.0:
            menu()
         else:
          hasil =(kelvin-273)
          print(f"Jadi Hasil konvertnya adalah :{hasil:.2f} CELCIUS")
         break
      except ValueError:
         print("Data Harus berformat desimal contoh (36,0)")

def nomor4():   
   while True:
      try:
         reamur =float(input("Masukkan suhu REAMUR dalam bentuk desimal (0.0 untuk exit): "))
         if reamur==0.0:
            menu()
         else:
          hasil =(reamur*5/4)
          print(f"Jadi Hasil konvertnya adalah :{hasil:.2f} CELCIUS")
         break
      except ValueError:
         print("Data Harus berformat desimal contoh (36,0)")

def nomor5():
   while True:
      try:
         celcius=float(input("Masukkan suhu CELCIUS dalam bentuk desimal (atau keluar 0.0) : "))
         if celcius==0.0:
            menu()
         else:
            hasil =celcius+273 
            print(f"Jadi Hasil konvertnya adalah :{hasil:.2f} KELVIN")
         break
      except ValueError:
         print("Data Harus berformat desimal contoh (36,0)")

def nomor6():
   while True:
      try:
         celcius=float(input("Masukkan suhu CELCIUS dalam bentuk desimal (atau keluar 0.0) : "))
         if celcius==0.0:
            menu()
         else:
            hasil =celcius *4/5 
            print(f"Jadi Hasil konvertnya adalah :{hasil:.2f} REAMUR")
         break
      except ValueError:
         print("Data Harus berformat desimal contoh (36,0)")

def nomor7():   
   while True:
      try:
         fahrenheit =float(input("Masukkan suhu fahrenheit dalam bentuk desimal (0.0 untuk exit): "))
         if fahrenheit==0.0:
            menu()
         else:
          hasil =(fahrenheit)
          print(f"Jadi Hasil konvertnya adalah :{hasil:.2f} KELVIN")
         break
      except ValueError:
         print("Data Harus berformat desimal contoh (36,0)")

def nomor8():   
   while True:
      try:
         fahrenheit =float(input("Masukkan suhu fahrenheit dalam bentuk desimal (0.0 untuk exit): "))
         if fahrenheit==0.0:
            menu()
         else:
          hasil =4/9*(fahrenheit-32)
          print(f"Jadi Hasil konvertnya adalah :{hasil:.2f} REAMUR")
         break
      except ValueError:
         print("Data Harus berformat desimal contoh (36,0)")

def nomor9():   
   while True:
      try:
         kelvin =float(input("Masukkan suhu KELVIN dalam bentuk desimal (0.0 untuk exit): "))
         if kelvin==0.0:
            menu()
         else:
          hasil =(kelvin)
          print(f"Jadi Hasil konvertnya adalah :{hasil:.2f} FAHRENHEIT")
         break
      except ValueError:
         print("Data Harus berformat desimal contoh (36,0)")

def nomor10():   
   while True:
      try:
         kelvin =float(input("Masukkan suhu KELVIN dalam bentuk desimal (0.0 untuk exit): "))
         if kelvin==0.0:
            menu()
         else:
          hasil =4/5*(kelvin-273)
          print(f"Jadi Hasil konvertnya adalah :{hasil:.2f} REAMUR")
         break
      except ValueError:
         print("Data Harus berformat desimal contoh (36,0)")

def nomor11():   
   while True:
      try:
         reamur =float(input("Masukkan suhu REAMUR dalam bentuk desimal (0.0 untuk exit): "))
         if reamur==0.0:
            menu()
         else:
          hasil =(reamur*9/4)+32
          print(f"Jadi Hasil konvertnya adalah :{hasil:.2f} FAHRENHEIT")
         break
      except ValueError:
         print("Data Harus berformat desimal contoh (36,0)")

def nomor12():   
   while True:
      try:
         reamur =float(input("Masukkan suhu REAMUR dalam bentuk desimal (0.0 untuk exit): "))
         if reamur==0.0:
            menu()
         else:
          hasil =(reamur*5/4)+273
          print(f"Jadi Hasil konvertnya adalah :{hasil:.2f} KELVIN")
         break
      except ValueError:
         print("Data Harus berformat desimal contoh (36,0)")

