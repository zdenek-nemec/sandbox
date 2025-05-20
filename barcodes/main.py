import cv2
import os
from pyzbar.pyzbar import decode


def print_environment_details():
    import sys
    print(f"Python {sys.version}")
    print(f"Environment {sys.prefix}")


def read_barcode(image_path: str):
    if not os.path.isfile(image_path):
        print(f"{image_path}: File not found")
        return

    image = cv2.imread(image_path)
    detected_barcodes = decode(image)
    if not detected_barcodes:
        print(f"{image_path}: Barcode not detected")
    else:
        for barcode in detected_barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(image, (x - 10, y - 10),
                          (x + w + 10, y + h + 10),
                          (255, 0, 0), 2)
            if barcode.data:
                print(f"{image_path}: {barcode.data=}, {barcode.type=}")
    # cv2.imshow("Image", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def detect_barcodes(directory="img"):
    for image_filename in os.listdir(directory):
        image_path = f"{directory}/{image_filename}"
        read_barcode(image_path)


def main():
    print("Hello, Barcodes!")
    # print_environment_details()

    # for image_path in [
    #     "barcode39.png",
    #     "barcode39chris.png",
    #     "barcodex.png"
    # ]:
    #     read_barcode(image_path)

    # for printer in os.listdir("extracted_images"):
    #     for image_filename in os.listdir(f"extracted_images/{printer}"):
    #         image_path = f"extracted_images/{printer}/{image_filename}"
    #         read_barcode(image_path)

    detect_barcodes("c:/Zdenek/_tmp/L4C-5060 QR/2025-05-20 MyScans")
    # detect_barcodes("c:/Zdenek/_tmp/L4C-5060 QR/2025-05-20 Theirs")
    # detect_barcodes("generated_qr")


if __name__ == "__main__":
    main()
