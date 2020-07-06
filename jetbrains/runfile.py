#! /usr/bin/python3
import os

file_path = "/home/jixingwu/.local/share/applications/jetbrains-clion.desktop"
file = open(file_path, "r")
content = file.read()

content_add = "bash -i -c "
pose = content.find("Exec=")

if pose != 1:
	content = content[:pose+5] + content_add + content[pose+5:]
	file_ = open(file_path,"w")
	file_.write(content)
	file_.close()

print("Finshed: insert 'bash -i -c' to jecbrains-clion.desktop")

