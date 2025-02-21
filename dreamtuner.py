"""
DreamTuner
Tweak Gaming No Root
versi 1.6
"""

import os, time, re

line = "="*36

def banner():
    os.system("clear")
    print(f"╔╦╗┬─┐┌─┐┌─┐┌┬┐  ┌┬┐┬ ┬┌┐┌┌─┐┬─┐\n ║║├┬┘├┤ ├─┤│││───│ │ ││││├┤ ├┬┘\n═╩╝┴└─└─┘┴ ┴┴ ┴   ┴ └─┘┘└┘└─┘┴└─\n{line}\n[!] Pastikan sudah mengikuti tutorial dengan benar.\n{line}")

def menu():
    banner()
    print("[01]. Aktifkan semua tweak (Termasuk force stop & hapus cache - aktifkan 1x saja setiap reboot)")
    print("[02]. Hapus cache & force stop only (Gunakan setiap ingin bermain game)")
    print("[03]. Ubah resolusi & dpi only")
    print("[04]. Reset resolusi & dpi layar ke resolusi & dpi asli")
    print("[05]. Aktifkan tweak hemat baterai (aktifkan kembali tweak no 1 jika ingin main game)")
    print("[00]. Exit")
    print(line)
    pilih = input("[??]. Pilih: ")
    print(line)
    if pilih == "1" or pilih == "01":
        aktifkanTweak()
    elif pilih == "2" or pilih == "02":
        forceStopApp(deb=1)
    elif pilih == "3" or pilih == "03":
        menuResolusi(main=1)
    elif pilih == "4" or pilih == "04":
        resetLayar()
    elif pilih == "5" or pilih == "05":
        modeHematBaterai()
    else:
        print("[**]. Terimakasih, sampai jumpa...")
        exit()

def resetLayar():
    os.system("adb shell wm size reset")
    os.system("adb shell wm density reset")
    print("[✓✓]. Tunggu sebentar...")
    time.sleep(2)

def aktifkanTweak():
    listCommand = [
        "adb shell pm trim-caches 9999G",
        "adb shell setprop debug.egl.hw 1",
        "adb shell setprop debug.sf.hw 1",
        "adb shell setprop debug.composition.type gpu",
        "adb shell setprop debug.overlayui.enable 0",
        "adb shell setprop debug.force-opengl 1",
        "adb shell setprop debug.window.anim.fps 0",
        "adb shell setprop debug.sf.vsync 0",
        "adb shell setprop debug.sf.low_latency 1",
        "adb shell setprop debug.hwui.use_gpu 1",
        "adb shell settings put global window_animation_scale 0",
        "adb shell settings put global transition_animation_scale 0",
        "adb shell settings put global animator_duration_scale 0",
        "adb shell settings put global dev.pm.dyn_samplingrate 1",
        "adb shell settings put global touch.presure.scale 0.001",
        "adb shell settings put global disable_window_blurs 1",
        "adb shell settings put global accessibility_reduce_transparency 1",
        "adb shell settings put global activity_starts_logging_enabled 0",
        "adb shell settings put global automatic_power_save_mode 0",
        "adb shell settings put global adaptive_battery_management_enabled 0",
        "adb shell settings put global net.tcp.buffersize.default 4096,87380,256960,4096,16384,256960",
        "adb shell settings put global net.tcp.buffersize.wifi 4096,87380,256960,4096,16384,256960",
        "adb shell settings put global net.tcp.buffersize.umts 4096,87380,256960,4096,16384,256960",
        "adb shell settings put global net.tcp.buffersize.gprs 4096,87380,256960,4096,16384,256960",
        "adb shell settings put global net.tcp.buffersize.edge 4096,87380,256960,4096,16384,256960",
        "adb shell settings put global net.tcp.buffersize.hspa 6144,87380,524288,6144,16384,262144",
        "adb shell settings put global net.tcp.buffersize.lte 524288,1048576,2097152,524288,1048576,2097152",
        "adb shell settings put global net.tcp.buffersize.hsdpa 6144,87380,1048576,6144,87380,1048576",
        "adb shell settings put global net.tcp.buffersize.evdo_b 6144,87380,1048576,6144,87380,1048576",
        "adb shell settings put global net.rmnet0.dns1 8.8.8.8",
        "adb shell settings put global net.rmnet0.dns2 8.8.4.4",
        "adb shell settings put global net.dns1 8.8.8.8",
        "adb shell settings put global net.dns2 8.8.4.4",
        "adb shell settings put global net.ppp0.dns1 8.8.8.8",
        "adb shell settings put global net.ppp0.dns2 8.8.4.4",
        "adb shell settings put global net.wlan0.dns1 8.8.8.8",
        "adb shell settings put global net.wlan0.dns2 8.8.4.4",
        "adb shell settings put global net.eth0.dns1 8.8.8.8",
        "adb shell settings put global net.eth0.dns2 8.8.4.4",
        "adb shell settings put global net.gprs.dns1 8.8.8.8",
        "adb shell settings put global net.gprs.dns2 8.8.4.4",
        "adb shell settings put system rakuten_denwa 0",
        "adb shell settings put system send_security_reports 0",
        "adb shell settings put system multicore_packet_scheduler 1",
        "adb shell settings put secure send_action_app_error 0",
        "adb shell settings put system performance_mode 1",
        "adb shell cmd power set-fixed-performance-mode-enabled true"
    ]
    getRamInfo = os.popen("adb shell cat /proc/meminfo | grep MemTotal").read().replace("\n", "")
    ramSize = int(re.search("(\d+)", getRamInfo).group(1))
    if ramSize >= 1900000:
        listCommand.append("adb shell settings put global zram_enabled 0")
    for command in listCommand:
        os.system(command)
        print(f"[✓✓]. Mengeksekusi command {command}")
        time.sleep(0.3)
    menuResolusi()

