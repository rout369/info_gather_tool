import os
import platform
import psutil
import hashlib
import json
import csv
import re
from win32evtlog import OpenEventLog, ReadEventLog, EVENTLOG_FORWARDS_READ, EVENTLOG_SEQUENTIAL_READ
import time
import sys
import random
import subprocess
import ctypes
import itertools
import threading
from datetime import datetime, timedelta
from colorama import Fore, Style, init
import colorama


# Initialize colorama
colorama.init(autoreset=True)

# Define colors
RED = Fore.RED  # Red color (malicious theme)
GREEN = Fore.GREEN  # Green color (malware effect)
RESET = Style.RESET_ALL  # Reset color

# Banner
def print_banner():
    banner = f"""
    {RED}
  ▄▀  ▄███▄      ▄      ▄▄▄▄▄   ▄█    ▄▄▄▄▄   ██     ▄   ██▄   ▄█    ▄▄▄▄▀ 
▄▀    █▀   ▀      █    █     ▀▄ ██   █     ▀▄ █ █     █  █  █  ██ ▀▀▀ █    
█ ▀▄  ██▄▄    ██   █ ▄  ▀▀▀▀▄   ██ ▄  ▀▀▀▀▄   █▄▄█ █   █ █   █ ██     █    
█   █ █▄   ▄▀ █ █  █  ▀▄▄▄▄▀    ▐█  ▀▄▄▄▄▀    █  █ █   █ █  █  ▐█    █     
 ███  ▀███▀   █  █ █             ▐               █ █▄ ▄█ ███▀   ▐   ▀      
              █   ██                            █   ▀▀▀                    
                                               ▀                           
              
Author: Biswajit (bloodHowl)
Version: 1.0
Date_of_build: 2 January 2025
                                           ____ ____ __ _ ____ _ ____ ____ _  _ ___  _ ___
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> |__, |=== | \\| ==== | ==== |--| |__| |__> |  |  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    {RESET}
    """
    print(banner)
    time.sleep(2)  # Delay for a dramatic effect

def print_banner2():
    banner = f"""
    {RED}
                                           ____ ____ __ _ ____ _ ____ ____ _  _ ___  _ ___
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> |__, |=== | \\| ==== | ==== |--| |__| |__> |  |  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    {RESET}
    """
    print(banner)
    time.sleep(2)  # Delay for a dramatic effect

