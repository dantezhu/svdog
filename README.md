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
    redirect_stderr=false

注意: 

    supervisor 3.2.0 及之后的版本，开始不允许 eventlistener 类型使用 redirect_stderr=true
