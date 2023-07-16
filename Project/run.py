
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
            import create_line
        elif choice == 2:
            import create_ellipse
        elif choice == 3:
            import transformasi
        elif choice == 4:
            print("Fitur Belum tersedia")
        elif choice == 5:
            print("Fitur belum tersedia")
        elif choice == 6:
            print("Terima kasih telah menggunakan program ini.")
        else:
            print("Pilihan tidak tersedia.")

# Jalankan program utama
main()
