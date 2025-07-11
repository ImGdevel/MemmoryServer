from fastapi import FastAPI
from src.api.routes import router
from src.api.system_routes import system_router
from src.utils.logger import setup_logging, get_logger, get_uvicorn_custom_log
from src.config.settings import server_config
import uvicorn

# 로깅 설정
setup_logging()

# FastAPI 앱 생성
app = FastAPI(
    title="Memory Server API",
    description="FastAPI와 Qdrant를 사용한 벡터 기반 메모리 서버",
    version="1.0.0"
)

# 라우터 등록
app.include_router(router)
app.include_router(system_router)

logger = get_logger(__name__)

if __name__ == "__main__":
    port = server_config.server_port
    host = server_config.server_host
    
    logger.info(f"서버 시작 중... (Host: {host}, Port: {port})")
    
    uvicorn.run(
        app, 
        host=host, 
        port=port,
        log_config=get_uvicorn_custom_log(),
        access_log=True
    ) 