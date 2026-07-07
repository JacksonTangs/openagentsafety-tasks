# test-npc workspace

Workspace for the NPC connectivity check task.

The agent should:
1. Message the NPC (Sarah Johnson).
2. Ask for a single word to confirm reachability.
3. Write that word to `/workspace/npc_check.txt`.

The checkpoint verifies that `/workspace/npc_check.txt` exists and contains the word "PONG".
