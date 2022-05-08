import subprocess
if __name__ == '__main__':
      s = subprocess.run('behave –f json.pretty –o reports.json', shell=True, check=True)

