
import logging
from functools import lru_cache

from pydantic_settings import BaseSettings


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = 0

# LRU Cache 是什麼？
# lru_cache 是 Python 內建標準函式庫 functools 模組提供的一個裝飾器 (Decorator)。
# •	Cache (快取)：它的核心功能是將函式的「執行結果」暫存到記憶體中。如果下次呼叫該函式時傳入的參數一模一樣，它就會直接回傳暫存的結果，而不會重新執行函式內部的程式碼。
# •	LRU (Least Recently Used)：這是一種快取淘汰策略，意思是「最近最少使用」。當快取的記憶體空間達到上限時，它會自動清除掉最久沒有被使用到的暫存資料（不過在載入設定檔的這個情境中，我們通常不會遇到快取塞滿的問題）。
@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()