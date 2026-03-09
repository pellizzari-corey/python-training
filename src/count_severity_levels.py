def count_severity_levels(logs): 
    severity_count = {} 
    # Picking out each string in the list 
    for log in logs: 
        # Initializing an variable storing and empty string 
        severity = ""
        # Picking out the actual severity before the Colon 
        for word in log: 
            if word == ":": 
                break 
            severity += word 
        # If the severity exists add a count, else add to the dictionary 
        if severity in severity_count: 
            severity_count[severity] += 1 
        else: 
            severity_count[severity] = 1 
    # return dictionary 
    return severity_count