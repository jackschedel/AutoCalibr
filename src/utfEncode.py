import os

for filename in os.listdir("../trainingSet/fbx/"):
    if filename.endswith(".fbx"):
        with open(os.path.join("../trainingSet/fbx/", filename), "rb") as binary_file:
            binary_data = binary_file.read()
            utf8_data = binary_data.decode("utf-8", "ignore")

        output_filename = os.path.splitext(filename)[0] + ".fbxutf"
        with open(os.path.join("../utfConvert/", output_filename), "w", encoding="utf-8") as utf8_file:
            utf8_file.write(utf8_data)