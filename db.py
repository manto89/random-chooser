import asyncio
import psycopg

from typing import Optional

from psycopg_pool import AsyncConnectionPool, AsyncNullConnectionPool

class Db: 
    _pool = Optional[AsyncConnectionPool]

    def __init__(self) -> None:
        self.conninfo = "postgresql://postgres:postgres@localhost:5432/postgres"
        self._pool = None
        pass

    async def get_pool(self):
        conn_dict =  psycopg.conninfo.conninfo_to_dict(self.conninfo)
        print(str(conn_dict))
        pool = AsyncConnectionPool(self.conninfo)
        await pool.open(wait=True)
        return pool
        # return AsyncConnectionPool(self.conninfo)

    def init_pool(self):
        pool = self.get_pool
        pool = asyncio.run(self.get_pool())
        self._pool = pool

    async def get_random_items(self):
        ret = []
        async with self._pool.connection() as conn:
            async with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
                await cur.execute("SELECT * FROM items")
                items = await cur.fetchall()
                for record in items:
                    ret.append(record)
                    print(record)
        return ret
