import matplotlib.pyplot as plt

def get_coordinates_from_keyboard():
    x1 = int(input("Masukkan koordinat x1: "))
    y1 = int(input("Masukkan koordinat y1: "))
    x2 = int(input("Masukkan koordinat x2: "))
    y2 = int(input("Masukkan koordinat y2: "))
    return [(x1, y1), (x2, y2)]

def get_coordinates_from_mouse():
    fig, ax = plt.subplots()
    coords = plt.ginput(4)
    plt.close(fig)
    return coords

def draw_line(coordinates):
    x = [coord[0] for coord in coordinates]
    y = [coord[1] for coord in coordinates]
    plt.plot(x, y, marker='o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Garis')
    plt.show()

def print_line_coordinates(coordinates):
    print("Koordinat titik awal: ({}, {})".format(coordinates[0][0], coordinates[0][1]))
    print("Koordinat titik akhir: ({}, {})".format(coordinates[1][0], coordinates[1][1]))

def transform_line(coordinates):
    transformed_coordinates = []
    for coord in coordinates:
        # Implementasi logika transformasi sesuai kebutuhan Anda
        transformed_x = coord[0] + 10
        transformed_y = coord[1] + 10
        transformed_coordinates.append((transformed_x, transformed_y))
    return transformed_coordinates

def print_transformed_line_coordinates(coordinates):
    print("Koordinat titik awal: ({}, {})".format(coordinates[0][0], coordinates[0][1]))
    print("Koordinat titik akhir: ({}, {})".format(coordinates[1][0], coordinates[1][1]))

def get_window_coordinates():
    x1 = int(input("Masukkan koordinat x1 window: "))
    y1 = int(input("Masukkan koordinat y1 window: "))
    x2 = int(input("Masukkan koordinat x2 window: "))
    y2 = int(input("Masukkan koordinat y2 window: "))
    return [(x1, y1), (x2, y2)]

def select_objects_in_window(objects, window_coordinates):
    selected_objects = []
    for obj in objects:
        # Implementasi logika untuk memilih objek yang berada di dalam jendela
        if obj[0][0] >= window_coordinates[0][0] and obj[0][1] >= window_coordinates[0][1] and obj[1][0] <= window_coordinates[1][0] and obj[1][1] <= window_coordinates[1][1]:
            selected_objects.append(obj)
    return selected_objects

def draw_objects(objects):
    for obj in objects:
        x = [coord[0] for coord in obj]
        y = [coord[1] for coord in obj]
        plt.plot(x, y, marker='o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Objek dalam Jendela')
    plt.show()

def print_selected_objects(objects):
    print("Daftar objek yang terpilih:")
    for i, obj in enumerate(objects):
        print("Objek {}: ({}, {}) - ({}, {})".format(i+1, obj[0][0], obj[0][1], obj[1][0], obj[1][1]))

def get_clipping_coordinates():
    x1 = int(input("Masukkan koordinat x1 window clipping: "))
    y1 = int(input("Masukkan koordinat y1 window clipping: "))
    x2 = int(input("Masukkan koordinat x2 window clipping: "))
    y2 = int(input("Masukkan koordinat y2 window clipping: "))
    return [(x1, y1), (x2, y2)]

def clip_objects(objects, clipping_coordinates):
    clipped_objects = []
    for obj in objects:
        # Implementasi logika untuk melakukan clipping objek terhadap window
        # Jika objek tidak ada bagian yang berada di dalam window, objek tidak di-clip
        # Jika objek ada bagian yang berada di dalam window, objek di-clip dan titik potong ditambahkan
        clipped_obj = obj  # Ganti dengan implementasi sesuai kebutuhan
        clipped_objects.append(clipped_obj)
    return clipped_objects

def print_clipped_objects(objects):
    print("Daftar objek hasil clipping:")
    for i, obj in enumerate(objects):
        print("Objek {}: ({}, {}) - ({}, {})".format(i+1, obj[0][0], obj[0][1], obj[1][0], obj[1][1]))

