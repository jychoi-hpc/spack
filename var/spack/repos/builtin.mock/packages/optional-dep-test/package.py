##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class OptionalDepTest(Package):
    """Description"""

    homepage = "http://www.example.com"
    url      = "http://www.example.com/optional_dep_test-1.0.tar.gz"

    version('1.0', '0123456789abcdef0123456789abcdef')
    version('1.1', '0123456789abcdef0123456789abcdef')

    variant('a',   default=False)
    variant('f',   default=False)
    variant('mpi', default=False)

    depends_on('a', when='+a')
    depends_on('b', when='@1.1')
    depends_on('c', when='%intel')
    depends_on('d', when='%intel@64.1')
    depends_on('e', when='%clang@34:40')

    depends_on('f', when='+f')
    depends_on('g', when='^f')
    depends_on('mpi', when='^g')

    depends_on('mpi', when='+mpi')

    def install(self, spec, prefix):
        pass
