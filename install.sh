#!/bin/bash

# Warna ANSI
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
MAGENTA="\033[35m"
CYAN="\033[36m"
RESET="\033[0m"

# Menampilkan teks berwarna

echo -e "${CYAN}Install.....${RESET}"
pip install requests
pip install rich

echo -e "${RED}End."

echo - e "${RED}Install......"
pkg install figlet

clear

# Menampilkan teks dengan kombinasi warna
echo -e "${RED}$(figlet DARK FORGE)${RESET}"

# Fungsi untuk animasi mengetik
function typing_animation() {
    local text="$1"  # Teks yang akan diketik
    local delay=0.1  # Waktu jeda antar karakter

    for (( i=0; i<${#text}; i++ )); do
        echo -n "${text:$i:1}"
        sleep $delay
    done
    echo ""  # Baris baru setelah selesai
}

# Teks animasi mengetik
typing_animation "Memulai Tools Darkforge..."
typing_animation "Harap tunggu sebentar..."

# Jalankan skrip Python setelah animasi selesai
python3 darkforge.py
