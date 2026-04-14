import pytest
import nvme as d

def test_hello_world(nvme0, nvme0n1, qpair):
    read_buf = d.Buffer(512)
    write_buf = d.Buffer(512)
    write_buf[10:21] = b'hello world'

    def write_cb(cdw0, status1):
        nvme0n1.read(qpair, read_buf, 0, 1)

    nvme0n1.write(qpair, write_buf, 0, 1, cb=write_cb)
    qpair.waitdone(2)
    assert read_buf[10:21] == b'hello world'

# This is a pytest test and should be run with pytest, not called directly.
# Run: python -m pytest Interview_level_prep/practice_nvme_1.py
