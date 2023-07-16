import matplotlib.pyplot as plt

def create_line_from_keyboard():
    x1 = float(input("Masukkan koordinat x1: "))
    y1 = float(input("Masukkan koordinat y1: "))
    x2 = float(input("Masukkan koordinat x2: "))
    y2 = float(input("Masukkan koordinat y2: "))
    return [(x1, y1), (x2, y2)]

def create_line_from_mouse():
    fig, ax = plt.subplots()
    coords = plt.ginput(2)
    plt.close(fig)
    return coords

def print_line_coordinates(coordinates):
    print("Koordinat titik awal: ({}, {})".format(coordinates[0][0], coordinates[0][1]))
    print("Koordinat titik akhir: ({}, {})".format(coordinates[1][0], coordinates[1][1]))

def draw_line(coordinates):
    x = [coord[0] for coord in coordinates]
    y = [coord[1] for coord in coordinates]
    plt.plot(x, y, marker='o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Garis')
    plt.show()

def create_line():
    print("=== Membuat Garis ===")
    print("1. Input dari keyboard")
    print("2. Input dari mouse")

    choice = int(input("Pilih metode input (1-2): "))
    if choice == 1:
        coordinates = create_line_from_keyboard()
    elif choice == 2:
        coordinates = create_line_from_mouse()
    else:
        print("Pilihan tidak valid.")
        return

    print("=== Koordinat Garis ===")
    print_line_coordinates(coordinates)

    print("1. Output berupa teks")
    print("2. Output berupa gambar")

    output_choice = int(input("Pilih metode output (1-2): "))
    if output_choice == 1:
        # Output berupa teks
        print("=== Output Teks ===")
        print_line_coordinates(coordinates)
    elif output_choice == 2:
        # Output berupa gambar
        print("=== Output Gambar ===")
        draw_line(coordinates)
    else:
        print("Pilihan tidak valid.")
        return

# Contoh pemanggilan fungsi create_line()
create_line()
