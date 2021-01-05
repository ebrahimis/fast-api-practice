from typing import Optional
from app.apis.users import users_router
from app.apis.subscriptions import subscriptions_router
from app.apis.subscriptions_audit import subscription_audit_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(users_router, prefix='/users')
app.include_router(subscriptions_router, prefix='/subscriptions')
app.include_router(subscription_audit_router, prefix='/subscriptions_audit')

@app.get("/health")
def read_root():
    return {"Healthy": "Healthy"}
