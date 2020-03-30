# -*- coding: utf-8 -*-

import wormhole_update_ui
import sys
import wh_ssh, wh_api
import webbrowser

# global wormhole_directory
# global wh_system_version
# global update_forder_name
# global wh_sdk
# global ssh_manager

update_forder_check = "wh2web"

# class 호출
update_ui = wormhole_update_ui.Ui_wormhole_update_tool()
ssh_manager = wh_ssh.SSHManager()

# 웜홀 업데이트 UI 오브젝트 세팅
app = wormhole_update_ui.QApplication(sys.argv)
wormhole_update_tool = wormhole_update_ui.QDialog()


#setup_Ui init
update_ui.setupUi(wormhole_update_tool)


#빌드날짜 번인
update_ui.build_date.setText(wormhole_update_ui.QCoreApplication.translate("wormhole_update_tool", u"Update Tool Build Date: 2020/03/25", None))


def ssh_login_enable():
    if update_ui.input_host.text() \
            and update_ui.input_port.text() \
            and update_ui.input_id.text() \
            and update_ui.input_pw.text() != "":
        update_ui.pushb_server_login.setEnabled(True)
    else:
        update_ui.pushb_server_login.setEnabled(False)


def http_login_enable():
    if update_ui.input_host.text() \
            and update_ui.input_http_port.text() \
            and update_ui.input_http_id.text() \
            and update_ui.input_http_pw.text() != "":
        update_ui.pushb_http_login.setEnabled(True)
    else:
        update_ui.pushb_http_login.setEnabled(False)


def ssh_login():
    global wormhole_directory
    update_ui.pushb_server_login.setEnabled(False)
    update_ui.pushb_server_login.repaint()

    host = update_ui.input_host.text()
    port = update_ui.input_port.text()
    id = update_ui.input_id.text()
    pw = update_ui.input_pw.text()
    print(host, port, id + " ssh_connecting.....")

    # ssh.create_ssh_client(host, port, id, pw)
    try:
        ssh_manager.create_ssh_client(host, port, id, pw)
    except:
        ssh_manager.close_ssh_client()
        update_ui.textb_log.setText("SSH Connect Error")

    call = ssh_manager.send_command('find / -name wh2-challenger-deploy')
    # 결과 값 정리
    if len(call) == 1:
        wormhole_directory = call[0]
        update_ui.textb_log.setText('웜홀 설치 경로는 아래와 같습니다. \n ' + wormhole_directory)

        # SSH 접속 성공시 입력창 비활성화
        update_ui.input_host.setEnabled(False)
        update_ui.input_port.setEnabled(False)
        update_ui.input_id.setEnabled(False)
        update_ui.input_pw.setEnabled(False)
        update_ui.pushb_server_login.setEnabled(False)

        # SSH 접속 성공시 HTTP 입력창 활성화
        update_ui.input_http_port.setEnabled(True)
        update_ui.input_http_id.setEnabled(True)
        update_ui.input_http_pw.setEnabled(True)





    else:
        update_ui.textb_log.setText("웜홀의 설치 경로를 찾을 수 없습니다. \n 수동으로 업데이트 해야합니다.")
        update_ui.pushb_server_login.setEnabled(True)


