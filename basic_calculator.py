# Kalkulator sedeharna buatan Sei

# Function buat penambahan, pengurangan, perkalian, pembagian, dll
def tambah(x,y):
  return x + y

def kurang(x,y):
  return x - y

def kali(x,y):
  return x * y 

def bagi(x,y):
  return x / y

# Ambil Input Dari User
ambilInputX = input("Masukan Nomor ke-1: ")
ambilInputY = input("Masukan Nomor ke-2: ")
op = input("tambah, kurang, kali, bagi? ")

# Else-if untuk decision / penentuan output
if (op.upper() == "TAMBAH"):
  print(f'{ambilInputX} + {ambilInputY} = {tambah(int(ambilInputX), int(ambilInputY))}')
elif (op.upper() == "KURANG"):
  print(f'{ambilInputX} - {ambilInputY} = {kurang(int(ambilInputX), int(ambilInputY))}')
elif (op.upper() == "KALI"):
  print(f'{ambilInputX} x {ambilInputY} = {kali(int(ambilInputX), int(ambilInputY))}')
elif (op.upper() == "BAGI"):
  print(f'{ambilInputX} : {ambilInputY} = {bagi(int(ambilInputX), int(ambilInputY))}')
else:
  print("Error")
