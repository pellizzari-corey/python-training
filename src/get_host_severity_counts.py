def get_host_severity_counts(log_lines):
    # Initialize our "outer" dictionary to store hostnames as keys
    counts = {}

    for line in log_lines:
        # Step 1: Split the raw string into a list of "key=value" pairs
        # "host=web-1 severity=ERROR" -> ["host=web-1", "severity=ERROR"]
        parts = line.split(" ")
        
        # We use a temporary dictionary for each line to easily lookup keys
        fields = {}

        for part in parts:
            # Skip any parts that don't follow the "key=value" format
            if "=" not in part:
                continue
            
            # Step 2: Unpack the key and value
            # The "1" ensures we only split on the first "=" found
            key, value = part.split("=", 1)
            fields[key] = value

        # Step 3: Validation
        # If the log line is missing vital info, we skip the rest of this iteration
        if "host" not in fields or "severity" not in fields:
            continue

        host = fields["host"]
        severity = fields["severity"]

        # Step 4: Manage the nested structure
        # If we haven't seen this host before, add it with an empty inner dictionary
        if host not in counts:
            counts[host] = {}

        # Step 5: Manage the counts
        # If this severity (ERROR/INFO) is new for this host, start it at 0
        if severity not in counts[host]:
            counts[host][severity] = 0

        # Increment the count in the nested dictionary
        counts[host][severity] += 1

    return counts