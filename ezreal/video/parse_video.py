import os
import sys
import uuid
from tempfile import TemporaryDirectory

from Crypto.Cipher import AES

from config import config
from parse.container import MP4Container, FLVContainer
import subprocess


def parse_video(path):
    """
    ffmpeg -y -i templates/t.mp4 -c:v libx264 -c:aac copy -f
    hls -hls_time 180 -hls_list_size 0 -hls_key_info_file [密钥文件路径] -hls_playlist_type vod -hls_segment_filename [切片文件路径] [索引文件路径]

    :param path:
    :return:
    """
    import cv2

    # cap = cv2.VideoCapture('')
    file = MP4Container(filename='templates/test_video.mp4')
    for box in file.box:
        print(box)
        # print(dir(box))


if __name__ == '__main__':
    # with TemporaryDirectory(prefix=hex(int(uuid.uuid4().hex, 16)).lower()[2:], dir=config.VIDEO_FOLDER) as tempdir:

    key = os.urandom(AES.key_size[0])
    iv = os.urandom(AES.key_size[0])
    print(key, iv)
    file = FLVContainer(filename='templates/test.flv')
    # new_file_path = os.path.join(tempdir, 'test_demo.flv')
    new_file_path = './templates/test_demo.flv'
    length = file.encrypt(new_file_path, key, iv)
    # import ipdb;ipdb.set_trace();
    print(key.hex(), iv.hex(), length)

