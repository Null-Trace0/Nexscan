import subprocess
import os

def run_scan(target):

    os.makedirs("scans", exist_ok=True)

    command = [

        "nmap",
        "-sV",
        "-oX",
        "scans/scan.xml",
        target
    ]
    subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        timeout=90
    )
