# -*- coding: utf-8 -*-

import requests
import hashlib
import base64
import json
from wh_ffmpeg import Wh_ffmpeg


class Wh_api:
    def __init__(self, wh_url, user_id, user_pw):
        self.wh_url = wh_url

        # 웜홀 API URI 세팅
        whtoken_api = "/api/user/auth"  # 웜홀2 API 상세.
        login_api_url = self.wh_url + whtoken_api

        # 파라미터 확인
        origin_server = self.wh_url
        outside = "0"

        # 비밀번호 추가 세팅 - 이용자가 입력한 비밀번호를 sha256 해시 후 base64 인코딩 함
        user_pw = user_pw.encode("utf-8")
        user_pw_hashed = hashlib.sha256(user_pw).hexdigest()
        user_pw_hashed = user_pw_hashed.encode("utf-8")
        user_pw_encoded = base64.b64encode(user_pw_hashed)

        # 파라미터 세팅
        data = {"userid": user_id, "userpw": user_pw_encoded, "origin_server": origin_server,
                "outside": outside}

        # API 호출
        login_result = requests.post(login_api_url, data=data)

        # 결과 확인 / 토큰 획득
        if login_result.status_code == 200:
            login_result_json = json.loads(login_result.text)
            whtoken = login_result_json["data"]["token"]
            # print(whtoken)

            # 파라미터 세팅
            # whtoken = "eyaoiasddkaso.asodkaosd.asodoasdoas" # 로그인 API 를 통해 얻은 token 값
            self.cookies = {"whtoken": whtoken}
            # print(whtoken)
            print('login success')

        else:
            print("login fail")
            # 토큰 획득 실패한 경우

    # 웜홀과 버전리스트의 데이터 비교
    def compare_data(self, version_list):
        self.ver_project = version_list['project']
        self.ver_episode = version_list['episode']
        self.ver_sequence = version_list['sequence']
        self.ver_shot = version_list['shot']
        self.ver_task = version_list['task']

        # 형식
        # version_list = {"filename": file_name,
        #              "file_path": file_path(filename 빠져있음),
        #              "project": project_name,
        #              "episode": episode_name,
        #              "sequence": sequence_name,
        #              "shot": shot_name,
        #              "task": task_name}
        wh_ffmpeg = Wh_ffmpeg(version_list['file_path'])
        input_filename = version_list['filename']

        project = self.project_list()

        if self.ver_project in project.keys():
            episode = self.episode_list(self.ver_project)

            if self.ver_episode in episode.keys():
                sequence = self.sequence_list(self.ver_episode)

                # Sequence 유무 확인 및 생성
                if self.ver_sequence in sequence.keys():
                    shot = self.shot_list(self.ver_sequence)
                else:
                    self.sequence_create(self.ver_sequence)
                    shot = self.shot_list(self.ver_sequence)

                # Shot 유무 확인 및 생성
                if self.ver_shot in shot.keys():
                    task = self.shot_task_list(self.ver_shot)
                else:
                    self.shot_create(self.ver_shot)
                    task = self.shot_task_list(self.ver_shot)

                # Task 유무 확인 및 생성
                if self.ver_task in task.keys():
                    self.track_version_list()
                    print(str(version_list) + ' version upload')
                else:
                    self.shot_task_create(self.ver_task)
                    print(str(version_list) + ' 생성  후 version upload')

            else:
                print('선택한 에피소드가 없습니다.')

        else:
            print("프로젝트가 없습니다.")

    # Global setting
    def shot_tasktype_list(self):
        api = "/api/tasktype/shot/list"
        api_url = self.wh_url + api

        # 결과 호출
        result = requests.get(api_url, cookies=self.cookies)

        # 결과 확인
        if result.status_code == 200:
            json_list = json.loads(result.text)
            self.shot_tasktype_idx_list = {x['tasktype_name']: x['tasktype_idx'] for x in
                                           json_list['data']['tasktypes']}
            return self.shot_tasktype_idx_list
        else:
            self.shot_tasktype_idx_list = {"": ""}
            print("No Shot_tsktype")
            return self.shot_tasktype_idx_list

    def wh_system_version(self):
        api = "/api/setting/system/version/read"
        api_url = self.wh_url + api

        # 결과 호출
        result = requests.get(api_url, cookies=self.cookies)

        # 결과 확인
        if result.status_code == 200:
            json_list = json.loads(result.text)
            self.wh_system_ver = json_list['data']
            # print(self.wh_system_ver)
            return self.wh_system_ver
        else:
            self.wh_system_ver = {"": ""}
            print("No wh_system_ver")
            return self.wh_system_ver

    def db_check(self):
        api = "/api/setting/db/check"
        api_url = self.wh_url + api

        # 결과 호출
        result = requests.post(api_url, cookies=self.cookies)

        # 결과 확인
        if result.status_code == 200:
            return "DB_update_done"
        else:
            return "DB_update_error"


    # 조회 API  순서대로 조회해야함
    def project_list(self, finished=""):
        # finished = '1' 끝난 프로젝트도 조회

        api = "/api/project/list"
        api_url = self.wh_url + api

        # param
        data = {"including_finished": finished, "all": "1"}

        # api호출
        result = requests.get(api_url, data=data, cookies=self.cookies)

        # 결과 확인
        if result.status_code == 200:
            json_list = json.loads(result.text)
            self.project_idx_list = {x['name']: x['project_idx'] for x in json_list['data']['projects']}
            return self.project_idx_list
        else:
            self.project_idx_list = {"": ""}
            print("No Project_list")
            return self.project_idx_list

    def episode_list(self, project_name):
        # 프로젝트 조합
        self.project_idx = self.project_idx_list[project_name]

        api = "/api/project/%s/episode/list" % (self.project_idx)
        api_url = self.wh_url + api

        # param
        data = {"project_idx": self.project_idx}

        # api호출
        result = requests.get(api_url, data=data, cookies=self.cookies)
        json_list = json.loads(result.text)

        # 결과 확인
        if result.status_code == 200 and str(json_list['data']['episodes']) != 'None:':
            self.episode_idx_list = {x['name']: x['episode_idx'] for x in json_list['data']['episodes']}
            return self.episode_idx_list
        else:
            self.episode_idx_list = {"": ""}
            print("No Episode_list")
            return self.episode_idx_list

    def sequence_list(self, episode_name):
        # 사용하려는 에피소드이름의 idx추출

        self.episode_idx = self.episode_idx_list[episode_name]

        api = "/api/project/%s/episode/%s/sequence/list" % (self.project_idx, self.episode_idx)
        api_url = self.wh_url + api

        # param
        data = {"project_idx": self.project_idx, "episode_idx": self.episode_idx}

        # api호출
        result = requests.get(api_url, data=data, cookies=self.cookies)
        json_list = json.loads(result.text)

        # 결과 확인
        if result.status_code == 200 and str(json_list['data']['sequences']) != 'None':

            self.sequence_idx_list = {x['name']: x['sequence_idx'] for x in json_list['data']['sequences']}
            return self.sequence_idx_list

        else:
            self.sequence_idx_list = {"": ""}
            print(episode_name + " No Sequence_list")
            return self.sequence_idx_list

    def shot_list(self, sequence_name):
        # 사용하려는 시퀀스이름의 idx추출

        self.sequence_idx = self.sequence_idx_list[sequence_name]

        api = "//api/project/%s/episode/%s/sequence/%s/shot/list" % (
        self.project_idx, self.episode_idx, self.sequence_idx)
        api_url = self.wh_url + api

        # param
        data = {"project_idx": self.project_idx, "episode_idx": self.episode_idx, "sequence_idx": self.sequence_idx}

        # api호출
        result = requests.get(api_url, data=data, cookies=self.cookies)
        json_list = json.loads(result.text)

        # 결과 확인
        if result.status_code == 200 and str(json_list['data']['shots']) != 'None':

            self.shot_idx_list = {x['name']: x['shot_idx'] for x in json_list['data']['shots']}
            return self.shot_idx_list

        else:
            self.shot_idx_list = {"": ""}
            print(sequence_name + " No Shot_list")
            return self.shot_idx_list

    def shot_task_list(self, shot_name):
        # 사용하려는 샷이름의 idx추출

        self.shot_idx = self.shot_idx_list[shot_name]

        api = "/api/project/%s/shot/%s/task/list" % (self.project_idx, self.shot_idx)
        api_url = self.wh_url + api

        # param
        data = {"project_idx": self.project_idx, "shot_idx": self.shot_idx}

        # api호출
        result = requests.get(api_url, data=data, cookies=self.cookies)
        json_list = json.loads(result.text)
        # 결과 확인
        if result.status_code == 200 and str(json_list['data']['tasks']) != 'None':
            self.task_idx_list = {x['tasktype_name']: x['task_idx'] for x in json_list['data']['tasks']}
            return self.task_idx_list

        else:
            self.task_idx_list = {"": ""}
            print(shot_name + " No Task_list")
            return self.task_idx_list

    def track_version_list(self):

        api = "/api/project/%s/track/version/read" % (self.project_idx)
        api_url = self.wh_url + api

        # param
        data = {"project_idx": self.project_idx}

        # api호출
        result = requests.get(api_url, data=data, cookies=self.cookies)
        json_list = json.loads(result.text)
        print(result)
        # 결과 확인
        if result.status_code == 200 and str(json_list['data']['track']) != 'None':
            self.track_version_idx_list = {x['version_name']: x['idx'] for x in json_list['data']['track']}
            print(self.track_version_idx_list)
            return self.track_version_idx_list

        else:
            self.task_idx_list = {"": ""}
            print(" No track_version_list")
            # return self.track_version_idx_list

    # 생성 API
    def sequence_create(self, sequence_name):
        api = "/api/project/%s/episode/%s/sequence/create" % (self.project_idx, self.episode_idx)
        api_url = self.wh_url + api

        # param세팅
        data = {"project_idx": self.project_idx,
                "episode_idx": self.episode_idx,
                "sequence_name": sequence_name,
                "description": sequence_name}

        # api 호출
        result = requests.post(api_url, data=data, cookies=self.cookies)
        if result.status_code == 200:
            # 리스트 다시 조회
            self.sequence_list(self.ver_episode)
            print(sequence_name + ' :sequence_create')
        else:
            print('sequence_create_error')

    def shot_create(self, shot_name):

        api = "/api/project/%s/episode/%s/sequence/%s/shot/create" % (
        self.project_idx, self.episode_idx, self.sequence_idx)
        api_url = self.wh_url + api

        # param세팅
        data = {"project_idx": self.project_idx,
                "episode_idx": self.episode_idx,
                "sequence_name": self.sequence_idx,
                "shot_name": shot_name,
                "status_idx": 1}

        # api 호출
        result = requests.post(api_url, data=data, cookies=self.cookies)
        if result.status_code == 200:
            # 리스트 다시조회
            self.shot_list(self.ver_sequence)
            print(shot_name + ' :shot_create')
        else:
            print('sequence_create_error')

    def shot_task_create(self, task_name):

        project_tasktype_list = self.project_tasktype_list('shot')
        if task_name in project_tasktype_list.keys():

            api = "/api/project/%s/shot/%s/task/create" % (self.project_idx, self.shot_idx)
            api_url = self.wh_url + api

            # param세팅
            data = {"project_idx": self.project_idx,
                    "shot_idx": self.shot_idx,
                    "tasktype_name": task_name,
                    "status_idx": 1}

            # api 호출
            result = requests.post(api_url, data=data, cookies=self.cookies)
            if result.status_code == 200:
                # 리스트 다시조회
                self.shot_task_list(self.ver_shot)
                print(task_name + ' :task_create')
            else:
                print('task_create_error')

        else:
            print(task_name + ' :Task not allocation to project')

    def version_key_create(self, which, task_name):

        # 사용하려는 Task의 이름 idx조회
        self.task_idx = self.task_idx_list[task_name]

        api = "/api/%s/task/%s/version/setting/create" % (which, self.task_idx)
        api_url = self.wh_url + api

        # param
        data = {"which": which, "task_idx": self.task_idx}

        # api호출
        result = requests.get(api_url, data=data, cookies=self.cookies)
        json_list = json.loads(result.text)
        # 결과 확인
        if result.status_code == 200 and str(json_list['data']['tasks']) != 'None':
            self.version_key = {"version_key": x for x in json_list['data']['version_key']}

        else:
            self.version_key = {"version_key": ""}
            print(task_name + " No version_key")

    def version_setting(self):

        api = '/api/version/setting/read'
        api_url = self.wh_url + api

        # param
        data = {'version_key': self.version_key['version_key']}

        # api호출
        result = requests.get(api_url, data=data, cookies=self.cookies)
        json_list = json.loads(result.text)

        if result.status_code == 200:
            version_setting = json_list['data']
            return version_setting
        else:
            print('fail to get the version_setting')

    def version_create(self, which, version_list):

        # version_setting
        self.version_key_create(which, version_list['task'])
        version_setting = self.version_setting()

        api = "/api/%s/task/version/create" % (which)

    # project_detail
    def project_tasktype_list(self, which):

        api = "/api/project/%s/tasktype/%s/list" % (self.project_idx, which)
        api_url = self.wh_url + api

        # param
        data = {"project_idx": self.project_idx,
                "which": which}  # shot or asset

        # api호출
        result = requests.get(api_url, data=data, cookies=self.cookies)

        # 결과 확인
        if result.status_code == 200:
            json_list = json.loads(result.text)
            self.project_tasktype_idx_list = {x['tasktype_name']: x['tasktype_idx'] for x in
                                              json_list['data']['tasktypes']}
            return self.project_tasktype_idx_list
        else:
            self.project_tasktype_idx_list = {"": ""}
            print("No Allocation tasktype")
            return self.project_tasktype_idx_list
