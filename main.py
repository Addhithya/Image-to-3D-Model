from hy3dgen.shapegen import Hunyuan3DDiTFlowMatchingPipeline
from rembg import remove
from PIL import Image
import trimesh
import pyrender
# import numpy as np
import os

def remove_background(input_img: Image.Image) -> Image.Image:
    img_rgb = input_img.convert("RGB")
    output_img = remove(img_rgb)
    return output_img

def prepare_image(img: Image.Image, size: int = 518) -> Image.Image:
    img_resized = img.resize((size, size), Image.LANCZOS)
    return img_resized

def load_model():
    pipeline = Hunyuan3DDiTFlowMatchingPipeline.from_pretrained(
        'tencent/Hunyuan3D-2mini',
        subfolder='hunyuan3d-dit-v2-mini',
        variant='fp16'
    )
    # pipeline.to(device=torch.device("cpu"), dtype=torch.float32)
    return pipeline

def generate_mesh(pipeline, image_path: str):
    outputs = pipeline(image=image_path)
    mesh = outputs[0]
    return mesh

def save_mesh(mesh, output_path: str):
    mesh.export(output_path)

def visualize_mesh(path):
    mesh = trimesh.load(path)
    scene = pyrender.Scene()
    scene.add(pyrender.Mesh.from_trimesh(mesh))
    pyrender.Viewer(scene, use_raymond_lighting=True)

def main():
    print("Generating 3D OBJ from a single image using Hunyuan3D-DiT-v2-mini.")
    input = "./test.png"
    output_path = "./result/model.obj"

    img = Image.open(input)
    img_nobg = remove_background(img)        

    if img_nobg.mode == "RGBA":
        bg = Image.new("RGB", img_nobg.size, (255,255,255))
        bg.paste(img_nobg, mask=img_nobg.split()[3])  # 3 is alpha channel
        img_nobg = bg

    img_prepped = prepare_image(img_nobg, size=518)

    temp_path = "temp_prepped.png"
    img_prepped.save(temp_path)

    pipeline = load_model()
    mesh = generate_mesh(pipeline, temp_path)

    # Saving the mesh to OBJ
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    save_mesh(mesh, output_path)
    print(f"Saved 3D model to {output_path}")

    visualize_mesh(output_path)

if __name__ == "__main__":
    main()