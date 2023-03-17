from paddleocr import PaddleOCR,draw_ocrimport os
import cv2
import matplotlib.pyplot as plt
import os
import cv2
import matplotlib.pyplot as plt

ocr = PaddleOCR(use_angle_cls=True)

img_path = './input_images/05-receipt1.jpg'
result = ocr.ocr(img_path)
save_ocr(img_path, out_path, result, font)


# Specifying output path and font path.
out_path = './output_images'
font = './simfang.ttf'
def save_ocr(img_path, out_path, result, font):
  save_path = os.path.join(out_path, img_path.split('/')[-1] + 'output')
 
  image = cv2.imread(img_path)
 
  boxes = [line[0] for line in result]
  txts = [line[1][0] for line in result]
  scores = [line[1][1] for line in result]
 
  im_show = draw_ocr(image, boxes, txts, scores, font_path=font)
  
  cv2.imwrite(save_path, im_show)
 
  img = cv2.cvtColor(im_show, cv2.COLOR_BGR2RGB)
  plt.imshow(img)