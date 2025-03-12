import os


def list_files():
  for root, dirs, files in os.walk('.'):
    if '.git' in root:
      continue
    level = root.replace('.', '').count(os.sep)
    indent = ' ' * 4 * level
    print(f'{indent}{os.path.basename(root)}/')
    subindent = ' ' * 4 * (level + 1)
    for f in files:
      if f not in ['.gitignore', 'list_files.py', 'create_files.py']:
        print(f'{subindent}{f}')


if __name__ == '__main__':
  list_files()
