# no.3
from enum import Enum

class Status(Enum):
    ACTIVE = "active"
    BLOCKED = "blocked"

print(Status.ACTIVE)
print(Status.ACTIVE.name, Status.ACTIVE.value)
print(Status("active"))
print(Status.ACTIVE == "active")
print(Status.ACTIVE.value == "active")
print([s.name for s in Status])