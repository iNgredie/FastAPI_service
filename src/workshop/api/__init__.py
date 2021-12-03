from fastapi import APIRouter
from .auth import router as auth_router
from .operations import router as operations_routers
from .reports import router as reports_routers


router = APIRouter()
router.include_router(auth_router)
router.include_router(operations_routers)
router.include_router(reports_routers)
