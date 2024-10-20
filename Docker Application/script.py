from collections import Counter
import os
import socket

# Function to expand contractions based on a predefined dictionary
def expand_contractions(text):
    contractions_dict = {
        "I'm": "I am",
        "I'll": "I will",
        "can't": "cannot",
        "couldn't": "could not",
        "won't": "will not",
        "don't": "do not",
        "you're": "you are",
        "wanna": "want to",
        "that's": "that is",
        "it's": "it is",
    }

    # Replace contractions using the dictionary
    for contraction, full_form in contractions_dict.items():
        text = text.replace(contraction, full_form)
    
    return text

# Function to process a file's content
def process_file_content(file_path, split_contractions_flag=False):
    with open(file_path, 'r') as file:
        text = file.read()
        
        # Count total words before splitting contractions
        total_words_before_split = len(text.split())
        
        # Split contractions only if the flag is set
        if split_contractions_flag:
            text = expand_contractions(text)
        
        # Split the (potentially modified) text into words
        words = text.split()
        
        # Count frequency of each word
        word_counts = Counter(words)
        
        return total_words_before_split, word_counts

# Function to write results to a file
def write_results_to_file(results):
    output_dir = '/home/data/output'
    #os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist
    result_file_path = os.path.join(output_dir, 'result.txt')
    
    try:
        with open(result_file_path, 'w') as result_file:
            result_file.write(results)
        print(f"Results written to {result_file_path}")  # Confirmation message
    except Exception as e:
        print(f"Error writing results: {e}")

    return result_file_path
    

# Main function to test the logic with file processing
def main():
    # Paths to your files
    if_file_path = 'IF.txt'  # Change this path as needed
    always_remember_file_path = 'AlwaysRememberUsThisWay.txt'  # Change this path as needed

    # Process IF.txt without splitting contractions
    total_words_if, word_counts_if = process_file_content(if_file_path)
    top_3_if = word_counts_if.most_common(3)

    # Process AlwaysRememberUsThisWay.txt with splitting contractions
    total_words_always_remember_before, word_counts_always_remember = process_file_content(always_remember_file_path, split_contractions_flag=True)
    top_3_always_remember = word_counts_always_remember.most_common(3)

    # Calculate grand total of words across both files
    grand_total_words = total_words_if + total_words_always_remember_before

    ip_address = socket.gethostbyname(socket.gethostname())

    # Prepare results for writing
    results = (
        "Results for IF.txt:\n"
        f"Total words: {total_words_if}\n"
        "Top 3 most frequent words:\n"
    )
    for word, count in top_3_if:
        results += f"{word}: {count}\n"

    results += (
        "\nResults for AlwaysRememberUsThisWay.txt:\n"
        f"Total words before splitting contractions: {total_words_always_remember_before}\n"
        "Top 3 most frequent words:\n"
    )
    for word, count in top_3_always_remember:
        results += f"{word}: {count}\n"

    results += f"\nGrand total of words across both files: {grand_total_words}\n"

    results += f"IP Address of the container: {ip_address}\n"

    # Write results to result.txt
    result_file_path = write_results_to_file(results)

    # Print the contents of result.txt to the console
    with open(result_file_path, 'r') as result_file:
        print(result_file.read())

# Run the main function
if __name__ == "__main__":
    main()
