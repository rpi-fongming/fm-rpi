# SoftEther VPN Server (Ver 1.00, Build 9377, ARM EABI) for Linux
# Makefile
# 
# Copyright (c) SoftEther Project at University of Tsukuba, Japan. All Rights Reserved.
# Platform: linux-armeabi-32bit

CC=gcc
OPTIONS=-O2 -fsigned-char -lm -ldl -lrt -Wl,--no-warn-mismatch -lpthread -L./ lib/libssl.a lib/libcrypto.a lib/libiconv.a lib/libcharset.a lib/libedit.a lib/libncurses.a lib/libz.a

default:
	@./.install.sh

# NOTE:
# You have to read and agree the license agreement at the same directory
#  before using this software.

i_read_and_agree_the_license_agreement:
	@echo "Preparing SoftEther VPN Server..."
	-ranlib lib/libcharset.a
	-ranlib lib/libcrypto.a
	-ranlib lib/libedit.a
	-ranlib lib/libiconv.a
	-ranlib lib/libncurses.a
	-ranlib lib/libssl.a
	-ranlib lib/libz.a
	-ranlib code/vpnserver.a
	$(CC) code/vpnserver.a $(OPTIONS) -o vpnserver
	-ranlib code/vpncmd.a
	$(CC) code/vpncmd.a $(OPTIONS) -o vpncmd
	./vpncmd /tool /cmd:Check
	@echo
	@echo "--------------------------------------------------------------------"
	@echo "The preparation of SoftEther VPN Server is completed !"
	@echo
	@echo
	@echo "*** How to switch the display language of the SoftEther VPN Server Service ***"
	@echo "SoftEther VPN Server supports the following languages:"
	@echo "  - Japanese"
	@echo "  - English"
	@echo "  - Simplified Chinese"
	@echo
	@echo "You can choose your prefered language of SoftEther VPN Server at any time."
	@echo "To switch the current language, open and edit the 'lang.config' file."
	@echo
	@echo
	@echo "*** How to start the SoftEther VPN Server Service ***"
	@echo
	@echo "Please execute './vpnserver start' to run the SoftEther VPN Server Background Service."
	@echo "And please execute './vpncmd' to run the SoftEther VPN Command-Line Utility to configure SoftEther VPN Server."
	@echo "Of course, you can use the VPN Server Manager GUI Application for Windows on the other Windows PC in order to configure the SoftEther VPN Server remotely."
	@echo "--------------------------------------------------------------------"
	@echo

clean:
	rm -f vpnserver
	rm -f vpncmd

