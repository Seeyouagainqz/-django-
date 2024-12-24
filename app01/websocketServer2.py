import docker
import asyncio
import websockets
import os,pty, subprocess



async def handle_websocket(websocket, path):
    client = docker.from_env()
    # Start a new exec instance in the container  在容器中创建一个新的命令执行实例
    exec_instance = client.api.exec_create(
        container='a691e38d3358d4e1711b87d313567fd43f17fe9ecb91550b7716e617b654394e',
        cmd=['/bin/sh'],  # or any shell you want to use
        tty=True,
        stdin=True,
        stdout=True,
        stderr=True
    )

    client.api.exec_start(exec_instance['Id'], detach=True, stream=False) # 启动这个运行执行实例

    master_fd, slave_fd = pty.openpty()
    process = subprocess.Popen(
        ['docker', 'exec', '-it', 'a691e38d3358d4e1711b87d313567fd43f17fe9ecb91550b7716e617b654394e', '/bin/sh'],
        stdin=slave_fd, stdout=slave_fd, stderr=slave_fd
    )

    try:
        while True:
            # Read from WebSocket
            command = await websocket.recv()
            os.write(master_fd, command.encode())

            # Read from Docker container
            output = os.read(master_fd, 1024).decode()
            await websocket.send(output)
    except Exception as e:
        print(f"Connection error: {e}")
    finally:
        process.terminate()
        process.wait()


start_server = websockets.serve(handle_websocket, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
