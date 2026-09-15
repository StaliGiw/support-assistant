"""Техническая точка входа. Бизнес-логику добавляем по мере обучения."""
from fastapi import FastAPI

from app.api.health import router as health_router

app = FastAPI(title="Support Assistant", version="0.1.0")
app.include_router(health_router)
