import xml.etree.ElementTree as ET

def parse_scan(file):

    tree = ET.parse(file)

    root = tree.getroot()

    host = root.find("host")

    address = host.find("address").attrib["addr"]

    status = host.find("status").attrib["state"]

    ports = []

    ports_element = host.find("ports")

    if ports_element:

        for p in ports_element.findall("port"):
            state = p.find("state").attrib["state"]

            if state != "open":
                continue
            service = p.find("service")

            ports.append({
                "port": p.attrib["portid"],
                "service": service.attrib.get("name", "Unknown"),
                "version" : "{} {}" .format(
                    service.attrib.get("product", ""),
                    service.attrib.get("version", "")
                ).strip(),
                "state": state
            })
    return {
    "target": address,
    "status": status,
    "ports": ports
    }
