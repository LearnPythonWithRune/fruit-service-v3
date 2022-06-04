import logging
import os
from http import HTTPStatus
from typing import Dict

from fastapi import APIRouter

from app.routers.storage_module import Storage

logger = logging.getLogger(__file__)
router = APIRouter(tags=['income'])


storage = Storage(os.getenv('STORAGE_HOST', 'localhost'))


@router.post('/order', status_code=HTTPStatus.OK)
async def order_call(order: str) -> Dict[str, str]:
    logger.info(f'Incoming order: {order}')
    storage.ingest(order)
    logger.info(f'Ingested order: {order}')
    return {'Received order': order}
