def check_matplotlib():
    try:
        import matplotlib
        return True
    except ImportError:
        print("Modul Matplotlib tidak ditemukan.")
        print("Matplotlib diperlukan untuk menampilkan hasil grafik pada output")
        response = input("Apakah Anda ingin menginstal Matplotlib? (y/n): ")
        if response.lower() == "y":
            try:
                import subprocess
                subprocess.check_call(["pip", "install", "matplotlib"])
                print("Modul Matplotlib berhasil diinstal.")
                return True
            except subprocess.CalledProcessError:
                print("Gagal menginstal Matplotlib.")
                return False
        else:
            print("Anda memilih untuk tidak menginstal Matplotlib.")
            return False

check_matplotlib()
