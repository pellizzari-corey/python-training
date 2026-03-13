# Practice Challenge: Top Assignment Groups by Open Incidents

## Overview

In real environments, operations teams frequently generate reports to understand **which teams are carrying the most active incidents**.

This helps identify:

- overloaded support teams
- incident hotspots
- operational bottlenecks
- resource allocation issues

Your task is to write a Python function that processes a list of incident records and produces a **sorted report of assignment groups with open incidents**.

This type of logic is commonly used when building:

- reporting scripts
- incident backlog dashboards
- operational workload summaries
- incident analytics pipelines

---

# Assignment

Write a function:

```python
def top_assignment_groups_by_open_incidents(incidents):
```

The function should return a **list of tuples** representing assignment groups and their counts of **open incidents**.

Each tuple should have the format:

```python
(group_name, open_incident_count)
```

The list must be **sorted in descending order of incident count**.

---

# What Is an Open Incident?

Only count incidents whose `"state"` is:

- `"New"`
- `"In Progress"`

Incidents in these states should **NOT** be counted:

- `"Resolved"`
- `"Closed"`

These represent completed incidents.

---

# Example Input

```python
[
    {"number": "INC001", "assignment_group": "Network", "state": "New"},
    {"number": "INC002", "assignment_group": "Service Desk", "state": "In Progress"},
    {"number": "INC003", "assignment_group": "Network", "state": "Resolved"},
    {"number": "INC004", "assignment_group": "Network", "state": "New"},
    {"number": "INC005", "assignment_group": "Security", "state": "New"}
]
```

---

# Expected Output

```python
[
    ("Network", 2),
    ("Service Desk", 1),
    ("Security", 1)
]
```

Explanation:

| Incident | Group | State | Counted |
|--------|------|------|--------|
| INC001 | Network | New | ✔ |
| INC002 | Service Desk | In Progress | ✔ |
| INC003 | Network | Resolved | ✘ |
| INC004 | Network | New | ✔ |
| INC005 | Security | New | ✔ |

So the open incident totals are:

```
Network → 2
Service Desk → 1
Security → 1
```

Sorted descending:

```
2 → 1 → 1
```

---

# Rules

Only count incidents that have:

- a non-empty `"assignment_group"`
- a non-empty `"state"`

Skip any record where:

- `"assignment_group"` is missing
- `"state"` is missing
- `"assignment_group"` is `None` or `""`
- `"state"` is `None` or `""`

Additional requirements:

- Use **loops, dictionaries, and lists only**
- Do **not use external libraries**
- Do **not print inside the function**
- Return the final **sorted list of tuples**

---

# Edge Cases to Consider

Your function should correctly handle:

### Empty list

```python
[]
```

Expected output:

```python
[]
```

---

### Invalid records

These records should be skipped:

```python
{"number": "INC100", "assignment_group": "", "state": "New"}
{"number": "INC101", "state": "In Progress"}
{"number": "INC102", "assignment_group": "Network"}
```

---

# Example With More Data

Input:

```python
[
    {"number": "INC010", "assignment_group": "Network", "state": "New"},
    {"number": "INC011", "assignment_group": "Network", "state": "In Progress"},
    {"number": "INC012", "assignment_group": "Database", "state": "New"},
    {"number": "INC013", "assignment_group": "Database", "state": "Resolved"},
    {"number": "INC014", "assignment_group": "Security", "state": "New"},
    {"number": "INC015", "assignment_group": "Security", "state": "New"},
]
```

Expected output:

```python
[
    ("Network", 2),
    ("Security", 2),
    ("Database", 1)
]
```

---

# Goal

Your goal is to produce a **sorted report showing which assignment groups currently have the most open incidents**.

This is similar to what operations teams look at during:

- daily standups
- incident backlog reviews
- reliability reporting
- workload balancing

Priority and incident metrics are often used to determine **how quickly incidents must be addressed**, since higher-priority incidents require faster resolution due to greater impact or urgency. :contentReference[oaicite:0]{index=0}

---

# Starter Function

```python
def top_assignment_groups_by_open_incidents(incidents):
    pass
```

---

# Hint

You will likely solve this in **three phases**:

### Phase 1 — Filter and count

Build a dictionary like:

```python
{
    "Network": 2,
    "Security": 2,
    "Database": 1
}
```

---

### Phase 2 — Convert to tuples

Transform the dictionary into a list like:

```python
[
    ("Network", 2),
    ("Security", 2),
    ("Database", 1)
]
```

---

### Phase 3 — Sort

Sort the list by the **incident count in descending order**.