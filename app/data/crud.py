from pathlib import Path
from uuid import UUID

from sqlalchemy import select

from data import models, schemas
from data.database import async_session


async def create_upload(user_id: UUID, version: int, path: Path, schema: schemas.StreetGraphPair):
    upload = models.Upload(
        user_id=user_id,
        version=version,
        path=str(path.absolute()),
        json_data=schema.model_dump_json(),
    )

    async with async_session() as session:
        await session.merge(upload)
        await session.commit()


async def get_upload(user_id: UUID, version: int) -> models.Upload:
    statement = select(models.Upload).filter_by(user_id=user_id, version=version)

    async with async_session() as session:
        result = await session.execute(statement)

    return result.scalars().one()
