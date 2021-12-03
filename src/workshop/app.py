from fastapi import FastAPI

from .api import router

tags_metada = [
    {
        'name': 'auth',
        'description': 'Авторизация и регистраия',
    },
    {
        'name': 'operations',
        'description': 'Работа с операциями',
    },
    {
        'name': 'reports',
        'description': 'Импорт и экспорт отчетов',
    },
]


app = FastAPI(
    title='Workshop',
    description='Сервис учета личных расходов и доходов',
    version='1.0.0',
    openapi_tags=tags_metada,
)
app.include_router(router)
