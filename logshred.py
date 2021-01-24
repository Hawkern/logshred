
import os
import sys
cmd = input("Press enter to shred and delete log files permanently... ")
os.system('sudo find . -type f -name {"*.log"} -exec shred {} \;')
os.system('sudo find . -type f -name {"*.log"} -exec rm -rf {} \;')
os.system('sudo shred /var/log/ ~/.zsh_history ̃~/bash_history/ var/log/alteratives.log /var/log/auth.log /var/log/apt/eipp.log.xz /var/log/apt/history.log /var/log/apt/term.log /var/log/btmp /var/log/cloud-init-output.log /var/log/cloud-init.log /var/log/daemon.log /var/log/debug /var/log/dpkg.log /var/log/faillog /var/log/kern.log /var/log/lastlog /var/log/messages /var/log/postresql /var/log/private /var/log/syslog /var/log/unattended-upgrades/unattended-upgrades-shutdown.log /var/log/user.log /var/log/wtmp')
os.system('sudo rm -rf /var/log ~/bash_history')
print("Logs shredded and removed succesfully")
