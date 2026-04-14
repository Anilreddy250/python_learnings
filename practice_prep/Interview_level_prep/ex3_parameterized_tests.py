#create a parameter test with a argument list
import logging
import pytest

@pytest.mark.parametrize("qcount", [1,2,3,4,8,16])
def test_ioworker_iops_multiple_queue(nvme0n1, qcount):

    l = []
    io_total = 0
#create multiple ipworkers for read performance test
    for i in range(qcount):
        a = nvme0n1.ioworker(io_size=8, lba_align=8,
                             region_start=0, region_end=256*1024*8,
                             read_percentage=100, time=0).start()
        l.append(a)
    for a in l :
        r =a.close()
        io_total += (r.io_count_read+r.io_count_nonread)
    logging.info("Q %d IOPS: %dK" %(qcount, io_total/10000))