def http_login():
    global wh_system_version
    global wh_sdk

    url = 'http://' + update_ui.input_host.text() + ":" + update_ui.input_http_port.text()
    id = update_ui.input_http_id.text()
    pw = update_ui.input_http_pw.text()

    wh_sdk = wh_api.Wh_api(url, id, pw)

    try:
        wh_system_version = wh_sdk.wh_system_version()
    except:
        update_ui.wh_version.setText(
            wormhole_update_ui.QCoreApplication.translate("wormhole_update_tool", u"Sign_in Error", None))

        # 웜홀 http로그인 실패시 Wormhole server start만 활성화
        update_ui.pushb_wh_status_start.setEnabled(True)
        update_ui.pushb_wh_status_stop.setEnabled(False)

        return

    # 상단레이블 웜홀 버전 기록
    update_ui.wh_version.setText(wormhole_update_ui.QCoreApplication.translate("wormhole_update_tool",
                                                                               u"Current Version : " +
                                                                               wh_system_version['version'] +
                                                                               "\nLast Update_time : " +
                                                                               wh_system_version['updated_time'], None))

    # 로그인 성공시 입력 창 비활성화
    update_ui.input_host.setEnabled(False)
    update_ui.input_http_port.setEnabled(False)
    update_ui.input_http_id.setEnabled(False)
    update_ui.input_http_pw.setEnabled(False)
    update_ui.pushb_http_login.setEnabled(False)

    # 파일업로드 활성화
    update_ui.input_update_file_path.setEnabled(True)
    update_ui.toolb_find_file.setEnabled(True)

    # 웜홀 홈페이지 오픈 활성화
    update_ui.pushb_wormhole_hompage.setEnabled(True)

    # Wormhole Server stop 활성화
    update_ui.pushb_wh_status_stop.setEnabled(True)


def find_directory():
    global update_forder_name
    update_forder_name = wormhole_update_ui.QFileDialog.getExistingDirectory()
    print("update_forder : " + update_forder_name)

    wh2web_check = update_forder_name.split("/")
    if wh2web_check[-1] == update_forder_check:
        update_ui.input_update_file_path.setText(update_forder_name)
        update_ui.pushb_wh_update.setEnabled(True)
    else:
        update_ui.input_update_file_path.setText(update_forder_check + " 폴더를 선택해 주세요.")


def wormhole_update():
    global wormhole_directory
    global update_forder_name
    global wh_sdk

    # 버튼 잠금
    update_ui.pushb_wh_update.setEnabled(False)
    update_ui.pushb_wh_update.repaint()

    # 시스템 메시지 출력
    update_ui.textb_log.setText('웜홀을 업데이트 중입니다. \n 프로그램을 끄지 말아주세요.')
    update_ui.input_update_file_path.repaint()

    # Wh2web폴더 서버로 업로드
    remote_path = wormhole_directory.split()
    remote_path = remote_path[0] + "/"
    print(update_forder_name, ">>>copy>>>>", remote_path)
    ssh_manager.send_directory(update_forder_name, remote_path)

    # 웜홀 DB업데이트
    wh_sdk.db_check()

    update_ui.textb_log.setText('웜홀을 업데이트가 완료되었습니다.')
    update_ui.input_update_file_path.setText('update_done')
    update_forder_name = ""
    update_ui.input_update_file_path.setEnabled(False)
    update_ui.toolb_find_file.setEnabled(False)


def homepage_open():
    url = "http://" + update_ui.input_host.text() + ":" + update_ui.input_http_port.text()
    webbrowser.open(url)


def reset():
    update_ui.input_host.setEnabled(True)
    update_ui.input_port.setEnabled(True)
    update_ui.input_id.setEnabled(True)
    update_ui.input_pw.setEnabled(True)

    update_ui.input_http_port.setEnabled(False)
    update_ui.input_http_id.setEnabled(False)
    update_ui.input_http_pw.setEnabled(False)
    update_ui.pushb_http_login.setEnabled(False)

    update_ui.pushb_server_login.setEnabled(False)

    update_ui.input_update_file_path.setEnabled(False)
    update_ui.toolb_find_file.setEnabled(False)
    update_ui.pushb_wh_update.setEnabled(False)

    update_ui.pushb_wormhole_hompage.setEnabled(False)

    update_ui.pushb_wh_status_start.setEnabled(False)
    update_ui.pushb_wh_status_stop.setEnabled(False)

    update_ui.input_host.setText("")
    update_ui.input_pw.setText("")
    update_ui.input_http_pw.setText("")
    update_ui.input_update_file_path.setText(update_forder_check + " 폴더를 선택해 주세요.")
    update_ui.textb_log.setText("")
    update_ui.wh_version.setText(
        wormhole_update_ui.QCoreApplication.translate("wormhole_update_tool", u"Before connecting to the Wormhole",
                                                      None))


