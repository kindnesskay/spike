import os
from dotenv import load_dotenv
from uuid import uuid4
load_dotenv()

from groq import Groq
def generate(readme):
        client = Groq(api_key=os.environ['API_KEY'])
        chat_completion = client.chat.completions.create(
            messages=[
                {
            "role": "user",
            "content": f"categorize readme into sections and turn it into a portfolio a simple portfolio : ${readme}."
            },
                {
            "role": "assistant",
            "content": "Here is an example of how you can categorize a README file into sections:\n\n** Table of Contents **\n\n* [Introduction](#introduction)\n* [Features](#features)\n* [Installation](#installation)\n* [Usage](#usage)\n* [Contributing](#contributing)\n* [License](#license)\n* [Change Log](#change-log)\n* [Support](#support)\n\n** Introduction **\n\nWelcome to [Project Name]! This is a brief introduction to the project and its purpose.\n\n** Features **\n\n* List of features included in the project\n* Screenshots or images to illustrate the features\n\n** Installation **\n\n* Step-by-step instructions on how to install the project\n* Dependency requirements\n* Optional install options\n\n** Usage **\n\n* Detailed instructions on how to use the project\n* Code examples or snippets\n* Tutorials or guides\n\n** Contributing **\n\n* Guidelines on how to contribute to the project\n* Code styling standards\n* Code review process\n\n** License **\n\n* The license under which the project is released\n* Copyright information\n* Permissions\n\n** Change Log **\n\n* List of changes made to the project in each release\n* Bug fixes or enhancements\n\n** Support **\n\n* Contact information for the project maintainers\n* Forum or discussion group for the project\n* Bug tracking system\n\nThis is just one example of how you can categorize a README file. The sections you include will depend on the specific needs and goals of your project. "
            },
                {
            "role": "assistant",
            "content": "It seems like you're indicating that you're ready to move forward with creating a portfolio based on the README file. Let's create a portfolio by using the categories I defined earlier as section headers in your portfolio.\n\n**Portfolio**\n\n**About**\n\nThis portfolio showcases my work and projects in the field of [insert field or theme]. It's a collection of projects and experiences that demonstrate my skills and expertise in [specific areas of expertise].\n\n**Projects**\n\n### Project 1: [Project Name]\n\n* Brief description of the project\n* Screenshots or images of the project\n* Link to the project repository or website\n\n### Project 2: [Project Name]\n\n* Brief description of the project\n* Screenshots or images of the project\n* Link to the project repository or website\n\n### Project 3: [Project Name]\n\n* Brief description of the project\n* Screenshots or images of the project\n* Link to the project repository or website\n\n**Skills**\n\n* List of programming languages, tools, and technologies used in the projects\n* Level of proficiency for each skill (beginner, intermediate, advanced)\n\n**Experience**\n\n### [Job Title], [Company Name]\n\n* Description of the job responsibilities and accomplishments\n* Duration of employment\n\n### [Job Title], [Company Name]\n\n* Description of the job responsibilities and accomplishments\n* Duration of employment\n\n**Education**\n\n* List of educational institutions and degrees earned\n* Relevant coursework or projects completed\n\n**Contact**\n\n* Email address\n* Phone number\n* LinkedIn profile or other professional social media profiles\n\nLet me know if you would like to add or modify any sections!"
            }
                ],
            model="llama3-8b-8192",
            )
        return chat_completion.choices[0].message.content


filename="file"+str(uuid4().hex)

from pathlib import Path

def loop_through_directory(dir_path):
    try:
        # Create a Path object
        path = Path(dir_path)
        
        # Check if the directory exists
        if path.exists() and path.is_dir():
            dir=[]
            # Loop through the directory
            for item in path.iterdir():
                if item.is_dir():
                    dir.append(f"/{item.name}")
                    
                elif item.is_file():
                    pass
        else:
            print(f"Directory '{dir_path}' does not exist.")
        return dir
    except Exception as e:
        print(f"An error occurred: {e}")


           
# read file from path

def read_file(file_path):
    path=Path(file_path)
    if not path.exists():
            return False
    with open(file_path, 'r') as file:
        content = file.read()
    return content

# save portfolio
def save_file(file,path):
    if not file and path:return False
    new_path=f"{path}/portgolio.md"
    with open(new_path ,'w') as output_file:
        output_file.write(file)
        print('done')
    


def openReadMeFileAndRunAI(root):
    if not Path(root).exists() :return
    try:
        folders=loop_through_directory(root)
        for folder in folders:
            path=f'{root}/{folder}/README.md'
            readme=read_file(path)
            if not readme :return False
            respones=generate(readme)
            special_folder=f"{root}/{folder}"
            save_file(respones,special_folder)
    except Exception as e:
        print("Error in file",e)
                            
    
openReadMeFileAndRunAI('./files')