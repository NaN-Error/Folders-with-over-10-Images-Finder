import os
import subprocess

# Find folders with more than 10 pictures

def count_images_in_folder(folder_path):
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}
    image_count = 0
    
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path) and os.path.splitext(item_path)[1].lower() in image_extensions:
            image_count += 1

    return image_count

def find_folders_with_images(base_path, min_images=10):
    result_folders = []
    
    for folder_name in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder_name)
        
        if os.path.isdir(folder_path):
            image_count = count_images_in_folder(folder_path)
            print(f"Checked {folder_path}: {image_count} images")  # Debug print
            
            if image_count > min_images:
                result_folders.append(folder_path)
    
    return result_folders

def save_results_to_txt(result_folders, output_file='folders_with_images.txt'):
    try:
        with open(output_file, 'w') as f:
            for folder in result_folders:
                f.write(folder + '\n')
        print(f"Results saved to {output_file}")  # Debug print
    except Exception as e:
        print(f"Failed to write to {output_file}: {e}")  # Debug print

def open_file(file_path):
    try:
        if os.name == 'nt':  # For Windows
            os.startfile(file_path)
        elif os.name == 'posix':  # For macOS and Linux
            subprocess.call(('open', file_path))
    except Exception as e:
        print(f"Failed to open {file_path}: {e}")  # Debug print

def main():
    base_path = r'R:\Negocio\OneDrive\Work\Business\Inventory\To Sell'
    if not os.path.exists(base_path):
        print(f"Base path {base_path} does not exist.")  # Debug print
        return
    
    result_folders = find_folders_with_images(base_path)
    output_file = 'folders_with_images.txt'
    save_results_to_txt(result_folders, output_file)
    open_file(output_file)

if __name__ == '__main__':
    main()
