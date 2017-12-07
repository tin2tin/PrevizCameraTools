#
# P r e v i z   C a m e r a   T o o l s
#                
#             by Tin2tin
#                
#       (a proof of concept script)

# Version: 0.1

# Run the script:
# 1. Run the script in the text-editor.
# 2. Find the functions in the bottom of the right-hand-side
#    properties menu of the 3D View.

# Functions:
# The Button "Add Camera to Sequencer" will add a scene strip
# in the Sequencer with the current camera starting from the
# current frame.

# The checkbox "Link Sequencer to 3D View" will link the 
# framenumber and switch cameras in the 3D View. So playing 
# the sequencer will play the sequence in the 3D View. So 
# the camera work of the 3d scene can be edited instantly. 

# NB.: 
# - Jitter in the Sequencer playback means hit "Refresh Sequencer" button. 
# - Only scene strips are supported in the sequencer. 
# - And only cameras from the current scene can be shown in 3d View. 
#   (This is a limitation of Blender. There is only one scene pr. 
#   Screen) 

# Ideas for more functions: 
#   Checkbox: Add camera to sequencer strip from current frame(y/n)
#   Buttons(two): Set in and out points 
#   Buttons(two): Cycle cameras
#   Button: Add and fit camera to view
#   Button: "Walk navigation"

# API trouble:
#   Checkbox: Select Strip = Select Camera & update 3D View(missing function detect new strip selected?) 
#   Suggest API feature to access local scenes in Sequencer

import bpy

# ------------------------------------------------------------------------
#     Make Previz panel
# ------------------------------------------------------------------------

class PrevizMakerPanel(bpy.types.Panel) :
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"
    bl_label = "Previz Camera Tools"

    def draw(self, context) :
        TheCol = self.layout.column(align = False)
        scene = context.scene   
        TheCol.operator("view3d.make_previz", text = "Add Camera to Sequencer")  
        TheCol.prop(context.scene, "make_Previz_LinkSequencer") 
        
                # check if bool property is enabled
        if (context.scene.make_Previz_LinkSequencer == True):
            syncSceneLength()
            attachAsHandler()
        else:
            detachAsHandler()                      

class MakePreviz(bpy.types.Operator) :
    bl_idname = "view3d.make_previz"
    bl_label = "Add Previz"
    bl_options = {"UNDO"}

    def invoke(self, context, event) :
        addSceneStripInOut()
        return {"FINISHED"}


# ------------------------------------------------------------------------
#     3D Viewport Cameras to Sequencer
# ------------------------------------------------------------------------

        #update at frame change
def syncSceneLength(*pArgs):
    scn = bpy.context.scene
    seq = scn.sequence_editor
    cf = scn.frame_current
    for i in seq.sequences:    
        try:
            if (i.frame_final_start <= cf
            and i.frame_final_end > cf
            and i.type == "SCENE" #Must be OpenGL strip
            and i.scene.name==bpy.context.scene.name #Only if current scene in scene-strip
            and not i.mute): #Must be unmute strip
 
                for area in bpy.context.screen.areas:
                    if area.type == 'VIEW_3D': 
                        # Avoid Camera Local View                        
                        space = area.spaces[0]
                        if space.local_view: #check if using local view
                            for region in area.regions:
                                if region.type == 'WINDOW':
                                    override = {'area': area, 'region': region} #override context
                                    bpy.ops.view3d.localview(override) #switch to global view

                        bpy.context.scene.camera = bpy.data.objects[i.scene_camera.name] # Select camera as view
                        area.spaces.active.region_3d.view_perspective = 'CAMERA' # Use camera view            
                        
        except AttributeError:
                pass
  
        #Set 3D View to Global. Cameras can't be switched in local.      
def set3dViewGlobal():
    for region in area.regions:
        if region.type == 'WINDOW':
            override = {'area': area, 'region': region} #override context
            bpy.ops.view3d.localview(override) #switch to global view  
            
            
# ------------------------------------------------------------------------
#     Un/link Cameras from Video Editing
# ------------------------------------------------------------------------                        

        #setup update at frame change
def attachAsHandler():
    for f in bpy.app.handlers.frame_change_pre:
        bpy.app.handlers.frame_change_pre.remove(f)
    bpy.app.handlers.frame_change_pre.append(syncSceneLength)
    
def detachAsHandler():
    bpy.app.handlers.frame_change_pre.clear()    


# ------------------------------------------------------------------------
#     Add Camera as Scene strip in Sequencer
# ------------------------------------------------------------------------

def addSceneStripInOut():
        if not bpy.context.scene.sequence_editor:
            bpy.context.scene.sequence_editor_create()   
        scn = bpy.context.scene
        seq = scn.sequence_editor
        cf = scn.frame_current
        # Use current frame for insert position.
        addSceneIn = cf
        addSceneOut = cf+100
        addSceneChannel = 2
        addSceneTlStart = cf        
        newScene=bpy.context.scene.sequence_editor.sequences.new_scene('Scene', bpy.context.scene, addSceneChannel, addSceneTlStart)
        bpy.context.scene.sequence_editor.sequences_all[newScene.name].scene_camera = bpy.data.objects[bpy.context.scene.camera.name]
        bpy.context.scene.sequence_editor.sequences_all[newScene.name].animation_offset_start = addSceneIn
        bpy.context.scene.sequence_editor.sequences_all[newScene.name].frame_final_end = addSceneOut
        bpy.context.scene.sequence_editor.sequences_all[newScene.name].frame_start = cf        


# ------------------------------------------------------------------------
#     Register/Unregister
# ------------------------------------------------------------------------ 

def register() :
    bpy.utils.register_class(MakePreviz)
    bpy.utils.register_class(PrevizMakerPanel)
    bpy.types.Scene.make_Previz_LinkSequencer = bpy.props.BoolProperty \
      (
        name = "Link Sequencer to 3D View",
        description = "Let Sequencer control 3D View",
        default = False
      )

def unregister() :
    bpy.utils.unregister_class(MakePreviz)
    bpy.utils.unregister_class(PrevizMakerPanel)
    del bpy.types.Scene.make_Previz_LinkSequencer

if __name__ == "__main__" :
    register()

#unregister()

