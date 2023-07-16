from create_line import create_line
from create_ellipse import create_ellipse
from transformasi import transform_object
# from windowing import windowing
# from clipping import clipping

def main():
    while True:
        print("=== Program Grafika Komputer ===")
        print("1. Membuat Garis")
        print("2. Membuat Ellipse")
        print("3. Transformasi")
        print("4. Windowing")
        print("5. Clipping")
        print("6. Keluar")

        choice = int(input("Masukkan pilihan (1-6): "))

        if choice == 1:
            print("=== Membuat Garis ===")
            create_line()
        elif choice == 2:
            print("=== Membuat Ellipse ===")
            create_ellipse()
        elif choice == 3:
            print("=== Transformasi ===")
            transform_object()
        elif choice == 4:
            print("=== Windowing (Objek berupa garis) ===")
            # windowing
            print("fitur belum tersedia")
        elif choice == 5:
            print("=== Clipping (Objek berupa garis) ===")
            # clipping()
            print("Fitur belum tersedia")
        elif choice == 6:
            print("Terima kasih telah menggunakan program.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

if __name__ == '__main__':
    main()