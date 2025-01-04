def validasi_form():
    
    nama_lengkap = input("Masukkan nama lengkap: ")
    nomor_telepon = input("Masukkan nomor telepon: ")
    email = input("Masukkan email: ")
    
    if not nama_lengkap.replace(" ", "").isalpha():
        print("Error: Nama lengkap harus hanya berisi huruf.")
        return
    
    if not nomor_telepon.isdigit():
        print("Error: Nomor telepon harus hanya berisi angka.")
        return
    
    if "@" not in email or "." not in email:
        print("Error: Email harus mengandung karakter '@' dan '.'.")
        return
    
    print("Data pendaftaran valid.")

validasi_form()