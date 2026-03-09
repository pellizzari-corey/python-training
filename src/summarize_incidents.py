def summarize_incidents(incidents):

    report = {}

    for incident in incidents:
        
        # if either the state or assignment group are empty, skip it
        if "state" not in incident or "assignment_group" not in incident:
            continue
        if  incident['state'] is None or incident['state'] == '':
            continue
        if  incident['assignment_group'] is None or incident['assignment_group'] == '':
            continue

        group = incident['assignment_group']
        state = incident['state']

        # If the assignment is not in the report add it
        if group not in report:
            report[group] = {}

        # If the State is not in the report add it
        if state not in report[group]:
            report[group][state] = 0
        report[group][state] += 1

    return report