# RaspberryPi-E-ink-Display
This is my repository for my raspberry pi system with an e-ink display


### Running python file once device has started running:
Create a service file in /etc/systemd/system/{filename}.service
Service file content example:

[Unit]
Description=Run e-screen module

[Service]
ExecStart=/usr/bin/python3 /home/user/documents/file.py
WorkingDirectory=/home/user/documents
StandardOutput=journal
StandardError=journal
Restart=on-failure
RestartSec=2
User=User
Environment=PYTHONBUFFERED=1

[Install]
WantedBy=multi-user.target