from fastapi import APIRouter

router = APIRouter(tags=["system"])


@router.get("/health")
def health() -> dict[str, str]:
    """Проверка запуска приложения, без обращения к внешним сервисам."""
    return {"status": "ok"}
