import check_matplotlib
from create_ellipse import create_ellipse
from create_line import create_line
from transformasi import perform_translation

objects = []
def main():

    choice = 0

    while choice != 6:
        print("=== Menu Pilihan Fitur ===")
        print("1. Membuat Garis")
        print("2. Membuat Ellipse")
        print("3. Transformasi Objek")
        print("4. Windowing")
        print("5. Clipping")
        print("6. Keluar")

        choice = int(input("Pilih fitur (1-6): "))

        if choice == 1:
            coordinates = create_line()
            objects.append(coordinates)
        elif choice == 2:
            coordinates = create_ellipse()
            objects.append(coordinates)
        elif choice == 3:
            perform_translation(objects)
        elif choice == 4:
            print("\n!!!Fitur Belum tersedia!!!\n")
        elif choice == 5:
            print("\n!!!Fitur belum tersedia!!!\n")
        elif choice == 6:
            print("Terima kasih telah menggunakan program ini.")
        else:
            print("Pilihan tidak tersedia.")

# Jalankan program utama
main()
