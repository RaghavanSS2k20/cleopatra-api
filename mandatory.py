from pathlib import Path

def get_folder_size(path):
  """Calculates the total size of a folder and its subfolders."""
  total_size = 0
  for item in path.iterdir():
    if item.is_file():
      total_size += item.stat().st_size
    elif item.is_dir():
      total_size += get_folder_size(item)
    elif item.is_dir() and item.name != '$Recycle.Bin':
      total_size += get_folder_size(item)
  return total_size

def analyze_disk_space(root_dir):
  """Analyzes disk space usage for a directory and its subdirectories."""
  total_size = 0
  folder_sizes = {}
  for item in Path(root_dir).iterdir():
    if item.is_dir():
      size = get_folder_size(item)
      total_size += size
      folder_sizes[item.name] = size
  print(f"Total Disk Space Used: {total_size} bytes")
  # Print folder sizes in a user-friendly format (e.g., convert to MB/GB)
  for folder, size in folder_sizes.items():
    print(f"{folder}: {size} bytes (convert to desired unit manually)")

# Example usage (replace 'C:' with your desired drive)
analyze_disk_space('C:')
