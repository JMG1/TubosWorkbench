# -*- coding: utf-8 -*-
# Tubos workbench for FreeCAD
# (c) 2017 Javier Martínez García
#***************************************************************************
#*   (c) Javier Martínez García 2017                                       *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU General Public License (GPL)            *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Lesser General Public License for more details.                   *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with FreeCAD; if not, write to the Free Software        *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************/

__title__="Tubos Workbench for FreeCAD"
__author__ = "Javier Martínez García"
__url__ = "http://linuxforanengineer.blogspot.com"

import FreeCAD
import FreeCADGui



class Tubos(Workbench):
    import Tubos
    Icon = Tubos.__dir__ + '/icons/workbenchIcon.svg'
    MenuText = 'Tubos'
    ToolTip = 'Create structures with tubes'

    def GetClassName(self):
        return 'Gui::PythonWorkbench'

    def Initialize(self):
        self.TubeCreationTools = ['CreateRectangularTube',
                                  'CreateRoundTube',
                                  'CreateWeld']
        self.appendToolbar( 'TubeCreationTools', self.TubeCreationTools )

    def Activated(self):
        FreeCAD.Console.PrintMessage( 'Tubos workbench loaded')


FreeCADGui.addWorkbench(Tubos)
