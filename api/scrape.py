import os
from git import Repo
from uuid import uuid4
def cloneRepoAndGetReadme(repo_url,clone_dir):
    try:
        # clone respository
        Repo.clone_from(repo_url,clone_dir)
        print(f"cloned respository to {clone_dir}")
        
        # look for readme file
        readme_files=['README.md','README.rst','README.txt']
        readme_path=None
        
        for filename in readme_files:
            file_path=os.path.join(clone_dir,filename)
            if os.path.isfile(file_path):
                readme_path =file_path
                break
            
        else: 
            print("No README file found in the respository")       
    except Exception as e:
        print(f'error:{e}')
        
 
        
# Example usage
repo_url = "https://github.com/KaluDavid/KaluDavid.git"
clone_dir = "./files/"+ str(uuid4().hex)
cloneRepoAndGetReadme(repo_url, clone_dir)