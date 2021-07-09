
from collections import namedtuple

BoxHeader = namedtuple("BoxHeader", ["box_size", "box_type", "header_size"])


class Box:

    box_type = None

    def __init__(self, header=None, payload=None):
        self.header = header
        self.payload = payload

    def parse_data(self, box_bs, header):
        self.header = header
        self.payload = box_bs.read(header.box_size * 8).bytes


class FileTypeBox(Box):

    box_type = 'ftyp'


class FreeBox(Box):

    box_type = 'free'


class MediaDataBox(Box):

    box_type = 'mdat'

    def parse_data(self, box_bs, header):
        self.header = header
        self.payload = box_bs.read(header.box_size * 8).bytes


class MovieMetaDataBox(Box):

    box_type = 'moov'


box_mapping = {
    'ftyp': FileTypeBox,
    'free': FreeBox,
    'mdat': MediaDataBox,
    'moov': MovieMetaDataBox
}
