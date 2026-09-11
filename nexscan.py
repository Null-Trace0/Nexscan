from banner import show_banner
from scanner import run_scan
from parser import parse_scan
from risk import cal_risk
from risk import get_risk_level
from recommendations import get_recommendations
from report import generate_html
from vuln import analyze_vulnerabilities
import datetime

filename = datetime.datetime.now().strftime("%Y_%m_%D_%H_%M_%S")

from rich.table import Table
from rich.console import Console

import time

show_banner()
def main():


    target = input("Enter Target: ")
    print(" ")

    print("\n <+> Initializing NexScan...\n")
    time.sleep(1)
    print("\n <+> NexScan Intialized, Scanning Target...\n")

    start = time.time()

    run_scan(target)

    data = parse_scan("scans/scan.xml")

    findings = analyze_vulnerabilities(
        data["ports"]
    )

    end = time.time()
    scan_time = round(end - start,2)

    port_score = cal_risk(data["ports"])
    risk = get_risk_level(port_score)
    recommendation_list = get_recommendations(data["ports"])
    print()

    print("\n<*>-------<*> NexScan Results <*>--------<*>")


        #-----------------
        #Scan informations
        #-----------------

    print()
    print(f"+---+ Scan Informantion +---+")
    print(f"<*> Target : {data['target']}")
    print(f"<*> Status : {data['status']}")

    print()
    print(f"+---+ Risk +---+")
    print(f"Risk Score: {port_score}")
    print(f"Risk Level: {risk}")
    print()
    print("+---+ Scan Time +---+")
    print(f"Scan Time : {scan_time} sec")
    print()
    print("+---+ Open Ports +---+")
    print(f"Open Ports : {len(data['ports'])}")
    print(f"Findings : {len(findings)}")
    print("")


        #-----------------
        #Port Information
        #-----------------

    print("{:^8} {:^15} {:^40}".format(
        "PORT",
        "SERVICE",
        "VERSION"
    ))

    print("+","-" * 60,"+")

    for port in data["ports"]:
            print(
                "{:^8} {:^15} {:^40}".format(
                    port["port"],
                    port["service"],
                    port["version"]
                )
            )


        #-----------------
        #Vuln Analyaser
        #-----------------

    print()
    print()
    print("<+>----<+> Vulerability Analysis <+>----")
    print()

    if findings:

            for finding in findings:

                print(f"Severity : {finding['severity']}")
                print(f"Software : {finding['software']}")
                print(f"Issue    : {finding['issue']}")
                print("+", "-" * 75, "+")

            print()
    else:

            print("No known findings.")
            print()

        #-----------------
        #Recommenddations
        #-----------------

    print("\n               Recommendations:")
    print("*","-" * 45, "*")

    for rec in recommendation_list:
        print(f"• {rec}")

        #-----------------
        #Report Generator
        #-----------------

    generate_html(
        data,
        risk,
        recommendation_list,
        findings
    )

    print("\n<*> Report Saved")
    print("Location : exports/report.html")

if  __name__ == "__main__":
    main()

