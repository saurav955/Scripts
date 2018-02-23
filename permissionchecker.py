import os
import argparse
import stat
import sys

def parse_options():
  parser = argparse.ArgumentParser(description="""checks the permissions at a particular path against specific permission and prints the deviators""", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('-p', '--path', help='Particular location on your system', required=True, type=str)
  parser.add_argument('-t', '--type', help='Specify Directory or File or both', default='both', required=False, type=str)
  parser.add_argument('-P', '--permissions', help='Specify the permission to be checked against', required=True, type=str)
  args = parser.parse_args()
  if not os.path.isdir(args.path):
    parser.error('Could not find the path %s' % args.path)
  return args

def directory_list(location):
  os.chdir(location)
  VAR2=[]
  for x in os.listdir(location):
    if os.path.isdir(x):
      VAR2.append(x)
  return VAR2

def file_list(location):
  os.chdir(location)
  VAR2=[]
  for x in os.listdir(location):
    if os.path.isfile(x):
      VAR2.append(x)
  return VAR2  

def whole_list(location):
  os.chdir(location)
  VAR2=[]
  for x in os.listdir(location):
    VAR2.append(x)
  return VAR2

def resulting_dictionary(location, permission, dir_list):
  os.chdir(location)
  user_dictionary = {}
  for x in dir_list:
    VAR1 = oct(os.stat(x).st_mode)[-4:]
    if VAR1!=permission:
      user_dictionary[x] = VAR1
  return user_dictionary

def main():
  args = parse_options()
  if args.type == 'both':
    list_desired = whole_list(args.path)
  elif args.type == 'dir':  
    list_desired = directory_list(args.path)
  elif args.type == 'file': 
    list_desired = file_list(args.path)
  else:
    print("Unknown type specified %s" % args.type)
    sys.exit(0)
  result = resulting_dictionary(args.path, args.permissions, list_desired)
  print(result)

if __name__ == "__main__":
    main()
