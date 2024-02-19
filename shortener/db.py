import asyncio
import asyncpg


async def create_conn(db_url):
    connection = await asyncpg.connect(db_url)
    return connection


async def close_conn(connection):
    if connection:
        await connection.close()


async def add_url(conn, url):
    await conn.execute(
        '''INSERT INTO urls (url)
        VALUES ($1);''', url,
    )
