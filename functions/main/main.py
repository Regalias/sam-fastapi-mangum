from aws_lambda_powertools import Tracer, Logger
from mangum import Mangum
from api.routes import app

logger = Logger()
tracer = Tracer()

handler = Mangum(app=app, api_gateway_base_path='/v2', lifespan='off')

@logger.inject_lambda_context
@tracer.capture_lambda_handler
def lambda_handler(event, context):
    client_ip = event.get("requestContext", {}).get("http", {}).get("sourceIp")
    logger.info(f"Processing request from {client_ip}")
    return handler(event, context)