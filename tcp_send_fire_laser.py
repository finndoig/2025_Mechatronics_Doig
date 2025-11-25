"""
TCP send helper for firing laser (refactored)

Provides a callable function `send_fire_signal(value, host, port, repeat=1, delay=0.0)`
which sends the bytes [0,1] when `value` is truthy and [0,0] when falsy.

When run as a script it accepts a single argument `on|off` to test sending.
"""

import socket
import time
import logging
from typing import Union

logging.basicConfig(level=logging.INFO)

# default server settings (can be overridden when calling the function)
DEFAULT_TCP_IP = "138.38.227.166"
DEFAULT_TCP_PORT = 25000


def send_fire_signal(value: Union[bool, int]) -> bool:
    """Send a fire signal over TCP.

    Only a single argument is required:
      - value: truthy -> send [0,1], falsy -> send [0,0]

    All other parameters (host, port, repeat, delay, timeout) are defined
    inside the function and can be adjusted here if needed.

    Returns True on success, False on error.
    """
    # First we import our libraries
    import socket
    import time
    import logging
    from typing import Union
    
    # internal configuration (change here if needed)
    host = "138.38.227.166" # This is the IP address of the machine that the data will be send to
    port = 25000 # This is the REMOTE port of the Server that we are sending the data to
    repeat = 1 # number of times to repeat sending
    delay = 0.0 # delay between repeats in seconds
    timeout = 2.0 # socket timeout in seconds

    data_on = bytes([0, 1])
    data_off = bytes([0, 0])
    payload = data_on if bool(value) else data_off

    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        logging.info("Creating socket and connecting to %s:%d", host, port)
        s.connect((host, port))

        for i in range(repeat):
            logging.debug("Sending payload %s (attempt %d/%d)", payload, i + 1, repeat)
            s.sendall(payload)
            if delay and i < repeat - 1:
                time.sleep(delay)

        logging.info("Sent %d message(s) to %s:%d", repeat, host, port)
        return True
    except Exception as exc:
        logging.exception("Failed to send fire signal: %s", exc)
        return False
    finally:
        if s:
            try:
                s.close()
            except Exception:
                pass

send_fire_signal(True)