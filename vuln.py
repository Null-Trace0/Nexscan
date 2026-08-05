vuln_db =  {
    
    "OpenSSH": {
        "severity": "Medium",
        "issue": "Older OpenSSH versions may contain known security vulnerabilities.",
        "recommendation": "Upgrade to a supported OpenSSH release."
    },
    
    "Apache": {
        "severity": "High",
        "issue": "Outdated Apache versions may expose web services.",
        "recommendation": "Update Apache and review server configuration.",
    },
    
    "MySQL": {
      "severity": "High",
        "issue": "Database service exposed to the network.",
        "recommendation": "Restrict access using firewall rules.",  
    },
    
    "nginx": {
        "severity": "Medium",
        "issue": "Review nginx version and security updates.",
        "recommendation": "Keep nginx updated.",
    }
        
}

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
                        vuln_db[software]["issue"]                          
                    }) 
    return findings