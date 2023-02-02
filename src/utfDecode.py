import os

for filename in os.listdir("../utfConvert/"):
    if filename.endswith(".fbxutf"):
        with open(os.path.join("../utfConvert/", filename), "r", encoding="utf-8") as utf8_file:
            utf8_data = utf8_file.read()
            binary_data = utf8_data.encode("utf-8")

        output_filename = os.path.splitext(filename)[0] + ".fbx"
        with open(os.path.join("../fbxDecodeTest/", output_filename), "wb") as binary_file:
            binary_file.write(binary_data)
