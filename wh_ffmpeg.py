# -*- coding: utf-8 -*-

import subprocess
import os
import json


class Wh_ffmpeg:

    def __init__(self,file_path):
        self.file_path = file_path
        self.output_forder= file_path + "/tmp"

        self.ffmpeg_path = r"./exec/ffmpeg"
        self.ffprobe_path = r"./exec/ffprobe"

    def file_conv (self,input_filename):
        input_file = self.file_path +"/" + input_filename
        output_file = self.output_forder +"/"+ input_filename


        ffprobe_cmd = self.ffprobe_path + " -v quiet -print_format json -show_format -show_streams %s"%(input_file)
        file_info = subprocess.check_output(ffprobe_cmd).decode('utf-8')
        file_info_json = json.loads(file_info)
        if int(file_info_json['format']['bit_rate']) < 4000000:
            print(file_info_json['format']['bit_rate'])
            pass
        else:
            # print(file_info_json['format']['bit_rate'])
            if os.path.isdir(self.output_forder):
                pass
            else:
                os.mkdir(self.output_forder)

            ffmpeg_cmd = self.ffmpeg_path +" -i %s -b:v 4000000 -maxrate 4000000 -bufsize 4000000 -y %s"%(input_file,output_file)
            subprocess.call(ffmpeg_cmd)


# test = Wh_ffmpeg("Z:\\Animation_Thumbnail")
# test2 = test.file_conv("big_s0010_c0020_anim_v001.mp4.jpg")
# test3 = test2['format']['bit_rate']
# print(test3)