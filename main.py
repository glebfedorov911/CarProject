from fastapi import FastAPI

from api_v1_version.owner.views  import router as owner_router
from api_v1_version.car.views  import router as car_router

import uvicorn


app = FastAPI()
app.include_router(owner_router)
app.include_router(car_router)

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)