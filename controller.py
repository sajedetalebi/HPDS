from fastapi import APIRouter, HTTPException
from services.ram_service import RAMService

router = APIRouter()
ram_service = RAMService()

@router.get("/ram_stats/{n}")
def get_last_n_ram_stats(n: int):
    if n <= 0:
        raise HTTPException(status_code=400, detail="Invalid value for n. Must be a positive integer.")

    data = ram_service.get_last_n_ram_stats(n)
    if data:
        return [record.to_dict() for record in data]
    else:
        raise HTTPException(status_code=404, detail="No data found")
