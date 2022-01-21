import moviepy.editor as mp
clip = mp.VideoFileClip(r"C:\Users\butterfly\Downloads\solar.mp4")
clip.audio.write_audiofile("movie_audio.mp3")