from fastapi.routing import APIRouter
from . import runner

router = APIRouter(prefix='/v1')
router.include_router(
    runner.router,
    prefix="/drivers",
    tags=["actions"]
)
