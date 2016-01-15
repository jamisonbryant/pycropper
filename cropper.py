import os

from PIL import Image

input_dir = 'img'
output_dir = 'out'

def process(file):
    # Print out some file information
    image = Image.open(file)
    image_width = image.size[0]
    image_height = image.size[1]

    print("Image type: " + image.format + "; mode: " + image.mode + "; dimensions: " +
          str(image_width) + "x" + str(image_height))

    # Sample background color
    def rgb_tuple_to_str(tuple):
        return 'rgb(' + str(tuple[0]) + ', ' + str(tuple[1]) + ', ' + str(tuple[2]) + ')'

    def is_like_bg_color(color):
        color_r, color_g, color_b = color[0], color[1], color[2]
        bg_r, bg_g, bg_b = bg_color[0], bg_color[1], bg_color[2]
        r_similar, g_similar, b_similar = False, False, False
        tolerance = 11

        if color_r in range(bg_r - tolerance, bg_r + tolerance):
            r_similar = True
            
        if color_g in range(bg_g - tolerance, bg_g + tolerance):
            g_similar = True
            
        if color_b in range(bg_b - tolerance, bg_b + tolerance):
            b_similar = True

        return r_similar and g_similar and b_similar

    print("Sampling background color...")
    pixel_map = image.load()
    x_offset = image_width * 0.05
    y_offset = image_height * 0.05

    ul_color = pixel_map[x_offset, y_offset]
    ur_color = pixel_map[image_width - x_offset, y_offset]
    ll_color = pixel_map[x_offset, image_height - y_offset]
    lr_color = pixel_map[image_width - x_offset, image_height - y_offset]
    bg_color = ()

    # print("Upper left color sample: " + rgb_tuple_to_str(ul_color))
    # print("Upper right color sample: " + rgb_tuple_to_str(ur_color))
    # print("Lower left color sample: " + rgb_tuple_to_str(ll_color))
    # print("Lower right color sample: " + rgb_tuple_to_str(lr_color))

    if ul_color == ur_color and ur_color == ll_color and ll_color == lr_color:
        bg_color = ul_color
        print("Sampled background color: " + rgb_tuple_to_str(ul_color))

    # Search for top edge
    print("Searching for top edge...")
    top_edge_coords = []

    for i in range(0, image_width, int(image_width / 10)):
        for y in range(0, image_height - 1):
            if not is_like_bg_color(pixel_map[i, y]):
                top_edge_coords.append(y)
                break

    top_edge_coord = top_edge_coords[0]
    for c in top_edge_coords:
        if c < top_edge_coord:
            top_edge_coord = c

    print("Found top edge at y = " + str(top_edge_coord))

    # Search for bottom edge
    print("Searching for bottom edge...")
    bottom_edge_coords = []

    for i in range(0, image_width, int(image_width / 10)):
        for y in range(image_height - 1, 0, -1):
            if not is_like_bg_color(pixel_map[i, y]):
                bottom_edge_coords.append(y)
                break

    bottom_edge_coord = bottom_edge_coords[0]
    for c in bottom_edge_coords:
        if c > bottom_edge_coord:
            bottom_edge_coord = c

    print("Found bottom edge at y = " + str(bottom_edge_coord))

    # Search for left edge
    print("Searching for left edge...")
    left_edge_coords = []

    for i in range(0, image_height, int(image_height / 10)):
        for x in range(0, image_width - 1):
            if not is_like_bg_color(pixel_map[x, i]):
                left_edge_coords.append(x)
                break

    left_edge_coord = left_edge_coords[0]
    for c in left_edge_coords:
        if c < left_edge_coord:
            left_edge_coord = c

    print("Found left edge at x = " + str(left_edge_coord))
    
    # Search for right edge
    print("Searching for right edge...")
    right_edge_coords = []

    for i in range(0, image_height, int(image_height / 10)):
        for x in range(image_width - 1, 0, -1):
            try:
                if not is_like_bg_color(pixel_map[x, i]):
                    right_edge_coords.append(x)
                    break
            except IndexError:
                pass

    right_edge_coord = right_edge_coords[0]
    for c in right_edge_coords:
        if c > right_edge_coord:
            right_edge_coord = c

    print("Found right edge at x = " + str(right_edge_coord))

    # Crop image
    print("Cropping image...")
    cropped_image = image.crop((left_edge_coord, top_edge_coord, right_edge_coord, bottom_edge_coord))

    # Display original and cropped images
    # image.show()
    # cropped_image.show()
    # os.system('pause')

    # Save image to output dir
    file_name, file_ext = os.path.splitext(file)
    output_file_name = os.path.basename(file_name) + '_processed' + file_ext
    output_file_path = os.path.join(os.getcwd(), output_dir, output_file_name)
    print("Saving image to " + output_file_path)
    cropped_image.save(output_file_path)

def main():
    image_exts = [ '.jpg', '.jpeg', '.png' ]
    input_dir = os.path.join(os.getcwd(), 'img')
    output_dir = os.path.join(os.getcwd(), 'out')

    # Create output directory, if not present
    try:
        os.stat(output_dir)
    except:
        os.mkdir(output_dir)

    # Iterate over working directory
    for file in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file)
        file_name, file_ext = os.path.splitext(file_path)

        # Check if file is an image file
        if file_ext not in image_exts:
            print("Skipping " + file + " (not an image file)")
            continue
        else:
            print()
            print("Processing " + file + "...")
            process(file_path)

if __name__ == '__main__':
    main()