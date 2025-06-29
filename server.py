import os
import shutil
from fastmcp import FastMCP

mcp = FastMCP("utility-server")

@mcp.tool()
def create_folder(path: str):
    os.makedirs(path, exist_ok = True)
    return f"Folder Created: {path}"

@mcp.tool()
def read_file(path: str):
    if not os.path.isfile(path):
        return f"File not Found: {path}"
    with open(path, 'r') as f:
        return f.read()
    
@mcp.tool()
def write_file(path: str, content: str):
    
    try:
        if os.path.exists(path):
            os.chmod(path, 0o666)
            print("File Permissions modified successfully")
        else: 
            print("File not found:", path)
    except PermissionError:
        print("Permission denied: you don't have the necessary permissions to change the permissions of this")
        
    with open(path, 'w') as f:
        f.write(content)
    return f"Written to: {path}"

@mcp.tool()
def move_file(src: str, dest: str):
    os.makedirs(os.path.dirname(dest), exist_ok = True)
    shutil.move(src, dest)
    return f"Moved from {src} to {dest}"

@mcp.tool()
def list_files(directory: str):
    if not os.path.isdir(directory):
        return f"Directory not found: {directory}"
    return os.listdir(directory)

@mcp.tool()
def delete_file(path: str):
    if not os.path.exists(path):
        return f"Path does not exist: {path}"
    if os.path.isfile(path):
        os.remove(path)
        return f"Deleted file: path"
    elif os.path.isdir(path):
        os.rmdir(path)
        return f"Deleted directory: path"
    
if __name__ == "__main__":
    mcp.run()