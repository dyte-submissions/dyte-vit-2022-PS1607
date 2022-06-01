# importing required modules
import os
import argparse
import pandas as pd
import requests
import github_token

# ERROR MESSAGES
INVALID_FILETYPE_MSG = "\nError: Invalid file format. Input must be a .csv file.\n"
INVALID_PATH_MSG = "\nError: Invalid file path/name. Path %s does not exist.\n"

def validate_file(file_name):
    '''
    validate file name and path.
    '''
    if not valid_filetype(file_name):
        print(INVALID_FILETYPE_MSG)
        quit()

    elif not valid_path(file_name):
        print(INVALID_PATH_MSG%(file_name))
        quit()
    
    return
     
def valid_filetype(file_name):
    # validate file type
    return file_name.endswith('.csv')
 
def valid_path(path):
    # validate file path
    return os.path.exists(path)

def constructURL(user = "404",repo_name= "404",path_to_file= "404",url= "404"):
  url = url.replace("{user}",user)
  url = url.replace("{repo_name}",repo_name)
  url = url.replace("{path_to_file}",path_to_file)
  return url

def compareVersion(version1, version2):
      versions1 = [int(v) for v in version1.split(".")]
      versions2 = [int(v) for v in version2.split(".")]
      for i in range(max(len(versions1),len(versions2))):
         v1 = versions1[i] if i < len(versions1) else 0
         v2 = versions2[i] if i < len(versions2) else 0
         if v1 > v2:
            return 1
         elif v1 <v2:
            return -1
      return 0

def input(args):
    # get the file name/path

    file_name = args.input[0]
    dep_name = args.input[1]
    dep_version = args.input[2]
 
    # validate the file name/path
    validate_file(file_name)

    data = pd.read_csv(file_name)

    data["version"] = ""
    data["version_satisfied"] = ""

    data.to_csv(file_name, index=False)
    i = 0

    for each in data.repo:
        na = 0
        extracted_string = each[19:]

        token = github_token.token
        owner = extracted_string.rsplit('/')[0]
        repo = extracted_string.rsplit('/')[1]
        path1 = 'package.json'
        path2 = 'package-lock.json'
        response = requests.get(
                'https://api.github.com/repos/{owner}/{repo}/contents/{path}'.format(
                owner=owner, repo=repo, path=path1),
                headers={
                    'accept': 'application/vnd.github.v3.raw',
                    'authorization': 'token {}'.format(token)
                        }
                ) #get data from json file located at specified URL 

        if response.status_code == requests.codes.ok:
            jsonResponse = response.json()  # the response is a JSON
            for key, value in jsonResponse.items():
                if(key == "devDependencies"):
                    try:
                        version = value[dep_name][1:]
                        data.version[i] = version
                        break
                    except:
                        continue
                elif(key == "dependencies"):
                    try:
                        version = value[dep_name][1:]
                        data.version[i] = version
                        break
                    except:
                        data.version[i] = "NA"
                        na = 1
        else:
            print('Content was not found.')
        if(na != 1):
            if(compareVersion(version, dep_version) == 0):
                data.version_satisfied[i] = "true"
            elif(compareVersion(version, dep_version) == 1):
                data.version_satisfied[i] = "true"
            else:
                data.version_satisfied[i] = "false" 

        else:
            data.version_satisfied[i] = "NA"

        i=i+1

        
    data.to_csv(file_name, index=False)
    print("\n")
    print(data)
    print("\n")

# create a parser object
parser = argparse.ArgumentParser(description = "A program to Maintain and Manage dependency versions.")

def main():
    # add argument

    parser.add_argument('-i','--input', type = str, nargs = 3,
                        metavar = ("file_name", "dependency_name", "dependency_version"), 
                        default = None, help = "Takes a .csv file as an input")

    args = parser.parse_args()

    # calling functions depending on type of argument
    if args.input != None:
        input(args)

if __name__ == "__main__":
    # calling the main function
    main()