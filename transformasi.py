import matplotlib.pyplot as plt

def translate_from_keyboard():
    tx = int(input("Masukkan nilai translasi tx: "))
    ty = int(input("Masukkan nilai translasi ty: "))
    return tx, ty

def translate_from_mouse():
    fig, ax = plt.subplots()
    coords = plt.ginput(1)
    plt.close(fig)
    tx = int(coords[0][0])
    ty = int(coords[0][1])
    return tx, ty

def translate_from_object(objects):
    print("Daftar objek yang tersedia:")
    for i, obj in enumerate(objects):
        print("{}. Objek: {}".format(i+1, obj))

    choice = int(input("Pilih objek yang akan ditranslasikan (1-{}): ".format(len(objects))))
    if choice < 1 or choice > len(objects):
        print("Pilihan tidak valid.")
        return None

    obj = objects[choice-1]
    tx = int(input("Masukkan nilai translasi tx: "))
    ty = int(input("Masukkan nilai translasi ty: "))
    return [(x+tx, y+ty) for x, y in obj]

def print_object_coordinates(coordinates):
    for i, coord in enumerate(coordinates):
        print("Koordinat objek {}: {}".format(i+1, coord))

def plot_objects(objects):
    fig, ax = plt.subplots()
    for obj in objects:
        x_coords, y_coords = zip(*obj)
        plt.plot(x_coords, y_coords, marker='o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Translasi Objek')
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.show()

def perform_translation(objects):
    # objects = []

    while True:
        print("=== Transformasi ===")
        print("1. Input dari keyboard")
        print("2. Input dari mouse")
        print("3. Input dari objek")
        print("4. Selesai")

        choice = int(input("Pilih metode input (1-4): "))

        if choice == 1:
            tx, ty = translate_from_keyboard()
            if objects:
                objects.append([(x+tx, y+ty) for x, y in objects[-1]])
            else:
                print("Belum ada objek yang ditambahkan.")
        elif choice == 2:
            tx, ty = translate_from_mouse()
            if objects:
                objects.append([(x+tx, y+ty) for x, y in objects[-1]])
            else:
                print("Belum ada objek yang ditambahkan.")
        elif choice == 3:
            if not objects:
                print("Belum ada objek yang ditambahkan.")
                continue
            translated_obj = translate_from_object(objects)
            if translated_obj:
                objects.append(translated_obj)
        elif choice == 4:
            break
        else:
            print("Pilihan tidak valid.")
            continue

    if objects:
        print("=== Koordinat Objek ===")
        print_object_coordinates(objects[-1])

        print("1. Output berupa teks")
        print("2. Output berupa grafik")

        output_choice = int(input("Pilih metode output (1-2): "))
        if output_choice == 1:
            # Output berupa teks
            print("=== Output Teks ===")
            print_object_coordinates(objects[-1])
        elif output_choice == 2:
            # Output berupa grafik
            print("=== Output Grafik ===")
            plot_objects(objects)
        else:
            print("Pilihan tidak valid.")
    else:
        print("Tidak ada objek yang ditambahkan.")

# Contoh pemanggilan fungsi perform_translation()
# perform_translation()
