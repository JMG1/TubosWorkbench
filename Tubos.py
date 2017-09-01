# -*- coding: utf-8 -*-
# Javier Martínez García Agosto 2017
# TUBOS WORKBENCH
import os
import FreeCAD
import Part

__dir__ = os.path.dirname(__file__)

######################### RECTANGULAR TUBE #####################################
class RectangularTube:
    def __init__(self, obj):
        obj.addProperty("App::PropertyFloat", "width" ).width = 50.0
        obj.addProperty("App::PropertyFloat", "height" ).height = 20.0
        obj.addProperty("App::PropertyFloat", "length" ).length = 1000.0
        obj.addProperty("App::PropertyFloat", "thickness" ).thickness = 1.5
        obj.addProperty("App::PropertyFloat", "r" ).r = 1.5
        obj.Proxy = self

    def execute(self, fp):
        fp.Shape = self.doRectangularTube( fp.width, fp.height, fp.thickness, fp.length, fp.r)
        fp.Label = str(fp.width)+'x'+str(fp.height)+'x'+str(fp.thickness)+'x'+str(fp.length)
    
    def onChanged( self, fp, prop ):
        if prop == "width":
            fp.Shape = self.doRectangularTube( fp.width, fp.height, fp.thickness, fp.length, fp.r)
            
    
    def doRectangularTube(self, w=50.0, h=20.0, th=1.5, length=1000.0, r=1.0 ):
        outer_profile = Part.makePlane( w, h, FreeCAD.Vector(0,0,0), FreeCAD.Vector(1,0,0) )
        inner_profile = Part.makePlane( w-2*th, h-2*th, FreeCAD.Vector(0,-th,th), FreeCAD.Vector(1,0,0) )
        tube_profile = outer_profile.cut(inner_profile)
        tube = tube_profile.extrude( FreeCAD.Vector( length, 0, 0 ) )
        if r > 0.0:
            # find 4 longer edges to
            edges_to_round = []
            for edge in tube.Edges:
                if (edge.Length > w+1) and (edge.Length > h+1):
                    edges_to_round.append( edge )

            tube = tube.makeFillet( r, edges_to_round)
        
        return tube


class ViewProviderRectangularTube:
    def __init__(self, obj):
        obj.Proxy = self

    def getDefaultDisplayMode(self):
        return "Flat Lines"

    def getIcon(self):
        return __dir__ + '/icons/rectangularTube.svg'


class CreateRectangularTube:
    def GetResources(self):
        return { 'Pixmap': __dir__ + '/icons/rectangularTube.svg',
                'MenuText': 'Rectangular tube',
                'ToolTip':'Create a rectangular tube object' }

    def IsActive(self):
        return True

    def Activated(self):
        tube_obj = FreeCAD.ActiveDocument.addObject('Part::FeaturePython', 'RectangularTube')
        RectangularTube( tube_obj )
        ViewProviderRectangularTube( tube_obj.ViewObject )
        FreeCAD.ActiveDocument.recompute()


######################### ROUND TUBE ###########################################
class RoundTube:
    def __init__(self, obj):
        obj.addProperty("App::PropertyFloat", "diameter" ).diameter = 20.0
        obj.addProperty("App::PropertyFloat", "length" ).length = 1000.0
        obj.addProperty("App::PropertyFloat", "thickness" ).thickness = 1.5
        obj.Proxy = self

    def execute(self, fp):
        fp.Shape = self.doCircularTube( fp.diameter, fp.thickness, fp.length )
        fp.Label = 'Ø' + str(fp.diameter) + 'x' + str(fp.thickness) + 'x' + str(fp.length)

    def doCircularTube( self, d=20.0, th=1.5, length=1000.0 ):
        outer_profile = Part.makeCircle( d/2.0, FreeCAD.Vector(0,0,0), FreeCAD.Vector(1,0,0) )
        inner_profile = Part.makeCircle( (d/2.0)-th, FreeCAD.Vector(0,0,0), FreeCAD.Vector(1,0,0) )
        tube_profile = Part.Face([Part.Wire( [outer_profile] ),Part.Wire([inner_profile] )] )
        tube = tube_profile.extrude( FreeCAD.Vector( length, 0, 0 ) )
        return tube


class ViewProviderRoundTube:
    def __init__(self, obj):
        obj.Proxy = self

    def getDefaultDisplayMode(self):
        return "Flat Lines"

    def getIcon(self):
        return __dir__ + '/icons/roundTube.svg'


class CreateRoundTube:
    def GetResources(self):
        return { 'Pixmap': __dir__ + '/icons/roundTube.svg',
                'MenuText': 'Round tube',
                'ToolTip':'Create a round tube object' }

    def IsActive(self):
        return True

    def Activated(self):
        tube_obj = FreeCAD.ActiveDocument.addObject('Part::FeaturePython', 'RoundTube')
        RoundTube( tube_obj )
        ViewProviderRoundTube( tube_obj.ViewObject )
        FreeCAD.ActiveDocument.recompute()





if FreeCAD.GuiUp:
    FreeCAD.Gui.addCommand('CreateRectangularTube', CreateRectangularTube() )
    FreeCAD.Gui.addCommand('CreateRoundTube', CreateRoundTube() )
