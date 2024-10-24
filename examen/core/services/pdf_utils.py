import fitz

def invert_pdf_colors(input_path, output_path):
    document = fitz.open(input_path)
    for page in document:
        pix = page.get_pixmap()
        pix.invert_irect()
        pix.save(output_path)
    document.close()
