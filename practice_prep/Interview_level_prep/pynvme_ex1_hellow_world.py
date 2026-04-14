import pytest
import nvme as d
def test_hello_world(nvme0, nvme0n1: d.Namespace):
    read_buf = d.Buffer(512)
    data_buf = d.Buffer(512)
    data_buf[10:21] = b'hello world'

    qpair = d.Qpair(nvme0,16)
    def write_cb(cdw0, status1):
        nvme0n1.read(qpair, read_buf, 0, 1)
    nvme0n1.write(qpair,data_buf, 0,1, cb=write_cb)
    qpair.waitdone(2)

    assert read_buf[10:21] == b'hello world'


