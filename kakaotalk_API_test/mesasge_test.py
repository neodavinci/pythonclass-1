import json
import requests

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# 사용자 토큰
headers = {
    "Authorization": "Bearer " + "IVV53nwIYf6fN5j5jKEM-5bpPKGUUNCok8EKKwzTAAABjT4Tcqaxu3fh8M0xkQ"
}

template = {
    "object_type" : "list",
    "header_title" : "초밥 사진",
    "header_link" : {
        "web_url" : "www.naver.com",
        "mobile_web_url" : "www.naver.com"
    },
    "contents" : [
        {
            "title" : "1. 광어초밥",
            "description" : "광어는 맛있다",
            "image_url" : "https://search1.kakaocdn.net/argon/0x200_85_hr/8x5qcdbcQwi",
            "image_width" : 50, "image_height" : 50,
            "link" : {
                "web_url" : "www.naver.com",
                "mobile_web_url" : "www.naver.com"
            }
        },
        {
            "title" : "2. 참치초밥",
            "description" : "참치는 맛있다",
            "image_url" : "https://search2.kakaocdn.net/argon/0x200_85_hr/IjIToH1S7J1",
            "image_width" : 50, "image_height" : 50,
            "link" : {
                "web_url" : "www.naver.com",
                "mobile_web_url" : "www.naver.com"
            }
        }
        
    ],
    "buttons" : [
        {
            "title" : "웹으로 이동",
            "link" : {
                "web_url" : "www.naver.com",
                "mobile_web_url" : "www.naver.com"
            }
        }
    ]
    
}

data = {
    "template_object" : json.dumps(template)
}

res = requests.post(url, data=data, headers=headers)
print(res.status_code)
if res.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(res.json()))