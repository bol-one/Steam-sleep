def check(path):
    import time
    with open(path + '/logs/content_log.txt', 'r', encoding='utf-8', errors='ignore') as f:
        f.seek(0, 2)
        while True:
            log = f.readline()
            if log:
                print(log)
                if ('scheduler finished : removed from schedule' in log) or ('Failed to get list of download sources' in log):
                    break
            else:
                time.sleep(0.1)


def send(token, id):
    import requests
    from mss import mss
    from mss.tools import to_png

    with mss() as sct:
        screenshot = sct.grab(sct.monitors[0])
        to_png(screenshot.rgb, screenshot.size, output="screens.png")

    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    with open('screens.png', 'rb') as file:
        files = {
            'photo': file
        }
        data = {
            'chat_id': id,
            'caption': 'Download complete!'
        }
        requests.post(url, data=data, files=files)

if __name__ == '__main__':
    import os
    check('D:/steam')
    send('123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew1', '-100123456789')
    os.system('shutdown /s /t 30')
