def count_critical_by_host(scan_lines):
    # Initialize an empty dictionary to store host names as keys 
    # and their critical vulnerability counts as values.
    counts = {}

    for line in scan_lines:
        # Create a temporary dictionary for each line to store its specific key=value pairs.
        fields = {}
        # Break the line string into a list of strings based on spaces.
        parts = line.split(" ")

        for part in parts:
            # Check if the segment actually looks like a key=value pair.
            if "=" not in part:
                continue
            
            # Split the part at the first "=" found. 
            # key_value will be a list: [key, value]
            key_value = part.split("=", 1)
            key = key_value[0]
            value = key_value[1]
            
            # Add this pair to our temporary fields dictionary.
            fields[key] = value

        # Guard Clause: If the line didn't contain both required keys, skip to the next line.
        if "host" not in fields or "severity" not in fields:
            continue

        # Guard Clause: We only care about "CRITICAL" severity. 
        # If it's anything else, skip it.
        if fields["severity"] != "CRITICAL":
            continue

        # Extract the host name for easier readability.
        host = fields["host"]
        
        # Update the main counts dictionary.
        if host in counts:
            # If the host exists, increment the existing integer value.
            counts[host] += 1
        else:
            # If this is the first time we see this host, initialize it at 1.
            counts[host] = 1

    # Return the completed map of hosts and their critical counts.
    return counts