# Practice Challenge: Count Open Incidents by Priority

## Overview

In many IT operations environments and workflows, teams often need quick summaries of **open incidents** by priority to understand workload, operational risk, and escalation needs.

Your task is to write a Python function that processes a list of incident records and returns a summary of **open incidents grouped by priority**.

This challenge simulates the type of data transformation commonly used in:

- automation scripts
- monitoring dashboards
- operational reporting
- incident management pipelines

---

# Assignment

Write a function:

```python
def count_open_incidents_by_priority(incidents):
```

The function should return a dictionary where:

- each key is an incident **priority**
- each value is the **count of open incidents** with that priority

Each incident record is represented as a dictionary that may contain the following keys:

- `"number"` – the incident number (example: `"INC0012345"`)
- `"priority"` – example values: `"P1"`, `"P2"`, `"P3"`
- `"state"` – example values: `"New"`, `"In Progress"`, `"Resolved"`, `"Closed"`

---

# Open Incident Rule

Only count incidents whose `"state"` is considered **open**.

Open states are:

- `"New"`
- `"In Progress"`

Incidents in the following states should **not** be counted:

- `"Resolved"`
- `"Closed"`

---

# Example Input

```python
[
    {"number": "INC001", "priority": "P1", "state": "New"},
    {"number": "INC002", "priority": "P2", "state": "In Progress"},
    {"number": "INC003", "priority": "P1", "state": "Resolved"},
    {"number": "INC004", "priority": "P1", "state": "New"}
]
```

---

# Expected Output

```python
{
    "P1": 2,
    "P2": 1
}
```

Explanation:

- `INC001` → counted (New, P1)
- `INC002` → counted (In Progress, P2)
- `INC003` → ignored (Resolved)
- `INC004` → counted (New, P1)

---

# Rules

Only count incidents that have:

- a non-empty `"priority"`
- a non-empty `"state"`

If either field is missing or empty, **skip that record**.

Additional requirements:

- Use **loops and dictionaries only**
- Do **not use external libraries**
- Preserve the **exact priority strings**
- Do **not print inside the function**
- Return the resulting dictionary

---

# Edge Cases to Consider

Your function should correctly handle:

- An empty incident list
- Incidents missing `"priority"`
- Incidents missing `"state"`
- Incidents with empty values for those fields

---

# Example Invalid Records (Should Be Skipped)

```python
{"number": "INC010", "priority": "", "state": "New"}
{"number": "INC011", "priority": "P1", "state": ""}
{"number": "INC012", "state": "New"}
{"number": "INC013", "priority": "P2"}
```

---

# Goal

Your goal is to produce a dictionary that summarizes **open incidents by priority**.

This is a common task when building scripts for:

- automation
- operations dashboards
- incident backlog reporting
- monitoring integrations

---

# Starter Function

You may begin with this stub:

```python
def count_open_incidents_by_priority(incidents):
    pass
```

---

# Hint

The general pattern for solving this problem is:

1. Loop through each incident
2. Validate that required fields exist
3. Check whether the incident state is considered **open**
4. Count incidents grouped by **priority**

Conceptually the counting step looks like:

```
priority_counts[priority] += 1
```

But first you must ensure the priority key exists in the dictionary.