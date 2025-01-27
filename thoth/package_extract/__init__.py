#!/usr/bin/env python3
# thoth-package-extract
# Copyright(C) 2018-2021 The Thoth authors.
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Extraction of installed packages for project Thoth."""

from .core import extract_image  # noqa F401

__version__ = "1.2.0"
__title__ = "thoth-package-extract"
__author__ = "Fridolin Pokorny"
__license__ = "GPLv3+"
__copyright__ = "Copyright 2018 Fridolin Pokorny"
__all__ = ["extract_image"]
