import cv2
import numpy as np
import datetime

# Function to load image
def read_file(filename):
    img = cv2.imread(filename)  # read image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # convert image from bgr format to rgb
    return img

# Creating edges
def edge_mask(img, line_size, blur_value):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray_blur = cv2.medianBlur(gray, blur_value)
    edges = cv2.adaptiveThreshold(
        gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value
    )
    return edges

# Reduce color palette
def color_quantization(img, k):
    data = np.float32(img).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.01)
    ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    result = center[label.flatten()]
    result = result.reshape(img.shape)
    return result

# Applying filter to reduce noise
def reduce_noise(img):
    blurred = cv2.bilateralFilter(img, d=8, sigmaColor=200, sigmaSpace=200)
    return blurred

# Combining edge with quantized image
def Paintify(img, edges, output_filename):
    img_quantized = color_quantization(img, k=10)
    blurred = reduce_noise(img_quantized)
    processed_image = cv2.bitwise_and(blurred, blurred, mask=edges)
    
    
    # Generate a unique filename with a timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    save_output = f"output_folder/paint{timestamp}.png"
    
    # Save the processed image in system
    cv2.imwrite(save_output, processed_image)
    

    # Save the processed image
    save_success = cv2.imwrite(output_filename, processed_image)
    print(f"Save success: {save_success}")
    return output_filename

def outline(image, output_filename):
    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(grey_img)
    blur = cv2.GaussianBlur(invert, (21, 21), 0)
    invertedblur = cv2.bitwise_not(blur)
    sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
    
    # Generate a unique filename with a timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    save_output = f"output_folder/sketch{timestamp}.png"
    
    # Save the processed image in system
    cv2.imwrite(save_output, sketch)
    
    # Save the processed image
    save_success = cv2.imwrite(output_filename, sketch)
    print(f"Save success: {save_success}")
    return output_filename
    #return sketch
    
def pencil_color(img, output_filename):
    pencil, colored = cv2.pencilSketch(img, 200, 0.1, shade_factor=0.1)
    
    # Generate a unique filename with a timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    save_output = f"output_folder/pencil{timestamp}.png"
    
    # Save the processed image in system
    cv2.imwrite(save_output, colored)
    
    # Save the processed image
    save_success = cv2.imwrite(output_filename, colored)
    print(f"Save success: {save_success}")
    
    return output_filename

def light_color(img, output_filename):
    
    hsvimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype('float32')
    h,s,v = cv2.split(hsvimg)
    s = s * 0.4
    s = np.clip(s,0,255)
    hsvimg = cv2.merge([h,s,v])
    light = cv2.cvtColor(hsvimg.astype('uint8'), cv2.COLOR_HSV2BGR)

    # Generate a unique filename with a timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    save_output = f"output_folder/light{timestamp}.png"
    
    # Save the processed image in system
    cv2.imwrite(save_output, light)
    
    # Save the processed image
    save_success = cv2.imwrite(output_filename, light)
    print(f"Save success: {save_success}")
    
    return output_filename

def dark_color(img, output_filename):
    
    hsvimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype('float32')
    h,s,v = cv2.split(hsvimg)
    s = s * 6
    s = np.clip(s,0,255)
    hsvimg = cv2.merge([h,s,v])
    dark1 = cv2.cvtColor(hsvimg.astype('uint8'), cv2.COLOR_HSV2BGR)
    dark = cv2.bilateralFilter(dark1, d=8, sigmaColor=200, sigmaSpace=200)


    # Generate a unique filename with a timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    save_output = f"output_folder/dark{timestamp}.png"
    
    # Save the processed image in system
    cv2.imwrite(save_output, dark)
    
    # Save the processed image
    save_success = cv2.imwrite(output_filename, dark)
    print(f"Save success: {save_success}")
    
    return output_filename