
'''
import cv2
import numpy
import time


camera = cv2.VideoCapture(0)
ret, frame = camera.read()
# 转灰度图
gray_pic = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

if not ret:
    print("打开摄像头失败")
end = time.time()

cv2.imshow("capture", frame)
    
cv2.waitKey(0)

'''

import cv2  
import time
  
cap = cv2.VideoCapture(0)  
face_cascade = cv2.CascadeClassifier("E:\\PythonProject\\JZTX\\haarcascade_frontalface_default.xml")  
  
working = True

start_time = time.time()
while True:  
    ret, frame = cap.read()  
    # cv2.imshow("capture", frame)
    if ret:  
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
        faces_rects = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)  
        
        for (x, y, w, h) in faces_rects:  
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  
            working = True
        if working :
            time.sleep(2)
            elapsed_time = time.time() - start_time
            if elapsed_time >= 10:  # 10 minutes = 600 seconds
                cv2.imshow('Face Detection', frame)  
               # if cv2.waitKey(1) & 0xFF == ord('q'):  
                #    break
                start_time = time.time()
            print("true continue")
           # start_time = time.time()
            continue  
        else:
            working = False
            time.sleep(2)
            start_time = time.time()
            print("not working")
            continue
 

        for (x, y, w, h) in faces_rects:  
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  
        cv2.imshow('Face Detection', frame)  
        if cv2.waitKey(1) & 0xFF == ord('q'):  
            break  
    else:  
        break
# 使用release()方法释放摄像头，并使用destroyAllWindows()方法关闭所有窗口
cap.release()  
cv2.destroyAllWindows()

'''
import cv2
import matplotlib as plt
import face_recognition


def show_detection(image, faces):
    """在每个检测到的人脸上绘制一个矩形进行标示"""
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 5)
    return image



# 可视化函数
def show_img_with_matplotlib(color_img, title, pos):
    img_RGB = color_img[:, :, ::-1]
    ax = plt.subplot(2, 2, pos)
    plt.imshow(img_RGB)
    plt.title(title, fontsize=8)
    plt.axis('off')
    
# 加载图像
img = cv2.imread("test_face_detection.jpg")
# 将 BGR 图像转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 加载分类器
cas_alt2 = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
cas_default = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# 检测人脸
faces_alt2 = cas_alt2.detectMultiScale(gray)
faces_default = cas_default.detectMultiScale(gray)
retval, faces_haar_alt2 = cv2.face.getFacesHAAR(img, "haarcascade_frontalface_alt2.xml")
faces_haar_alt2 = np.squeeze(faces_haar_alt2)
retval, faces_haar_default = cv2.face.getFacesHAAR(img, "haarcascade_frontalface_default.xml")
faces_haar_default = np.squeeze(faces_haar_default)
# 绘制人脸检测框
img_faces_alt2 = show_detection(img.copy(), faces_alt2)
img_faces_default = show_detection(img.copy(), faces_default)
img_faces_haar_alt2 = show_detection(img.copy(), faces_haar_alt2)
img_faces_haar_default = show_detection(img.copy(), faces_haar_default)
# 可视化
show_img_with_matplotlib(img_faces_alt2, "detectMultiScale(frontalface_alt2): " + str(len(faces_alt2)), 1)
show_img_with_matplotlib(img_faces_default, "detectMultiScale(frontalface_default): " + str(len(faces_default)), 2)
show_img_with_matplotlib(img_faces_haar_alt2, "getFacesHAAR(frontalface_alt2): " + str(len(faces_haar_alt2)), 3)
show_img_with_matplotlib(img_faces_haar_default, "getFacesHAAR(frontalface_default): " + str(len(faces_haar_default)), 4)
plt.show()


def show_detection(image, faces):
    for face in faces:
        top, right, bottom, left = face
        cv2.rectangle(image, (left, top), (right, bottom), (255, 255, 0), 10)
    return image
# 显示检测结果
# 执行检测
# 第二种方法的第二行代码，至此第二种方法也讲解完毕了
# 第三种方法需要且仅需要一行代码
rects_1 = face_recognition.face_locations(rgb, 0, "hog")
rects_2 = face_recognition.face_locations(rgb, 1, "hog")



img_faces_1 = show_detection(img.copy(), rects_1)
img_faces_2 = show_detection(img.copy(), rects_2)
show_img_with_matplotlib(img_faces_1, "face_locations(rgb, 0, hog): " + str(len(rects_1)), 1)
show_img_with_matplotlib(img_faces_2, "face_locations(rgb, 1, hog): " + str(len(rects_2)), 2)
plt.show()

'''
