#!/usr/bin/env python
# encoding: utf-8

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# Copyright (C) Albert Kottke, 2013-2015


import os
import pytest

from numpy.testing import assert_almost_equal, assert_equal

from pysra import motion


@pytest.fixture
def tsm():
    '''Setup the default time series for testing.'''
    return motion.TimeSeriesMotion.load_at2_file(
        os.path.join(os.path.dirname(__file__), 'data', 'NIS090.AT2'))


def test_ts_load_at2_file(tsm):
    assert_equal(tsm.accels.size, 4096)
    assert_almost_equal(tsm.time_step, 0.01)

    assert_almost_equal(tsm.accels[0], 0.233833E-06)
    assert_almost_equal(tsm.accels[-1], 0.496963E-04)


def test_ts_freqs(tsm):
    freqs = tsm.freqs
    assert_almost_equal(freqs[0], 0)
    assert_almost_equal(freqs[-1], 50.)

    assert_equal(tsm.freqs.size, tsm.fourier_amps.size)
