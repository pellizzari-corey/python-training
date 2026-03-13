# Practice Challenge: Top N States by Incident Count

## Overview

In many environments, teams need to quickly determine which incident states appear most frequently. This is useful when building dashboards, analytics tools, and operational reports.

Your task is to write a function that returns the **top N incident states by count**.

---

## Assignment

Write a function:

```python
def top_n_states_by_incident_count(incidents, n):
```

The function should return a **list of tuples** containing the top `n` states and their incident counts.

The list must be sorted in **descending order of incident count**.

---

## Example Input

```python
incidents = [
    {"number": "INC001", "state": "New"},
    {"number": "INC002", "state": "In Progress"},
    {"number": "INC003", "state": "Resolved"},
    {"number": "INC004", "state": "New"},
    {"number": "INC005", "state": "Closed"},
    {"number": "INC006", "state": "New"},
    {"number": "INC007", "state": "Resolved"},
]

n = 2
```

---

## Expected Output

```python
[
    ("New", 3),
    ("Resolved", 2)
]
```

Explanation:

State counts:

```
New → 3
Resolved → 2
In Progress → 1
Closed → 1
```

The top 2 are returned.

---

## Rules

Skip incidents that:

- do not contain `"state"`
- contain `"state": None`
- contain `"state": ""`

Additional requirements:

- Use loops, dictionaries, and sorting
- Do not use external libraries
- Do not print inside the function
- Return a list of tuples

---

## Edge Cases

Your function should handle:

- an empty incident list
- `n` larger than the number of states
- incidents with missing `"state"` values

---

## Example Invalid Records

Skip these:

```python
{"number": "INC010", "state": ""}
{"number": "INC011"}
{"number": "INC012", "state": None}
```

---

## Goal

Return the **top N most common incident states**.

This pattern appears frequently when building:

- analytics dashboards
- reporting systems
- monitoring summaries
- backend data pipelines

---

## Starter Code

```python
def top_n_states_by_incident_count(incidents, n):
    pass
```

---

## Hint

The solution follows **four phases**:

### Phase 1 — Count

Build a dictionary:

```
state_counts[state] += 1
```

---

### Phase 2 — Convert

Convert the dictionary to a list:

```
list(state_counts.items())
```

---

### Phase 3 — Sort

Sort by count descending:

```
key=lambda item: item[1]
```

---

### Phase 4 — Slice

Return only the top `n` results.

This is the new concept introduced in this challenge.