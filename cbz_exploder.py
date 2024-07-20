import os
import re
import zipfile
import shutil

# Get inputs from user
directory = input("Enter path containing CBZ files: ")
title = input("Enter title of series: ")

# Define paths
output_dir_path = os.path.join(directory, "output")
tmp_dir_path = os.path.join(directory, "tmp")


# Clean output directory if exists and make anew
if os.path.exists(output_dir_path):
    shutil.rmtree(output_dir_path)
os.makedirs(output_dir_path)


# Function which extracts important information from filename
def extract_numbers_from_file(filename):
    vol_reg = re.search(r"[Vv].*?(\d+).*?", filename)
    chap_reg = re.search(r"[Cc]?.*?(\d+)\.?(\d*)", filename)
    vol_no = vol_reg.group(1) if vol_reg else "0"
    chap_no = chap_reg.group(1)
    chap_minor_part = chap_reg.group(2)
    return [vol_no, chap_no, chap_minor_part]


for file in os.listdir(directory):
    if file.endswith(".cbz"):
        print(f"PROCESSING {file}")
        [vol_no, chap_no, chap_minor_part] = extract_numbers_from_file(file)
        print(
            f"""EXPLODED {title} Volume {vol_no} Chapter {chap_no if chap_no.isalnum() else "0"}.{chap_minor_part if chap_minor_part.isalnum() else "0"}"""
        )

        with zipfile.ZipFile(os.path.join(directory, file), "r") as zip_ref:
            if not os.path.exists(tmp_dir_path):
                os.makedirs(tmp_dir_path)

            # For every cbz, extract all to temp directory
            zip_ref.extractall(tmp_dir_path)

            for root, subdirs, files in os.walk(tmp_dir_path):
                for file in files:
                    volume_dir = os.path.join(
                        output_dir_path, f"{title} Volume {vol_no}"
                    )
                    if not os.path.exists(volume_dir):
                        os.makedirs(volume_dir)

                    chapter_dir = os.path.join(
                        volume_dir,
                        f"Chapter {chap_no}"
                        + ("_" + chap_minor_part if chap_minor_part.isalnum() else ""),
                    )
                    if not os.path.exists(chapter_dir):
                        os.makedirs(chapter_dir)

                    os.rename(os.path.join(root, file), os.path.join(chapter_dir, file))

            shutil.rmtree(tmp_dir_path)
