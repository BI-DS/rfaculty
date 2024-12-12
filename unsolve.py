import glob


def process_file(input_file, output_file):
    start_marker = "### Sol"
    end_markers = [":::", "##"]
    replacement_code = "```{r}\n\n```\n"

    with open(input_file, "r") as file:
        lines = file.readlines()

    new_lines = []
    remove_block = False
    # Loop over each line
    for line in lines:
        if line.startswith(start_marker):
            remove_block = True
            # Add start marker line
            new_lines.append(line)
            new_lines.append(replacement_code + "\n")
            added_replacement = True
        elif any(line.startswith(marker) for marker in end_markers):
            remove_block = False
            # Add end marker line
            new_lines.append(line)
        elif not remove_block:
            new_lines.append(line)

    with open(output_file, "w") as file:
        file.writelines(new_lines)


def process_all_qmd_files():
    # Find all .qmd files in the current directory
    qmd_files = glob.glob("*.qmd")

    for file in qmd_files:
        output_file = file.rsplit(".", 1)[0] + "_unsolved.qmd"
        print(f"Processing {file} → {output_file}")
        process_file(file, output_file)
    print("All files processed.")


if __name__ == "__main__":
    process_all_qmd_files()
