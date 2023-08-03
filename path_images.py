import os



def read_images_from_folder(folder):
    path_images = []

    # Get the list of all files in the folder.
    files = os.listdir(folder)

    # Iterate over the files and load the images.
    for file in files:
        if file.endswith(".jpg") or file.endswith(".png"):
            path_image = folder+ "/" + file
            path_images.append(path_image)
    def extract_frame_number(frame_path):
        return int(frame_path.split('_')[1].split('.')[0])
    path_images.sort(key=extract_frame_number)
    return path_images

if __name__ == "__main__":
    # The path to the folder where the images are stored.
    folder = "frames"

    path_images = read_images_from_folder(folder)

   
    print(path_images)
  