import cv2
from pyzbar.pyzbar import decode


def print_environment_details():
    import sys
    print(f"Python {sys.version}")
    print(f"Environment {sys.prefix}")


def read_barcode(image):
    img = cv2.imread(image)
    detected_barcodes = decode(img)

    if not detected_barcodes:
        print("Barcode not detected or your barcode is blank/corrupted!")
    else:
        for barcode in detected_barcodes:

            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect

            # Put the rectangle in image using
            # cv2 to highlight the barcode
            cv2.rectangle(img, (x - 10, y - 10),
                          (x + w + 10, y + h + 10),
                          (255, 0, 0), 2)

            if barcode.data != "":
                print(barcode.data)
                print(barcode.type)

    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    print("Hello, World!")
    print_environment_details()

    for image in [
        "barcode39.png",
        "barcode39chris.png",
        "barcodex.png"
    ]:
        print(image)
        read_barcode(image)


if __name__ == "__main__":
    main()
