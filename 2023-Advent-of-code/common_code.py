def read_file_lines(file_path: str):
    """ Reads a file and returns a list of lines"""
    try:
        with open(file_path, 'r') as file:
            content = file.read().splitlines()

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {str(e)}")

    
    return content

def extract_k_len_substr(word: str, k: int):
    """ Extracts all substrings of length k from a given word """
    substrings = []
    for i in range(len(word) - k + 1):
        substrings.append(word[i:i+k])
    return substrings

 