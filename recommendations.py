recommendations = {
    
    21: "FTP detected. Consider SFTP instead. ",
    
    22: "SSH detected. Disable password login. ",
    
    23: "Telnet detected. Replace with SSH. ",
    
    80: "Ensure HTTP redirects to HTTPS. ",
    
    445: "SMB detected. Disable if unused. ",
    
    3389: "RDP detected. Restrict access. ",
    
    3306: " Do not expose MySQL publicaly."
    
}

def get_recommendations(port_list):
    result = []
    
    for p in port_list:
        port = int(p["port"])
        
        if port in recommendations:
            result.append(recommendations[port])
    return result
