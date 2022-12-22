# ExportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
import bpy
import json
import mathutils
import os

from bpy_extras.io_utils import ExportHelper, axis_conversion
from bpy.props import StringProperty, BoolProperty, EnumProperty, FloatProperty, FloatVectorProperty, IntProperty
from bpy.types import Operator
from mathutils import Matrix

class BasicModelling(Operator, ExportHelper):
	"""Export objects as a model with normals """ 
	bl_idname = "export_mesh.basic_json"
	bl_label = "Export (.json)"

	filename_ext = ".json"

	use_mesh_modifiers = BoolProperty(name="Apply Modifiers", description="Apply Modifiers to the exported mesh", default=True)            
	
	use_normals = BoolProperty(name="Use Normals", description="Include normals in meshes", default=True)	
	
	axis_forward = EnumProperty(name="Forward",items=(('X', "X Forward", ""),('Y', "Y Forward", ""),('Z', "Z Forward", ""),('-X', "-X Forward", ""),('-Y', "-Y Forward", ""),('-Z', "-Z Forward", ""),),default='Z',)	
	axis_up = EnumProperty(name="Up",items=(('X', "X Up", ""),('Y', "Y Up", ""),('Z', "Z Up", ""),('-X', "-X Up", ""),('-Y', "-Y Up", ""),('-Z', "-Z Up", ""),),default='Y',)

	def execute(self, context):
		self.global_matrix = axis_conversion(to_forward=self.axis_forward,to_up=self.axis_up).to_4x4()
	
		return self.write_some_data(context, self.filepath)		 

	def write_some_data(self, context, filepath):
		print("running write_some_data...")	 

		basename = os.path.basename(filepath)
		modelName = os.path.splitext(basename)[0] + ".bsm"
		modelPath = os.path.join(os.path.split(filepath)[0], modelName)
		
		metaFile = filepath
		self.writeHeader(metaFile, modelName)
		self.writeModel(context, modelPath)
		print(basename)

		return {'FINISHED'}
	
	def writeHeader(self, metaFile, modelFile):
		f = open(metaFile, 'w', encoding='utf-8')  
		
		blob = {"source" : modelFile}		
	
		json.dump(blob, f, indent="\t", sort_keys=True) 
		f.close()

	def writeModel(self, context, modelfile):
		f = open(modelfile, 'w', encoding='utf-8')  
		
		blob = {}
		
		scene = context.scene				

		if bpy.ops.object.mode_set.poll():
			bpy.ops.object.mode_set(mode='OBJECT')		
		
		if self.global_matrix is None:
			from mathutils import Matrix
			self.global_matrix = Matrix()		
		
		meshes = []
		
		# Get all objects
		for ob_main in  scene.objects:

			if ob_main.type not in {'MESH'}:
				print(ob_main.name, 'is not a mesh')
				continue				
			
			# ignore dupli children
			if ob_main.parent and ob_main.parent.dupli_type in {'VERTS', 'FACES'}:
				# XXX
				print(ob_main.name, 'is a dupli child - ignoring')
				continue

			obs = []
			if ob_main.dupli_type != 'NONE':
				# XXX
				print('creating dupli_list on', ob_main.name)
				ob_main.dupli_list_create(scene)

				obs = [(dob.object, dob.matrix) for dob in ob_main.dupli_list]

				# XXX debug print
				print(ob_main.name, 'has', len(obs), 'dupli children')
			else:
				obs = [(ob_main, ob_main.matrix_world)]

			for ob, ob_mat in obs:		
				output = self.writeMesh(ob, scene, ob_mat)
				if output is not None:
					meshes.append(output)
	
		blob["meshes"] = meshes
	
		json.dump(blob, f, indent="\t", sort_keys=True)
		f.close()
	
	def writeMesh(self, obj, scene, local_matrix):
		try:		
			if self.use_mesh_modifiers and obj.modifiers:
				mesh = obj.to_mesh(scene, True, 'PREVIEW')
			else:
				mesh = obj.data.copy()			
		except RuntimeError:
			return None		

		final_matrix = self.global_matrix * local_matrix		
		
		mesh.transform(final_matrix)
		mesh_triangulate(mesh)			
			
		if self.use_normals:
			mesh.calc_normals()
		
		location, rotation, scale = final_matrix.decompose()
		
		objectData = {"name" : obj.name, "scale":writeVec3(scale), "location":writeVec3(location), "rotation":writeQuaternion(rotation)}
		
		vertexData = []
		
		for v in mesh.vertices:
			vertex = {}
		
			vertex["position"] = writeVec3(v.co)		
			
			if self.use_normals:
				vertex["normal"] = writeVec3(v.normal)
			
			vertexData.append(vertex)
		
		objectData["vertices"] = vertexData
		
		meshSections = {}
		
		for p in mesh.polygons:	
			key = p.material_index
			section = None
			if key in meshSections:
				section = meshSections[key]
			else:                           
				section = {"indexBuffer" : [], "materialIndex": key}
				if len(mesh.materials) > 0:
					section["material"] = mesh.materials[key].name
				meshSections[key] = section
			section["indexBuffer"].append(list(p.vertices))
		
		objectData["faces"] = list(meshSections.values())		
		
		return objectData

def writeQuaternion(quat):
	return {"x" :quat[0], "y" : quat[1], "z": quat[2], "w": quat[3],}  

def writeVec3(vertex):
	return {"x" :vertex[0], "y" : vertex[1], "z": vertex[2]}  
		
		
def mesh_triangulate(me):
    import bmesh
    bm = bmesh.new()
    bm.from_mesh(me)
    bmesh.ops.triangulate(bm, faces=bm.faces)
    bm.to_mesh(me)
    bm.free()			
#
		# Only needed if you want to add into a dynamic menu
def menu_func_export(self, context):
	self.layout.operator(BasicModelling.bl_idname, text="Basic Model (.json)")

def unregister():
	bpy.utils.unregister_class(BasicModelling)
	bpy.types.INFO_MT_file_export.remove(menu_func_export)

def register():
	bpy.utils.register_class(BasicModelling)
	bpy.types.INFO_MT_file_export.append(menu_func_export)   

if __name__ == "__main__":
#   unregister()

	register()

	# test call
	bpy.ops.export_mesh.basic_json('INVOKE_DEFAULT')
#   print("HELLO")