import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    nik_pelapor = input("Masukan NIK:")
    nama_pelapor = input("Nama:")
    nama_covid = input("Nama Pasien:")
    alamat_covid = input("Alamat Pasien:")
    gejala = input("Gejala:")
    print("Mengirim Laporan ke Server: %s" % str(proxy.is_even(
        nik_pelapor, nama_pelapor, nama_covid, alamat_covid, gejala)))
