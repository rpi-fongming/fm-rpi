_IP=$(hostname -I) || true
_HOST=$(hostname) || true
/etc/rpi-event/systemLog.py $_HOST:$_IP "rc.local"
