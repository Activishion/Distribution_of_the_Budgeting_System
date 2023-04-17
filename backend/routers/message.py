from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_async_session
from repository.message import MessageRepository
from schemas.message import MessageRead


router = APIRouter()


@router.get("/")
async def get_all_message(
        limit: int = 10,
        skip: int = 0,
        session: AsyncSession = Depends(get_async_session)
) -> List[MessageRead]:
    async with session.begin():
        async_session = MessageRepository(session, limit, skip)
        messages: list = await async_session.get_all_message_in_year()
        if messages is None:
            return {
                'status': status.HTTP_404_NOT_FOUND,
                'data': None,
                'description': "Messages is not defined."
            }
        return messages


@router.get("/{message_id}")
async def get_message_by_id(
        message_id: int,
        session: AsyncSession = Depends(get_async_session)
) -> List[MessageRead]:
    async with session.begin():
        async_session = MessageRepository(session)
        message = await async_session.get_message_by_id(message_id)
        if message is None:
            return {
                'status': status.HTTP_404_NOT_FOUND,
                'data': None,
                'description': "Message with id={message_id} is not defined."
            }
        return message
