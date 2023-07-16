import matplotlib.pyplot as plt

def create_line_from_keyboard():
    x1 = int(input("Masukkan koordinat x1: "))
    y1 = int(input("Masukkan koordinat y1: "))
    x2 = int(input("Masukkan koordinat x2: "))
    y2 = int(input("Masukkan koordinat y2: "))
    return x1, y1, x2, y2

def create_line_from_mouse():
    fig, ax = plt.subplots()
    ax.set_xlim([0, 10])  # Set x-axis limits to encompass a larger area
    ax.set_ylim([0, 10])  # Set y-axis limits to encompass a larger area
    coords = plt.ginput(2)
    plt.close(fig)
    x1, y1 = int(coords[0][0]), int(coords[0][1])
    x2, y2 = int(coords[1][0]), int(coords[1][1])
    return x1, y1, x2, y2

def print_line_coordinates(coordinates):
    x1, y1, x2, y2 = coordinates
    print("Koordinat titik awal: ({}, {})".format(x1, y1))
    print("Koordinat titik akhir: ({}, {})".format(x2, y2))

def draw_line(coordinates):
    x1, y1, x2, y2 = coordinates

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = 2 * dy - dx

    x = x1
    y = y1

    points = [(x, y)]

    while x < x2:
        x += 1
        if p < 0:
            p += 2 * dy
        else:
            y += 1 if y < y2 else -1
            p += 2 * (dy - dx)
        points.append((x, y))

    x_coords, y_coords = zip(*points)

    plt.plot(x_coords, y_coords, marker='o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Garis')
    plt.grid(True, linestyle='--', linewidth=0.5)
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