def create_env_example():
    try:
        with open('.env', 'r') as env_file:
            env_content = env_file.readlines()

        with open('.env.example', 'w') as env_example_file:
            for line in env_content:
                if "=" in line:
                    variable, value = line.strip().split('=')
                    env_example_file.write(f"{variable}=example\n")
                else:
                    variable = line.strip()
                    env_example_file.write(f"{variable}\n")
        print("Created .env.example successfully.")
    except FileNotFoundError:
        print("The .env file does not exist. Make sure it's present.")


if __name__ == "__main__":
    create_env_example()
