# import asyncio
# import logging
# import uvicorn
# from app import app as app_fastapi
# from scheduler import app as app_rocketry
#
#
# class Server(uvicorn.Server):
#
#
#     def handle_exit(self, sig: int, frame) -> None:
#         app_rocketry.session.shut_down()
#         return super().handle_exit(sig, frame)
#
#
# async def main():
#     server = Server(config=uvicorn.Config(app_fastapi, workers=1, loop="asyncio", port=3000))
#     api = asyncio.create_task(server.serve())
#     schedule = asyncio.create_task(app_rocketry.serve())
#     await asyncio.wait([schedule, api])
#
# print(__name__)
# if __name__ == "__main__":
#     logger = logging.getLogger("rocketry.task")
#     logger.addHandler(logging.StreamHandler())
#     asyncio.run(main())

import uvicorn

if __name__ == '__main__':
    uvicorn.run('app:app', host="0.0.0.0", port=8000, reload=True)
