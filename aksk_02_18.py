import cv2

img = cv2.imread('./img.jpg', cv2.IMREAD_COLOR )
gray = cv2.imread('./img.jpg', cv2.IMREAD_GRAYSCALE)

unchange = cv2.imread('./img.jpg', cv2.IMREAD_UNCHANGED)
"""
#사진 보여주기
cv2.imshow('orginal', img)
cv2.imshow('gray', gray)
cv2.imshow('unchanged', unchange)

#그레이로 사진 저장
cv2.imwrite('gray.png',gray)

#이미지의 크기 조절
small = cv2.resize(img, None,fx = 0.5, fy = 0.5,interpolation=cv2.INTER_AREA)

cv2.imshow('shrink',small)
"""
#a,b값만큼 이미지 크기 출력
a,b = map(int,input().split())

zoom = cv2.resize(img, (a,b), interpolation=cv2.INTER_CUBIC)
cv2.imshow('zooooom',zoom)

#이미지 회전
rows,cols = img.shape[:2]
m = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 0.5)

dst = cv2.warpAffine(img,m,(cols,rows))
cv2.imshow('Rotation',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
