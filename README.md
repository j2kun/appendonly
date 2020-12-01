# Appendonly

A dumb webserver that has a single `GET` endpoint `/`, which accepts a single
url param `data`, and appends that string as a single line in a file.

The filename is configured in the environment as `APPENDONLY_FILENAME`.

Run the webserver with `./run.sh`, which spins up a gunicorn WSGI wrapping the
flask app, exposing port 80 on the local network.

## Why

I want a simple webserver to run from my laptop on a local WIFI network,
which I can use to collect sensor data on hobby projects.
