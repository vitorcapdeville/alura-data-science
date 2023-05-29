import asyncio
import requests


async def requests_get_async(url: str):
    return await asyncio.to_thread(requests.get, url)


def pegar_cursos() -> list[dict[str, str]]:
    return requests.get("https://www.alura.com.br/api/cursos").json()


async def pegar_detalhe_curso(curso: str) -> dict:
    result = await requests_get_async(
        f"https://www.alura.com.br/api/curso-{curso}"
    )
    return result.json()


async def pegar_detalhes(cursos: list[dict[str, str]]):
    return await asyncio.gather(
        *[pegar_detalhe_curso(curso["slug"]) for curso in cursos]
    )
