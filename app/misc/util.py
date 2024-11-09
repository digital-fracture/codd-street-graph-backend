from pathlib import Path
from uuid import uuid4

import aiofiles
from fastapi import UploadFile

from misc.config import storage_dir


async def save_to_storage(file: UploadFile):
    path = storage_dir / Path(file.filename).with_stem(str(uuid4())).name

    async with aiofiles.open(path, "wb") as async_file:
        await async_file.write(await file.read())

    return path
