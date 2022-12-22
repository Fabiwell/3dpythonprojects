# import pygame
# import pywavefront
# from pywavefront import visualization

# # Initialize Pygame and create a window
# pygame.init()
# screen = pygame.display.set_mode((640, 480))

# # Load the OBJ file
# mesh = visualization.Wavefront(r"C:\Users\gebruiker\OneDrive\PythonScript\3dpython\objects\cube.mtl")

# # Render the OBJ file
# mesh.draw()

# # Update the display
# pygame.display.flip()

# # Run the Pygame loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# # Clean up
# pygame.quit()


import bpy

# Import the OBJ file
bpy.ops.import_scene.obj(filepath=r"C:\Users\gebruiker\OneDrive\PythonScript\3dpython\objects\FinalBaseMesh.obj")

# Render the scene
bpy.ops.render.render(write_still=True)