# Loading Bar Animation
def loading_bar():
    symbols = "|/-\\"
    for _ in range(5):
        for symbol in symbols:
            sys.stdout.write(f"\r{GREEN}[Installing... {symbol}]{RESET}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write(f"\r{GREEN}[Installation Complete!]{RESET}\n")
    time.sleep(1)

# Run functions



def is_admin():
    """Check if script is running with administrator privileges"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def elevate_to_admin():
    """Restart the script with admin privileges if not already running as admin."""
    print_banner2()
    if not is_admin():
        print(f"\n{Fore.YELLOW}[!] This tool requires administrator privileges.{Style.RESET_ALL}")
        choice = input(f"{Fore.RED}[?] Do you want to restart as admin? (y/n): {Style.RESET_ALL}").strip().lower()

        if choice == "y":
            print(f"\n{Fore.CYAN}[*] Restarting with administrator privileges...{Style.RESET_ALL}")
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            sys.exit()
        else:
            print(f"\n{Fore.RED}[✘] Sorry, this tool requires administrator privileges to run. Exiting...{Style.RESET_ALL}")
            sys.exit(1)

def dynamic_text():
    phrases = [
        "System Analysis... Please Wait...",
        "Accessing Core Data... Be Ready...",
        "Searching for Vulnerabilities...",
        "System Compromised: Proceeding with Data Harvest...",
        "Security Flaw Detected: Exploiting...",
        "Deploying Data Extraction... Please Do Not Disconnect!"
    ]
    
    for _ in range(5):
        time.sleep(random.uniform(1, 2))
        sys.stdout.write(f"\r\x1b[35m{random.choice(phrases)}\x1b[0m")
        sys.stdout.flush()

def gather_background_processes():
    """Gathers background processes running on the system."""
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        # Consider only processes that are not related to current user session
        try:
            if proc.info['username'] != psutil.users()[0].name:  # Exclude the current user's processes
                processes.append(f"PID: {proc.info['pid']} Name: {proc.info['name']}")
        except psutil.NoSuchProcess:
            continue  # Skip processes that no longer exist

    # Limit to the first 10 background processes for better output
    return processes[:10]


def scrolling_output():
    """Simulates scrolling terminal output showing only background processes."""
    background_processes = gather_background_processes()

    # List of color codes for red and blue only
    colors = [
        "\x1b[31m",  # Red
        "\x1b[96m",  # Blue
    ]
    
    for _ in range(50):  # Adjust the number of scrolling lines
        if background_processes:  # Print background process data
            color = random.choice(colors)  # Choose a random color (red or blue)
            line = f"{color}{random.choice(background_processes)}\x1b[0m"
        else:
            line = "\x1b[31m[Error] No Background Processes Found\x1b[0m"
        
        print(line)
        time.sleep(0.05)  # Adjust scrolling speed

def back_processs():
    """Simulates the main process with background processes."""
    print("\n\x1b[34mStarting background process monitoring...\x1b[0m")
    time.sleep(1)
    scrolling_output()
    print("\n\x1b[32mBackground process monitoring completed.\x1b[0m")

def simulated_process():
    dynamic_text()

    print("\n\x1b[34mStarting forensic data collection...\x1b[0m")
    time.sleep(1)
    print("System information saved to system_info.json")
    time.sleep(1)
    print("File metadata saved to file_metadata.csv")
    time.sleep(1)
    print("Forensic report saved to forensic_report.txt")
    time.sleep(1)
    print("\n\x1b[32mData collection and report generation completed.\x1b[0m")


# Module 1: Collect System Information
def collect_system_info():
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "OS Build": platform.release(),
        "Architecture": platform.architecture()[0],
        "Processor": platform.processor(),
        "RAM (GB)": round(psutil.virtual_memory().total / (1024**3), 2),
        "Disk Usage (GB)": {
            part.mountpoint: round(psutil.disk_usage(part.mountpoint).total / (1024**3), 2)
            for part in psutil.disk_partitions()
        },
        "IP Address": psutil.net_if_addrs()
    }
    with open("system_info.json", "w") as f:
        json.dump(system_info, f, indent=4)
    return system_info

def list_drives():
    """List available drives on the system using psutil."""
    drives = []
    partitions = psutil.disk_partitions()
    for partition in partitions:
        drive = partition.device.split(' ')[0]
        if drive not in drives:  # Avoid duplicates
            drives.append(drive)
    return drives

# Choose drive function
def choose_drive():
    """Prompt the user to choose a drive."""
    drives = list_drives()
    if not drives:
        print("No drives found.")
        return None
    
    print("\nAvailable drives:")
    for idx, drive in enumerate(drives, start=1):
        print(f"{idx}. {drive}")
    
    while True:
        try:
            choice = int(input("\nEnter the number of the drive you want to choose: "))
            if 1 <= choice <= len(drives):
                selected_drive = drives[choice - 1]
                print(f"Selected drive: {selected_drive}")
                return selected_drive
            else:
                print("Invalid choice. Please choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def list_directories(path, max_depth=2):
    """List directories up to a maximum depth."""
    directories = []
    for root, dirs, files in os.walk(path):
        depth = root[len(path):].count(os.sep)
        if depth < max_depth:  # Limit depth
            for d in dirs:
                directories.append(os.path.join(root, d))
    return directories

def navigate_directories(path, max_depth=2, batch_size=300):
    """Recursively navigate through directories and allow the user to select one, with scrolling effect."""
    all_directories = list_directories(path, max_depth)
    total_dirs = len(all_directories)
    start_idx = 0
    global_counter = 1  # Start numbering from 1

    while start_idx < total_dirs:
        # Get a batch of directories
        batch = all_directories[start_idx:start_idx + batch_size]

        # Print each directory with a delay and cyan color, continuing the numbering
        for directory in batch:
            # Print the index and directory in cyan
            print(f"\x1b[36m{global_counter}. {directory}\x1b[0m")
            global_counter += 1  # Increment global counter
            time.sleep(0.03)  # Delay between directories to simulate scrolling

        # Ask the user if they want to see more directories
        user_choice = input("\nDo you want to see more directories? (y/n): ").strip().lower()
        if user_choice != 'y':
            break

        start_idx += batch_size  # Move to the next batch

    # After showing directories, ask the user for the directory they want information from
    choice = input("\nEnter the number of the directory you want to gather info from: ").strip()
    try:
        chosen_directory = all_directories[int(choice) - 1]  # Convert to 0-based index
        print(f"Gathering information from: {chosen_directory}")
    except (ValueError, IndexError):
        print("Invalid choice. Exiting.")
        return None

    return chosen_directory

# Collect file metadata
def collect_file_metadata(directory, output_file="file_metadata.csv", file_extension_filter=None, size_filter=None, max_depth=2):
    """Collect metadata from files in the selected directory."""
    file_metadata_list = []
    with open(output_file, "w", newline="") as csvfile:
        fieldnames = ["File Path", "File Size", "Creation Time", "Modification Time", "Access Time", "MD5 Hash", "SHA256 Hash"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for root, dirs, files in os.walk(directory):
            depth = root[len(directory):].count(os.sep)
            if depth >= max_depth:
                continue

            for file in files:
                file_path = os.path.join(root, file)
                
                if file_extension_filter and not file.lower().endswith(file_extension_filter):
                    continue
                
                if size_filter and os.stat(file_path).st_size < size_filter:
                    continue

                try:
                    stats = os.stat(file_path)
                    file_metadata = {
                        "File Path": file_path,
                        "File Size": stats.st_size,
                        "Creation Time": stats.st_ctime,
                        "Modification Time": stats.st_mtime,
                        "Access Time": stats.st_atime,
                        "MD5 Hash": calculate_hash(file_path, "md5"),
                        "SHA256 Hash": calculate_hash(file_path, "sha256")
                    }
                    writer.writerow(file_metadata)
                    file_metadata_list.append(file_metadata)
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    return file_metadata_list

# Helper function to calculate hashes
def calculate_hash(file_path, hash_type="md5"):
    try:
        hash_func = hashlib.md5() if hash_type == "md5" else hashlib.sha256()
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except Exception as e:
        return f"Error: {e}"
def collect_event_logs(log_name="System"):
    event_logs = []
    try:
        log_handle = OpenEventLog(None, log_name)
        events = ReadEventLog(log_handle, EVENTLOG_FORWARDS_READ | EVENTLOG_SEQUENTIAL_READ, 0)
        
        for event in events:
            event_details = {
                "Event ID": event.EventID,
                "Time Generated": event.TimeGenerated.Format(),
                "Event Category": event.EventCategory,
                "Source Name": event.SourceName,
                "Message": event.StringInserts if hasattr(event, 'StringInserts') else 'No message'
            }
            event_logs.append(event_details)
    except Exception as e:
        print(f"Error reading event logs: {e}")
    return event_logs

# Module 6: Disk and Memory Analysis (Optional)
def collect_disk_and_memory_info():
    disk_info = {
        "Disk Usage (GB)": {
            part.mountpoint: round(psutil.disk_usage(part.mountpoint).total / (1024**3), 2)
            for part in psutil.disk_partitions()
        },
        "RAM Snapshot": {
            "Total RAM (GB)": round(psutil.virtual_memory().total / (1024**3), 2),
            "Used RAM (GB)": round(psutil.virtual_memory().used / (1024**3), 2),
            "Free RAM (GB)": round(psutil.virtual_memory().available / (1024**3), 2),
            "Process Memory Usage": [
                {"PID": proc.info["pid"], "Name": proc.info["name"], "Memory (GB)": round(proc.info["memory_info"].rss / (1024**3), 2)}
                for proc in psutil.process_iter(['pid', 'name', 'memory_info'])
            ]
        }
    }
    return disk_info

# Module 7: Threat Indicators
def collect_threat_indicators():
    # Example suspicious file paths and patterns (e.g., files that are often used by malware or have unusual names)
    suspicious_files = [
        "C:\\Windows\\System32\\malicious.exe",
        "C:\\Users\\Public\\Documents\\unusual_file.exe",
        "C:\\Windows\\Temp\\temp_malware.dll"
    ]

    # Check if suspicious file paths exist on the system
    existing_suspicious_files = [file for file in suspicious_files if os.path.exists(file)]

    # Check for processes with suspicious patterns in their names (e.g., "malware", "crypto", etc.)
    suspicious_processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        if re.search(r"malware|crypto|suspicious", proc.info["name"].lower()):
            suspicious_processes.append({
                "PID": proc.info["pid"],
                "Name": proc.info["name"]
            })

    return {
        "Suspicious File Paths": existing_suspicious_files,
        "Suspicious Processes": suspicious_processes
    }

# Helper function to save the gathered data to a .txt file
def save_to_txt(system_info, file_metadata_list, event_logs, disk_info, threat_indicators, output_file="forensic_report.txt"):
    with open(output_file, "w") as f:
        f.write("Forensic Report\n")
        f.write("=" * 80 + "\n\n")

        # System Information
        f.write("System Information\n")
        f.write("-" * 80 + "\n")
        for key, value in system_info.items():
            if key == "IP Address":
                f.write(f"{key}:\n")
                for interface, addresses in value.items():
                    f.write(f"  {interface}:\n")
                    for address in addresses:
                        if address.family == 2:  # IPv4
                            f.write(f"    IPv4: {address.address}\n")
                        elif address.family == 23:  # IPv6
                            f.write(f"    IPv6: {address.address}\n")
                        else:  # Link layer address (MAC address)
                            f.write(f"    MAC: {address.address}\n")
            else:
                f.write(f"{key}: {value}\n")
        f.write("\n")

        # File Metadata
        f.write("File Metadata\n")
        f.write("-" * 80 + "\n")
        for file_metadata in file_metadata_list:
            for key, value in file_metadata.items():
                f.write(f"{key}: {value}\n")
            f.write("\n")
        
        # Event Logs
        f.write("Event Logs\n")
        f.write("-" * 80 + "\n")
        for event in event_logs:
            event_details = f"Event ID: {event['Event ID']} | Time: {event['Time Generated']} | Category: {event['Event Category']} | Source: {event['Source Name']} | Message: {event['Message']}\n"
            f.write(event_details)

        # Disk and Memory Info
        f.write("\nDisk and Memory Analysis\n")
        f.write("-" * 80 + "\n")
        for key, value in disk_info["Disk Usage (GB)"].items():
            f.write(f"{key}: {value} GB\n")
        f.write("\nRAM Snapshot:\n")
        for mem_info in disk_info["RAM Snapshot"]["Process Memory Usage"]:
            f.write(f"  PID: {mem_info['PID']} | Name: {mem_info['Name']} | Memory: {mem_info['Memory (GB)']} GB\n")

        # Threat Indicators
        f.write("\nThreat Indicators\n")
        f.write("-" * 80 + "\n")
        f.write("Suspicious File Paths:\n")
        for suspicious_file in threat_indicators["Suspicious File Paths"]:
            f.write(f"  {suspicious_file}\n")

        f.write("\nSuspicious Processes:\n")
        for process in threat_indicators["Suspicious Processes"]:
            f.write(f"  PID: {process['PID']} | Name: {process['Name']}\n")

        f.write("=" * 80 + "\n")

# - ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def loading_animation(message, stop_event):
    spinner = itertools.cycle(["|", "/", "-", "\\"])
    while not stop_event.is_set():
        sys.stdout.write(f"\r{Fore.CYAN}{message} {next(spinner)}{Style.RESET_ALL}")  
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * (len(message) + 2) + "\r")  # Clear loading text

def find_recent_files(directory, hours=24, suspicious_ext=None):
    """Find recently modified or created files"""
    print(f"{Fore.CYAN}[*] Checking for recent files...{Style.RESET_ALL}")
    
    recent_files = []
    time_threshold = datetime.now() - timedelta(hours=hours)
    
    stop_event = threading.Event()
    loader_thread = threading.Thread(target=loading_animation, args=("[*] Scanning files...", stop_event))
    loader_thread.start()

    try:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                    created_time = datetime.fromtimestamp(os.path.getctime(file_path))

                    if modified_time > time_threshold or created_time > time_threshold:
                        if suspicious_ext and not file.lower().endswith(tuple(suspicious_ext)):
                            continue  

                        print(f"\n{Fore.GREEN}[+] Found recent file: {file_path}{Style.RESET_ALL}")  
                        recent_files.append({
                            "File": file_path,
                            "Created": created_time.strftime("%Y-%m-%d %H:%M:%S"),
                            "Modified": modified_time.strftime("%Y-%m-%d %H:%M:%S")
                        })
                except PermissionError:
                    print(f"\n{Fore.YELLOW}[!] Skipping (Permission Denied): {file_path} -> [⚠️ Manual Check Required]{Style.RESET_ALL}")
                except FileNotFoundError:
                    print(f"\n{Fore.RED}[!] Skipping (File Not Found): {file_path}{Style.RESET_ALL}")
                except OSError:
                    print(f"\n{Fore.YELLOW}[!] Skipping (System Restricted): {file_path} -> [⚠️ Manual Check Recommended]{Style.RESET_ALL}")
    finally:
        stop_event.set()
        loader_thread.join()  

    return recent_files

def get_recent_logins():
    """Fetch last 5 login events from Windows Event Log (Requires Admin Privileges)"""
    print(f"{Fore.CYAN}[*] Checking for recent logins...{Style.RESET_ALL}")  
    
    stop_event = threading.Event()
    loader_thread = threading.Thread(target=loading_animation, args=("[*] Fetching login events...", stop_event))
    loader_thread.start()

    try:
        output = subprocess.check_output("wevtutil qe Security /c:10 /rd:true /f:text", shell=True, encoding="utf-8")
        logins = re.findall(r"Account Name:\s+(.+)", output)
        return logins[-5:]  
    except subprocess.CalledProcessError as e:
        print(f"\n{Fore.RED}[!] Error fetching logins: {e}{Style.RESET_ALL}")
        return []
    finally:
        stop_event.set()
        loader_thread.join()

# 🔹 Ensure script runs with admin privileges before fetching logins
def main2():
    """Main function to control script flow"""
    elevate_to_admin()

    # Run file scan
    suspicious_ext = [".exe", ".bat", ".ps1", ".dll"]
    recent_files = find_recent_files("C:\\", hours=24, suspicious_ext=suspicious_ext)

    if recent_files:
        print(f"\n{Fore.GREEN}[+] Suspicious Recent Files Found:{Style.RESET_ALL}")
        for file in recent_files:
            print(f"  - {Fore.GREEN}{file['File']} (Modified: {file['Modified']}){Style.RESET_ALL}")
    else:
        print(f"\n{Fore.RED}[-] No suspicious recent files found.{Style.RESET_ALL}")

    # Run login check
    recent_logins = get_recent_logins()
    print(f"\n{Fore.GREEN}[+] Recent Logins Detected:{Style.RESET_ALL}")
    print("\n".join(recent_logins))

    print(f"\n{Fore.CYAN}[*] Script execution completed!{Style.RESET_ALL}")

    # 🔹 Keep window open
    input(f"\n{Fore.CYAN}[Press Enter to exit...]{Style.RESET_ALL}")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    elevate_to_admin()
    print_banner()  # Show the banner
    loading_bar()
    back_processs() 

    # Choose the drive
    selected_drive = choose_drive()
    if not selected_drive:
        return
    
    # Start navigating the selected drive's directories
    selected_directory = navigate_directories(selected_drive)

    # Collect file metadata from the selected directory
    file_extension_filter = input("Enter file extension to filter (e.g., .txt, .exe) or leave empty for no filter: ").strip()
    size_filter = input("Enter minimum file size in bytes (leave empty for no filter): ").strip()
    if size_filter:
        size_filter = int(size_filter)
    else:
        size_filter = None

    file_metadata_list = collect_file_metadata(
        selected_directory,
        file_extension_filter=file_extension_filter,
        size_filter=size_filter,
        max_depth=2  # Set the depth to limit the number of subdirectories
    )

    system_info = collect_system_info()
    # Save data to a .txt file
    event_logs = collect_event_logs()
    disk_info = collect_disk_and_memory_info()
    threat_indicators = collect_threat_indicators()
    save_to_txt(system_info, file_metadata_list, event_logs, disk_info, threat_indicators)

    simulated_process()



if __name__ == "__main__":
    main()
    main2()
