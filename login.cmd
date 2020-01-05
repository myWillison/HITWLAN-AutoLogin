@echo off

REM 获取name of 当前连接的WLAN
set x=None
@for /f "tokens=1,2,3" %%i in ('netsh WLAN show interfaces') do (
if [%%i]==[SSID] set x=%%k
)

REM 若未连接校园网则先连接
if %x%==HIT-WLAN (
    echo Connected to HIT-WLAN
) else (
    netsh wlan connect name=HIT-WLAN
)

REM 在当前目录运行python文件，可修改路径
cd %~sdp0
python login.py
pause