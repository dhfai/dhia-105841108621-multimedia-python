from PIL import Image
from PIL import ImageFilter

from pydub import AudioSegment


# Memuat gambar
image = Image.open('images/image.png')

# Menyimpan gambar
image.save('images/result.jpg')

# cropping
cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('images/cropped_result.jpg')

# resize
resized_image = cropped_image.resize((100, 100))
resized_image.save('images/resized_result.jpg')


# filtering
filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('images/filtered_result.jpg')


# Memuat file audio
audio = AudioSegment.from_file('audio/musik.mp3')

# Menyimpan file audio
audio.export('audio/result.mp3', format='mp3')

clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
clipped_audio.export('audio/clipped_result.mp3', format='mp3')

combined_audio = audio + clipped_audio
combined_audio.export('audio/combined_result.mp3', format='mp3')

audio.export('audio/result.wav', format='wav')


louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
louder_audio.export('audio/louder_result.mp3', format='mp3')