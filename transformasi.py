import matplotlib.pyplot as plt
import create_line as ln

def translate_from_keyboard():
    tx = int(input("Masukkan nilai translasi tx: "))
    ty = int(input("Masukkan nilai translasi ty: "))
    return tx, ty

def translate_from_object(objects):
    print("Daftar objek yang tersedia:")
    for i, obj in enumerate(objects):
        print("{}. Line: {}".format(i+1, obj))

    choice = int(input("Pilih objek yang akan ditranslasikan (1-{}): ".format(len(objects))))
    if choice < 1 or choice > len(objects):
        print("Pilihan tidak valid.")
        return None

    obj = objects[choice-1]
    tx = int(input("Masukkan nilai translasi tx: "))
    ty = int(input("Masukkan nilai translasi ty: "))
    return obj, tx, ty

def print_object_coordinates(coordinates):
    x1, y1, x2, y2 = coordinates
    print("Titik A: {}, {}".format(x1, y1))
    print("Titik B: {}, {}".format(x2, y2))

def plot_objects(objects):
    x_coords = objects[::2]  # Get the x-coordinates
    y_coords = objects[1::2]  # Get the y-coordinates

    plt.plot(x_coords, y_coords, marker='o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Translasi Objek')
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.show()


def perform_translation(objects):

    print("=== Transformasi ===")
    print("1. Input dari keyboard")
    print("2. Input dari mouse")
    print("3. Input dari objek yang sudah ada")

    choice = int(input("Pilih metode input (1-4): "))

    if choice == 1:
        [(x1, y1), (x2, y2)] = ln.create_line_from_keyboard()
        tx, ty = translate_from_keyboard()
        objects = [x1+tx, y1+ty, x2+tx, y2+ty]
    elif choice == 2:
        [(x1, y1), (x2, y2)] = ln.create_line_from_mouse()
        tx, ty = translate_from_keyboard()
        objects = [x1+tx, y1+ty, x2+tx, y2+ty]
    elif choice == 3:
        if not objects:
            print("Belum ada objek yang ditambahkan.")
            return
        obj, tx, ty = translate_from_object(objects)
        [(x1, y1), (x2, y2)] = obj
        objects = [x1+tx, y1+ty, x2+tx, y2+ty]
    else:
        print("Pilihan tidak valid.")
        return

    if objects:
        print("=== Koordinat Objek ===")
        print_object_coordinates(objects)

        print("1. Output berupa teks")
        print("2. Output berupa grafik")

        output_choice = int(input("Pilih metode output (1-2): "))
        if output_choice == 1:
            print("=== Output Teks ===")
            print_object_coordinates(objects)
        elif output_choice == 2:
            print("=== Output Grafik ===")
            plot_objects(objects)
        else:
            print("Pilihan tidak valid.")
    else:
        print("Tidak ada objek yang ditambahkan.")

