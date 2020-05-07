import os
import ffmpeg_streaming as stm

output_folder = "./hls"

video = stm.input('test.mp4') # Opening a Resource
hls = video.hls(stm.Formats.h264()) # hls_time / second segment duration, 
hls.auto_generate_representations()
if os.path.exists(output_folder):
    hls.output('./hls/test.m3u8')
else:
    os.makedirs(output_folder)
    hls.output('./hls/test.m3u8')
