from collections import namedtuple


class FLVTag:

    tag_type = None

    def __init__(self, type_, data_size, payload=None):
        self.type_ = type_
        self.data_size = data_size
        self.payload = payload

    @property
    def body(self):
        return self.type_.bytes.hex()+self.data_size.bytes.hex()+self.payload.hex()


class VideoTag(FLVTag):
    tag_type = 'video'


class AudioTag(FLVTag):
    tag_type = 'audio'


class ScriptTag(FLVTag):
    tag_type = 'script'


flv_tag_mapping = {
    0x12: ScriptTag,
    0x08: AudioTag,
    0x09: VideoTag
}