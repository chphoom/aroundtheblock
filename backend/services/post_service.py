from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import Post
from ..entities import PostEntity, ChallengeEntity, UserEntity

class PostService:

    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session

    def all(self) -> list[Post]:
        query = select(PostEntity)
        entities = self._session.scalars(query).all()
        return [entity.to_model() for entity in entities]
    
    def create(self, post: Post) -> Post:
        temp = self._session.get(UserEntity, post.postedBy.email)
        if temp:
            post.postedBy = temp
            temp2 = self._session.get(ChallengeEntity, post.challenge.id)
            post.challenge = temp2
            post_entity: PostEntity = PostEntity.from_model(post)
            temp.userPosts.append(post_entity)
            temp2.posts.append(post_entity)
            self._session.add(post_entity)
            self._session.commit()
            return post
        else:
            raise ValueError(f"No user found with PID: {post.postedBy.email}")
            
    def get(self, id: int) -> Post | None:
        # 
        post = self._session.get(PostEntity, id)
        if post:
            return post.to_model()
        else:
            raise ValueError(f"Post not found")

    def delete(self, id: int) -> Post:
        # 
        post = self._session.get(PostEntity, id)
        if post:
            temp = self._session.get(UserEntity, post.postedBy.email)
            temp2 = self._session.get(ChallengeEntity, post.challenge.id)
            temp.userPosts.remove(post)
            temp2.posts.remove(post)
            self._session.delete(post)
            self._session.commit()
            return post
        else:
            raise ValueError(f"No post found")
        
    def update(self, post: Post) -> Post:
        temp = self._session.get(PostEntity, post.id)
        if temp:
            temp.desc = post.desc
            temp.tags = post.tags
            temp.comments = post.comments
            self._session.commit()
            return temp.to_model()
        else:
            raise ValueError(f"Post not found")
