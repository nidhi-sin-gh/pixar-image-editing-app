from flask import Flask, render_template, request, send_file
from image_processor import read_file, edge_mask, Paintify, light_color, dark_color, outline, pencil_color
import cv2
import numpy as np

app = Flask(__name__, static_folder='static')  # Ensure Flask Static Folder Configuration
print(app.static_folder)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    file = request.files['image']
    if file:
        img_data = file.read()
        input_image = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)
        
        # Apply image processing functions from paint_image_create.py
        line_size, blur_value = 3, 3
        edges = edge_mask(input_image, line_size, blur_value)
        output_filename = "static/processed_image.png"  # Save processed image to static folder
        processed_image_path = Paintify(input_image, edges, output_filename)

        # Provide the processed image path to the template
        return render_template('index.html', img_path=processed_image_path)

    return render_template('index.html')

@app.route('/out_process', methods=['POST'])
def out_process():
    file = request.files['image']
    if file:
        img_data = file.read()
        input_image = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)
        
        # Apply image processing functions from paint_image_create.py
        line_size, blur_value = 3, 3
        edges = edge_mask(input_image, line_size, blur_value)
        output_filename = "static/processed_image.png"  # Save processed image to static folder
        processed_image_path = outline(input_image,output_filename)

        # Provide the processed image path to the template
        return render_template('index.html', img_path=processed_image_path)

    return render_template('index.html')

@app.route('/pen_out', methods=['POST'])
def pen_out():
    file = request.files['image']
    if file:
        img_data = file.read()
        input_image = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)
        
        # Apply image processing functions from paint_image_create.py
        line_size, blur_value = 3, 3
        edges = edge_mask(input_image, line_size, blur_value)
        output_filename = "static/processed_image.png"  # Save processed image to static folder
        processed_image_path = pencil_color(input_image,output_filename)

        # Provide the processed image path to the template
        return render_template('index.html', img_path=processed_image_path)

    return render_template('index.html')

@app.route('/light_out', methods=['POST'])
def light_out():
    file = request.files['image']
    if file:
        img_data = file.read()
        input_image = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)
        
        # Apply image processing functions from paint_image_create.py
        line_size, blur_value = 3, 3
        edges = edge_mask(input_image, line_size, blur_value)
        output_filename = "static/processed_image.png"  # Save processed image to static folder
        processed_image_path = light_color(input_image,output_filename)

        # Provide the processed image path to the template
        return render_template('index.html', img_path=processed_image_path)

    return render_template('index.html')

@app.route('/dark_out', methods=['POST'])
def dark_out():
    file = request.files['image']
    if file:
        img_data = file.read()
        input_image = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)
        
        # Apply image processing functions from paint_image_create.py
        line_size, blur_value = 3, 3
        edges = edge_mask(input_image, line_size, blur_value)
        output_filename = "static/processed_image.png"  # Save processed image to static folder
        processed_image_path = dark_color(input_image,output_filename)

        # Provide the processed image path to the template
        return render_template('index.html', img_path=processed_image_path)

    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
