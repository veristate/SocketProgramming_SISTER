from xmlrpc.server import SimpleXMLRPCServer
from tinydb import TinyDB, Query
from datetime import datetime, timedelta
import numpy as np

db = TinyDB('db.json')
Nik = Query()
now = datetime.now() + timedelta(minutes=20)
current_time = now.strftime("%H:%M:%S")
petugas = np.random.randint(2, 4)


def is_even(nik_pelapor, nama_pelapor, nama_covid, alamat_covid, gejala):
    result = db.search(Nik.nik == nik_pelapor)
    x = "Laporan atas nama {} dengan NIK {}, untuk pasien dengan nama {} di {} dengan gejala {} diterima, {} petugas diperkirakan tiba pukul {}"
    y = x.format(nama_pelapor, nik_pelapor, nama_covid,
                 alamat_covid, gejala, petugas, current_time)
    if not result:
        return "Laporan ditolak"
    else:
        return y


server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(is_even, "is_even")
server.serve_forever()
