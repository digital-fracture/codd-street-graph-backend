from pathlib import Path
from uuid import UUID, uuid4

from data import models
from data.database import async_session


async def create_upload(user_id: UUID, version: int, path: Path) -> None:
    upload = models.Upload(
        upload_id=uuid4(), user_id=user_id, version=version, path=str(path.absolute())
    )

    async with async_session.begin() as session:
        session.add(upload)
        await session.commit()
