import cv2
import numpy as np
from PIL import Image, ImageEnhance

def split_image_into_grids(image, grid_size):
    """
    Split the image into smaller grids of size grid_size x grid_size.
    """
    height, width, _ = image.shape
    grids = []
    
    for y in range(0, height, grid_size):
        for x in range(0, width, grid_size):
            grid = image[y:y+grid_size, x:x+grid_size]
            grids.append(grid)
    
    return grids

def enhance_contrast(grid, factor=1.5):
    """
    Enhance the contrast of a single grid using PIL's ImageEnhance.
    """
    grid_pil = Image.fromarray(grid)
    enhancer = ImageEnhance.Contrast(grid_pil)
    enhanced_grid = enhancer.enhance(factor)
    return np.array(enhanced_grid)

def reconstruct_image(grids, original_shape, grid_size):
    """
    Reconstruct the image from the list of grids.
    """
    height, width, _ = original_shape
    reconstructed_image = np.zeros((height, width, 3), dtype=np.uint8)
    
    index = 0
    for y in range(0, height, grid_size):
        for x in range(0, width, grid_size):
            grid_height, grid_width, _ = grids[index].shape
            reconstructed_image[y:y+grid_height, x:x+grid_width] = grids[index]
            index += 1
    
    return reconstructed_image

def process_image(image_path, grid_size=32, contrast_factor=1.5):
    """
    Main function to process the image.
    """
    # Load the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB for PIL
    
    # Split into grids
    grids = split_image_into_grids(image, grid_size)
    
    # Enhance contrast of each grid
    enhanced_grids = [enhance_contrast(grid, contrast_factor) for grid in grids]
    
    # Reconstruct the image
    reconstructed_image = reconstruct_image(enhanced_grids, image.shape, grid_size)
    
    # Save or display the result
    reconstructed_image = cv2.cvtColor(reconstructed_image, cv2.COLOR_RGB2BGR)  # Convert back to BGR for OpenCV
    cv2.imwrite("output_image.jpg", reconstructed_image)
    cv2.imshow("Enhanced Image", reconstructed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
process_image("/home/su-rays/projects/skills/libraries/opencv/data/elephant.jpg", grid_size=1, contrast_factor=3.0)