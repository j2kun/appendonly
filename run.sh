#!/bin/bash

gunicorn -b 0.0.0.0:80 appendonly:app
