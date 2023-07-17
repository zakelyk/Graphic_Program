import matplotlib as plt

def print_clipped_objects(objects):
    print("Daftar objek hasil clipping:")
    for i, obj in enumerate(objects):
        print("Objek {}: ({}, {}) - ({}, {})".format(i+1, obj[0][0], obj[0][1], obj[1][0], obj[1][1]))

def clip_objects(clipping_coordinates, objects):
    clipped_objects = []
    for obj in objects:
        if obj[0][0] >= clipping_coordinates[0][0] and obj[0][1] >= clipping_coordinates[0][1] and obj[1][0] <= clipping_coordinates[1][0] and obj[1][1] <= clipping_coordinates[1][1]:
            clipped_objects.append(obj)
    return clipped_objects

def get_clipping_coordinates():
    x1 = int(input("Masukkan koordinat x1 window clipping: "))
    y1 = int(input("Masukkan koordinat y1 window clipping: "))
    x2 = int(input("Masukkan koordinat x2 window clipping: "))
    y2 = int(input("Masukkan koordinat y2 window clipping: "))
    return [(x1, y1), (x2, y2)]

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

def print_object_list(objects):
    print("Daftar objek yang telah dibuat:")
    for i, obj in enumerate(objects):
        print("Objek {}: ({}, {}) - ({}, {})".format(i+1, obj[0][0], obj[0][1], obj[1][0], obj[1][1]))

def draw_objects(objects):
    for obj in objects:
        x = [coord[0] for coord in obj]
        y = [coord[1] for coord in obj]
        plt.plot(x, y, marker='o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Objek dalam Jendela')
    plt.show()

def clip(objects):
    print("=== Clipping (Objek berupa garis) ===")
    if not objects:
        print("Tidak ada objek yang dibuat. Silakan buat objek terlebih dahulu.")
        return
    print_object_list(objects)

    obj_index = int(input("Pilih objek yang akan di-clip (1-{}): ".format(len(objects))))
    if obj_index < 1 or obj_index > len(objects):
        print("Pilihan objek tidak valid.")
        return

    coordinates = objects[obj_index-1]
    print("=== Objek Sebelum Clipping ===")
    print_line_coordinates(coordinates)
    draw_line(coordinates)

    clipping_coordinates = get_clipping_coordinates()
    if clipping_coordinates[0][0] > clipping_coordinates[1][0] or clipping_coordinates[0][1] > clipping_coordinates[1][1]:
        print("Koordinat window tidak valid.")
        return

    if clipping_coordinates[0][0] == clipping_coordinates[1][0] or clipping_coordinates[0][1] == clipping_coordinates[1][1]:
        print("Koordinat window tidak valid.")
        return

    clipped_objects = clip_objects(clipping_coordinates, objects)
    print_clipped_objects(clipped_objects)
    draw_objects(clipped_objects)