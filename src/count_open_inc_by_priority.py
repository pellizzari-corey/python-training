def count_open_incidents_by_priority(incidents):
    report = {}

    for incident in incidents:

        # Handle edge cases
        if "priority" not in incident or "state" not in incident:
            continue
        if incident['priority'] is None or incident['priority'] == "":
            continue
        if incident['state'] is None or incident['state'] == "": 
            continue
        if incident['state'] == "Resolved" or incident['state'] == "Closed":
            continue

        priority = incident['priority']

        if priority not in report:
            report[priority] = 0
        report[priority] += 1

    return report