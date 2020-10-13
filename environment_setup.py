import pkg_resources
import os

#packages available in colab's environment
env_packages = [dist.project_name for dist in pkg_resources.working_set]

#packages required by our requirement available or not
#if not installed ,make a list of them
required_packages = open(os.getcwd+"/requirements.txt", "r")

install_these = []

for package_with_version in required_packages.readlines():
  name_without_version=""
  for letter in package_with_version :
    if letter != '=':
      name_without_version += letter
    elif name_without_version not in env_packages:
        install_these.append(package_with_version)

#install required unavailable packages
file = open("create_req_file.txt", "w")
for package in install_these:
    file.write(package)


