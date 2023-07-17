import matplotlib.pyplot as plt

def create_ellipse_from_keyboard():
    xc = int(input("Masukkan koordinat x pusat ellipse: "))
    yc = int(input("Masukkan koordinat y pusat ellipse: "))
    r = int(input("Masukkan jari-jari ellipse: "))
    return [(xc, yc), (r,r)]

def create_ellipse_from_mouse():
    fig, ax = plt.subplots()
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])
    coords = plt.ginput(2)
    plt.close(fig)
    xc = int(coords[0][0])
    yc = int(coords[0][1])
    r = int(coords[1][0] - coords[0][0])
    return [(xc, yc), (r,r)]

def print_ellipse_coordinates(coordinates):
    [(xc, yc), (r,r)] = coordinates
    print("Koordinat pusat ellipse: ({}, {})".format(xc, yc))
    print("Jari-jari ellipse:", r)

    x = 0
    y = r

    p = round((5/4) - r)

    points = []

    while x <= y:
        points.append((xc + x, yc + y))
        points.append((xc - x, yc + y))
        points.append((xc + x, yc - y))
        points.append((xc - x, yc - y))

        print("Line : ("+xc+", "+yc+"), ("+(xc + x)+", "+(yc + y)+")")
        print("Line : ("+xc+", "+yc+"), ("+(xc - x)+", "+(yc + y)+")")
        print("Line : ("+xc+", "+yc+"), ("+(xc + x)+", "+(yc - y)+")")
        print("Line : ("+xc+", "+yc+"), ("+(xc - x)+", "+(yc - y)+")")


        if p < 0:
            x += 1
            p += 2 * x + 1
        else:
            x += 1
            y -= 1
            p += 2 * (x - y) + 1

def plot_ellipse(coordinates):
    x_center = coordinates[0][0]
    y_center = coordinates[0][1]
    width = coordinates[1][0]
    height = coordinates[1][1]

    ellipse = plt.Circle((x_center, y_center), width/2)  # Perhatikan perubahan di sini
    fig, ax = plt.subplots()
    ax.add_artist(ellipse)
    ax.set_aspect('equal')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Ellips')
    plt.xlim(x_center - width/2 - 1, x_center + width/2 + 1)
    plt.ylim(y_center - height/2 - 1, y_center + height/2 + 1)
    plt.grid(True)
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

    print("1. Output berupa teks")
    print("2. Output berupa grafik")

    output_choice = int(input("Pilih metode output (1-2): "))
    if output_choice == 1:
        print("=== Output Teks ===")
        print_ellipse_coordinates(coordinates)
        return coordinates
    elif output_choice == 2:
        print("=== Output Grafik ===")
        plot_ellipse(coordinates)
        return coordinates
    else:
        print("Pilihan tidak valid.")
        return

