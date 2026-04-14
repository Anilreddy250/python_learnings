import PySimpleGUI as sg
import pytest
import logging
import time

def test_sanitize(nvme0, nvme0n1, buf):
    if nvme0.id_data(331, 328) == 0:
        pytest.skip("sanitization operation not supported")
    logging.info("supported sanitize operation: %d" % nvme0.id_data(331, 328))
    nvme0.sanitize().waitdone()
    nvme0.getlogpage(0x81,buf,20).waitdone()
    while (buf.data(3,2) & 0x7) != 1:
        progress = buf.data(1,0)*100/0xffff
        sg.OneLineProgressMeter("Sanitization Progress", progress, 100, "Progress",orientation='h')
        nvme0.getlogpage(0x81,buf,20).waitdone()
        time.sleep(1)
