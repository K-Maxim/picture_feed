from fastapi import APIRouter
from .comment import view as comment_view
from .picture import view as picture_view
from .stats import view as stats_view

routes = APIRouter()


routes.include_router(picture_view.router, prefix='/picture', tags=['picture'])
routes.include_router(comment_view.router, tags=['comment'])
routes.include_router(stats_view.router, tags=['stat'])