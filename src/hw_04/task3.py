import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)


def list_directory_contents(target_path: Path, indent: str = "") -> None:
    if not target_path.exists() or not target_path.is_dir():
        print(f"{Fore.RED}Error: Path does not exist or is not a directory.")
        return

    try:
        items = sorted(target_path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    except PermissionError:
        print(f"{indent}{Fore.RED} Permission denied")
        return

    for i, item in enumerate(items):
        is_last = (i == len(items) - 1)
        char = "┗ " if is_last else "┣ "

        if item.is_dir():
            print(f"{indent}{char}{Fore.BLUE}{Style.BRIGHT}📂 {item.name}/")
            new_indent = indent + ("  " if is_last else "┃ ")
            list_directory_contents(item, new_indent)
        else:
            print(f"{indent}{char}{Fore.GREEN}📜 {item.name}")


def main() -> None:
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW} Missing required argument <directory_path>")
        return

    path = Path(sys.argv[1])
    print(f"{Fore.CYAN}{Style.BRIGHT} Directory structure: {path.absolute()}\n")
    list_directory_contents(path)


if __name__ == "__main__":
    main()