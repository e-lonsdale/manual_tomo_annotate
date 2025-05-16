#!/bin/sh

# get login credentials
read -p "Enter your supercomputer username: " username
read -sp "Enter your supercomputer password: " password
echo
read -sp "Enter your supercomputer 2FA code: " twofactor
echo

# # Check if the multiplexed connection is active
# ssh -O check "$username" 2>/dev/null

# # If the check command fails, establish the connection
# if [ $? -ne 0 ]; then
#     echo "Multiplexing connection not found. Establishing connection..."
#     ssh "$username"
#     if [ $? -ne 0 ]; then
#         echo "Failed to establish the multiplexing connection."
#         exit 1
#     fi
# fi

# check for annotations directory
if [ ! -d "$HOME/segmentation_data/annotations/" ]; then
    echo "Error: Local directory does not exist."
    exit 1
fi

# transfer files to supercomputer
expect_status=0
expect << EOF
spawn rsync -avzP --exclude=".DS_Store" --rsync-path='mkdir -p ~/groups/fslg_imagseg/nobackup/archive/segmentation_data && rsync' "$HOME/segmentation_data/annotations/" "$username@ssh.rc.byu.edu:~/groups/fslg_imagseg/nobackup/archive/segmentation_data/"
expect "Password:"
send "$password\r"
expect "Verification code:"
send "$twofactor\r"
expect eof
catch wait result
set expect_status [lindex \$result 3]
EOF

if [ $expect_status -eq 0 ]; then
    echo "Files transferred successfully."
else
    echo "Error during file transfer. Exit status: $expect_status"
fi