# -*- coding: utf-8 -*-
import pdb
from pprint import pprint
import re
import sys
import os
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), '../lib')))
import config
from models import Superblock, Proposal, GovernanceObject, Setting, Signal, Vote, Outcome, Watchdog
from models import VoteSignals, VoteOutcomes
from peewee import PeeweeException  # , OperationalError, IntegrityError
from celerd import CelerDaemon
import celerlib
from decimal import Decimal
celerd = CelerDaemon.from_celer_conf(config.celer_conf)
import misc
# ==============================================================================
# do stuff here

pr = Proposal(
    name='proposal',
    url='https://celercoin.com/proposal',
    payment_address='CWeEWfhUtoQ7ZcPan7dtXmVcxefUKL94z2',
    payment_amount=39.23,
    start_epoch=1521594900,
    end_epoch=1521858000,
)


bh = 131112
bh_epoch = celerd.block_height_to_epoch(bh)

fudge = 72000
window_start = 1522544400 - fudge
window_end = 1522630800 + fudge

print("Window start: %s" % misc.epoch2str(window_start))
print("Window end: %s" % misc.epoch2str(window_end))
print("\nbh_epoch: %s" % misc.epoch2str(bh_epoch))


if (bh_epoch < window_start or bh_epoch > window_end):
    print("outside of window!")
else:
    print("Within window, we're good!")

# pdb.set_trace()
# celerd.get_object_list()
# ==============================================================================
# pdb.set_trace()
1
