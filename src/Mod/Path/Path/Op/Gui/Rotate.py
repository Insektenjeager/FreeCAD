# -*- coding: utf-8 -*-
# ***************************************************************************
# *   Copyright (c) 2017 sliptonic <shopinthewoods@gmail.com>               *
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

from PySide.QtCore import QT_TRANSLATE_NOOP
import FreeCAD
import Path
import Path.Op.Gui.Base as PathOpGui
import Path.Base.Gui.Util as PathGuiUtil
import Path.Op.Gui.Rotate as PathRotateBaseGui
import Path.Op.Rotate as PathRotate
import FreeCADGui

__title__ = "Rotate Operation UI"
__author__ = "Edler Markus"
__url__ = "https://www.freecadweb.org"
__doc__ = "Rotate Operation Controller."

if False:
    Path.Log.setLevel(Path.Log.Level.DEBUG, Path.Log.thisModule())
    Path.Log.trackModule(Path.Log.thisModule())
else:
    Path.Log.setLevel(Path.Log.Level.INFO, Path.Log.thisModule())

translate = FreeCAD.Qt.translate


class TaskPanelOpPage(PathOpGui.TaskPanelPage):
    """Page controller class for the Rotate operation."""

    def getForm(self):
        """getForm() ... returns UI"""
        return FreeCADGui.PySideUic.loadUi(":/panels/PageOpRotateEdit.ui")
    
    def getFields(self, obj):
        """getFields(obj) ... transfers values from UI to obj's properties"""
        self.updateToolController(obj, self.form.toolController)
        PathGuiUtil.updateInputField(obj, "Xoffset", self.form.Xoffset)
        PathGuiUtil.updateInputField(obj, "Yoffset", self.form.Yoffset)
        PathGuiUtil.updateInputField(obj, "Zoffset", self.form.Zoffset)
        obj.PointCountX = self.form.PointCountX.value()
        obj.PointCountY = self.form.PointCountY.value()
        obj.PointCountZ = self.form.PointCountZ.value()



Command = PathOpGui.SetupOperation(
    "Rotate",
    PathRotate.Create,
    TaskPanelOpPage,
    "Path_Rotate",
    QT_TRANSLATE_NOOP("Path_Rotate", "Rotate"),
    QT_TRANSLATE_NOOP("Path_Rotate", "Create a Rotating Operation from a model or face"),
    PathRotate.SetupProperties,
)

FreeCAD.Console.PrintLog("Loading PathRotateGui... done\n")

