#! / usr / bin / python
# - * - pengkodean: utf-8 - * -
impor sys
permintaan impor
import json
waktu impor
import urllib.request, urllib.parse, urllib.error
impor os

warna kelas:
   UNGU = '\ 033 [95m'
   CYAN = '\ 033 [96m'
   DARKCYAN = '\ 033 [36m'
   BIRU = '\ 033 [94m'
   HIJAU = '\ 033 [92m'
   KUNING = '\ 033 [93m'
   MERAH = '\ 033 [91m'
   BOLD = '\ 033 [1m'
   UNDERLINE = '\ 033 [4m'
   AKHIR = '\ 033 [0m'
   KEPALA = '\ 033 [95m'
   OKBLUE = '\ 033 [94 jt'
   OKGREEN = '\ 033 [92 jt'
   PERINGATAN = '\ 033 [93m'
   GAGAL = '\ 033 [91m'

konfigurasi kelas:
	key = "4a1ede76e87d9e64682b284e8620ad68" #buka https://numverify.com/

def spanduk ():
	os.system ('clear')
	cetak (color.YELLOW + "" "
 _     ______  __
| |   / ___\ \/ /
| |  | |    \  / 
| |__| |___ /  \ 
|_____\____/_/\_\

	"" "+ warna.END)

def main ():
	spanduk()
	jika len (sys.argv) == 2:
		angka = sys.argv [1]
		api = "http://apilayer.net/api/validate?access_key=" + config.key + "& number =" + number + "& country_code = & format = 1"
		output = requests.get (api)
		konten = output.text
		obj = json.loads (konten)
		country_code = obj ['country_code']
		country_name = obj ['country_name']
		location = obj ['location']
		carrier = obj ['carrier']
		line_type = obj ['line_type']

		cetak (color.YELLOW + "omr >>" + color.END + "Pengumpulan informasi nomor telepon")
		mencetak("--------------------------------------")
		waktu tidur (0,2)

		jika country_code == "":
			print ("- Mendapatkan Negara [" + color.RED + "FAILED" + color.END + "]")
		lain:
			print ("- Mendapatkan Negara [" + color.GREEN + "OK" + color.END + "]")

		waktu tidur (0,2)
		jika nama_negara == "":
			print ("- Mendapatkan Nama Negara [" + color.RED + "FAILED" + color.END + "]")
		lain:
			print ("- Mendapatkan Nama Negara [" + color.GREEN + "OK" + color.END + "]")

		waktu tidur (0,2)
		jika lokasi == "":
			print ("- Mendapatkan Lokasi [" + color.RED + "FAILED" + color.END + "]")
		lain:
			print ("- Mendapatkan Lokasi [" + color.GREEN + "OK" + color.END + "]")

		waktu tidur (0,2)
		jika operator == "":
			print ("- Mendapatkan Operator [" + color.RED + "FAILED" + color.END + "]")
		lain:
			print ("- Mendapatkan Operator [" + color.GREEN + "OK" + color.END + "]")

		waktu tidur (0,2)
		jika line_type == Tidak ada:
			print ("- Mendapatkan Perangkat [" + color.RED + "FAILED" + color.END + "]")
		lain:
			print ("- Mendapatkan Perangkat [" + color.GREEN + "OK" + color.END + "]")

		mencetak("")
		cetak (color.YELLOW + "omr >>" + color.END + "Information Output")
		mencetak("--------------------------------------")
		print ("- Nomor telepon:" + str (nomor))
		print ("- Country:" + str (country_code))
		print ("- Nama Negara:" + str (nama_negara))
		print ("- Lokasi:" + str (lokasi))
		print ("- Operator:" + str (operator))
		print ("- Perangkat:" + str (line_type))
	lain:
		print ("[?] Penggunaan:")
		cetak ("./%s <phone-number>"% (sys.argv [0]))

utama()
