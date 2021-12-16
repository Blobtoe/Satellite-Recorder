#!/usr/bin/env python3

from bottle import post, run, request, response, get
import os
from datetime import datetime
import json
import threading

is_recording = False
recording_start = None
recording_duration = None

def log(msg):
    print(datetime.now().strftime("%Y %b. %m %H:%M:%S"), ":", str(msg))

def get_config():
    with open("config.json") as f:
        return json.loads(f.read())

# connects to the netcat pipe and stream the rtl_fm data to the server
def start_pipe(command):
    global is_recording, recording_start, recording_duration
    is_recording = True
    recording_start = datetime.now()
    log("starting pipe")
    log(command)
    os.system(command)
    log("closing pipe")
    is_recording = False
    recording_start = None
    recording_duration = None

# parses the recording command and starts the netcat pipe
@post("/record")
def record():
    global recording_duration
    if not all(parameter in ["center_frequency", "samplerate", "format", "duration", "gain"] for parameter in request.json.keys()):
        log("Not all necessary parameters given.")
        response.status = 400
        return "Not all necessary parameters given"
    
    params = request.json
    recording_duration = params['duration']
    server_ip = get_config()["server_ip"]
    pipe_port = get_config()["pipe_port"]
    threading.Thread(target=start_pipe, args=(f"timeout {params['duration']} rtl_fm -M {params['format']} -s {params['samplerate']} -f {params['center_frequency']} -g {params['gain']} - | nc -q 1 {server_ip} {pipe_port}", )).start()
    return

#gets the status of the recording
@get("/status")
def status():
    if is_recording:
        recording_progress = (datetime.now() - recording_start).total_seconds() / recording_duration
    else:
        recording_progress = None
    
    response.content_type = "application/json"
    return json.dumps({"is_recording": is_recording, "recording_progress": recording_progress})

run(host="localhost", port=8000, debug=True)