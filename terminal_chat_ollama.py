import requests
import json

MODEL = "gemma3:1b"
SERVER = "http://localhost:11434"
URL = f"{SERVER}/api/generate"


def get_response(prompt):

    data = {
        "model": MODEL,
        "prompt": prompt,
        "stream": True
    }

    try:

        with requests.post(URL, json=data, stream=True, timeout=(5, 120)) as response:
            
            response.raise_for_status()

            print("Assistant: ", end="", flush=True)

            for line in response.iter_lines():

                if not line:
                    continue

                try:
                    json_data = json.loads(line.decode("utf-8"))

                    if "response" in json_data:
                        print(json_data["response"], end="", flush=True)

                    if json_data.get("done"):
                        break

                except json.JSONDecodeError:
                    print("\nInvalid JSON received.")

            print("\n")

    except requests.exceptions.ConnectionError:
        print("\nError: Ollama server is not running.")

    except requests.exceptions.Timeout:
        print("\nError: Request timed out.")

    except requests.exceptions.HTTPError as error:
        print(f"\nHTTP Error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"\nRequest Error: {error}")


def main():

    print("=" * 50)
    print(f"Send request to model: {MODEL}")
    print("If you are done, type 'exit'")
    print("=" * 50)

    while True:

        try:
            user_prompt = input("\nYou: ").strip()

            if user_prompt.lower() == "exit":
                break

            if not user_prompt:
                continue

            get_response(user_prompt)

        except KeyboardInterrupt:
            print("\n\nProgram interrupted.")
            break

    print("=" * 50)
    print("End of program execution")
    print("=" * 50)


if __name__ == "__main__":
    main()
