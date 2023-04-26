# ARMM
The axis-referenced morphometric model of hippocampus.

This repository storges code and results for the paper "Mapping lamellar organization to the MRI-based hippocampal morphology by an axis-referenced morphometric model". 
The axis-referenced morphometric model (ARMM) represent the hippocampus by longitudinal lamellar architecture. This model has been verified to precisely measure morphometric features and shape variations due to the neurodegeneration. The three advantages of the model:
1)	By characterizing lamellae (functional units) along the entire long-axis, ARMM provides finer structural subdivisions in the longitudinal of the hippocampus. 
2)	ARMM allows to stably align hippocampi across individuals with variable morphologies by a uniform planar orthogonal coordinate system. 
3)	The method offers a way to generate anatomical motivated structural features that characterizes aging and diseases associated damage of hippocampus.

The full code of this project and an automatic pipeline to generate population hippocampi on 3T MRI will be avaiable soon.

![github_4](https://user-images.githubusercontent.com/47969752/234547595-0a032eaa-b870-43c1-81f0-ae9082a5f831.png)



Files in this repository:

All vtk files can be viewed by visulization tools such as 3DSlicer, paraview...or by code in ViewResults.py.

hippo.vtk: Original hippocampal surface.

IMS.vtk: the inscribed surface within the hippocampal shape, the superior-inferior symmetric surface of the hippocampal shape, with long-axis, longitudinal and transverse axes on it.

ImpliedSurfAll_LinesHigh2_NotCorrected.vtk: The conformal parameterized boundary surface of the hippocampus. The scalar on the surface reffers to subfield subdivisions. The surface is the implied surface from the ARMM, not corrected to strictly agree with the original hippocampal boundary surface.

LamellarOnSurface.vtk: Lamellar organized hippocampal surface.

Refined_skelpt_HippoLines2.vtk: Points on the IMS.

RepairSkeleton_HippoLines2.vtk: Points on the implied boundary surface by skeletal model.

ViewResults.py: a simple python code to visualize the vtk file.



Hippocampal local atrophy pattern measured by ARMM during normal to Alzheimer's Disease progression:

![21](https://user-images.githubusercontent.com/47969752/234550390-33353918-1130-407e-8a75-0a9eb13b0390.gif)
