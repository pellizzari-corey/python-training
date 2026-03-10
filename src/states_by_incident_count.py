def states_by_incident_count(incidents):

    counts = {}

    for incident in incidents:
        
        if "state" not in incident:
            continue

        state = incident["state"]

        if state is None or state == "":
            continue

        if state not in counts:
            counts[state] = 0
        counts[state] += 1

    converted_counts = list(counts.items())
    converted_counts.sort(key=lambda index: index[1], reverse=True)

    return converted_counts