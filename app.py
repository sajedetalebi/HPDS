from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from services.ram_service import RAMService
from controller import router

app = FastAPI()

app.include_router(router)

ram_service = RAMService()

scheduler = BackgroundScheduler()
scheduler.add_job(ram_service.collect_ram_stats, 'interval', minutes=1)
scheduler.start()

@app.on_event("startup")
def startup_event():
    ram_service.repository._initialize_db()

# To run: uvicorn app:app --reload
