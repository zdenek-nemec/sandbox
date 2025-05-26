import barcode
from barcode.writer import ImageWriter


def generate_barcode():
    barcode_format = "Code39"
    barcode_data = "Test123"

    barcode_class = barcode.get_barcode_class(barcode_format)
    barcode_instance = barcode_class(barcode_data, writer=ImageWriter())

    barcode_instance.save("generated/barcode_sample")


def main():
    print("Hello, Generate QR")
    generate_barcode()


if __name__ == "__main__":
    main()
