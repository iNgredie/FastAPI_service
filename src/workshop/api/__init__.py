from fastapi import APIRouter
from .operations import router as operations_routers


router = APIRouter()
router.include_router(operations_routers)
