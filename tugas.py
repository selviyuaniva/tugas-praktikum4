data=[]
while(True):
    NIM=input("NIM: ")
    Nama=input("Nama: ")
    Tugas=int(input("Nilai Tugas: "))
    UTS=int(input("Nilai UTS: "))
    UAS=int(input("Nilai UAS: "))
    Akhir=(30 * Tugas / 100) + (35 * UTS / 100) + (35 * UAS / 100)
    data.append([NIM, Nama, Tugas, UTS, UAS, Akhir])
    ulangi=input("Tambah data (y/t)?")
    if ulangi.lower() == 't' :
        break;

print("\nDaftar Nama\n")
print("====================================================================")
print("|    NIM    |      Nama     |  Tugas  |  UTS   |  UAS   |   Akhir  |")
print("====================================================================")
for x in data:
    print("| {0:8s} | {1:6s} | {2:6d}  | {3:5d}  | {4:4d}  | {5:5f} |".format(x[0], x[1], x[2], x[3], x[4], x[5]))
print ("====================================================================")


