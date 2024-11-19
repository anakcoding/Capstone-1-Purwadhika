import datetime
from tabulate import tabulate

def rupiah_format(angka, with_prefix=True, desimal=2):
    formatted_angka = f"{angka:,.{0}f}"
    
    # Mengganti koma dengan titik untuk pemisah ribuan
    formatted_angka = formatted_angka.replace(",", ".")
    
    # Menambahkan prefix "Rp" jika dengan_prefix True
    if with_prefix:
        return f"Rp{formatted_angka}" + ',00'
    
    return formatted_angka + ',00'

def validate_date(date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
            return True
        except ValueError:
            return False

transactions = [
    {"id": 1, "tanggal": datetime.date(2024, 9, 1), "kategori": "Gaji", "jenis": "Pemasukan", "jumlah": 10000000, "deskripsi": "Gaji bulan September"},
    {"id": 2, "tanggal": datetime.date(2024, 9, 2), "kategori": "Makanan", "jenis": "Pengeluaran", "jumlah": 50000, "deskripsi": "Makan siang September"},
    {"id": 3, "tanggal": datetime.date(2024, 9, 3), "kategori": "Transportasi", "jenis": "Pengeluaran", "jumlah": 25000, "deskripsi": "Naik ojek September"},
    {"id": 4, "tanggal": datetime.date(2024, 9, 4), "kategori": "Belanja", "jenis": "Pengeluaran", "jumlah": 80000, "deskripsi": "Belanja bulanan September"},
    {"id": 5, "tanggal": datetime.date(2024, 9, 5), "kategori": "Kesehatan", "jenis": "Pengeluaran", "jumlah": 50000, "deskripsi": "Beli obat September"},
    {"id": 6, "tanggal": datetime.date(2024, 9, 6), "kategori": "Bonus", "jenis": "Pemasukan", "jumlah": 2000000, "deskripsi": "Bonus kinerja September"},
    {"id": 7, "tanggal": datetime.date(2024, 10, 1), "kategori": "Gaji", "jenis": "Pemasukan", "jumlah": 10000000, "deskripsi": "Gaji bulan Oktober"},
    {"id": 8, "tanggal": datetime.date(2024, 10, 2), "kategori": "Transportasi", "jenis": "Pengeluaran", "jumlah": 25000, "deskripsi": "Naik ojek ke kantor Oktober"},
    {"id": 9, "tanggal": datetime.date(2024, 10, 3), "kategori": "Makanan", "jenis": "Pengeluaran", "jumlah": 50000, "deskripsi": "Makan siang Oktober"},
    {"id": 10, "tanggal": datetime.date(2024, 10, 5), "kategori": "Belanja", "jenis": "Pengeluaran", "jumlah": 70000, "deskripsi": "Belanja mingguan Oktober"},
    {"id": 11, "tanggal": datetime.date(2024, 11, 1), "kategori": "Gaji", "jenis": "Pemasukan", "jumlah": 10000000, "deskripsi": "Gaji bulanan"},
    {"id": 12, "tanggal": datetime.date(2024, 11, 2), "kategori": "Makanan", "jenis": "Pengeluaran", "jumlah": 45000, "deskripsi": "Makan siang di kantin"},
    {"id": 13, "tanggal": datetime.date(2024, 11, 3), "kategori": "Bonus", "jenis": "Pemasukan", "jumlah": 1000000, "deskripsi": "Bonus kinerja"},
    {"id": 14, "tanggal": datetime.date(2024, 11, 4), "kategori": "Transportasi", "jenis": "Pengeluaran", "jumlah": 20000, "deskripsi": "Naik ojek ke kantor"},
    {"id": 15, "tanggal": datetime.date(2024, 11, 5), "kategori": "Belanja", "jenis": "Pengeluaran", "jumlah": 120000, "deskripsi": "Belanja bulanan di supermarket"},
    {"id": 16, "tanggal": datetime.date(2024, 11, 6), "kategori": "Makanan", "jenis": "Pengeluaran", "jumlah": 30000, "deskripsi": "Sarapan di warung"},
    {"id": 17, "tanggal": datetime.date(2024, 11, 7), "kategori": "Hiburan", "jenis": "Pengeluaran", "jumlah": 100000, "deskripsi": "Nonton film di bioskop"},
    {"id": 18, "tanggal": datetime.date(2024, 11, 8), "kategori": "Bunga Investasi", "jenis": "Pemasukan", "jumlah": 200000, "deskripsi": "Bunga investasi bulanan"},
    {"id": 19, "tanggal": datetime.date(2024, 11, 9), "kategori": "Makanan", "jenis": "Pengeluaran", "jumlah": 60000, "deskripsi": "Makan malam di restoran"},
    {"id": 20, "tanggal": datetime.date(2024, 11, 10), "kategori": "Transportasi", "jenis": "Pengeluaran", "jumlah": 15000, "deskripsi": "Naik angkot"},
    {"id": 21, "tanggal": datetime.date(2024, 11, 11), "kategori": "Kesehatan", "jenis": "Pengeluaran", "jumlah": 80000, "deskripsi": "Beli vitamin"},
    {"id": 22, "tanggal": datetime.date(2024, 11, 13), "kategori": "Belanja", "jenis": "Pengeluaran", "jumlah": 50000, "deskripsi": "Beli kebutuhan rumah tangga"},
    {"id": 23, "tanggal": datetime.date(2024, 11, 14), "kategori": "Pendidikan", "jenis": "Pengeluaran", "jumlah": 120000, "deskripsi": "Beli buku pelajaran"},
    {"id": 24, "tanggal": datetime.date(2024, 11, 15), "kategori": "Bonus", "jenis": "Pemasukan", "jumlah": 1500000, "deskripsi": "Bonus proyek selesai"},
    {"id": 25, "tanggal": datetime.date(2024, 11, 16), "kategori": "Makanan", "jenis": "Pengeluaran", "jumlah": 40000, "deskripsi": "Beli kopi di kafe"},
    {"id": 26, "tanggal": datetime.date(2024, 11, 17), "kategori": "Transportasi", "jenis": "Pengeluaran", "jumlah": 25000, "deskripsi": "Naik taksi online"},
    {"id": 27, "tanggal": datetime.date(2024, 11, 18), "kategori": "Investasi", "jenis": "Pemasukan", "jumlah": 500000, "deskripsi": "Dividen saham"}
]

budget = [
    {"kategori": "Makanan", "anggaran": 1000000, "pengeluaran": 0},
    {"kategori": "Transportasi", "anggaran": 500000, "pengeluaran": 0},
    {"kategori": "Belanja", "anggaran": 1000000, "pengeluaran": 0},    
    {"kategori": "Hiburan", "anggaran": 1000000, "pengeluaran": 0},
    {"kategori": "Kesehatan", "anggaran": 1000000, "pengeluaran": 0},
    {"kategori": "Pendidikan", "anggaran": 1000000, "pengeluaran": 0},
    {"kategori": "Investasi", "anggaran": 500000, "pengeluaran": 0},
]

list_column_transaction = [{"name": "tanggal", 'can_change': True, 'type': 'date'}, {"name": "kategori", 'can_change': True, 'type': 'str'}, {"name": "jenis", 'can_change': False, 'type': 'str'}, {"name": "jumlah", 'can_change': True, 'type': 'int'}, {"name": "deskripsi", 'can_change': True, 'type': 'str'}]

list_column_anggaran = [{"name": "kategori", 'can_change': True, 'type': 'str'}, {"name": "anggaran", 'can_change': True, 'type': 'int'}]

def search_transactions(transactions, column, search_term=None, search_type=None, amount=None, amount_range=None, search_date_type=None, search_date=None, date_range=None):
    search_term = search_term.lower() if search_term else None  # Mengubah ke huruf kecil agar pencarian tidak case-sensitive
    results = []

    for transaction in transactions:
        # Pencarian berdasarkan search_term (kategori, jenis, deskripsi, tanggal)
        matches_search_term = False
        if search_term:
            if (search_term in str(transaction[column]).lower()):
                matches_search_term = True
        else:
            matches_search_term = True

        # Pencarian berdasarkan jumlah
        matches_amount = False
        if search_type and amount is not None:
            if search_type == "exact" and transaction['jumlah'] == amount:
                matches_amount = True
            elif search_type == "greater" and transaction['jumlah'] > amount:
                matches_amount = True
            elif search_type == "less" and transaction['jumlah'] < amount:
                matches_amount = True
        elif amount_range:  # Cek apakah ada rentang jumlah
            if amount_range[0] <= transaction['jumlah'] <= amount_range[1]:
                matches_amount = True
        else:
            matches_amount = True
            
        matches_date = False
        if search_date_type and search_date:
            if search_date_type == "exact" and transaction['tanggal'] == search_date:
                matches_date = True
            elif search_date_type == "before" and transaction['tanggal'] < search_date:
                matches_date = True
            elif search_date_type == "after" and transaction['tanggal'] > search_date:
                matches_date = True
        elif date_range:  # Cek apakah ada rentang tanggal
            if date_range[0] <= transaction['tanggal'] <= date_range[1]:
                matches_date = True
        else:
            matches_date = True
        
        if (matches_search_term and matches_amount and matches_date):
            results.append(transaction)

    return results

def bubble_sort(list_data, key, reverse=False):
    data = list_data.copy()
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            # Membandingkan dua data berdasarkan key (misalnya 'jumlah')
            if reverse:
                if data[j][key] < data[j+1][key]:  # Urutkan menurun
                    data[j], data[j+1] = data[j+1], data[j]
            else:
                if data[j][key] > data[j+1][key]:  # Urutkan menaik
                    data[j], data[j+1] = data[j+1], data[j]
    return data

def find_column_in_transaction(name,list_column,can_change=False):
    column_transaction = next(filter(lambda column : column['name'] == name,list_column), False)
    if(column_transaction == False):
        return False
    else:
        if can_change == False:
            return column_transaction
        else:
            if column_transaction['can_change'] == True:
                return column_transaction
            else: return False

def invalid_input():
    print(text_infromasi(text="Input invalid, silahkan masukkan ulang!"))

def validasi_integer(value, text):
    while True:
        if(value.isdigit() == False):
            invalid_input()
            value = input(f'{text}').strip()
        else:
            break
    return int(value)

def validasi_date(text):
    value = input(f'{text}').strip()
    while True:
        if(validate_date(value) == False):
            invalid_input()
            value = input(f'{text}').strip()
        else:
            return datetime.datetime.fromisoformat(value).date()

def validasi_input_kosong(text):
    value = input(f'{text}').strip()
    while True:
        if not value:
            invalid_input()
            value = input(f'{text}').strip()
        else:
            return value
    
def text_infromasi(sep='-', text=''):
    return f'{sep * (20 + len(text))}\n{' '*10}{text}\n{sep * (20 + len(text))}'

def main_menu():
    calculate_budget()
    
    while True:
        print("\n"+tabulate([["1. Tampilkan Transaksi"],[ "2. Tambah Transaksi"],["3. Ubah Transaksi"],["4. Hapus Transaksi"],["5. Anggaran per bulan"],["6. Laporan"],["7. Exit Program"]], headers=["Menu Utama"], tablefmt="rounded_outline"))
        program = input('''
Masukkan angka Menu yang ingin di jalankan: ''')
        print("")
        if(program == '1'): #Menampilkan daftar transaksi
            menu_tampilkan_transaksi()
        elif(program == '2'): #Membuat transaksi baru
            menu_tambah_transaksi()
        elif(program == '3'):
            menu_ubah_transaksi()
        elif(program == '4'):
            menu_hapus_transaksi()    
        elif(program == '5'):
            menu_anggaran()
        elif(program == '6'):
            menu_laporan()
        elif(program == '7'):
            print(text_infromasi(sep='=',text='Terimakasih telah menggunakan aplikasi ini'))
            break
        else:
            invalid_input()
    
def ada_data_transaksi():
    if(len(transactions) > 0):
        return True
    else:
        print(text_infromasi(text='Data Transaksi Tidak Di temukan'))
        return False
    
def menu_tampilkan_transaksi():
    while True:
        print(tabulate([["1. Tampilkan Semua Transaksi"],[ "2. Tampilkan Transaksi Berdasarkan ID"],[ "3. Tampilkan Pemasukan"],[ "4. Tampilkan Pengeluaran"],["5. Urutkan transaksi per kolom"],["6. Filter transaksi per kolom"],["7. Kembali ke menu utama"]], headers=["Menu Tampilkan Transaksi"], tablefmt="rounded_outline"))
        program = input('''
Masukkan angka Menu yang ingin di jalankan: ''')
        if(program != '7'):
            if(ada_data_transaksi() == False):
                continue
        if program == '1':
            tampilkan_table('transaksi', transactions)
        elif program == '2':
            id_transaksi = validasi_integer(input("\nMasukkan Id transaksi yang ingin di tampilkan: ").strip(), "\nMasukkan Id transaksi yang ingin di tampilkan: ")
            data = next(filter(lambda transaction: transaction['id'] == int(id_transaksi), transactions), False)
            if(data == False):
                print(text_infromasi(text='Data Transaksi Tidak Di temukan'))
            else:
                tampilkan_table('transaksi',[data])
        elif program == '3':
            data = list(filter(lambda transaction: transaction['jenis'] == 'Pemasukan', transactions))
            if(len(data) > 0):
                tampilkan_table('transaksi',data)
            else: 
                print(text_infromasi(text='Data Transaksi Tidak Di temukan'))
        elif program == '4':
            data = list(filter(lambda transaction: transaction['jenis'] == 'Pengeluaran', transactions))
            if(len(data) > 0):
                tampilkan_table('transaksi',data)
            else: 
                print(text_infromasi(text='Data Transaksi Tidak Di temukan'))
        elif program == '5':
            urutkan_transaksi()
        elif program == '6':
            filter_transaksi()
        elif program == '7':
            break
        else:
            invalid_input()

def menu_tambah_transaksi():
    while True:
        print(tabulate([["1. Tambah Pemasukan"],[ "2. Tambah Pengeluaran"],["3. Kembali ke menu utama"]], headers=["Menu Tambah Transaksi"], tablefmt="rounded_outline"))
        program_tambah = input('''
Masukkan angka Menu yang ingin di jalankan: ''')
        if(program_tambah == '1'):
            tambah_transaksi('Pemasukan')
        elif(program_tambah == '2'):
            tambah_transaksi('Pengeluaran')
        elif(program_tambah == '3'):
            break
        else:
            invalid_input()

def menu_ubah_transaksi():
    while True:
        print(tabulate([["1. Ubah Transaksi berdasarkan ID"],["2. Kembali ke menu utama"]], headers=["Menu Ubah Transaksi"], tablefmt="rounded_outline"))
        program_ubah = input('''
Masukkan angka Menu yang ingin di jalankan: ''')
        if(program_ubah == '1'):
            ubah_transaksi()
        elif(program_ubah == '2'):
            break
        else:
            invalid_input()

def menu_hapus_transaksi():
    while True:
        print(tabulate([["1. Hapus Transaksi berdasarkan ID"],["2. Hapus Seluruh Transaksi"],["3. Kembali ke menu utama"]], headers=["Menu Hapus Transaksi"], tablefmt="rounded_outline"))
        program_hapus = input('''
Masukkan angka Menu yang ingin di jalankan: ''')
        if(program_hapus == '1'):
            hapus_transaksi()
        elif(program_hapus == '2'):
            if(ada_data_transaksi() == False):
                continue
            hapus_transaksi('semua')
        elif(program_hapus == '3'):
            break
        else:
            invalid_input()
        calculate_budget()

def tambah_transaksi(jenis):
    print("\n--------------------------------------------------------")
    tanggal = validasi_date("Masukkan Tanggal (Format YYYY-mm-dd): \t")
    
    print("--------------------------------------------------------")
    kategori = validasi_input_kosong("Masukan Kategori Transaksi :\t").strip()
    
    kategori_exists = next((anggaran for anggaran in budget if anggaran['kategori'].lower().strip() == kategori.lower().strip()), None)
    if jenis == 'Pengeluaran':        
        if not kategori_exists:
            print("--------------------------------------------------------")
            if konfirmasi_input('Kategori anggaran tidak ditemukan, apakah anda ingin membuat kategori baru? '):
                print(kategori)
                tambah_anggaran(nama=kategori)
            else:
                return
    else:
        if kategori_exists:
            print(text_infromasi(text='Kategori pemasukan, tidak boleh sama dengan kategori anggaran'))
            return
    
    print("--------------------------------------------------------")
    jumlah = validasi_integer(input("Masukkan Jumlah Transaksi :\t"), "Masukkan Jumlah Transaksi :\t")
    if jumlah < 1:
        print("Jumlah transaksi harus lebih dari 0.")
        return    
    
    if jenis == 'Pengeluaran':
        if kategori_exists:
            if (kategori_exists['pengeluaran'] + jumlah) > kategori_exists['anggaran']:
                if not konfirmasi_input(f'Transaksi yang anda masukkan melebihi anggaran (anggaran: {rupiah_format(kategori_exists['anggaran'])}, total jika ditambahkan: {rupiah_format((kategori_exists['pengeluaran'] + jumlah))}), apakah anda yakin ingin membuat transaksi ini? '):
                    return
        calculate_budget()
    
    print("--------------------------------------------------------")
    deskripsi = input("Masukan Deskripsi Transaksi : \t").strip()
    
    new_id = transactions[-1]["id"] + 1 if transactions else 1
    new_transaction = {"id": new_id, "tanggal": tanggal, "kategori": kategori, "jenis": jenis, "jumlah": jumlah, "deskripsi": deskripsi}
    
    if konfirmasi_input('Apakah anda ingin menyimpan transaksi ini?'):
        transactions.append(new_transaction)
        print('\n' + text_infromasi(sep='=', text='Transaksi Baru Berhasil Disimpan'))

def calculate_budget():
    datenow = datetime.datetime.now()
    for kategori in budget:
        kategori['pengeluaran'] = 0
        for transaction in transactions:
            tanggal = transaction['tanggal']
            if tanggal.year == datenow.year and tanggal.month == datenow.month and transaction['jenis'] == 'Pengeluaran' and transaction['kategori'] == kategori['kategori']:
                kategori['pengeluaran'] += transaction['jumlah']

def ubah_transaksi():
    if(len(transactions)) > 0:
        tampilkan_table('transaksi', transactions)
    print("--------------------------------------------------------")

    # Validasi ID transaksi
    id_transaksi = validasi_integer(input("Masukkan ID transaksi yang ingin diubah: \t"), "Masukkan ID transaksi yang ingin diubah: \t")
    
    transaksi = next((transaction for transaction in transactions if transaction["id"] == id_transaksi), None)    
    if not transaksi:
        print(text_infromasi(text=f'Transaksi dengan ID {id_transaksi} tidak ditemukan!'))
        return
    
    tampilkan_table('transaksi', [transaksi])
    
    if not konfirmasi_input('Apakah anda yakin ingin mengubah transaksi ini?'):
        return
    
    # Memilih kolom yang ingin diubah
    column = get_column(list_column_transaction, "Pilih no kolom yang ingin diubah: ")
    if not column or not column['can_change']:
        print(text_infromasi(text='Kolom tidak dapat diubah.'))
        return
    
    # Input untuk nilai baru
    print("--------------------------------------------------------")
    new_value = validasi_input_kosong(f'Masukkan {column["name"].capitalize()} baru:\t')
    
    # Validasi sesuai tipe data
    if column['type'] == 'int':
        new_value = validasi_integer(new_value, f'Masukkan {column["name"].capitalize()} baru:\t')
    elif column['type'] == 'date':
        if not validate_date(new_value):
            invalid_input()
            new_value = validasi_date(f'Masukkan {column["name"].capitalize()} baru:\t')
    
    # Konfirmasi dan simpan perubahan
    if konfirmasi_input('Apakah anda yakin ingin mengubah kolom ini?'):
        transaksi[column['name']] = new_value
        calculate_budget()
        print(text_infromasi(sep='=', text="Transaksi berhasil disimpan"))

def hapus_transaksi(opsi='id'):
    if(len(transactions)) > 0:
        tampilkan_table('transaksi', transactions)
    print("--------------------------------------------------------")
    
    if opsi == 'id':
        
        # Meminta ID transaksi yang ingin dihapus
        id_transaksi = validasi_integer(input("Masukkan ID transaksi yang ingin dihapus: \t"), "Masukkan ID transaksi yang ingin dihapus: \t")
        
        if(ada_data_transaksi() == False):
            return
        
        # Mencari transaksi berdasarkan ID
        transaksi = next((t for t in transactions if t["id"] == id_transaksi), None)
        
        if not transaksi:
            print(text_infromasi(text=f'Transaksi dengan ID {id_transaksi} tidak ditemukan!'))
            return
        
        tampilkan_table('transaksi', [transaksi])
        
        # Konfirmasi dari pengguna sebelum menghapus transaksi
        if konfirmasi_input('Apakah anda yakin ingin menghapus transaksi ini?'):
            transactions.remove(transaksi)  # Menghapus transaksi dari daftar
            print(text_infromasi(sep='=', text="Transaksi berhasil dihapus"))
    
    elif opsi == 'semua':
        # Konfrimasi dari pengguna sebelum menghapus semua transaksi
        if konfirmasi_input('Apakah anda yakin ingin menghapus semua transaksi?'):
            transactions.clear()  # Menghapus semua transaksi
            print(text_infromasi(sep='=', text="Semua transaksi berhasil dihapus"))

def urutkan_transaksi():
    # Meminta kolom yang ingin diurutkan
    kolom = get_column(list_column_transaction, 'Masukkan no kolom yang ingin anda urutkan: ')
    
    if not kolom:
        print(text_infromasi(text='Kolom tidak ditemukan, silahkan masukan ulang'))
        return

    print(f'{'-'*50}')
    # Meminta pilihan ASC atau DESC
    while True:
        urutan = input('Pilih urutan (ASC/DESC): ').strip().lower()
        if urutan in ['asc', 'desc']:
            break
        else:
            print("Input tidak valid. Harap masukkan 'ASC' atau 'DESC'.")
            
    transaksi_urut = bubble_sort(transactions, kolom['name'], reverse=(urutan == 'desc'))
    tampilkan_table('transaksi', transaksi_urut)

def filter_transaksi():
    kolom = get_column(list_column_transaction, 'Masukkan no kolom yang ingin anda filter: ')
    
    # Fungsi untuk menangani input dan validasi range
    def get_range_input(prompt_min, prompt_max):
        min_value = validasi_integer(input(prompt_min), prompt_min)
        max_value = validasi_integer(input(prompt_max), prompt_max)
        return min_value, max_value

    # Fungsi untuk menangani input tanggal dan validasi
    def get_date_input(prompt_start, prompt_end):
        try:
            start_date = datetime.datetime.strptime(input(prompt_start), '%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(input(prompt_end), '%Y-%m-%d').date()
            return start_date, end_date
        except ValueError:
            print("Format tanggal tidak valid!")
            return None, None

    if kolom:
        if kolom['name'] not in ['tanggal', 'jumlah']:  # Filter berdasarkan kolom selain 'tanggal' dan 'jumlah'
            print(f"{'-'*50}")
            value_filter = input('Masukkan nilai yang ingin anda filter: ')
            data_filter = search_transactions(transactions, kolom['name'], search_term=value_filter)
        
        elif kolom['name'] == 'jumlah':  # Filter berdasarkan jumlah
            print(f"{'-'*50}")
            filter_type = input('Pilih filter:\n "exact" untuk nilai eksak\n "range" untuk rentang: ').strip().lower()
            print(filter_type)
            if filter_type == "exact":
                try:
                    amount = float(input('Masukkan jumlah yang ingin difilter: '))
                    data_filter = search_transactions(transactions, kolom['name'], amount=amount, search_type="exact")
                except ValueError:
                    print("Input tidak valid, pastikan anda memasukkan angka.")
                    return
            elif filter_type == "range":
                min_amount, max_amount = get_range_input('Masukkan jumlah minimal: ', 'Masukkan jumlah maksimal: ')
                if min_amount is not None and max_amount is not None:
                    data_filter = search_transactions(transactions, kolom['name'], amount_range=(min_amount, max_amount))
            else:
                print(text_infromasi(text='Pilihan tidak valid!'))
                return
        
        elif kolom['name'] == 'tanggal':  # Filter berdasarkan tanggal
            print(f"{'-'*50}")
            filter_type = input(f'Pilih filter yang anda mau:\n{'-'*28}\n"exact" untuk nilai eksak\n"range" untuk rentang:\n{'-'*28}\nPilh: ').lower()
            
            if filter_type == "exact":
                try:
                    date_input = input('Masukkan tanggal yang ingin difilter (format YYYY-MM-DD): ')
                    filter_date = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
                    data_filter = search_transactions(transactions, kolom['name'], search_date=filter_date, search_date_type="exact")
                except ValueError:
                    print("Format tanggal tidak valid!")
                    return
            elif filter_type == "range":
                start_date, end_date = get_date_input('Masukkan tanggal mulai (format YYYY-MM-DD): ', 'Masukkan tanggal akhir (format YYYY-MM-DD): ')
                if start_date and end_date:
                    data_filter = search_transactions(transactions, kolom['name'], date_range=(start_date, end_date))
            else:
                print(text_infromasi(text='Pilihan tidak valid!'))
                return

        # Menampilkan hasil pencarian
        if 'data_filter' in locals() and data_filter:
            tampilkan_table('transaksi', data_filter)
        else:
            print(text_infromasi(text='Data tidak ditemukan'))

    else:
        print(text_infromasi(text='Kolom tidak ditemukan atau tidak dapat difilter'))

def tampilkan_table(nama_table, data=None, table_header=[],new_line=True):  
    if nama_table == 'anggaran':
        table_header = ["Kategori", "Anggaran", "Pengeluaran", "Sisa Anggaran"]
    elif nama_table == 'transaksi':
        table_header = ["ID", "Tanggal", "Kategori", "Jenis", "Jumlah", "Deskripsi"]
    
    def format_row(item, nama_table):
        row = []
        for key, val in item.items():
            if (key != 'id' and isinstance(val, int)):
                row.append(rupiah_format(val, with_prefix=True))
            else:
                row.append(val)
        if nama_table == 'anggaran':
            sisa = item['anggaran'] - item['pengeluaran']
            row.append(rupiah_format(sisa, with_prefix=True) + (' (Pengeluaran sudah melebihi anggaran!)' if sisa < 0 else ''))
        return row

    rows = []
    if data is None:
        data = budget
    
    if nama_table == 'opsi':
        rows = [[index+1] + [val.capitalize().replace('_', ' ') for key, val in item.items() if key == 'name'] for index, item in enumerate(data)]
    else:
        rows = [format_row(item, nama_table) for item in data]
    
    print(tabulate(rows, headers=table_header, tablefmt='fancy_grid'))
    if nama_table != "opsi" and new_line:
        print("\n\n")

def menu_anggaran():
    while True:
        print("\n"+tabulate([["1. Lihat Anggaran"],[ "2. Buat Anggaran"],["3. Ubah Anggaran"],["4. Hapus Anggaran"],["5. Kembali Ke Menu Utama"]], headers=["Menu Anggaran per bulan"], tablefmt="rounded_outline"))
        program_anggaran = input('''
Masukkan angka Menu yang ingin di jalankan: ''')
        if (program_anggaran == '1'):
            tampilkan_table('anggaran', budget)
        elif(program_anggaran == '2'):
            tambah_anggaran()
        elif(program_anggaran == '3'):
            ubah_anggaran()
        elif(program_anggaran == '4'):
            hapus_anggaran()
        elif(program_anggaran == '5'):
            break
        else:
            invalid_input()
            
def tambah_anggaran(nama=None):
    print("\n--------------------------------------------------------")
    if not nama:
        kategori = input("Masukkan kategori anggaran:\t").strip()
        if any(anggaran['kategori'].lower().replace(" ", "") == kategori.lower().replace(" ", "") for anggaran in budget):
            print(text_infromasi(text='Anggaran sudah ada, silahkan masukkan anggaran baru!'))
            return
    else: kategori = nama
        
    anggaran_baru = validasi_integer(input("Masukkan jumlah anggaran:\t").strip(), "Masukkan jumlah anggaran:\t")
    
    if konfirmasi_input('Apakah anda ingin menyimpan anggaran ini?'):
        budget.append({"kategori": kategori, 'anggaran': anggaran_baru, 'pengeluaran': 0})
        print('\n' + text_infromasi(sep='=', text='Anggaran Baru Berhasil Disimpan'))

def konfirmasi_input(text):
    while True:
        konfirmasi = input(f"{text} (y/n)  ").lower().strip()
        if(konfirmasi == 'y' or konfirmasi == 'yes'):
            return True
        elif(konfirmasi == 'n' or konfirmasi == 'no'):
            return False
        else:
            invalid_input()

def ubah_anggaran():
    tampilkan_table('anggaran', budget)
    print("--------------------------------------------------------")
    kategori = validasi_input_kosong("Masukkan kategori anggaran:\t").strip()
    kategori_exists = next((anggaran for anggaran in budget if anggaran['kategori'].lower().strip() == kategori.lower().strip()), None)
    if not kategori_exists:
        print(text_infromasi(text='Anggaran tidak ditemukan, silahkan masukkan lagi!'))
        return
    tampilkan_table('anggaran',[kategori_exists])
    if(konfirmasi_input('Apakah anda yakin ingin mengubah anggaran ini?')):
        print("--------------------------------------------------------")        
        column = get_column(list_column_anggaran, "Pilih no kolom yang ingin diubah: ")
        if (column != False):
                print("--------------------------------------------------------")
                new_value = validasi_input_kosong(f'Masukkan {column['name']} baru:\t').strip()
                if(column['type'] == 'int'):
                    new_value = validasi_integer(new_value, f'Masukkan {column['name']} baru:\t')
                if(konfirmasi_input('Apakah  anda yakin ingin mengubah kolom ini?')):
                    if(column['name'] == 'kategori'):
                        transaksi_kategori = [t for t in transactions if t['kategori'].lower().replace(" ", "") == kategori.lower().replace(" ", "")]
                        if transaksi_kategori and konfirmasi_input("Apakah anda ingin mengubah semua transaksi yang terkait dengan anggaran ini?"):
                                for transaksi in transaksi_kategori:
                                    transactions[transactions.index(transaksi)]['kategori'] = new_value
                                print('\n'+text_infromasi(sep='=', text='Anggaran dan Transaksi Berhasil Diubah'))
                        else:
                            print('\n'+text_infromasi(sep='=', text='Anggaran Berhasil Diubah'))
                else:
                    kategori_exists[column['name']] = new_value
            
def hapus_anggaran():
    print("\n--------------------------------------------------------")
    kategori = input("Masukkan kategori anggaran:\t")
    kategori_exists = next((anggaran for anggaran in budget if anggaran['kategori'].lower().replace(" ", "") == kategori.lower().replace(" ", "")), None)
    if not kategori_exists:
        print(text_infromasi(text='Anggaran tidak ditemukan, silahkan masukkan lagi!'))
        return
    print("--------------------------------------------------------\n")
    tampilkan_table('anggaran',[kategori_exists])
    
    if not konfirmasi_input("Apakah anda yakin ingin menghapus anggaran ini? (y/n)"):
        return
    
    del budget[budget.index(kategori_exists)]
    transaksi_kategori = [t for t in transactions if t['kategori'].lower().replace(" ", "") == kategori.lower().replace(" ", "")]
    
    if transaksi_kategori:
        if konfirmasi_input("Apakah anda ingin menghapus semua transaksi yang terkait dengan anggaran ini? (y/n)"):
            for transaksi in transaksi_kategori:
                transactions.remove(transaksi)
            print('\n' + text_infromasi(sep='=', text='Anggaran dan Transaksi Berhasil Dihapus'))
        else:
            print('\n' + text_infromasi(sep='=', text='Anggaran Berhasil Dihapus'))
    else:
        print('\n' + text_infromasi(sep='=', text='Anggaran Berhasil Dihapus'))
        
def get_column(list_column, text):
    tampilkan_table('opsi',data=list_column, table_header=["No", "Kolom"])
    while True: 
        input_column = input(text).lower().replace(" ", "")
        if(input_column.isdigit() == True):
            break
        else:
            invalid_input()            
    print('')
    if( int(input_column) <= len(list_column) and int(input_column) >= 1):
        return list_column[int(input_column) - 1]
    else:
        print(text_infromasi(text="Kolom tidak di temukan"))
        return False

def menu_laporan():
    while True:
        print(tabulate([["1. Ringkasan Pemasukan dan Pengeluaran"],[ "2. Laporan Berdasarkan Kategori"],[ "3. Laporan Keuangan Per Tahun"],[ "4. Laporan Keuangan Per Bulan"],["5. Kembali Ke Menu Utama"]], headers=["Menu Laporan"], tablefmt="rounded_outline"))
        program = input('''
Masukkan angka Menu yang ingin di jalankan: ''')
        print("")
        if(program == '1'):
            ringkasan_pemasukan_pengeluaran()
        elif(program == '2'):
            laporan_per_kategori()
        elif(program == '3'):
            laporan_keuangan_per_tahun()
        elif(program == '4'):
            laporan_keunagan_per_bulan()    
        elif(program == '5'):
            break
        else:
            invalid_input()
            
def ringkasan_pemasukan_pengeluaran():
    total_pemasukan = 0
    total_pengeluaran = 0
    for transaction in transactions:
        if transaction["jenis"] == "Pengeluaran":
            total_pengeluaran += transaction["jumlah"]
        elif transaction["jenis"] == "Pemasukan":
            total_pemasukan += transaction["jumlah"]
    saldo_bersih = total_pemasukan - total_pengeluaran
    
    tampilkan_table('laporan',[{'total_pemasukan': total_pemasukan, 'total_pengeluaran': total_pengeluaran, 'saldo_bersih': saldo_bersih}], ['Total Pemasukan', 'Total Pengeluaran', 'Saldo Bersih'])
    
def laporan_per_kategori():
    list_kategori = []
    for transaction in transactions:
        kategori_exists = next((kategori for kategori in list_kategori if kategori["nama"] == transaction['kategori']), None)    
        if not kategori_exists:
            list_kategori.append({'nama': transaction['kategori'], 'jenis': transaction['jenis'], 'jumlah': transaction['jumlah']})
        else:
            kategori_exists['jumlah']+= transaction['jumlah']
    tampilkan_table('laporan', list_kategori, ['Kategori', 'Jenis', 'Jumlah'])

def laporan_keuangan_per_tahun():
    tahun = validasi_integer(input('Masukkan tahun yang ingin anda tampilkan: ').strip(), 'Masukkan tahun yang ingin anda tampilkan: ')
    bulan = [
    {'bulan': 'Januari', 'total_pemasukan': 0, 'total_pengeluaran': 0, 'saldo': 0},
    {'bulan': 'Februari', 'total_pemasukan': 0, 'total_pengeluaran': 0, 'saldo': 0},
    {'bulan': 'Maret', 'total_pemasukan': 0, 'total_pengeluaran': 0, 'saldo': 0},
    {'bulan': 'April', 'total_pemasukan': 0, 'total_pengeluaran': 0, 'saldo': 0},
    {'bulan': 'Mei', 'total_pemasukan': 0, 'total_pengeluaran': 0, 'saldo': 0},
    {'bulan': 'Juni', 'total_pemasukan': 0, 'total_pengeluaran': 0, 'saldo': 0},
    {'bulan': 'Juli', 'total_pemasukan': 0, 'total_pengeluaran': 0, 'saldo': 0},
    {'bulan': 'Agustus', 'total_pemasukan': 0, 'total_pengeluaran': 0, 'saldo': 0},
    {'bulan': 'September', 'total_pemasukan': 0, 'total_pengeluaran': 0, 'saldo': 0},
    {'bulan': 'Oktober', 'total_pemasukan': 0, 'total_pengeluaran': 0, 'saldo': 0},
    {'bulan': 'November', 'total_pemasukan': 0, 'total_pengeluaran': 0, 'saldo': 0},
    {'bulan': 'Desember', 'total_pemasukan': 0, 'total_pengeluaran': 0, 'saldo': 0}
]
    total_pemasukan = 0
    total_pengeluaran = 0
    found = False

    for transaction in transactions:
        tanggal = transaction['tanggal']
        if tanggal.year == tahun:
            found = True
            if transaction['jenis'] == "Pemasukan":
                bulan[tanggal.month - 1]['total_pemasukan'] += transaction['jumlah']
                bulan[tanggal.month - 1]['saldo'] += transaction['jumlah']
                total_pemasukan += transaction['jumlah']
            else: 
                bulan[tanggal.month - 1]['total_pengeluaran'] += transaction['jumlah']
                bulan[tanggal.month - 1]['saldo'] -= transaction['jumlah']
                total_pengeluaran += transaction['jumlah']
    if found == False:
        print(text_infromasi(text='Data Tidak Ditemukan'))
        return
        
    saldo_bersih = total_pemasukan - total_pengeluaran            
    print(text_infromasi('=', f'{' '*14}Laporan Keuangan Tahun {str(tahun)}{' '*14}'))
    tampilkan_table('laporan', bulan, ['Bulan', 'Total Pemasukkan', 'Total Pengeluaran', 'Saldo'], new_line=False)   
    tampilkan_table('laporan',[{'total_pemasukan': total_pemasukan, 'total_pengeluaran': total_pengeluaran, 'saldo_bersih': saldo_bersih}], [f'Total Pemasukan {str(tahun)}', f'Total Pengeluaran {str(tahun)}', f'Saldo Bersih {str(tahun)}'])

def laporan_keunagan_per_bulan():
    datenow = datetime.datetime.now()
    nama_bulan = [
    {"name": "Januari"},
    {"name": "Februari"},
    {"name": "Maret"},
    {"name": "April"},
    {"name": "Mei"},
    {"name": "Juni"},
    {"name": "Juli"},
    {"name": "Agustus"},
    {"name": "September"},
    {"name": "Oktober"},
    {"name": "November"},
    {"name": "Desember"}
]
    bulan = nama_bulan.index(get_column(nama_bulan, 'Pilih no bulan yang anda inginkan: '))
    data_pemasukan = []
    data_pengeluaran = []
    total_pemasukan = 0
    total_pengeluaran = 0
    found = False

    for transaction in transactions:
        tanggal = transaction['tanggal']
        if tanggal.year == datenow.year and tanggal.month == bulan:
            found = True
            if transaction['jenis'] == "Pemasukan":
                kategori_exists = next((kategori for kategori in data_pemasukan if kategori["nama"] == transaction['kategori']), None)    
                if not kategori_exists:
                    data_pemasukan.append({'nama': transaction['kategori'], 'jumlah': transaction['jumlah']})
                else:
                    kategori_exists['jumlah']+= transaction['jumlah']
                total_pemasukan += transaction['jumlah']
            else: 
                kategori_exists = next((kategori for kategori in data_pengeluaran if kategori["nama"] == transaction['kategori']), None)    
                if not kategori_exists:
                    data_pengeluaran.append({'nama': transaction['kategori'], 'jumlah': transaction['jumlah']})
                else:
                    kategori_exists['jumlah']+= transaction['jumlah']
                total_pengeluaran += transaction['jumlah']
                
    if found == False:
        print(text_infromasi(text='Data Tidak Ditemukan'))
        return  
             
    saldo_bersih = total_pemasukan - total_pengeluaran
    index_bulan = bulan -1
    print(text_infromasi(sep='=', text=f'Laporan Keuangan {nama_bulan[index_bulan]['name']} {datenow.year}'))
    print(text_infromasi(sep='=', text=f'Daftar Pemasukan'))
    tampilkan_table('laporan', data_pemasukan, ['Kategori', 'Jumlah'], False)
    print(text_infromasi(sep='=', text=f'Daftar Pengeluaran'))
    tampilkan_table('laporan', data_pengeluaran, ['Kategori', 'Jumlah'], False)
    tampilkan_table('laporan',[{'total_pemasukan': total_pemasukan, 'total_pengeluaran': total_pengeluaran, 'saldo_bersih': saldo_bersih}], [f'Total Pemasukan {nama_bulan[index_bulan]['name']} {str(datenow.year)}', f'Total Pengeluaran {nama_bulan[index_bulan]['name']} {str(datenow.year)}', f'Saldo Bersih {nama_bulan[index_bulan]['name']} {str(datenow.year)}'])

print(text_infromasi(sep='=',text='Selamat Datang Di Aplikasi Manajemen Keuangan Pribadi'))

main_menu()