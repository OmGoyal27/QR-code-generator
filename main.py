import qrcode
import pyautogui as pg

def generate_qr_code(data, filename):                       # Function for the QR code
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
    data = pg.prompt("Enter the data to encode: ")                  # Prompts for the url
    fn = pg.prompt("Enter the name to save the QR code : ")         # Prompts for the filename
    fn += ".png"

    generate_qr_code(data, fn)                                      # Generates the QR code
    print("QR code generated successfully!")