def wh_server_start():
    global wormhole_directory
    update_ui.pushb_wh_status_start.setEnabled(False)
    update_ui.pushb_wh_status_start.repaint()
    update_ui.pushb_wh_status_stop.setEnabled(True)
    update_ui.pushb_wh_status_stop.repaint()
    update_ui.textb_log.setText('웜홀 서버를 시작 하는 중입니다.\n Wormhole update tool을 끄지마세요.')
    update_ui.textb_log.repaint()

    cd_comment = 'cd %s\n' \
                 'docker-compose up -d' % (wormhole_directory)
    ssh_manager.send_command(cd_comment)
    update_ui.textb_log.setText('Wormhole server start')


def wh_server_stop():
    global wormhole_directory
    update_ui.pushb_wh_status_start.setEnabled(True)
    update_ui.pushb_wh_status_start.repaint()
    update_ui.pushb_wh_status_stop.setEnabled(False)
    update_ui.pushb_wh_status_stop.repaint()
    update_ui.textb_log.setText('웜홀 서버를 종료 하는 중입니다.\n Wormhole update tool을 끄지마세요.')
    update_ui.textb_log.repaint()

    cd_comment = 'cd %s\n' \
                 'docker-compose down' % (wormhole_directory)
    ssh_manager.send_command(cd_comment)
    reset()
    update_ui.textb_log.setText('wormhole server Stop')


# ssh_접속 정보 기본값 설정
# update_ui.input_host.setText("211.60.77.119")
update_ui.input_port.setText("22")
update_ui.input_id.setText("root")
# update_ui.input_pw.setText("c2monster")


# SSH_로그인 버튼 활성화
update_ui.input_host.editingFinished.connect(ssh_login_enable)
update_ui.input_port.editingFinished.connect(ssh_login_enable)
update_ui.input_id.editingFinished.connect(ssh_login_enable)
update_ui.input_pw.textChanged.connect(ssh_login_enable)

# SSH_비밀번호 안보이도록 처리
update_ui.input_pw.setEchoMode(wormhole_update_ui.QLineEdit.Password)
update_ui.input_http_pw.setEchoMode(wormhole_update_ui.QLineEdit.Password)

# SSH_로그인 버튼
update_ui.pushb_server_login.clicked.connect(ssh_login)

# http_접속 정보 기본값 설정
update_ui.input_http_port.setText("80")
update_ui.input_http_id.setText("c2m")
# update_ui.input_http_pw.setText("c2m")


# HTTP_로그인 버튼 활성화
update_ui.input_host.editingFinished.connect(http_login_enable)
update_ui.input_http_port.editingFinished.connect(http_login_enable)
update_ui.input_http_id.editingFinished.connect(http_login_enable)
update_ui.input_http_pw.textChanged.connect(http_login_enable)

# http_비밀번호 안보이도록 처리
update_ui.input_http_pw.setEchoMode(wormhole_update_ui.QLineEdit.Password)

# http_로그인 버튼
update_ui.pushb_http_login.clicked.connect(http_login)

# 파일 찾기 버튼
update_ui.toolb_find_file.clicked.connect(find_directory)

# 파일 찾기 기본 값
update_ui.input_update_file_path.setText(update_forder_check + " 폴더를 선택해 주세요.")

# 웜홀 업데이트 버튼
update_ui.pushb_wh_update.clicked.connect(wormhole_update)

# 웜홀 홈페이지 버튼
update_ui.pushb_wormhole_hompage.clicked.connect(homepage_open)

# reset버튼
update_ui.pushb_reset.clicked.connect(reset)

# 웜홀 서버 start
update_ui.pushb_wh_status_start.clicked.connect(wh_server_start)

# 웜홀 서버 Stop
update_ui.pushb_wh_status_stop.clicked.connect(wh_server_stop)

wormhole_update_tool.show()
sys.exit(app.exec_())
