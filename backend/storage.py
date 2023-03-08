"""Stand-in data layer until we connect to the database.

This file provides some overly simplistic access functions to support the minimum
API of this exercise. Ultimately, functions like these will be backed by an actual
storage system such as a relational database.
"""
from user import User
from datetime import datetime
from checkin import Checkin


__author__ = "Kris Jordan"
__copyright__ = "Copyright 2023"
__license__ = "MIT"


_registrations: dict[int, User] = {}
"""Private module data simulating a simple key-value store where keys are PID and values are User objects. Do not reference externally."""

_checkins: list[Checkin] = []
"""Private module data simulating a simple append-only store where values are Checkin objects. Do not reference externally."""


def create_registration(user: User) -> User:
    """Register a new user.

    Args:
        user is a valid User model.

    Returns:
        The registered User object.

    Raises:
        Exception if a user with the same PID is already registered.
    """
    if len(str(user.pid)) != 9:
        raise Exception(f"Invalid PID: {user.pid}")

    if len(user.first_name) == 0 or len(user.last_name) == 0:
        raise Exception(f"First and Last Name required.")

    if user.pid in _registrations:
        raise Exception(f"User with PID {user.pid} already registered.")
    _registrations[user.pid] = user
    return user


def get_registrations() -> list[User]:
    """Get a list of all registered users.
    
    Args:
        None

    Returns:
        List of all registered users.
    """
    return list(_registrations.values())


def get_user_by_pid(pid: int) -> Checkin | None:
    """Lookup a User by their PID.
    
    Args:
        pid of the user to lookup.

    Returns:
        None if the user's PID is not registered. Otherwise,
        returns the corresponding User model.
    """
    return _registrations[pid] if pid in _registrations else None


def create_checkin(pid: int) -> Checkin:
    """Checkin a User by their PID.
    
    Args:
        pid of the user checking in.
        
    Returns:
        Checkin object of a successful checkin.
        
    Raises:
        Exception if user with PID does not exist.
    """
    user = get_user_by_pid(pid)
    if user:
        checkin = Checkin(user=user, created_at=datetime.now())
        _checkins.append(checkin)
        return checkin
    else:
        raise Exception(f"User with PID {pid} does not exist.")


def get_checkins() -> list[Checkin]:
    """Get all checkins in the system.
    
    Args:
        None
        
    Returns:
        List of all checkins."""
    return _checkins


def delete_user(user: User) -> User: 
    """Delete a user
    
    Args:
        user that will be passed down from frontend
        
    Returns:
        deleted user."""
    deletionPID = user.pid #pid that must be delted
    deletedUser = _registrations.pop(deletionPID) #deleted registration user gets passed down through pop

    for checkins in _checkins:
        if checkins.user == deletedUser:
            _checkins.remove(checkins)
    
    return deletedUser
    

def reset() -> None:
    """Reset registration and checkin data at the module level used in unit testing.
    
    Args:
        None
        
    Returns:
        None
    """
    global _registrations, _checkins
    _registrations = {}
    _checkins = []