import cv2

//carregar imagem
img = 
cv2.putText(img,
            "Sol",
             (100,80),
             cv2.FONT_HERSHEY_COMPLEX,
             2,
             (0,0,255)
             )



cv2.imshow("Resultado",img)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)
