from moviepy.editor import *
from PIL import ImageColor, Image, ImageFilter, ImageFont, ImageDraw, ImageEnhance
import PIL
import os
import subprocess
from moviepy.editor import VideoFileClip, concatenate_videoclips

#name of video without .mp4
video_name = "boggy"

#directory to folder with video with \x at the end
start_directory = r"C:\Users\isaac\OneDrive\Desktop\clips\x"
start_directory = start_directory[:-1]

full_directory = start_directory + video_name + ".mp4"

print(full_directory)

my_video = VideoFileClip(full_directory)
my_video = my_video.resize(0.54)

my_video.write_videofile("nukedmovie.mp4")
 

