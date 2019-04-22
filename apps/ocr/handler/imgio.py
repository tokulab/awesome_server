import base64
import io

def encode_to_b64(raw_img):
    b64 = base64.b64encode(raw_img.read())
    return b64

def decode_to_img(b64_img):
    img_bin = io.BytesIO(base64.b64decode(b64_img))
    return img_bin

