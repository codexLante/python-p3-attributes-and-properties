#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    approved_jobs = ["Sales", "Marketing", "Engineering", "ITC", "HR"]

    def __init__(self, name=None, job=None):
        if name is not None:
            if not isinstance(name, str) or len(name.strip()) == 0 or len(name) > 25:
                print("Name must be string between 1 and 25 characters.")
            else:
                self.name = name.title()

        if job is not None:
            if job not in Person.approved_jobs:
                print("Job must be in list of approved jobs.")
            else:
                self.job = job

