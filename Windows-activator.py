import os
from halo import Halo
spinner = Halo(text='Loading', spinner='dots')

verziok = ["TX9XD-98N7V-6WMQ6-BX7FG-H8Q99", "3KHY7-WNT83-DGQKR-F7HPR-844BM", "7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH", "PVMJN-6DFY6-9CCP6-7BKTT-D3WVR", "W269N-WFGWX-YVC9B-4J6C9-T83GX", "MH37W-N47XK-V7XM9-C7227-GCQG9", "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2", "2WH4N-8QGBV-H22JP-CT43Q-MDWWJ", "NPPR9-FWDCX-D2C8J-H872K-2YT43", "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4"]
print("[0] Windows 10 Home")
print("[1] Windows 10 Home N")
print("[2] Windows 10 Home Single Language")
print("[3] Windows 10 Country Specific")
print("[4] Windows 10 Pro")
print("[5] Wind9ws 10 Pro N")
print("[6] Windows 10 Education")
print("[8] Windows 10 Education N")
print("[9] Windows 10 Enterprise")
print("[10] Windows 10 Enterprise N")
print("Milyen Windows verzió van telepítve?")

try:
    verzio = int(input("Selected number: "))
    print("")
    spinner.start()
    os.system(f"slmgr /ipk {verziok[verzio]}")
    os.system("slmgr /skms kms8.msguides.com")
    os.system("slmgr /ato")
    spinner.stop_and_persist("[Finished]","")
    print("Press enter to exit")
    input()
except: print("Hiba/Error \n Kérlek indítsd újra a programot/Please try again")
