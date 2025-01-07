from transformers import pipeline
import os

generator = pipeline("text-generation", model="gpt2")

topics = [
    "Introduction to Linux",
    "The Linux Kernel Architecture",
    "Linux File Permissions and Ownership",
    "Linux Networking Fundamentals",
    "Package Management in Linux",
    "Linux File Systems Explained",
    "Command Line Basics",
    "Advanced Bash Scripting",
    "Linux Security Best Practices",
    "Managing Users and Groups",
    "Linux Process Management",
    "System Monitoring and Performance Tuning",
    "Virtualization in Linux",
    "Linux Distributions Overview",
    "Linux for Developers",
    "Automating Tasks with Cron",
    "Building Custom Linux Kernels",
    "Setting Up Linux Servers",
    "Linux Troubleshooting and Debugging",
    "Future of Linux and Open Source"
]

progress_file = "progress.txt"
output_file = "linux_book.md"

def get_last_topic_index():
    """Retrieve the last completed topic index from the progress file."""
    if os.path.exists(progress_file):
        with open(progress_file, "r") as f:
            return int(f.read().strip())
    return 0

def save_progress(index):
    """Save the current progress (topic index) to the progress file."""
    with open(progress_file, "w") as f:
        f.write(str(index))

def generate_content(prompt):
    """Generate content using GPT-2."""
    result = generator(prompt, max_length=500, num_return_sequences=1)
    return result[0]['generated_text']

if __name__ == "__main__":
    last_index = get_last_topic_index()

    if last_index < len(topics):
        prompt = topics[last_index]
        print(f"Generating content for: {prompt}")
        
        content = generate_content(f"{prompt}: ")

        with open(output_file, "a") as f:
            f.write(f"\n## {prompt}\n")
            f.write(content)
            f.write("\n\n---\n\n")

        save_progress(last_index + 1)
        print(f"Updated progress to topic index: {last_index + 1}")
    else:
        print("All topics have been generated. Book is complete.")
