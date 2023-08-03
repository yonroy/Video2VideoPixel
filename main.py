from lib import *

def capture_frame(video_file, folder, spacing):
    # Open the video file.
    video = cv2.VideoCapture(video_file)

    # Get the total number of frames in the video.
    num_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)

    # Get the current frame number.
    frame_number = 0

    # Capture the frames and save them to the folder.
    while frame_number < num_frames:
        frame = video.read()[1]

        # Save the frame to the folder.
        file_name = "frame_{}.jpg".format(frame_number)
        cv2.imwrite(os.path.join(folder, file_name), frame)

        # Get the next frame number.
        frame_number += spacing

    # Close the video file.
    video.release()

class image2pixel():

  def __init__(self, pixel_size,palette_path):
    self.pixel_size = pixel_size
    self.palette_path = palette_path
  def create_pixel_art(self,input_image_path, output_image_path ):
      # Mở bản đồ màu
      with open(self.palette_path, 'r') as f:
          color_palette = [tuple(map(int, line.strip().split(','))) for line in f.readlines()]
      
      # Mở hình ảnh gốc
      img = Image.open(input_image_path)
      
      # Lấy kích thước của hình ảnh gốc
      width, height = img.size
      
      # Tính toán kích thước của hình ảnh pixel dựa trên pixel_size
      pixel_width = width // self.pixel_size
      pixel_height = height // self.pixel_size
      
      # Tạo hình ảnh pixel mới với kích thước đã tính toán
      pixel_img = Image.new('RGB', (pixel_width * self.pixel_size, pixel_height * self.pixel_size))
      
      for x in range(pixel_width):
          for y in range(pixel_height):
              # Lấy màu của pixel tại vị trí tương ứng trong hình ảnh gốc
              pixel_color = img.getpixel((x * self.pixel_size, y * self.pixel_size))
              
              # Tìm màu gần nhất trong bản đồ màu
              nearest_color = self.find_nearest_color(pixel_color, color_palette)
              
              # Đặt màu cho tất cả các pixel trong vùng tương ứng
              for i in range(self.pixel_size):
                  for j in range(self.pixel_size):
                      pixel_img.putpixel((x * self.pixel_size + i, y * self.pixel_size + j), nearest_color)
      
      # Lưu hình ảnh pixel
      pixel_img.save(output_image_path)

  def find_nearest_color(self,target_color, color_palette):
      # Tìm màu gần nhất trong bản đồ màu
      min_distance = float('inf')
      nearest_color = None
      for color in color_palette:
          distance = self.color_distance(target_color, color)
          if distance < min_distance:
              min_distance = distance
              nearest_color = color
      
      return nearest_color

  def color_distance(self,color1, color2):
      # Tính khoảng cách Euclidean giữa hai màu sắc
      r1, g1, b1 = color1
      r2, g2, b2 = color2
      return ((r2 - r1) ** 2 + (g2 - g1) ** 2 + (b2 - b1) ** 2) ** 0.5


if __name__ == "__main__":


  # # Đường dẫn để lưu bản đồ màu
  palette_path = "palette.txt"

  # Đường dẫn để lưu hình ảnh pixel
  output_image_path = "output"

  # Kích thước của pixel (càng lớn thì càng ít pixel)
  pixel_size = 5

   # The path to the video file.
  video_file = "video.mp4"

  # The path to the folder where the images will be saved.
  folder = "frames"

  # The spacing between frames.
  spacing = 10

  # Capture the frames and save them to the folder.
  # capture_frame(video_file, folder, spacing)
  path_images = read_images_from_folder(folder)

  Img2Pixl = image2pixel(pixel_size,palette_path)
  for input_path in path_images:
    print(output_image_path+input_path[6:])
    Img2Pixl.create_pixel_art(input_path,output_image_path+input_path[6:])