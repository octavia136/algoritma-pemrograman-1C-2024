ukuran = int(input("Masukkan ukuran: "))

# Mencetak angka 0
for i in range(ukuran):
    if i == 0 or i == ukuran - 1:
        print('x' * ukuran)  # Baris atas dan bawah
    else:
        print('x' + ' ' * (ukuran - 2) + 'x')  # Baris tengah


print()

# Mencetak angka 7
for i in range(ukuran):
    if i == 0:
        print('x' * ukuran)  # Baris atas
    elif i == ukuran - 1:
        print(' ' * (ukuran-1) + 'x')  # Garis vertikal bawah
    else:
        print(' ' * (ukuran-1) + 'x')  # Garis vertikal
print()

# Mencetak angka 0
for i in range(ukuran):
    if i == 0 or i == ukuran - 1:
        print('x' * ukuran)  # Baris atas dan bawah
    else:
        print('x' + ' ' * (ukuran - 2) + 'x')  # Baris tengah

print()
