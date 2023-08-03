from lib import *

def convert_images_to_video(path_images, output_file, fps):
    

    # Get the list of all files in the folder.
    images = []
    for filename in path_images:
        print(filename)
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        images.append(img)

    # Create the video writer.
    video = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), fps, (images[0].shape[1], images[0].shape[0]))

    # Write the images to the video file.
    for image in images:
        video.write(image)

    # Close the video writer.
    video.release()

if __name__ == "__main__":
    # The path to the folder where the images are stored.
    folder = "output"

    # The path to the output video file.
    output_file = "video.mp4"

    # The frames per second of the video.
    fps = 10

    path_images = read_images_from_folder(folder)
    # Convert the images to a video.
    convert_images_to_video(path_images, output_file, fps)