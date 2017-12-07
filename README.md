# Previz Camera Tools
                
A proof of concept script - Version: 0.1

Previz Camera Tools lets Blender Video Editor control
the camera selection in the 3D View. Which makes it possible
to edit the clip timings in the same screen and at the same
time as cameras and everything else in the 3D Viewport.  

 # Run the script
 1. Run the script in the text-editor in Blender.
 2. Find the functions in the bottom of the right-hand-side
    properties menu of the 3D View.

 # Functions
 A. The button "Add Camera to Sequencer" will add a scene strip
 in the Sequencer with the current camera starting from the
 current frame.

 B. The checkbox "Link Sequencer to 3D View" will link the 
 framenumber and switch cameras in the 3D View. So playing 
 the sequencer will play the sequence in the 3D View and the camera
 work can be edited instantly. 

 # NB. 
 - Jitter in the Sequencer playback means hit "Refresh Sequencer" button. 
 - Only scene strips are supported in the sequencer. 
 - And only cameras from the current scene can be shown in 3d View. 
   (This is a limitation of Blender. There is only one scene pr. 
   Screen) 

# Video on YouTube
https://www.youtube.com/watch?v=b4eQrns5KpQ
