# Headquarters !¡MEGA¡! Improved

Category: pwn

Author: enxgmatic

Flag: `sctf{f1n3_1_g1v3_up_dud3}`

## Description

Ok fine, we added a canary and enabled PIE. Are you happy now? (now please stop breaking into our headquarters)

## Solution
Refer to `solution.py`

Buffer overflow => leak PIE and canary (based on values on the stack, because `printf` prints till a null byte)

Then ret2win.

## References

- Resources

---

# Remove this section

*note that everything in this section is my personal opinion and preferences, please do not follow if y'all have decided on something different or have ur own workflow/preferences lol*

## why template??

- consistent use of same format makes everything easier to deploy and distribute later on
- same format = can script = automation = profit??
- idk it looks nice to have an organised git repo lol
- pet peeve: as a ctf player i don't like to have distrib zips that are named ambiguously or unzip in different manners cos that makes my folders very messy :<

anyways how to use my hacky scripts:

1. Develop challenge source in [src/](./src/).
2. Fill in details of challenge in this current README.md. **Make sure to specify correct flag in correct format.**
3. Run copysrc.sh (beware that this script is experimental, no one other than me test before lol).  
   The script should replace all instances of the flag, including those without the `sctf{}` wrap, with `NOT_A_FLAG`. [src/](./src/) is then copied into [distrib/](./distrib/).  
   `usage: ./copysrc.sh [path/to/chall/directory]` (if no directory is specified, current directory is assumed as challenge directory)
4. Run zipdist.sh (beware same as above, should sanity check).  
   The script checks for flags within [distrib/](./distrib/), then zips the distrib directory to a zip file with name `challenge-name-distrib.zip`, where `challenge-name` is the basename of the challenge directory.  
   `usage: ./zipdist.sh [path/to/chall/directory]` (if no directory is specified, current directory is assumed as challenge directory)  
   If the script complains that a flag is found but you do not see it in your editor or file explorer, it may be a hidden file/folder (i.e. .env, .vscode, .idea, etc.). Please look at the output of the zipdist.sh (or use `unzip -l`) to double check no such folders are present in the zip file as it makes the distib very messy, even if they do not contain the flag.
5. Add solution to this current README.md, and place solve script(s) in [solve/](./solve/). **Please test your challs to make sure they can actually be solved.**

## challenge source

- For challenges that require a service running (e.g. raw TCP/IP (nc) or HTTP etc), containerise using Docker. Participants should be able to directly run the challenge locally with the given source and Dockerfile (and maybe docker-compose.yaml, see below).
- For challenges that do not require a service (e.g. forensics, misc, osint), you may wish to manually copy the files over from src to distrib and zip manually to avoid the script from detecting any flag strings and corrupting files (ideally flags should not be present in plaintext in any file though, as this means the challenge can solved by just grep/strings, which is typically unintended).

## containerisation

- **Every service must be containerised, safely!**
- I strongly recommend having a docker-compose.yaml in distrib, so that participants can just `docker compose up` to run locally. However, this makes it harder to manage deployment, since each challenge must be deployed individually, and the ports adjusted in each docker-compose.yaml to prevent conflicts.
  - A possible solution for this is to provide a standardised docker-compose.yaml in distrib (which only handles ports, all other things like flags stored in env put in Dockerfile), and then remove that file for depolyment. With this setup, only a single docker-compose.yaml is needed on the server, and that would only be needed to manage ports of all services. The minor caveat is that it may be slightly harder to manage challenges with multiple services running in different containers.
- sorry my devops skills not very good so dun really have like excellent reccs here lol
