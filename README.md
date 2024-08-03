# RevPi DIO Module API
- app: falcon api (python)

## Aditional Documentation:
- [Google Drive Dastions](https://drive.google.com/drive/folders/1honehxIuXjCowpb9NmtajVL2zvVSq0VC)
## Requirements
- RevPi Core 3 + Module DIO
- Python3 (falcon)
- [revpimodio2](https://revpimodio.org/en)

**Directories and Files ENV Must have**
- `~venv/` - Python env

```
$ sudo apt-get install python3-venv
$ python3 -m venv {path}/revpi-dio-server/venv/
$ venv/bin/pip3 install -r requirements.txt
```

## Run API
```
$ gunicorn router:api
```

## Methods:
- `GET /api/inputs`
- `GET /api/outputs`
- `POST /api/outputs/:id/`
- `POST /api/outputs`

**Header:**
```
Content-Type: application/json
'X-API-KEY': 'YOUR-API-KEY-TOKEN'
```

**Body:**
```
{
	"outputs": {
        "id": "O_1"
		"value": 0 or 1
	}
}
```

**Respone:**
```
{
    
}
```

**Errors Respone:**


## Add api as a Systemd service
[Font resources](https://www.digitalocean.com/community/tutorials/how-to-deploy-falcon-web-applications-with-gunicorn-and-nginx-on-ubuntu-16-04)
`/etc/systemd/system/revpi-dio-server.service`
Application Path: `/home/.../revpi-dio-server/`

- **Edit System File**
```
[Unit]
Description=Gunicorn instance to serve the revpi-dio API
After=network.target
[Service]
User=<customer>
Group=www-data
PIDFile=/tmp/gunicorn.pid
Environment="PATH=/home/<customer>/mauri/revpi-dio-server/venv/bin"
WorkingDirectory=/home/<customer>/mauri/revpi-dio-server
ExecStart=/home/<customer>/mauri/revpi-dio-server/venv/bin/gunicorn --workers 1 -b 0.0.0.0:8000 router:api
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID
[Install]
WantedBy=multi-user.target
```

- **Handle Service**
```
$ systemctl daemon-reload
==== AUTHENTICATING FOR org.freedesktop.systemd1.reload-daemon ===
Password:
==== AUTHENTICATION COMPLETE ===
$ sudo systemctl stop revpi-dio-server.service
$ sudo systemctl start revpi-dio-server.service
$ sudo systemctl enable revpi-dio-server.service
$ sudo systemctl restart revpi-dio-server.service
$ sudo systemctl status revpi-dio-server.service
● revpi-dio-server.service - Gunicorn instance to serve the revpi-dio API LCR MAURI
     Loaded: loaded (/etc/systemd/system/revpi-dio-server.service; enabled; vendor preset: enabled)
     Active: active (running) since Fri 2021-06-25 11:55:47 CEST; 2s ago
   Main PID: 24868 (gunicorn)
      Tasks: 3 (limit: 9173)
     Memory: 30.2M
     CGroup: /system.slice/revpi-dio-server.service
             └─24872 gunicorn --workers 1 -b 0.0.0.0:8000 router:api

[INFO] Booting worker with pid: 24872

```