def main():
    lines = []
    while True:
        print("=== Program Grafika Komputer ===")
        print("1. Gambar Garis (Input dari keyboard)")
        print("2. Gambar Garis (Input dari mouse)")
        print("3. Transformasi")
        print("4. Windowing (Objek berupa garis)")
        print("5. Clipping (Objek berupa garis)")
        print("6. Keluar")

        choice = int(input("Masukkan pilihan (1-6): "))

        if choice == 1:
            print("=== Buat Garis (Input dari keyboard) ===")
            coordinates = get_coordinates_from_keyboard()
            print_line_coordinates(coordinates)
            lines.append(coordinates)
            draw_line(coordinates)
        elif choice == 2:
            print("=== Buat Garis (Input dari mouse) ===")
            coordinates = get_coordinates_from_mouse()
            print_line_coordinates(coordinates)
            lines.append(coordinates)
            draw_line(coordinates)
        elif choice == 3:
            print("=== Transformasi ===")
            if not lines:
                print("Tidak ada objek yang dibuat. Silakan buat objek terlebih dahulu.")
                continue
            print("Objek yang tersedia:")
            for i, line in enumerate(lines):
                print("Objek {}: ({}, {}) - ({}, {})".format(i+1, line[0][0], line[0][1], line[1][0], line[1][1]))

            obj_index = int(input("Pilih objek yang akan diubah (1-{}): ".format(len(lines))))
            if obj_index < 1 or obj_index > len(lines):
                print("Pilihan objek tidak valid.")
                continue

            coordinates = lines[obj_index-1]
            print("=== Objek Sebelum Transformasi ===")
            print_line_coordinates(coordinates)
            draw_line(coordinates)

            transform_type = int(input("Pilih jenis transformasi (1-3): "))
            if transform_type < 1 or transform_type > 3:
                print("Jenis transformasi tidak valid.")
                continue

            transformed_coordinates = transform_line(coordinates)
            print("=== Objek Setelah Transformasi ===")
            print_transformed_line_coordinates(transformed_coordinates)
            draw_line(transformed_coordinates)
        elif choice == 4:
            print("=== Windowing (Objek berupa garis) ===")
            if not lines:
                print("Tidak ada objek yang dibuat. Silakan buat objek terlebih dahulu.")
                continue
            print("Objek yang tersedia:")
            for i, line in enumerate(lines):
                print("Objek {}: ({}, {}) - ({}, {})".format(i+1, line[0][0], line[0][1], line[1][0], line[1][1]))

            obj_index = int(input("Pilih objek yang akan dipilih dalam jendela (1-{}): ".format(len(lines))))
            if obj_index < 1 or obj_index > len(lines):
                print("Pilihan objek tidak valid.")
                continue

            coordinates = lines[obj_index-1]
            print("=== Objek yang Dipilih ===")
            print_line_coordinates(coordinates)
            draw_line(coordinates)

            window_coordinates = get_window_coordinates()
            selected_objects = select_objects_in_window(lines, window_coordinates)
            print_selected_objects(selected_objects)
            draw_objects(selected_objects)
        elif choice == 5:
            print("=== Clipping (Objek berupa garis) ===")
            if not lines:
                print("Tidak ada objek yang dibuat. Silakan buat objek terlebih dahulu.")
                continue
            print("Objek yang tersedia:")
            for i, line in enumerate(lines):
                print("Objek {}: ({}, {}) - ({}, {})".format(i+1, line[0][0], line[0][1], line[1][0], line[1][1]))

            obj_index = int(input("Pilih objek yang akan di-clip (1-{}): ".format(len(lines))))
            if obj_index < 1 or obj_index > len(lines):
                print("Pilihan objek tidak valid.")
                continue

            coordinates = lines[obj_index-1]
            print("=== Objek Sebelum Clipping ===")
            print_line_coordinates(coordinates)
            draw_line(coordinates)

            window_coordinates = get_window_coordinates()
            if window_coordinates[0][0] > window_coordinates[1][0] or window_coordinates[0][1] > window_coordinates[1][1]:
                print("Koordinat window tidak valid.")
                continue

            if window_coordinates[0][0] == window_coordinates[1][0] or window_coordinates[0][1] == window_coordinates[1][1]:
                print("Koordinat window tidak valid.")
                continue

            clipped_objects = clip_objects(lines, window_coordinates)
            print_clipped_objects(clipped_objects)
            draw_objects(clipped_objects)
        elif choice == 6:
            print("Terima kasih telah menggunakan program.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

if __name__ == '__main__':
    main()