def modeHematBaterai():
    listCommand = [
        "adb shell pm trim-caches 9999G",
        "adb shell setprop debug.egl.hw 1",
        "adb shell setprop debug.sf.hw 1",
        "adb shell setprop debug.composition.type cpu",
        "adb shell setprop debug.overlayui.enable 0",
        "adb shell setprop debug.force-opengl 0",
        "adb shell setprop debug.window.anim.fps 0",
        "adb shell setprop debug.sf.vsync 0",
        "adb shell setprop debug.sf.low_latency 0",
        "adb shell setprop debug.hwui.use_gpu 0",
        "adb shell settings put global window_animation_scale 0",
        "adb shell settings put global transition_animation_scale 0",
        "adb shell settings put global animator_duration_scale 0",
        "adb shell settings put global dev.pm.dyn_samplingrate 1",
        "adb shell settings put global touch.presure.scale 0.001",
        "adb shell settings put global disable_window_blurs 1",
        "adb shell settings put global accessibility_reduce_transparency 1",
        "adb shell settings put global activity_starts_logging_enabled 0",
        "adb shell settings put global zram_enabled 1",
        "adb shell settings put global automatic_power_save_mode 1",
        "adb shell settings put global adaptive_battery_management_enabled 1",
        "adb shell settings put global net.tcp.buffersize.default 2048,65536,131072,2048,8192,131072",
        "adb shell settings put global net.tcp.buffersize.wifi 2048,65536,131072,2048,8192,131072",
        "adb shell settings put global net.tcp.buffersize.umts 2048,65536,131072,2048,8192,131072",
        "adb shell settings put global net.tcp.buffersize.gprs 2048,65536,131072,2048,8192,131072",
        "adb shell settings put global net.tcp.buffersize.edge 2048,65536,131072,2048,8192,131072",
        "adb shell settings put global net.tcp.buffersize.hspa 4096,65536,262144,4096,8192,262144",
        "adb shell settings put global net.tcp.buffersize.lte 262144,524288,1048576,262144,524288,1048576",
        "adb shell settings put global net.tcp.buffersize.hsdpa 4096,65536,1048576,4096,65536,1048576",
        "adb shell settings put global net.tcp.buffersize.evdo_b 4096,65536,1048576,4096,65536,1048576",
        "adb shell settings put global net.rmnet0.dns1 8.8.8.8",
        "adb shell settings put global net.rmnet0.dns2 8.8.4.4",
        "adb shell settings put global net.dns1 8.8.8.8",
        "adb shell settings put global net.dns2 8.8.4.4",
        "adb shell settings put global net.ppp0.dns1 8.8.8.8",
        "adb shell settings put global net.ppp0.dns2 8.8.4.4",
        "adb shell settings put global net.wlan0.dns1 8.8.8.8",
        "adb shell settings put global net.wlan0.dns2 8.8.4.4",
        "adb shell settings put global net.eth0.dns1 8.8.8.8",
        "adb shell settings put global net.eth0.dns2 8.8.4.4",
        "adb shell settings put global net.gprs.dns1 8.8.8.8",
        "adb shell settings put global net.gprs.dns2 8.8.4.4",
        "adb shell settings put system rakuten_denwa 0",
        "adb shell settings put system send_security_reports 0",
        "adb shell settings put system multicore_packet_scheduler 0",
        "adb shell settings put secure send_action_app_error 0",
        "adb shell settings put system performance_mode 0",
        "adb shell cmd power set-fixed-performance-mode-enabled false"
    ]
    for command in listCommand:
        os.system(command)
        print(f"[✓✓]. Mengeksekusi command {command}")
        time.sleep(0.3)

