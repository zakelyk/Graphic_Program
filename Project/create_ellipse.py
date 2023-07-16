import matplotlib.pyplot as plt

def create_ellipse_from_keyboard():
    xc = int(input("Masukkan koordinat x pusat ellipse: "))
    yc = int(input("Masukkan koordinat y pusat ellipse: "))
    a = int(input("Masukkan panjang sumbu horizontal (a): "))
    b = int(input("Masukkan panjang sumbu vertikal (b): "))
    return xc, yc, a, b

def create_ellipse_from_mouse():
    fig, ax = plt.subplots()
    ax.set_xlim([0, 10])  # Set x-axis limits to encompass a larger area
    ax.set_ylim([0, 10])  # Set y-axis limits to encompass a larger area
    coords = plt.ginput(2)
    plt.close(fig)
    xc = int(coords[0][0])
    yc = int(coords[0][1])
    a = int(coords[1][0] - coords[0][0])
    b = int(coords[1][1] - coords[0][1])
    return xc, yc, a, b

def print_ellipse_coordinates(coordinates):
    xc, yc, a, b = coordinates
    print("Koordinat pusat ellipse: ({}, {})".format(xc, yc))
    print("Panjang sumbu horizontal (a):", a)
    print("Panjang sumbu vertikal (b):", b)

def plot_ellipse(coordinates):
    xc, yc, a, b = coordinates

    x = 0
    y = b

    p = round(b**2 - a**2 * b + (a**2) / 4)

    points = []

    while 2 * (b**2) * x < 2 * (a**2) * y:
        points.append((xc + x, yc + y))
        points.append((xc - x, yc + y))
        points.append((xc + x, yc - y))
        points.append((xc - x, yc - y))

        if p < 0:
            x += 1
            p += 2 * (b**2) * x + (b**2)
        else:
            x += 1
            y -= 1
            p += 2 * (b**2) * x - 2 * (a**2) * y + (b**2)

    p = round(b**2 * (x + 0.5)**2 + a**2 * (y - 1)**2 - a**2 * b**2)

    while y >= 0:
        points.append((xc + x, yc + y))
        points.append((xc - x, yc + y))
        points.append((xc + x, yc - y))
        points.append((xc - x, yc - y))

        if p > 0:
            y -= 1
            p += -2 * (a**2) * y + (a**2)
        else:
            x += 1
            y -= 1
            p += 2 * (b**2) * x - 2 * (a**2) * y + (a**2)

    x_coords, y_coords = zip(*points)

    plt.plot(x_coords, y_coords, marker='o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Ellipse')
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.show()

def create_ellipse():
    print("=== Membuat Ellipse ===")
    print("1. Input dari keyboard")
    print("2. Input dari mouse")

    choice = int(input("Pilih metode input (1-2): "))
    if choice == 1:
        coordinates = create_ellipse_from_keyboard()
    elif choice == 2:
        coordinates = create_ellipse_from_mouse()
    else:
        print("Pilihan tidak valid.")
        return

    print("=== Koordinat Ellipse ===")
    print_ellipse_coordinates(coordinates)

    print("1. Output berupa teks")
    print("2. Output berupa grafik")

    output_choice = int(input("Pilih metode output (1-2): "))
    if output_choice == 1:
        # Output berupa teks
        print("=== Output Teks ===")
        print_ellipse_coordinates(coordinates)
    elif output_choice == 2:
        # Output berupa grafik
        print("=== Output Grafik ===")
        plot_ellipse(coordinates)
    else:
        print("Pilihan tidak valid.")
        return

# Contoh pemanggilan fungsi create_ellipse()
create_ellipse()
