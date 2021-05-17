#!-*-coding:utf-8-*-

from src.config import CACHE_EXPTIME
from src.cache.icache import ICache


class NoCache(ICache):

    def client(self) -> object:
        return None

    async def get(self, key: bytes) -> bytes:
        return None

    async def set(self, key: bytes, val: bytes, exptime: int = CACHE_EXPTIME):
        return None

    async def delete(self, key: bytes) -> object:
        return None