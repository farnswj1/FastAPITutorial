from fastapi import APIRouter, WebSocket, WebSocketDisconnect


router = APIRouter(prefix='/ws', tags=['Websockets'])


@router.websocket('/example')
async def websocket_example(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f'Message text was: {data}')
    except WebSocketDisconnect:
        pass
    else:
        await websocket.close()
