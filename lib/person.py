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
    def __init__(self,name="Kenn",job="QA"):
        self.name = name
        self.job = job

    def get_name(self):
        return self._name

    
    def set_name(self, value):
        if isinstance(value, str) and len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be a string under 25 characters.")

    name = property(get_name, set_name)

    def get_job(self):
        return self._job

    
    def set_job(self, value):
        if value in self.APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in the list of approved jobs.")
    job = property(get_name, set_name)