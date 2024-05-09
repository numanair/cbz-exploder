import os
import re
import zipfile
import shutil

directory = input("Insert directory on where to extract cbz files: ")
    
output_dir_path = f"{directory}/output"
tmp_dir_path = f"{directory}/tmp"

if os.path.exists(output_dir_path):
    shutil.rmtree(output_dir_path)
os.makedirs(output_dir_path)
    
for file in os.listdir(directory):
    if file.endswith(".cbz"): 
        reg = re.search(r"[Vv].*?(\d+).*?[Cc]?.*?(\d+)\.?(\d*)", file)
        print(f"PROCESSING {file}")
        vol_no = reg.group(1)
        chap_no = reg.group(2)
        chap_minor_part = reg.group(3)
        print(f"""EXPLODED Volume {vol_no} Chapter {chap_no if chap_no.isalnum() else "0"}.{chap_minor_part if chap_minor_part.isalnum() else "0"}""")
        with zipfile.ZipFile(os.path.join(directory, file), 'r') as zip_ref:            
            if not os.path.exists(tmp_dir_path):
                os.makedirs(tmp_dir_path)
                
            zip_ref.extractall(tmp_dir_path)
            for file in os.listdir(tmp_dir_path):
                os.rename(os.path.join(tmp_dir_path, file), os.path.join(output_dir_path, f"V{vol_no}_C{chap_no}_{chap_minor_part}_{file}"))
            
            shutil.rmtree(tmp_dir_path)
            