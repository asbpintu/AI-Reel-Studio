from enum import Enum


class UserRole(str, Enum):

    ADMIN = "Admin"

    CREATOR = "Creator"

    USER = "User"