def menuResolusi(main=0):
    print(line)
    print("[**]. 50% adalah setengah dari resolusi & dpi asli")
    print("[**]. 70% adalah 70% dari resolusi & dpi asli")
    print("[**]. 90% adalah 90% dari resolusi & dpi asli")
    print("[**]. Semakin kecil persentasi layar yang digunakan akan semakin cepat performanya")
    print("[**]. Semakin kecil persentasi layar yang digunakan akan semakin kabur layar / grafik di game")
    print("[**]. Pengaturan ini bisa direset pada fitur no 3 di menu utama")
    print(line)
    print("[01]. Turunkan resolusi & dpi layar (50% dari aslinya)")
    print("[02]. Turunkan resolusi & dpi layar (70% dari aslinya)")
    print("[03]. Turunkan resolusi & dpi layar (90% dari aslinya)")
    print("[00]. Skip (resolusi & dpi (tidak diubah/diturunkan)")
    ubahResolusi = input("[??]. Pilih: ")
    if int(ubahResolusi) == 1:
        ubahResolusiDpi(1)
    elif int(ubahResolusi) == 2:
        ubahResolusiDpi(2)
    elif int(ubahResolusi) == 3:
        ubahResolusiDpi(3)
    if not main:
        print(line)
        forceStopApp()

def forceStopApp(deb=0):
    if deb:
        os.system("adb shell pm trim-caches 999G")
        print("[✓✓]. Menghapus cache semua apkikasi")
        time.sleep(0.3)
    listPackage = os.popen("adb shell pm list packages -3").read().split("\n")
    del listPackage[-1]
    for pack in listPackage:
        packageName = pack.replace("package:", "")
        if packageName != "com.termux":
            os.system(f"adb shell am force-stop {packageName}")
            print(f"[✓✓]. Force stop aplikasi {packageName}")
            time.sleep(0.3)
    print(line)
    print("[**]. Tekan enter sekarang")
    print("[**]. Akan otomatis keluar apk termux")
    input("[ ENTER ]")
    os.system("adb shell am force-stop com.termux")

def ubahResolusiDpi(rasio):
    getResolution = os.popen("adb shell wm size").read().split("\n")[0]
    width, height = getResolution.replace("Physical size: ", "").split("x")
    getDpi = os.popen("adb shell wm density").read().split("\n")[0]
    dpi = getDpi.replace("Physical density: ", "")
    if rasio == 1:
        width = int((int(width) / 100) * 50)
        height = int((int(height) / 100) * 50)
        dpi = int((int(dpi) / 100) * 50)
    elif rasio == 2:
        width = int((int(width) / 100) * 70)
        height = int((int(height) / 100) * 70)
        dpi = int((int(dpi) / 100) * 70)
    elif rasio == 3:
        width = int((int(width) / 100) * 90)
        height = int((int(height) / 100) * 90)
        dpi = int((int(dpi) / 100) * 90)
    os.system(f"adb shell wm size {width}x{height}")
    os.system(f"adb shell wm density {dpi}")
    print("[✓✓]. Tunggu sebentar...")
    time.sleep(2)

def adbPermanenNoReboot():
    banner()
    print("[**]. Tunggu sebentar, memulai server...")
    print("[**]. Mengubah koneksi adb shell menjadi permanen sampai perangkat dimulai ulang.")
    print(line)
    os.system("adb tcpip 5555")
    os.system("adb connect localhost")
    os.system("adb kill-server")
    os.system("adb start-server")
    print(line)
    print("[✓✓]. Berhasil, dialihkan dalam 2 detik...")
    time.sleep(2)

def autoUpdate():
    gitPull = os.popen("git pull").read()
    if "Already up to date." not in gitPull:
        if gitPull != "" and "file changed" in gitPull:
            print("[✓✓]. Tweak baru saja diupdate, jalankan ulang untuk menggunakan.")
            exit()
        print(f"[!!]. Update error, script masih bisa digunakan dengan versi saat ini")
        time.sleep(3)
        
if __name__=="__main__":
    autoUpdate()
    adbPermanenNoReboot()
    menu()
