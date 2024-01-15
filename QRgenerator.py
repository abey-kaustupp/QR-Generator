import qrcode

def generate_qr_code(link, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(file_name)
    print(f"QR code generated and saved as {file_name}")

if __name__ == "__main__":
    # Take the link input from the user
    link = input("Enter the link: ")

    # Provide a default filename or customize as needed
    file_name = "generated_qr_code_khu.png"

    # Generate the QR code
    generate_qr_code(link, file_name)
