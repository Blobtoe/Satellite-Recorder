<h1 align="center"> Satellite Recorder </h1>

### **Current Work in Progress**

Satellite Recorder is satellite recording software that is meant to be run on nodes for <a href="https://github.com/Blobtoe/Satellite-Processor">Satellite Processor</a>. It will interface with your SDR and record satellites when the central processing server requests. It works by running a lightweight webserver to allow the processing server to access it, then pipes I/Q data directly to the server.

## Installing
```
# clone this repo
git clone https://github.com/Blobtoe/Satellite-Recorder.git
cd Satellite-Recorder
# assign execution permissions
chmod +x SatelliteRecorder.py
# run Satellite Recorder
./SatelliteRecorder
```

## Upcoming Features
- More SDR support

## Supported SDRs
- RTL-SDR

## External Tools
- **rtl_fm** to interface with RTL-SDR