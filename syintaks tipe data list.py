daftar_hewan = ['Harimau','Beruang','Panda']
print ('Tampilkan daftar hewan yang ada')
print(daftar_hewan)

for hewan in daftar_hewan:
    print(hewan)

print('Tampilkan list yang ada')
print(daftar_hewan[1])

print('\nproses semua dengan for in')
# for hewan in daftar_hewan:
#print(hewan)
daftar_hewan.append('rusa')
daftar_hewan.append('Babi')
daftar_hewan.append('Kuda')

for hewan in daftar_hewan:
    print(hewan)

for hewan in range(0,len(daftar_hewan)):
    print(daftar_hewan[hewan])