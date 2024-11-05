# import qrcode as qr
# img =qr.make("https://github.com/pradnyaa12")
# img.save("pradnya_git.png")

import qrcode  # Importing the qrcode library
from PIL import Image  # Importing Image class from PIL (Pillow)

def generate_qr_code(data, version=1, error_correction='L', box_size=10, border=4, fill_color='black', back_color='white', output_file='qr_code.png'):
    """
    Generate a customizable QR code and save it as an image.

    Parameters:
    - data (str): The data to encode in the QR code (e.g., URL, text).
    - version (int): Version of the QR code (1 to 40). Default is 1.
    - error_correction (str): Error correction level ('L', 'M', 'Q', 'H'). Default is 'L'.
    - box_size (int): Size of each box in pixels. Default is 10.
    - border (int): Thickness of the border (minimum is 4). Default is 4.
    - fill_color (str): Color of the QR code. Default is 'black'.
    - back_color (str): Background color of the QR code. Default is 'white'.
    - output_file (str): Name of the output file (with extension). Default is 'qr_code.png'.

    Returns:
    - None: The function saves the generated QR code as an image file.
    """
    # Create a QRCode object with specified parameters
    qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_L if error_correction == 'L' else
        qrcode.constants.ERROR_CORRECT_M if error_correction == 'M' else
        qrcode.constants.ERROR_CORRECT_Q if error_correction == 'Q' else
        qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Save the image to the specified file
    img.save(output_file)
    print(f"QR Code generated and saved as '{output_file}'.")

if __name__ == '__main__':
    data_to_encode = "https://github.com/pradnyaa12"  # Data to encode in the QR code
    generate_qr_code(data=data_to_encode, version=1, error_correction='H', box_size=10, border=4, fill_color='blue', back_color='white', output_file='pradnya_qr_code.png')
