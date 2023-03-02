#!/usr/bin/env python
from __future__ import print_function
import numpy as np
import math
import vtk
from vtk.util.numpy_support import vtk_to_numpy
import pyvista as pv
# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonCore import (
    mutable,
    vtkPoints
)
from vtkmodules.vtkCommonDataModel import vtkPolygon

if __name__ == '__main__':
   surf = 'hippo.vtk' 
   surf_reader = vtk.vtkPolyDataReader()
   surf_reader.SetFileName(surf)
   surf_reader.Update()
   surf_vtk1 = surf_reader.GetOutput()    

   surf = 'IMS.vtk' 
   surf_reader = vtk.vtkPolyDataReader()
   surf_reader.SetFileName(surf)
   surf_reader.Update()
   surf_vtk2 = surf_reader.GetOutput()   
    
   pt = 'Refined_skelpt_HippoLines2.vtk'  
   pt_reader = vtk.vtkPolyDataReader()
   pt_reader.SetFileName(pt)
   pt_reader.Update()
   pt_vtk = pt_reader.GetOutput()

   ps = 'RepairSkeleton_HippoLines2.vtk' 
   ps_reader = vtk.vtkPolyDataReader()
   ps_reader.SetFileName(ps)
   ps_reader.Update()
   ps_vtk = ps_reader.GetOutput() 

   #Display results
   num_pt = pt_vtk.GetNumberOfPoints()
   pt_array = np.zeros((num_pt, 3))    
   num_ps = ps_vtk.GetNumberOfPoints()
   ps_array = np.zeros((num_ps, 3))
   p = pv.Plotter()
   p.add_mesh(surf_vtk1, color='orange', opacity=0.4)
   p.add_mesh(surf_vtk2, color='yellow', opacity=0.8)
   for i in range(num_pt):
       pt = np.array(pt_vtk.GetPoint(i))
       ps = np.array(ps_vtk.GetPoint(i))
       spoke = pt - ps
       spoke_length = np.linalg.norm(spoke)
       p.add_mesh(pv.Arrow(ps, spoke, scale=spoke_length), color='red')
   p.show() 

