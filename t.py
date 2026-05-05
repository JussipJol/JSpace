import threading
import time
from prompt_toolkit import PromptSession

# 1. We store our dynamic data in a global variable
dynamic_data = "Waiting for data..."

def background_task(session):
    global dynamic_data
    counter = 0
    
    while True:
        # 2. Update the variable
        dynamic_data = f"[Live Status] Data refreshed: {counter} times"
        counter += 1
        
        # 3. Force the prompt to redraw itself in-place with the new text
        if session.app and session.app.is_running:
            session.app.invalidate()
            
        time.sleep(1) # Refresh every 1 second

def get_custom_prompt():
    # 4. The prompt is multi-line: The live data on top, and the input on the bottom
    return f"{dynamic_data}\n> Enter command: "

def main():
    # Pass our function as the 'message'
    session = PromptSession(message=get_custom_prompt)
    
    # Start background thread, passing the session so it can trigger redraws
    thread = threading.Thread(target=background_task, args=(session,), daemon=True)
    thread.start()

    while True:
        try:
            # Wait for user input
            user_input = session.prompt()
            
            # Print what they typed (this will push the prompt down naturally)
            print(f"Success! You executed: {user_input}\n")
            
            if user_input.lower() == 'quit':
                break
                
        except (KeyboardInterrupt, EOFError):
            # Handles Ctrl+C and Ctrl+D gracefully
            break

if __name__ == "__main__":
    main()