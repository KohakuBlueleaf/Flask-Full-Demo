from subprocess import Popen


p_list = []
for port in [8001, 8002, 8003, 8004]:
    p_list.append(
        Popen([
            'gunicorn',
            '-kgeventwebsocket.gunicorn.workers.GeventWebSocketWorker',
            '-w1', f'-b127.0.0.1:{port}', 'main_ws:app'
        ])
    )

p_list.append(
    Popen(['haproxy', '-f', 'haproxy.cfg', '-V'])
)

try:
    input()
finally:
    for process in p_list:
        process.terminate()
        while not process.poll():
            pass
