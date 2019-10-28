ffmpeg -framerate 15 -pattern_type glob -i 'images/snapshots/*.png'  -c:v libx264 -pix_fmt yuv420p out.mp4

