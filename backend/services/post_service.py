from fastapi import Depends
from sqlalchemy import select, or_, func
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import Post
from ..entities import PostEntity, ChallengeEntity, UserEntity
from sqlalchemy.sql.expression import and_

class PostService:

    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session

    def all(self) -> list[Post]:
        query = select(PostEntity).where(PostEntity.private.is_(False))
        entities = self._session.scalars(query).all()
        return [entity.to_model() for entity in entities]
    
    def create(self, post: Post) -> Post:
        temp = self._session.get(UserEntity, post.user_id)
        if temp:
            temp2 = self._session.get(ChallengeEntity, post.challenge)
            if temp2:
                post_entity: PostEntity = PostEntity.from_model(post)
                temp.userPosts.append(post_entity)
                temp2.posts.append(post_entity)
                self._session.add(post_entity)
                self._session.commit()
                return post_entity.to_model()
            else:
                raise ValueError(f"No challenge found with id: {post.challenge}")
        else:
            raise ValueError(f"No user found with email: {post.user_id}")
            
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
            temp = self._session.get(UserEntity, post.user_id)
            temp2 = self._session.get(ChallengeEntity, post.challenge)
            temp.userPosts.remove(post)
            temp2.posts.remove(post)
            self._session.delete(post)
            self._session.commit()
            return post
        else:
            raise ValueError(f"No post found")
        
    def update(self, 
               id: int,
               desc: str | None,
               tags: list[str] | None) -> Post:
        temp = self._session.get(PostEntity, id)
        if temp:
            if desc:
                temp.desc = desc
            if tags:
                temp.tags = tags
            self._session.commit()
            return temp.to_model()
        else:
            raise ValueError(f"Post not found")
        
    def get_me_posts(self) -> list[Post]:
        query = (
            select(PostEntity)
            .join(ChallengeEntity)
            .filter(ChallengeEntity.type == "me")
            .where(PostEntity.private.is_(False))
        )
        entities = self._session.scalars(query).all()
        return [entity.to_model() for entity in entities]
    
    
    def get_we_posts(self) -> list[Post]:
        query = (
            select(PostEntity)
            .join(ChallengeEntity)
            .filter(ChallengeEntity.type == "we")
            .where(PostEntity.private.is_(False))
        )
        entities = self._session.scalars(query).all()
        return [entity.to_model() for entity in entities]
    
    def get_by_challenge(self, challenge_type: str) -> list[Post]:
        query = (
            self._session.query(PostEntity)
            .join(PostEntity.challenge)
            .filter(and_(PostEntity.challenge.type == challenge_type, PostEntity.deleted == False))
            .where(PostEntity.private.is_(False))
        )
        entities = query.all()
        return [entity.to_model() for entity in entities]
    
    def search(self, query: str) -> list[Post] | None:      
        statement = select(PostEntity)
        criteria = or_(
            PostEntity.title.ilike(f'%{query}%'),
            PostEntity.desc.ilike(f'%{query}%'),
            func.array_to_string(PostEntity.tags, ',').ilike(f'%{query}%')
            )
        statement = statement.where(criteria).limit(25)
        entities = self._session.execute(statement).scalars()
        return [entity.to_model() for entity in entities]

    def tagged(self, query: str) -> list[Post] | None:      
        statement = select(PostEntity).where(func.array_to_string(PostEntity.tags, ',').ilike(f'%{query}%')).limit(25)
        entities = self._session.execute(statement).scalars()
        return [entity.to_model() for entity in entities]