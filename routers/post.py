from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import AsyncSessionLocal
from models.post import Post
from schemas.post import PostCreate, PostUpdate, PostRead
from utils.auth import get_current_user
from models.user import User

router = APIRouter()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# Create Post
@router.post("/posts",reponse_model=PostRead,status_code=status.HTTP_201_CREATED)
async def create_post(post:PostCreate,
                      db:AsyncSession=Depends(get_db),
                      current_user:User=Depends(get_current_user)
):
    new_post = Post(
        title=post.title,
        content=post.content,
        author_id=current_user.id
    )
    db.add(new_post)
    await db.commit()
    await db.refresh(new_post)
    return new_post 

#Single Post
@router.get("/posts/{post_id}",response_model=PostRead)
async def read_post(post_id:int,db:AsyncSession=Depends(get_db)):
    result = await db.execute(select(Post).where(Post.id==post_id))
    post = result.scalar()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")
    return post 


#Update Post
@router.put("/posts/{post_id}",response_model=PostRead)
async def update_post(
    post_id:int,
    post_username:PostUpdate,
    db:AsyncSession=Depends(get_db),
    current_user:User=Depends(get_current_user)
):
    result = await db.execute(select(Post).where(Post.id==post_id))
    post =result.scalar()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")
    if post.author_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You are not the author of this post")
    
    post.title = post_username.title
    post.content = post_update.title 
    await db.commit()
    await db.refresh(post)
    return post 

