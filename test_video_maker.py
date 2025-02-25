import unittest
import cv2
from pathlib import Path
import shutil
import os

class TestVideoMaker(unittest.TestCase):
    
    def test_app_run(self):
        # Get the filename from the output path
        pngs = []
        png_names = os.listdir("pictures")
        for png in png_names:
            pngs.append("pictures/" + png)
        print(pngs)
        output = "output/example.mp4"
        filename = Path(output).name
        fps = 24
        print(f'Creating video "{filename}" from images "{pngs}"')

        # Load the first image to get the frame size
        frame = cv2.imread(pngs[0])
        height, width, layers = frame.shape

        # Create a VideoWriter object to write the video file
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video = cv2.VideoWriter(filename=filename, fourcc=fourcc, fps=fps, frameSize=(width, height))

        # Loop through the input images and add them to the video
        for image_path in pngs:
            print(f'Adding image "{image_path}" to video "{output}"... ')
            video.write(cv2.imread(image_path))

        # Release the VideoWriter and move the output file to the specified location
        cv2.destroyAllWindows()
        video.release()

        shutil.move(filename, output)