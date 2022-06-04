import logging
from http import HTTPStatus
from typing import Dict

from fastapi import FastAPI
from starlette_exporter import PrometheusMiddleware, handle_metrics

from .routers import order

logging.basicConfig(encoding='utf-8', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__file__)

app = FastAPI(
    title='Your Fruit Self Service',
    version='1.0.0',
    description='Order your fruits here',
    root_path=''
)

app.add_middleware(
    PrometheusMiddleware,
    app_name=__name__,
    group_paths=True
)

app.add_route('/metrics', handle_metrics)
app.include_router(order.router)


@app.get('/', status_code=HTTPStatus.OK)
async def root() -> Dict[str, str]:
    """
    Endpoint for basic connectivity test.
    """
    logger.info('root called')
    return {'message': 'I am alive'}
