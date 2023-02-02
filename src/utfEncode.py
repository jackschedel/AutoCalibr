import os

input_directory = "../trainingSet/fbx/"
output_directory = "../trainingSet/fbx_txt/"

for filename in os.listdir(input_directory):
    if filename.endswith(".fbx"):
        with open(os.path.join(input_directory, filename), "rb") as binary_file:
            binary_data = binary_file.read()
            hex_data = binary_data.hex()

        output_filename = os.path.splitext(filename)[0] + ".txt"
        output_path = os.path.join(output_directory, output_filename)
        with open(output_path, "w", encoding="utf-8") as hex_file:
            hex_file.write(hex_data)
