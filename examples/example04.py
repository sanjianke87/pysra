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
# Copyright (C) Albert Kottke, 2013-2016

"""Randomize nonlinear properties."""

import matplotlib.pyplot as plt
import numpy as np

import pysra

soil_type = pysra.site.SoilType(
    'Soil', 18.,
    pysra.site.DarendeliNonlinearProperty(0, 1, 0.5, param='mod_reduc'),
    pysra.site.DarendeliNonlinearProperty(0, 1, 0.5, param='damping')
)
n = 30
correlation = 0

fig, axarr = plt.subplots(2, 2, sharex=True, sharey='row',
                          subplot_kw={'xscale': 'log'})

for i, (variation, name) in enumerate(zip(
        [pysra.variation.DarendeliVariation(correlation),
         pysra.variation.SpidVariation(correlation)],
        ['Darendeli (2001)', 'EPRI SPID (2014)'])):
    realizations = [variation(soil_type) for _ in range(n)]
    for j, prop in enumerate(['mod_reduc', 'damping']):
        axarr[j, i].plot(
            getattr(soil_type, prop).strains,
            np.transpose([getattr(r, prop).values for r in realizations]),
            'b-', linewidth=0.5, alpha=0.8
        )
        if j == 0:
            axarr[j, i].set_title(name)

axarr[0, 0].set_ylabel('$G/G_{max}$')
axarr[1, 0].set_ylabel('$D$ (%)')
plt.setp(axarr[1, :], xlabel='Strain, $\gamma$ (%)')

fig.tight_layout()
fig.savefig(__file__.replace('.py', '.png'), dpi=150)
