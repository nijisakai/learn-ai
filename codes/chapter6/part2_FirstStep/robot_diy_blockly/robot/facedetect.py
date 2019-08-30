import base64
import json
import requests
import numpy as np
import cv2
class BaiduPicIndentify:
    def __init__(self,img):
        self.AK = "tHjWWiNXlQLFNT2SdrNPWwH3"
        self.SK = "LXHQ5kP6GYewzOqFL1umrK4mfljx3W4r"
        self.img_src = img
        self.headers = {
            "Content-Type": "application/json; charset=UTF-8"
        }
 
    def get_accessToken(self):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + self.AK + '&client_secret=' + self.SK
        response = requests.get(host, headers=self.headers)
        json_result = json.loads(response.text)
        return json_result['access_token']
 
    def img_to_BASE64(slef,path):
        with open(path,'rb') as f:
            base64_data = base64.b64encode(f.read())
            return base64_data
 
    def detect_face(self):
        # 人脸检测与属性分析
        img_BASE64 = self.img_to_BASE64(self.img_src)
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
        post_data = {
            "image": img_BASE64,
            "image_type": "BASE64",
            "face_field": "gender,age,beauty,gender,race,emotion",
            "face_type": "LIVE"
        }
        #http://ai.baidu.com/docs#/Face-Detect-V3/top <---所有表情数据
        access_token = self.get_accessToken()
        request_url = request_url + "?access_token=" + access_token
        response = requests.post(url=request_url, data=post_data, headers=self.headers)
        json_result = json.loads(response.text)
        if json_result['error_msg']!='pic not has face':
            print("图片中包含人脸数：", json_result['result']['face_num'])
            print("图片中包含人物年龄：", json_result['result']['face_list'][0]['age'])
            print("图片中包含人物颜值评分：", json_result['result']['face_list'][0]['beauty'])
            print("图片中包含人物性别：", json_result['result']['face_list'][0]['gender']['type'])
            print("图片中包含人物种族：", json_result['result']['face_list'][0]['race']['type'])
            print("图片中包含人物表情：", json_result['result']['face_list'][0]['emotion']['type'])
    def capture_face(self):
        cap=cv2.VideoCapture(0)
        while True:
        #从摄像头读取图片
            ret,img=cap.read()
            cv2.imshow("img",img)
        #保持画面的持续。
            k=cv2.waitKey(1)
            if k == 27:
                #通过esc键退出摄像
                cv2.destroyAllWindows()
                break
            else: 
                #按任意键退出
                #k==ord("s"):
                #通过s键保存图片，并退出。
                cv2.imwrite("image2.jpg",img)
                cv2.destroyAllWindows()
                break
        #关闭摄像头
        cap.release()



if __name__=='__main__':
    cap=cv2.VideoCapture(0)
    while True:
        #从摄像头读取图片
        ret,img=cap.read()
        cv2.imshow("img",img)
        #保持画面的持续。
        k=cv2.waitKey(1)
        if k == 27:
                #通过esc键退出摄像
            cv2.destroyAllWindows()
            break
        elif k==ord("s"):
                #通过s键保存图片，并退出。
            cv2.imwrite("image2.jpg",img)
            cv2.destroyAllWindows()
            break
        #关闭摄像头
    cap.release()
    img_src='./image2.jpg'
    # img_src=input('请输入需要检测的本地图片路径:') //从命令行输入图片地址
    baiduDetect = BaiduPicIndentify(img_src)
    baiduDetect.detect_face()