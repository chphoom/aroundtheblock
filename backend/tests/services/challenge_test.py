""" Challenge test file.

This file provides unit tests for the ChallengeService class.

NOTE THAT IT DOESN'T WORK RIGHT NOW
"""

import pytest
from sqlalchemy.orm import Session
from backend.entities.challenge_entity import ChallengeEntity
from backend.entities.user_entity import UserEntity
from backend.entities.post_entity import PostEntity
from backend.models import User, Challenge, Post
from backend.services.challenge_service import ChallengeService
from backend.services.user_service import UserService
from datetime import datetime


# Mock Users for Testing TODO: add attributes of user and challenge
#user1 = User(email="test@test.com", displayName="testuser", password="test", created=datetime.now(), pfp="", userPosts=[], savedChallenges=[], savedPosts=[], connectedAccounts=[])

# Mock Challenges for Testing
chal1 = Challenge(id=1, posts=[], noun="", verb="", adj="", emotion="tired", style="", colors=[], start=None, end=None, createdBy=None)

@pytest.fixture(autouse=True)
def setup_for_tests(test_session: Session):
    #add all users and events to session TODO: add any additional mock data to session
    #user1_entity = UserEntity.from_model(user1)
    #test_session.add(user1_entity)
    chal1_entity = ChallengeEntity.from_model(chal1)
    test_session.add(chal1_entity)
    test_session.commit()

@pytest.fixture()
def challengeService(test_session: Session):
    return ChallengeService(test_session)
@pytest.fixture()
def userService(test_session: Session):
    return UserService(test_session)

# write tests below

def test_get_one_challenge(challengeService: ChallengeService):
   assert(challengeService.get(1).emotion.__eq__('tired'))