import cv2
img=cv2.imread("solar_system.jpg")

cv2.putText(img,
            "Sun",
            (20,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255)
)

cv2.putText(img,
            "Mercury",
            (20,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255)
)

cv2.putText(img,
            "Venus",
            (20,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255)
)

cv2.putText(img,
            "Earth",
            (20,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255)
)

cv2.putText(img,
            "mars",
            (20,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255)
)

cv2.putText(img,
            "jupiter",
            (20,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255)
)

cv2.putText(img,
            "Saturn",
            (20,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255)
)

cv2.putText(img,
            "uranus",
            (20,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255)
)

cv2.putText(img,
            "neptune",
            (20,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255)
)


cv2.imshow("output",img)
cv2.waitKey(0)





