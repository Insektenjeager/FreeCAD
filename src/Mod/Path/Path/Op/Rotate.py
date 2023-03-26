# -*- coding: utf-8 -*-
# ***************************************************************************
# *   Copyright (c) 2023 Edler Markus                                       *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************


import FreeCAD
import Path
import Path.Op.Base as PathOp
import Path.Op.Rotate as PathRotate
import PathScripts.PathUtils as PathUtils
from PySide.QtCore import QT_TRANSLATE_NOOP
import numpy

__title__ = "Rotate Operation"
__author__ = "Edler Markus"
__url__ = "https://www.freecadweb.org"
__doc__ = "Class and Implementation of Rotate Operation."


if False:
    Path.Log.setLevel(Path.Log.Level.DEBUG, Path.Log.thisModule())
    Path.Log.trackModule(Path.Log.thisModule())
else:
    Path.Log.setLevel(Path.Log.Level.INFO, Path.Log.thisModule())

translate = FreeCAD.Qt.translate


class ObjectRotate(PathOp.ObjectOp):
  
    def opFeatures(self, obj):
        return PathOp.FeatureTool
    

def SetupProperties():
    setup = []
    return setup


def Create(name, obj=None, parentJob=None):
    """Create(name) ... Creates and returns a Rotate operation."""
    if obj is None:
        obj = FreeCAD.ActiveDocument.addObject("Path::FeaturePython", name)
    obj.Proxy = ObjectRotate(obj, name, parentJob)
    return obj