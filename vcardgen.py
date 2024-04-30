
import qrcode
from datetime import datetime
import json

class VCardGenerator:
    
    def __init__(self, json_file_path=''):
        self.json_file_path = json_file_path
    
    def generate_vcard_from_json(self, input_dict = {}):
        if len(input_dict) == 0:
            with open(self.json_file_path, 'r') as json_file:
                loaded_data = json.load(json_file)
        else:
            loaded_data = input_dict
        
        vcard = "BEGIN:VCARD\nVERSION:3.0\n"

        for key, value in loaded_data.items():
            if key == "NONE":
                pass
            elif key == "EMAIL_WORK":
                vcard += f"EMAIL;type=WORK,INTERNET:{value}\n"
            elif key == "URL_LINKEDIN":
                vcard += f"URL;type=LINKEDIN,INTERNET:{value}\n"
            else:
                vcard += f"{key}:{value}\n"
                
        vcard += f"REV:{datetime.now()}\nEND:VCARD"
        
        return vcard
    

    def create_qr_code(self, vcard):
        """Create QR code image from content to output path."""
        qr_object = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        print(vcard)
        qr_object.add_data(vcard)
        qr_object.make(fit=True)
    
        img = qr_object.make_image(fill_color="black", back_color="white").convert("RGBA")
        return(img)
        
