import random
import string
import cv2
import pandas as pd
import numpy as np

def randomgen():
    random1 = ''.join([random.choice(string.ascii_uppercase+string.digits ) for n in range(10)])
    return random1

def main():
    UID=[]
    font=cv2.FONT_HERSHEY_COMPLEX
    font1=cv2.FONT_HERSHEY_DUPLEX
    data = pd.read_csv('Students.csv')
    for i in data.index:
        i=data['Name'][i]
        img = cv2.imread('cert.jpg', cv2.IMREAD_COLOR)
        if(len(i)>=0 and len(i)<=4):
            cv2.putText(img, i, (380, 257), font, 0.9, (0, 0, 255), 1, cv2.LINE_AA)
        if(len(i)>4 and len(i)<8):
            cv2.putText(img,i,(360,257),font,0.9,(0,0,255),1,cv2.LINE_AA)
        elif (len(i)>=8 and len(i)<10):
            cv2.putText(img, i, (340, 257), font, 0.9, (0, 0, 255), 1, cv2.LINE_AA)
        elif (len(i) >= 10 and len(i) < 12):
            cv2.putText(img, i, (350, 257), font, 0.9, (0, 0, 255), 1, cv2.LINE_AA)
        elif (len(i) >= 12 and len(i) < 14):
            cv2.putText(img, i, (340, 257), font, 0.9, (0, 0, 255), 1, cv2.LINE_AA)
        elif(len(i)>=14 and len(i)<16):
            cv2.putText(img, i, (310, 257), font, 0.9, (0, 0, 255), 1, cv2.LINE_AA)
        elif(len(i)>=16 and len(i)<18):
            cv2.putText(img, i, (300, 257), font, 0.9, (0, 0, 255), 1, cv2.LINE_AA)
        elif (len(i) >= 18 and len(i) < 20):
            cv2.putText(img, i, (280, 257), font, 0.9, (0, 0, 255), 1, cv2.LINE_AA)
        elif (len(i) >= 20 and len(i) < 24):
            cv2.putText(img, i, (240, 257), font, 0.9, (0, 0, 255), 1, cv2.LINE_AA)
        elif (len(i) >= 24 and len(i) < 30):
            cv2.putText(img, i, (220, 257), font, 0.9, (0, 0, 255), 1, cv2.LINE_AA)
        uniq=randomgen()
        UID.append(uniq)
        cv2.putText(img, uniq, (650, 437), font, 0.35, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.imshow('image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite('saved/'+uniq+'.png',img)
    data["UniqueID"]=UID
    data.to_csv('Demo.csv',index=False)
if __name__ == "__main__":
    main()
