def calculate_security_score(findings):
    
    score = 0 
    
    weights = {
        
        "Low": 10,
        "Medium": 20,
        "High": 30,
        "Criticl": 40,
    }
    
    for finding in findings:
        
        score += weights.get(
            finding["severity"],
            0
        )
    
    return score