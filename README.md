svdog
=====

supervisor's dog, should deploy with flylog

example:

    [eventlistener:svdog]
    environment=PYTHON_EGG_CACHE=/tmp/.python-eggs/
    command=/usr/local/bin/run_svdog.py
    user=user_00
    events=PROCESS_STATE_EXITED,PROCESS_STATE_FATAL
    autorestart=true
