import os

def get_project_root():
    path = os.path.abspath(os.path.dirname(__file__))
    #normalized_path = os.path.normpath(path)
    #return normalized_path
    return path

# 示例用法
project_root = get_project_root()
print(project_root)
