# Previz Camera Tools
                              
       (a proof of concept script)

# Run the script
 1. Run the script in the text-editor.
 2. Find the functions in the bottom of the right-hand-side
    properties menu of the 3D View.

# Functions
 "Walk Navigation" (native Blender function) will give f.p.s. 
 camera control. Shortcuts: q,w,e,a,s,d
 
 "Add Camera to View" by Rockbard will turn the view port
 into a camera. Shortcut: Ctrl+Shift+Num_0
 
 "Cycle Cameras" by CoDEmanX will cycle between cameras. 
 Shortcuts: Ctrl+Shift+Left/Right arrow.
      
 "Add Camera to Sequencer" will add a scene strip
 in the Sequencer with the current camera starting from the
 current frame.

 "Link Sequencer to 3D View" will link the 
 framenumber and switch cameras in the 3D View. So playing 
 the sequencer will play the sequence in the 3D View. So 
 the camera work of the 3d scene can be edited instantly. 

# NB. 
 - Jitter in the Sequencer playback means hit "Refresh Sequencer" button. 
 - Only scene strips are supported in the sequencer. 
 - And only cameras from the current scene can be shown in 3d View. 
   (This is a limitation of Blender. There is only one scene pr. 
   Screen) 

# Ideas for more functions 
   Checkbox: Add camera to sequencer strip from current frame(y/n)
   Buttons(two): Set in and out points 

# API trouble
   Checkbox: Select Strip = Select Camera & update 3D View(missing function detect new strip selected?) 
   Suggest API feature to access local scenes in Sequencer


# Video on YouTube
https://www.youtube.com/watch?v=b4eQrns5KpQ
