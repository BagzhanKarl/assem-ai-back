from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from assem.router import user_router, categoryAPI, typesApi, businessAPI, role_router, branch_router, product_router, \
    webhook_router, ai

app = FastAPI(title='Assem', version='1.0.0')

app.include_router(ai)
app.include_router(user_router)
app.include_router(businessAPI)
app.include_router(branch_router)
app.include_router(product_router)
app.include_router(categoryAPI)
app.include_router(typesApi)
app.include_router(role_router)

app.include_router(webhook_router)

origins = [
    "https://demo.assemcrm.kz",
    # Вы можете добавить другие разрешенные источники, если нужно
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)