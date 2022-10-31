from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from core.constant import TOKEN
from service.request import RequestService
from .auth_api import auth
from schema.request import RequestSchema
import datetime as dt
router = APIRouter()


@router.get('/', response_model=list[RequestSchema])
async def get_yesterday_request(requestService: RequestService = Depends(RequestService), _: bool = Depends(auth)):
    try:
        requests = await requestService.get_yesterday_request()
        print(requests)
        return requests
    finally:
        ...


@router.get('/{startDate}/{endDate}', response_model=list[RequestSchema])
async def get_request(startDate: str = None, endDate: str = None, requestService: RequestService =Depends(RequestService), _: bool = Depends(auth)):
        try:
            start = dt.datetime.strptime(startDate, '%Y-%m-%d')
            end = dt.datetime.strptime(endDate, '%Y-%m-%d')
            requests = await requestService.get_request(start, end)
            return requests
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Bad request!",
                )

@router.get('/request')
async def create_request(requestService: RequestService =Depends(RequestService),token:str=None):
        if token is None or token!=TOKEN:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="token invalid",
                )
        response=requestService.tools
        if response is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="BAD REQUEST",
                ) 
        return "request created!"
