def highest_priority_open_incident_count(incidents):

    outputs = {}

    for incident in incidents:

        # Edge cases
        if 'state' not in incident or 'priority' not in incident:
            continue
        if incident['state'] is None or incident['state'] == "":
            continue
        if incident['state'] == "Resolved" or incident['state'] == "Closed":
            continue
        if incident['priority'] is None or incident['priority'] == "":
            continue

        priority = incident['priority']
        if priority not in outputs:
            outputs[priority] = 0
        outputs[priority] += 1

    priority_count = list(outputs.items())

    best_count = 0
    best_priority = None
    for priority, count in priority_count:
        if count > best_count:
            best_count = count
            best_priority = priority
        elif count == best_count and priority < best_priority:
            best_priority = priority

    return (best_priority, best_count)