# ServiceNow Practice Challenge: Incident Summary

## Overview

In many IT operations environments (including ServiceNow), incident records are often processed to generate summaries and metrics for reporting and dashboards.

Your task is to write a Python function that processes a list of incident records and returns a structured summary of incident counts grouped by **assignment group** and **state**.

---

## Assignment

Write a function:

```python
def summarize_incidents(incidents):
```

The function should return a nested dictionary that summarizes incident counts by assignment group and state.

Each incident record is represented as a dictionary that may contain the following keys:

- "number" – the incident number (example: "INC0012345")

- "assignment_group" – the group responsible for the incident (example: "Network")

- "state" – the current state of the incident (example: "New", "In Progress", "Resolved")

**Example Input**
```python
[
    {"number": "INC001", "assignment_group": "Network", "state": "New"},
    {"number": "INC002", "assignment_group": "Network", "state": "Resolved"},
    {"number": "INC003", "assignment_group": "Service Desk", "state": "In Progress"},
    {"number": "INC004", "assignment_group": "Network", "state": "New"}
]
```
**Expected Output**
```pyton
{
    "Network": {
        "New": 2,
        "Resolved": 1
    },
    "Service Desk": {
        "In Progress": 1
    }
}
```
## Rules

**Only count incidents that have:**

- a non-empty "assignment_group"

- a non-empty "state"

If either field is missing or empty, **skip that record**.

Additional requirements:

- Use loops and dictionaries only

- Do not use external libraries

- Preserve the exact capitalization of group names and states

- Do not print inside the function

- Return the nested dictionary

- Edge Cases to Consider

**Your function should correctly handle:**

- An empty incident list

- Incidents missing "assignment_group"

- Incidents missing "state"

- Incidents with empty values for those fields

**Example of invalid records that should be skipped:**

```python
{"number": "INC100", "assignment_group": "", "state": "New"}
{"number": "INC101", "state": "Resolved"}
{"number": "INC102", "assignment_group": "Network"}
```
## Goal

**Your goal is to produce a clean nested dictionary structure that summarizes incident counts by group and state.**

This type of data transformation is common when building scripts for:

- ServiceNow automation

- monitoring dashboards

- operational reporting

- log aggregation systems

**Starter Function**

You may begin with this stu

```python
def summarize_incidents(incidents):
    pass
```
## Hint

A common pattern used in this problem is nested dictionary counting:

- Check if the group exists in the summary dictionary

- If not, create it

- Check if the state exists inside that group

- If not, initialize it

- Increment the count