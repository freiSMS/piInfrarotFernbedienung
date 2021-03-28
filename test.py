import subprocess
rtn = subprocess.call(["irsend", "SEND_ONCE", "Receiver", "KEY_POWER"])
# rtn should equal 0 if command ran without error