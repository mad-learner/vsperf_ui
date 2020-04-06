from django.db import models

class EntryForm(models.Model):
    VSWITCH_BRIDGE_NAME = models.CharField(max_length=200)
    WHITELIST_NICS = models.CharField(max_length=200)
    TRAFFICGEN = models.CharField(max_length=200)
    TRAFFICGEN_TREX_HOST_IP_ADDR = models.CharField(max_length=200)
    TRAFFICGEN_TREX_USER = models.CharField(max_length=200, default='')
    TRAFFICGEN_TREX_BASE_DIR = models.CharField(max_length=200, default='')
    TRAFFICGEN_TREX_LINE_SPEED_GBPS = models.CharField(max_length=200, default='')
    TRAFFICGEN_TREX_PORT1 = models.CharField(max_length=200, default='')
    TRAFFICGEN_TREX_PORT2 = models.CharField(max_length=200, default='')
    TRAFFICGEN_TREX_PROMISCUOUS = models.CharField(max_length=200, default='')
    TRAFFICGEN_DURATION = models.CharField(max_length=200, default='')
    TRAFFICGEN_LOSSRATE = models.CharField(max_length=200, default='')
    TRAFFICGEN_RFC2544_TESTS = models.CharField(max_length=200, default='')
    TRAFFICGEN_PKT_SIZES = models.CharField(max_length=200, default='')
    TRAFFICGEN_TREX_LATENCY_PPS = models.CharField(max_length=200, default='')
    TRAFFICGEN_TREX_RFC2544_BINARY_SEARCH_LOSS_VERIFICATION = models.CharField(max_length=200, default='')
    TRAFFICGEN_TREX_RFC2544_MAX_REPEAT = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.VSWITCH_BRIDGE_NAME
    
