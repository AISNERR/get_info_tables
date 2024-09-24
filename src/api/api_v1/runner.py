from http.client import HTTPException

from fastapi.routing import APIRouter
from models.models import Data1, Data2, Data3
from schemas.schemas import DataResponse, DataRequest


router = APIRouter()


@router.post("/add/")
async def add_data(data_info: DataRequest):
    try:
        if 1 >= data_info.id <= 10 or 31 >= data_info.id <= 40:
            new_data = await Data1(
                name=data_info.name
            ).save()
        elif 11 >= data_info.id <= 20 or 41 >= data_info.id <= 50:
            new_data = await Data2(
                name=data_info.name
            ).save()
        elif 21 >= data_info.id <= 30 or 51 >= data_info.id <= 60:
            new_data = await Data3(
                name=data_info.name
            ).save()
        else:
            raise HTTPException(status_code=400, detail="Invalid ID range for source")
            return {"message": "Data inserted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    return DataRequest(
        id=new_data.id,
        name=new_data.name
    )









