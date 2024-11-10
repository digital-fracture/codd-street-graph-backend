from contextlib import asynccontextmanager, AbstractAsyncContextManager
from uuid import UUID

from fastapi import FastAPI, APIRouter, UploadFile, Body, status
from fastapi.middleware.cors import CORSMiddleware

from data import schemas
from data.database import create_database, close_database
from logic.handlers import (
    handle_upload, handle_regenerate, _history
)


# noinspection PyUnusedLocal
@asynccontextmanager
async def lifespan(app: FastAPI) -> AbstractAsyncContextManager[None]:
    await create_database()

    yield

    await close_database()


app = FastAPI(lifespan=lifespan)

# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT"],
    allow_headers=["*"],
)


router = APIRouter()


@app.get("/")
async def index() -> dict[str, bool]:
    return {"healthy": True}


@router.post("/graph", status_code=status.HTTP_201_CREATED)
async def graph(
        file: UploadFile,
        user_id: UUID = Body(embed=True),
        year: int = Body(embed=True, gt=0)
) -> schemas.StreetGraphPair:
    return await handle_upload(file, user_id, year)


@router.post("/graph/regenerate")
async def graph_regenerate(
    user_id: UUID = Body(embed=True),
    year: int = Body(embed=True),
    parameters: schemas.PopulationDistribution = Body(embed=True),
) -> schemas.StreetGraph:
    return await handle_regenerate(user_id, year, parameters)


@router.post("/uploads")
async def uploads(user_id: UUID = Body(embed=True)) -> schemas.GraphHistory:
    # return schemas.GraphHistory(graphs=[])
    return _history


app.include_router(router, prefix="/api/v1", tags=["graphs"])
