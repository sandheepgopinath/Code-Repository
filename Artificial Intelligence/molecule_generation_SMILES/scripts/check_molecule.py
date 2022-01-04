

# Python script to check if a molecule exists
import smilite

class check_molecule:
    def __init__(self,smile_str,backend='zinc15'):
        self.smile_str=smile_str
        print(smilite.get_zincid_from_smile(self.smile_str,backend=backend))
