#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   settings.py
@Time    :   2024/09/30 10:22:20
@Author  :   CaptainJi 
@Version :   1.0
@Desc    :   None
@Software:   Cursor
"""


import os

from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_file = os.path.join(BASE_DIR, ".env")
env_file_encoding = "utf-8"

logger.add(
    sink=os.path.join(BASE_DIR, "./logs/all.log"),
    enqueue=True,
    rotation="4 weeks",
    retention="4 months",
    encoding="utf-8",
    backtrace=True,
    diagnose=True,
    compression="zip",
    catch=True,
)


class Settings(BaseSettings):
    PROJECT_DIR: str = BASE_DIR
    AGENT_DIR: str = os.path.join(PROJECT_DIR, 'agent')
    DATA_DIR: str = os.path.join(PROJECT_DIR, 'data')
    SCREEN_SHOT_DIR: str = os.path.join(PROJECT_DIR, 'data/imgs')
    MARK_FILE_DIR: str = os.path.join(PROJECT_DIR, 'data/mark')
    DASHSCOPE_API_KEY: str = ''
    OSS_ACCESS_KEY_ID: str = ''
    OSS_ACCESS_KEY_SECRET: str = ''
    OPENAI_API_KEY: str = ''
    CHATGLM_API_KEY: str = ''
    LAZYLLM_OPENAI_API_KEY: str = ''

    model_config = SettingsConfigDict(
        env_file=env_file, env_file_encoding=env_file_encoding
    )


settings = Settings()

if __name__ == '__main__':
    logger.info(BASE_DIR)
    logger.debug('日志测试')
    logger.warning(settings.LAZYLLM_OPENAI_API_KEY)
    logger.error(settings.LAZYLLM_OPENAI_API_KEY)
