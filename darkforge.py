import os
import subprocess
import webbrowser
from rich.console import Console
from rich.text import Text

# Inisialisasi rich console
console = Console()

# Fungsi untuk menampilkan logo gradient
def display_logo():
    logo_text = os.popen("figlet -f slant 'DarkForge'").read()
    gradient_text = Text()
    
    # Warna gradient
    colors = ["#FF0000", "#FF4500", "#FFD700", "#ADFF2F", "#00FF00", "#00CED1", "#1E90FF", "#8A2BE2"]
    for i, line in enumerate(logo_text.splitlines(), start=1):
        color = colors[i % len(colors)]
        gradient_text.append(line + "\n", style=f"bold {color}")
    
    console.print(gradient_text)

# Fungsi untuk menampilkan garis keren
def display_cracker_lines():
    lines = [
        "-" * 60,
        "[*] Made By Farel Dev",
        "[*] Initializing darkforge Environment...",
        "-" * 60,
    ]
    for line in lines:
        console.print(line, style="bold cyan")

# Fungsi untuk menampilkan menu
def show_menu():
    os.system("clear")
    display_logo()
    print("""
    ===========================================
                DARKFORGE TOOLS MENU
    ===========================================
    1. Open Google Maps Tracker
    2. Report Wa Account
    2. Exit Menu
    ===========================================
    """)
    choice = input("Select an option: ")
    if choice == "1":
        tracker()
    elif choice == "2":
        print("Exiting menu...")
    else:
        print("Invalid choice!")
        show_menu()

# Fungsi untuk membuka Google Maps
def tracker():
    print("\nLaunching Google Maps Tracker...")
    webbrowser.open("https://www.google.com/maps")
    print("Google Maps opened in your browser.\n")

# Fungsi utama
def main():
    os.system("clear")
    display_logo()
    display_cracker_lines()
    console.print("[green bold]Welcome to Darkforge Terminal![/]", justify="center")
        continue

    while True:
        try:
            # Custom prompt
            command = input("darkforge $ ").strip()
            
            if command == ".menu":
                show_menu()
            elif command:
                # Execute normal terminal commands
                subprocess.run(command, shell=True)
        except KeyboardInterrupt:
            print("\nExiting Darkforge Terminal. Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__": 
    main()
