from PIL import Image
from PIL import ImageShow
import tkinter
import time
import os
import serial
import pygame
from numpy import asarray
from pythonosc import udp_client




n = 96
i = 95
r = -1
VAL = 0
p = 0
bang = 1


ip = "127.0.0.1"
port = 5005

client = udp_client.SimpleUDPClient(ip, port)

import pygame
import numpy as np

def sonify_image(image_path, duration=2.0, freq_range=(100, 1000), sample_rate=44100):
    # Load the image
    img = pygame.image.load("cat.jpg")
    width, height = img.get_size()

    # Convert the image to a numpy array
    pixels = pygame.surfarray.array3d(img)
    red_pixels = pixels[:,:,0]

    # Normalize the pixel values to the range [0, 1]
    norm_pixels = red_pixels / 255.0

    # Reshape the pixel values into a 1D array
    pixel_values = norm_pixels.reshape(-1)

    # Create a time array for the audio signal
    t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)

    # Generate a sine wave with a frequency that varies with the pixel values
    freqs = np.interp(pixel_values, [0, 1], freq_range)
    audio_signal = np.sin(2 * np.pi * freqs * t)

    # Scale the audio signal to the range [-1, 1]
    max_amplitude = np.iinfo(np.int16).max
    audio_signal *= max_amplitude / np.max(np.abs(audio_signal))

    # Convert the audio signal to a byte string for output
    audio_data = audio_signal.astype(np.int16).tobytes()

    # Play the audio data
    pygame.mixer.init(sample_rate, -16, 1)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.load(audio_data)
    pygame.mixer.music.play()


while True:


	#with serial.Serial("com3", 9600) as ser:
	#	line = ser.readline()
	#	VAL = chr(line)


	im1 = Image.open("cat.jpg")
	im2 = im1.copy()
	im2.save("pasted.jpg")
	im3 = Image.open("pasted.jpg")
	print("copied and pasted!")
	time.sleep(2)


	while True:
		if i > r : 
			i -= 1
			client.send_message("/",0)
			img = Image.open("cat.jpg")
			img.save("cat.jpg", quality=i)
			pixels = list(img.getdata())
			w, h = img.size
	#		print(pixels)
	#		time.sleep(5)
	#		print("Compressed, saved and going down, ", end =" ")
	#		print("on run: ", end=" ")
	#		print(i)
	#		time.sleep(0.33)
			#pygame.init()
			#screen=pygame.display.set_mode((w, h))
			#pygame.display.set_caption('Image Lucier')
			#gameIcon = pygame.image.load('hex.jpg')
			#pygame.display.set_icon(gameIcon)
			#image = pygame.image.load("cat.jpg")
			#screen.blit(image,(0,0))
			#pygame.display.flip()
	#		client.send_message("/",bang)
	#		time.sleep(5)
			sonify_image('input_image.jpg', duration=2.0, freq_range=(100, 1000), sample_rate=44100)
		else:
			break
	

	while True:
		if i < n:
			i += 1
			ii = 95
			ii -= 1
			client.send_message("/",0)
			img = Image.open("cat.jpg")
			img.save("cat.jpg", quality=ii)
			pixels = list(img.getdata())
			w, h = img.size
	#		print(pixels)
	#		time.sleep(5)
	#		print("compressed, saved and going up, ", end =" ")
	#		print("on run: ", end=" ")
	#		print(i)
	#		time.sleep(0.5)
			#pygame.init()
			#screen=pygame.display.set_mode((w, h))
			#pygame.display.set_caption('Image Lucier')
			#gameIcon = pygame.image.load('hex.jpg')
			#pygame.display.set_icon(gameIcon)
			#image = pygame.image.load("cat.jpg")
			#screen.blit(image,(0,0))
			#pygame.display.flip()
	#		client.send_message("/",bang)
	#		time.sleep(5)
			sonify_image('input_image.jpg', duration=2.0, freq_range=(100, 1000), sample_rate=44100)
		else:
			break

	#print("Completed without errors!")
	#im1.paste(im3,(0,0))
	#im1.save("cat.jpg")
	#time.sleep(2)
	#print("concoctenated alllll the images!")
	#os.remove("pasted.jpg")
	#print("deleted the copy, only OG's in hare, yo.")
	time.sleep(1)



