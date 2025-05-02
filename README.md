# Image-to-3D-Model

This project uses Tencent's [Hunyuan3D-2](https://github.com/Tencent/Hunyuan3D-2) model to generate a simple 3D model (`.obj` , `.glb` or `.stl`) from a single input image (photo). It includes preprocessing such as background removal and resizing before passing the image to the model.

---

## Steps to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/Addhithya/Image-to-3D-Model.git
   cd Image-to-3D-Model

2. **Create a virtual environment (recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows : venv\Scripts\activate 

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

4. **Install and set up the Hunyuan3D model**
   
   **Clone the model repo**
   ```bash
   git clone https://github.com/Tencent/Hunyuan3D-2.git
   cd Hunyuan3D-2
   ```
   **Install the model**
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```
   **Return to your Project folder**
   ```bash
   cd ..

5. **Add your input image and run the code**

   Edit main() function in the main.py file to set your input image path and output path:

   Then run :
   ```bash
   python3 main.py

## Libraries Used

- **`rembg`**: Background removal
- **`Pillow`**: Image processing
- **`Hunyuan3D`**: 2D-to-3D model pipeline
- **`trimesh` & `pyrender`**: 3D visualization
- **`os`**, **`torch` **: General-purpose tools (File management & to run ML model)

---

## Thought Process


1. The goal was to build a pipeline that converts a 2D image into a 3D mesh using an open-source AI model.

2. Gone through multiple open source models like PIfuHD & Trellis and found Hunyuan more powerful and efficient.

3. To ensure consistent input, resized images and added background removal for model compatibility.

4. Output is saved in .obj format, which is usually used in most 3D software, and renders a preview to visualize the 3D object quickly.
   
5. Kept things modular and simple to test and reuse.

