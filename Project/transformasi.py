import matplotlib.pyplot as plt

def translate_object(coordinates, tx, ty):
    transformed_coordinates = []
    for x, y in coordinates:
        transformed_x = x + tx
        transformed_y = y + ty
        transformed_coordinates.append((transformed_x, transformed_y))
    return transformed_coordinates

def create_object_from_keyboard():
    num_points = int(input("Masukkan jumlah titik pada objek: "))
    coordinates = []
    for i in range(num_points):
        x = int(input("Masukkan koordinat x titik {}: ".format(i+1)))
        y = int(input("Masukkan koordinat y titik {}: ".format(i+1)))
        coordinates.append((x, y))
    return coordinates

def create_object_from_mouse():
    fig, ax = plt.subplots()
    coords = plt.ginput(-1)
    plt.close(fig)
    coordinates = [(int(coord[0]), int(coord[1])) for coord in coords]
    return coordinates

def print_object_coordinates(coordinates):
    for i, coord in enumerate(coordinates):
        x, y = coord
        print("Koordinat titik {}: ({}, {})".format(i+1, x, y))

def plot_object(coordinates):
    x_coords, y_coords = zip(*coordinates)
    plt.plot(x_coords, y_coords, marker='o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Objek')
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.show()

def transform_object():
    print("=== Transformasi Objek ===")
    print("1. Input dari keyboard")
    print("2. Input dari mouse")

    choice = int(input("Pilih metode input (1-2): "))
    if choice == 1:
        coordinates = create_object_from_keyboard()
    elif choice == 2:
        coordinates = create_object_from_mouse()
    else:
        print("Pilihan tidak valid.")
        return

    print("=== Koordinat Objek ===")
    print_object_coordinates(coordinates)

    num_transformations = int(input("Masukkan jumlah transformasi (1-3): "))

    for i in range(num_transformations):
        print("=== Translasi ke-{} ===".format(i+1))
        tx = int(input("Masukkan translasi pada sumbu x (tx): "))
        ty = int(input("Masukkan translasi pada sumbu y (ty): "))

        transformed_coordinates = translate_object(coordinates, tx, ty)

        print("=== Koordinat Objek Setelah Translasi ke-{} ===".format(i+1))
        print_object_coordinates(transformed_coordinates)

        print("1. Output berupa teks")
        print("2. Output berupa grafik")

        output_choice = int(input("Pilih metode output (1-2): "))
        if output_choice == 1:
            # Output berupa teks
            print("=== Output Teks ===")
            print_object_coordinates(transformed_coordinates)
        elif output_choice == 2:
            # Output berupa grafik
            print("=== Output Grafik ===")
            plot_object(transformed_coordinates)
        else:
            print("Pilihan tidak valid.")
            return

        coordinates = transformed_coordinates

# Contoh pemanggilan fungsi transform_object()
transform_object()
