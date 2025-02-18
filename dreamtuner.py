import os, time

line = "="*36

def menu():
    os.system("clear")
    print(f"╔╦╗┬─┐┌─┐┌─┐┌┬┐  ┌┬┐┬ ┬┌┐┌┌─┐┬─┐\n ║║├┬┘├┤ ├─┤│││───│ │ ││││├┤ ├┬┘\n═╩╝┴└─└─┘┴ ┴┴ ┴   ┴ └─┘┘└┘└─┘┴└─\n{line}\n[!] Pastikan sudah mengikuti tutorial dengan benar.\n{line}")
    print("[01]. Aktifkan tweak")
    print("[02]. Reset resolusi & dpi layar")
    print("[00]. Exit")
    print(line)
    pilih = input("[??]. Pilih: ")
    print(line)
    if pilih == "1" or pilih == "01":
        aktifkanTweak()
    elif pilih == "2" or pilih == "02":
        resetLayar()
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
    for command in listCommand:
        os.system(command)
        print(f"[✓✓]. Mengeksekusi command {command}")
        time.sleep(0.3)
    print(line)
    ubahResolusi = input("[??]. Ubah resolusi menjadi 50% (Recomended) [y/t]: ")
    if ubahResolusi.lower() == "y":
        ubahResolusiDpi()
    print(line)
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

def ubahResolusiDpi():
    getResolution = os.popen("adb shell wm size").read().split("\n")[0]
    width, height = getResolution.replace("Physical size: ", "").split("x")
    getDpi = os.popen("adb shell wm density").read().split("\n")[0]
    dpi = getDpi.replace("Physical density: ", "")
    width, height, dpi = int(width) // 2, int(height) // 2, int(dpi) // 2
    os.system(f"adb shell wm size {width}x{height}")
    os.system(f"adb shell wm density {dpi}")
    print("[✓✓]. Tunggu sebentar...")
    time.sleep(2)

if __name__=="__main__":
    menu()
