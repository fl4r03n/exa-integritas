import fitz  # PyMuPDF
from PIL import Image, ImageOps
import os

def invert_pdf_colors(input_path, output_path):
    # Abrir el documento PDF
    pdf_document = fitz.open(input_path)
    image_list = []

    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        inverted_image = ImageOps.invert(img)
        image_list.append(inverted_image)

    # Guardar las imágenes invertidas como un nuevo PDF
    if image_list:
        image_list[0].save(output_path, save_all=True, append_images=image_list[1:])
    else:
        raise ValueError("No se generaron imágenes para guardar en el PDF.")
