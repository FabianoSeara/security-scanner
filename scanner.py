import os
import re


def scan_file(filename):
    pattern = r"(password|token|key|secret|adm)\s*=\s*[\"'].*[\"']"

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                if re.search(pattern, line.lower()):
                    print(f"[ALERT] Suspicious line: {line.strip()}")
    except FileNotFoundError:
        print(f"file not found: {filename}")


def scan_folder(folder_path):
    for current_folder, subfolders, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".py"):
                full_path = os.path.join(current_folder, file_name)
                scan_file(full_path)
