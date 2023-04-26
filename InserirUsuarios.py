#!/usr/bin/env python3

import subprocess

# definir nome de usuario e senha do novo usuario

new_user_name = "david"
new_user_password = "123456"

# criar o usuario no sistema linux

subprocess.run(["sudo", "useradd", new_user_name])
subprocess.run(["sudo", "passwd", new_user_name], input=f"{new_user_password}\n{new_user_password}\n".encode())
