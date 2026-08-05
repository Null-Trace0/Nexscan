risk_table = {
    
    21: "High",         #FTP
    
    22: "Medium",       #SSH
    
    23: "Critical",     #Telnet
    
    25: "Medium",       #SMTP
    
    53:"Medium",        #DNS
        
    80: "Low",          #HTTP
    
    110: "Medium",      #POP3
    
    139: "High",        #NetBIOS
    
    443: "Low",         #HTTPS
    
    445: "Critical",    #SMB
    
    1433:"High",        #MSSQL
    
    3306: "High",       #MYSQL
    
    3389: "Critical",   #RDP
    
    5432: "High",       #PostgreSQL
    
    5900: "Critical",   #VNC
    
    6379: "Critical",   #Redis
    
    27017: "High",      #MongoDB
}

def cal_risk(port_list):
    score_map = {
        "Low": 10,
        "Medium": 20,
        "High": 30,
        "Critical": 40
    }

    total = 0

    for port in port_list:

        p = int(port["port"])

        if p not in risk_table:
            continue

        total += score_map[risk_table[p]]

    return total

def get_risk_level(score):
    
    if score >= 80:
        return "Critical"
    
    elif score >= 60:
        return "High"
    
    elif score >= 30:
        return "Medium"
    
    return "Low"    