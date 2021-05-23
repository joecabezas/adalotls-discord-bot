import re
import json

from adalotl_metadata import AdalotlMetadata

class Adalotl:
    POLICY_ID = '62ea7cb573306f6c272a2ff066679f2e4216270311d8e71b5f765251'

    def __init__(self, number):
        self.metadata = AdalotlMetadata().get(number)
        self.data = self.metadata[self.POLICY_ID][f"Adalotl{number}"]

    @property
    def name(self):
        return self.data['name']

    @property
    def morph(self):
        return self.data['morph']

    @property
    def image(self):
        return self.data['image']

    @property
    def number(self):
        return self.data['number']

    @property
    def attributes(self):
        return self.data['attributes']

    def __str__(self):
        return json.dumps(self.data, indent=4)

    @property
    def image_id(self):
        return re.search('ipfs:\/\/(\w+)', self.image).group(1)

    @property
    def image_url(self):
        return f"https://ipfs.io/ipfs/{self.image_id}"
