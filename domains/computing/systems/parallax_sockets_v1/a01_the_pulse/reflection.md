## Mastery Tier
*Rate your understanding of this mission (1-10):* [3/10]

> [!TIP]
> **Tier 1-3**: "I copy-pasted symbols and they worked by magic."
> **Tier 4-6**: "I can predict what happens if I change a line."
> **Tier 7-9**: "I can rewrite this from scratch without help."
> **Tier 10**: "I can explain the OS-level invariants of this system."

## The Mirror
1.  **The Ghost in the Machine**:
    When you source `px-link-v2.zsh`, where does the `while` loop go? Why can you still type after it starts?
    When you ran `nc -U ... | while read line; do ... done`, did your terminal freeze? If it did, how do you put a "Phone Line" in the background so you can still type?

2.  **The Data Loss Question**:
    Signals are like "Hey!" Sockets are like "Here is a letter." 
    What happens if the Python server sends 100 messages while your shell is busy running a long `sleep 10` command? Where do those 100 messages go?

3.  **The Security Question**:
    In Parallax v1, we sourced a file (`source /tmp/px...`). 
    In Parallax v2, we parse JSON and then `eval` the command.
    Is this safer? Why or why not? (Hint: Does the JSON format allow us to "inspect" the code before we run it?)

## My Notes
1. When I run ./px_subscriber.zsh, the process occupies the terminal, printing output into it (I think because of the debug statements maybe).
By putting & at the end of a command, the shell executes it in the background and frees up the terminal for further use. 

2. The commands go into the buffer when the terminal is busy I think?

3. We convert the message into json, so that it becomes inspectable

4. /dev/null is a black hole file that deletes anything written to it and always retuns empty when trying to read from it. we use this in combination with tail -f to create a persistent process that wont die, without using system resources.



## The Discovery
I learned that using nc -U makes nc use a UNIX socket instead of routing to an ip adress. I learned that using sockets for inter process communication (IPC) is the better approach, because it lets the message go into buffer.


## The Gap
I dont know, but a lot.