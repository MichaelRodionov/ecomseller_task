import requests
from fastapi import FastAPI, APIRouter, HTTPException, Request

from src.structures.result import ResultStruct
from src.tasks.db_write import add_result_db


# ----------------------------------------------------------------
# init fastapi
app = FastAPI()


# ----------------------------------------------------------------
# init router
result_router = APIRouter(prefix='/api/v1/result', tags=['results'])


# ----------------------------------------------------------------
@result_router.post('/{offer_id}')
async def get_results(offer_id, request: Request):
    ozon_auth_data = await request.json()
    ozon_api_response = requests.post(
        url='https://api-seller.ozon.ru/v1/product/info/description',
        headers={
            'Api-Key': ozon_auth_data['Api-Key'],
            'Client-Id': ozon_auth_data['Client-Id']
        },
        json={"offer_id": offer_id}
    )
    if ozon_api_response.status_code != 200:
        raise HTTPException(status_code=ozon_api_response.status_code, detail='Ozon API request failed')
    result = ozon_api_response.json()['result']
    result['item_id'] = result.pop('id')
    result_struct = ResultStruct(**result).model_dump()
    try:
        add_result_db.delay(result_struct)
    except Exception as e:
        raise HTTPException(status_code=500, detail='Failed to save result')
    return result_struct


@result_router.get('/fun')
async def get_celery_result():
    return 'Done'

app.include_router(result_router)
