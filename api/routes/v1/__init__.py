from fastapi import APIRouter
from routes.v1.generic import router as generic_router
from routes.v1.people import router as people_router
from routes.v1.ws import router as ws_router


router = APIRouter()
router.include_router(generic_router)
router.include_router(people_router)
router.include_router(ws_router)
