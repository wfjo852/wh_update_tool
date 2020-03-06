# -*- coding: utf-8 -*-

import os


class File_import:

    def __init__(self, file_path):#특정 폴더 지정
        self.file_path = file_path

    def file_endswith(self,end_swith):#끝문자를 기준으로 필터링
        if os.path.isdir(self.file_path):
            file_list_dir = os.listdir(self.file_path)
            file_list =[file for file in file_list_dir if file.endswith(end_swith)]
            if len(file_list) == 0:
                print('해당하는 파일이 없습니다. 확장자를 다시 확인해 주세요')
                return file_list
            else:
                return file_list
        else:
            print("is not directory")

    def filename_conventions(self, file_name, split_str):#버전네임 기준으로 샷정보 출력
        file_split = file_name.split(split_str)
        project_name = file_split[0]
        episode_name = ""
        sequence_name = file_split[1]
        shot_name = file_split[1]+"_"+file_split[2]
        task_name = file_split[3]
        file_info = {"filename":file_name,
                     "file_path": self.file_path,
                     "project":project_name,
                     "episode":episode_name,
                     "sequence":sequence_name,
                     "shot":shot_name,
                     "task":task_name}
        return file_info

