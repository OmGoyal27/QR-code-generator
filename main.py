import qrcode
import pyautogui as pg

def generate_qr_code(data, filename):
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

if __name__ == "__main__":
    data = pg.prompt("Enter the data to encode: ")
    fn = pg.prompt("Enter the name to save the QR code : ")
    fn += ".png"

    generate_qr_code(data, fn)
    print("QR code generated successfully!")
