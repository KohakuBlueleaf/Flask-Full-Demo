# Flask-Full-Demo
A full flask project example with jinja2 template/flask/flask-login/Flask-SocketIO

For online demo, click [this](https://flask.amb-ri.com)

---
## Requirements
* Python: 3.10
* Flask: 2.0↑
* System (for dev): Any system that can run python3.10
* System (for deployment): Any Linux distribution or MacOS that can run python3.10 and gunicorn

---
## Run Dev Server
**Ensure You have a MongoDB server running on port 27017 or change the URI in database/db.py**

1. Install the requirements

    ```bash
    python3 -m pip install -r requirement.txt
    ```
2. run the dev.py script.

    ```bash
    python3 dev.py
    ```

And then you will see something like this
```
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 470-377-815
(29532) wsgi starting up on http://127.0.0.1:9999
```

From now, you can access this demo site on http://127.0.0.1:9999 from browser.