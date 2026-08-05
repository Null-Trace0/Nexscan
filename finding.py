from vuln import vuln_db

def analyze_vulnerabilities(ports):
    
    findings = []
    
    for port in ports:
        version = port["version"]
        
        for software in vuln_db: 
            if software.lower() in version.lower():
                findings.append({
                    
                    "software": software,
                    
                    "severity":
                        vuln_db[software]["severity"],
                        
                    "issue":
                        vuln_db[software]["issue"],
                        
                    "recommendation":
                        vuln_db[software]["recommendation"]
                })
                
    return findings