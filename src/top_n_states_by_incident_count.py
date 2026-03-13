def top_n_states_by_incident_count(incidents, n):

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

    counts_list = list(counts.items())
    counts_list.sort(key=lambda item: item[1], reverse=True)

    return counts_list[:n]
