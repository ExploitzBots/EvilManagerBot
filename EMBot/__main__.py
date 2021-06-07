import glob
from pathlib import Path
from EMBot.utils import load_plugins
import logging
from EMBot import Evil

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "EMBot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
print("Successfully Started Bot!")
print("Running As Usain Bolt")

if __name__ == "__main__":
    Evil.run_until_disconnected()
