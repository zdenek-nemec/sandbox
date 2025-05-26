import qrcode


def generate_qr_code(data, filename="generated_qr/qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    return filename


def main():
    print("Hello, Generate QR")
    generate_qr_code("Test123")


if __name__ == "__main__":
    main()
