import cv2 as cv
import numpy as np
import sys

char_dict = { 0: ' ', 1: '.', 2: ':', 3: '=', 4: '+', 5: '*', 6: '!', 7: '?', 8: '#', 9: '%', 10: '@' }

def image_to_ascii(image_path, scale=1):
    output = ""
    
    img = cv.imread(image_path)
    if img is None:
        output = f"Image not found: {image_path}"
        return output
    
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    height, width = img.shape
    
    chunk_size = width // scale // 25
    img = cv.resize(img, (img.shape[1] * 2, img.shape[0]))
    
    for i in range(0, img.shape[0], chunk_size):
        for j in range(0, img.shape[1], chunk_size):
            block = img[i:i+chunk_size, j:j+chunk_size]
            avg_brightness = np.mean(block)
            brightness = int((255 - avg_brightness) / 255 * 10)
            brightness = max(0, min(10, brightness))
            output += char_dict[brightness]
        output += "\n"
    return output
    
if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(image_to_ascii(sys.argv[1]))
    elif len(sys.argv) == 3 and int(sys.argv[2]) >= 1:
        print(image_to_ascii(sys.argv[1], int(sys.argv[2])))
    else:
        print(
            """
            
            Please provide with:
            1 - image path
            2 - scale (scale must be greater than 0,)

            Example: asciiart  my_image.png  2
                         ^           ^       ^
            """)