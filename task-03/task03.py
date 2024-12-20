
import sys
from pathlib import Path
from colorama import init, Fore, Style


init(autoreset=True)

def visualize_directory(path: Path, indent: int = 0):
    try:
        for item in path.iterdir():
            if item.is_dir():
                print("  " * indent + Fore.BLUE + f"[DIR] {item.name}")
                visualize_directory(item, indent + 1)
            else:
                print("  " * indent + Fore.GREEN + f"[FILE] {item.name}")
    except PermissionError:
        print("  " * indent + Fore.RED + f"[ACCESS DENIED] {path}")

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python hw03.py <directory_path>")
        return

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(Fore.RED + f"Error: Path '{dir_path}' does not exist.")
        return
    if not dir_path.is_dir():
        print(Fore.RED + f"Error: Path '{dir_path}' is not a directory.")
        return

    print(Style.BRIGHT + Fore.CYAN + f"Directory structure for '{dir_path}':")
    visualize_directory(dir_path)

if __name__ == "__main__":
    main()