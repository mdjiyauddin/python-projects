import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=5,
)

qr.add_data("https://mdjiyauddin.github.io/my-portfolio/")
qr.make(fit=True)

img = qr.make_image(fill_color="green", back_color="black")
img.save("linkedin_qr.png")
