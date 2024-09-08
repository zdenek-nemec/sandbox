import fitz
import os


def extract_images_from_pdf(pdf_path, output_folder):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over PDF pages
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        image_list = page.get_images(full=True)

        # If no images found on the page, continue to the next page
        if not image_list:
            continue

        print(f"[INFO] Found {len(image_list)} images on page {page_number + 1}")

        # Iterate over the images
        for img_index, img in enumerate(image_list, start=1):
            xref = img[0]
            # Extract the image bytes
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]  # Image extension (e.g., "png", "jpeg")

            # Define the output path for the image
            image_filename = f"page_{page_number + 1}_img_{img_index}.{image_ext}"
            image_path = os.path.join(output_folder, image_filename)

            # Write the image to a file
            with open(image_path, "wb") as image_file:
                image_file.write(image_bytes)

            print(f"[INFO] Saved image: {image_path}")

    # Close the PDF document
    pdf_document.close()


def main():
    scan_directory = r"c:\Zdenek\_tmp\L4C-3660_Barcode_Separation\PDF scans"
    for printer in os.listdir(scan_directory):
        for document in os.listdir(scan_directory + "/" + printer):
            document_path = scan_directory + "/" + printer + "/" + document
            print(f"Processing {document_path=}, {os.path.isfile(document_path)=}")
            extract_images_from_pdf(document_path, f"extracted_images/{printer}")


if __name__ == "__main__":
    main()
