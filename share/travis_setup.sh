#!/bin/bash
set -evx

mkdir ~/.celercore

# safety check
if [ ! -f ~/.celercore/.celer.conf ]; then
  cp share/celer.conf.example ~/.celercore/celer.conf
fi
