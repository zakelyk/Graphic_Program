import create_line
import create_ellipse
import transformasi

def main():
    lines = []
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
            create_ellipse
        elif choice == 3:
            print("=== Transformasi ===")
            transformasi()
        elif choice == 4:
            print("=== Windowing (Objek berupa garis) ===")

        elif choice == 5:
            print("=== Clipping (Objek berupa garis) ===")

        elif choice == 6:
            print("Terima kasih telah menggunakan program.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")