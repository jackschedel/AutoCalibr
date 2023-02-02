import os

input_directory = "../trainingSet/fbx_txt/"
output_directory = "../trainingSet/fbx_txt_fbx/"

for filename in os.listdir(input_directory):
    if filename.endswith(".txt"):
        with open(os.path.join(input_directory, filename), "r", encoding="utf-8") as hex_file:
            hex_data = hex_file.read()
            binary_data = bytes.fromhex(hex_data)

        output_filename = os.path.splitext(filename)[0] + ".fbx"
        output_path = os.path.join(output_directory, output_filename)
        with open(output_path, "wb") as binary_file:
            binary_file.write(binary_data)
