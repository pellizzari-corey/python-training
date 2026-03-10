def top_assignment_groups_by_open_incidents(incidents):
    report = {}

    for incident in incidents:

        # Edge cases
        if 'state' not in incident or 'assignment_group' not in incident:
            continue
        if incident['state'] == "Resolved" or incident['state'] == "Closed" or incident['state'] == "" or incident['state'] is None:
            continue
        if incident['assignment_group'] == "" or incident['assignment_group'] is None:
            continue


        group = incident['assignment_group']
        if group not in report:
            report[group] = 0
        report[group] += 1

    inc_list = list(report.items())

    inc_list.sort(key=lambda count: count[1], reverse=True)
    
    return inc_list