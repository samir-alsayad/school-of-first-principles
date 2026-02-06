# Mission: The Signal (Remote Control)

## The Objective
You can control the **Shell** from outside the terminal. This is how `parallax` works. It sends a "Signal" (an invisible notification) to tell the shell to wake up and read a file.

## The Logic
1.  **The Mailbox**: A file where you put your command. (`/tmp/px-signal-PID.sh`)
2.  **The Bell**: A signal (`SIGUSR1`) that tells the shell "You have mail!"

## The Challenge: `hijack.sh`
1.  Find your current Shell PID: `echo $$`
2.  Create a "Bomb" file:
    ```bash
    echo 'echo "I AM SOVEREIGN"' > /tmp/px-signal-<YOUR_PID>.sh
    ```
3.  **The Trigger**:
    ```bash
    kill -USR1 <YOUR_PID>
    ```

## Verification
-   Did the shell print "I AM SOVEREIGN"?
-   Run `python3 verify.py` to confirm.
