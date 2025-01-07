from faker import Faker

fake = Faker()

# Generate Data
filename = "faker_data.md"

with open(filename, "a") as f:
    f.write(f"\n# {fake.catch_phrase()}\n")
    f.write(f"\n{fake.paragraph()}\n")

# Generate Commit Message
commit_message = fake.bs()

with open("commit_message.txt", "w") as f:
    f.write(commit_message)
