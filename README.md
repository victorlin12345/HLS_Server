# HLS Server

## Framework : Flask

## Process : 
- ffmpeg convert mp4 to m3u8, ts

```
python3 preprocessing.py
```

- HLS Server communicate with FrontEnd HLS video palyer

```
python3 server.py
```