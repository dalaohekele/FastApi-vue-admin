import os
from typing import Optional, Dict
from pathlib import Path

from pydantic import BaseSettings


class APISettings(BaseSettings):
    # 开发模式配置
    DEBUG: bool = os.environ.get('DEBUG', True)
    # 项目文档
    TITLE: str = "FastAPI+VUE 后管项目 "
    DESCRIPTION: str = "FastAPI 基于 Tortoise-orm 实现的项目框架"
    # 文档地址 默认为docs
    DOCS_URL: str = "/openapi/docs"
    # 文档关联请求数据接口
    OPENAPI_URL: str = "/openapi/openapi.json"
    # redoc 文档
    REDOC_URL: Optional[str] = "/openapi/redoc"

    # token过期时间 分钟
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # 生成token的加密算法
    ALGORITHM = os.environ.get('ALGORITHM')

    # 生产环境保管好 SECRET_KEY
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # 项目根路径
    BASE_PATH = Path(__file__).resolve().parent.parent

    # 权限控制配置
    CASBIN_MODEL_PATH = BASE_PATH.joinpath('config/rbac_model.conf')

    # 数据库连接配置
    DATABASE_URI = os.environ.get('DATABASE_URI')

    # 数据库配置
    DATABASE_CONFIG: Dict = {
        'connections': {
            'default': DATABASE_URI
        },
        'apps': {
            'models': {
                # 设置key值“default”的数据库连接
                'default_connection': 'default',
                'models': ['model.system.user', 'model.system.menu','casbin_tortoise_adapter']
            }
        },
        "routers": ["db_router.Router"],
        'use_tz': False,
        'timezone': 'Asia/Shanghai'
    }

    # redis配置
    REDIS_HOST: str = "127.0.0.1"
    REDIS_PASSWORD: str = ""
    REDIS_DB: int = 0
    REDIS_PORT: int = 6379
    REDIS_URL: str = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}?encoding=utf-8"
    REDIS_TIMEOUT: int = 5  # redis连接超时时间

    # 不需要登录认证的 API
    NO_VERIFY_URL: Dict = {
        "/": "eq",  # 根目录
        "openapi": "in",  # 开发 API
        "/user/login": "in",  # 登录
        "/user/register": "in",  # 注册
        "/ws/": "in"  # ws 服务不需要登录
    }


settings = APISettings()
