import bitstring
from parse.box import BoxHeader, box_mapping
from parse.tag import flv_tag_mapping, FLVTag
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


class MP4Container:

    container_type = 'mp4'

    def __init__(self, filename=None, bytes_input=None, offset_bytes=0):

        self.box = {

        }

        if filename:
            self.bs = bitstring.ConstBitStream(filename=filename, offset=offset_bytes * 8)
        elif bytes_input:
            self.bs = bitstring.ConstBitStream(bytes=bytes_input, offset=offset_bytes * 8)

        self.parse()

    def parse(self):
        while self.bs.pos < self.bs.len:
            # import ipdb;ipdb.set_trace();
            try:
                box = self._read_box()
            except bitstring.ReadError as e:
                raise

            self.box[box.box_type] = box

    def _read_box(self):
        header = self._read_box_header()

        box_class = box_mapping.get(header.box_type, None)
        if box_class is None:
            raise

        box = box_class()
        box.parse_data(self.bs, header)
        return box

    def _read_box_header(self):

        header_start_pos = self.bs.bytepos
        size, box_type = self.bs.readlist("uint:32, bytes:4")
        # import ipdb;ipdb.set_trace();
        try:
            box_type = box_type.decode('utf-8')
        except UnicodeDecodeError:
            # we'll leave as bytes instead
            pass

        if size == 1:
            size = self.bs.read("uint:64")
        header_end_pos = self.bs.bytepos
        header_size = header_end_pos - header_start_pos

        return BoxHeader(box_size=size - header_size, box_type=box_type, header_size=header_size)


class FLVContainer:
    container_type = 'flv'

    def __init__(self, filename=None, bytes_input=None, offset_bytes=0):
        if filename:
            self.bs = bitstring.ConstBitStream(filename=filename, offset=offset_bytes * 8)
        elif bytes_input:
            self.bs = bitstring.ConstBitStream(bytes=bytes_input, offset=offset_bytes * 8)

    def encrypt(self, new_file_path, key, iv):
        cryptor = AES.new(key, AES.MODE_CBC, iv=iv)
        fw = open(new_file_path, 'wb')
        type_ = self.bs.read('bytes:3')
        if type_ != b'FLV':
            raise
        fw.write(type_)
        fw.write(self.bs.read('bytes:10'))
        # version = self.bs.read('uint:8')
        # b = self.bs.read('uint:8')
        # has_video = (b & 0x01) == 0x01
        # has_audio = (b & 0x04) == 0x04
        # header_length = self.bs.read('uint:32')
        # zero = self.bs.read('uint:32')
        payload_length = 0
        new_tag_type = {
            0x08: '18',
            0x09: '19',
            0x12: '20'
        }
        while self.bs.pos < self.bs.len:
            type_ = self.bs.read(8)
            tag_type = type_.int & 0x1f
            data_size = self.bs.read(24)
            fw.write(bytes.fromhex(new_tag_type[tag_type]))
            # fw.write(type_.bytes)
            fw.write(data_size.bytes)
            fw.write(self.bs.read('bytes:7'))
            payload = self.bs.read(f'bytes:{data_size.int}')
            if tag_type == 0x12:
                print(len(payload))
                payload = cryptor.encrypt(pad(payload, AES.block_size))
                payload_length = len(payload)
                print(payload)
            fw.write(payload)
            fw.write(self.bs.read('bytes:4'))

        fw.close()
        return payload_length

    def parse_tag(self):
        tag_type = self.bs.read(8)
        data_size = self.bs.read(24)
        flv_tag_class = flv_tag_mapping.get(tag_type.int & 0x1f, FLVTag)
        payload = self.bs.read(f'bytes:{data_size.int + 7}')
        return flv_tag_class(tag_type, data_size, payload)
        # tag_type = self.bs.read('uint:8') & 0x1f
        # data_size = self.bs.read('uint:24')
        # timestamp = self.bs.read('uint:24')
        # timestamp_ext = self.bs.read('uint:8')
        # data = self.bs.read(f'bytes:{data_size+7}')
        # return tag_type, (timestamp_ext << 24) + timestamp, data


class TSContainer:
    container_type = 'ts'
    read_length = 188

    def __init__(self, filename=None, bytes_input=None, offset_bytes=0):
        if filename:
            self.bs = bitstring.ConstBitStream(filename=filename, offset=offset_bytes * 8)
        elif bytes_input:
            self.bs = bitstring.ConstBitStream(bytes=bytes_input, offset=offset_bytes * 8)
        self.count = 0
        self.parse()

    def parse(self):
        while self.bs.pos < self.bs.len:
            buffer = self.bs.read(f'bytes:{self.read_length}')
            pid = (buffer[1] & 0x1f) << 8 | buffer[2]
            if pid == 0x72b:
                print('PAT 表')
            elif pid == 0x01:
                print('')
