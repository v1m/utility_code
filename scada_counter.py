#!/usr/bin/env python
# encoding: utf-8

import re

#the relevant data is downloaded from https://ics-cert.us-cert.gov/advisories-by-vendor to the txt file
#
# head -n 15 scada-data-ics_cert.txt
# #https://ics-cert.us-cert.gov/advisories-by-vendor
# #Thu Nov 5, 10:50:46 EST 2015
# 360 Systems
# ICSA-13-038-01A : 360 Systems Image Server 2000 Series Remote Root Access (Update A)
# 3S-Smart Software Solutions
# ICSA-15-293-03 : 3S CODESYS Gateway Null Pointer Exception Vulnerability
# ICSA-13-050-01A : 3S CODESYS Gateway-Server Vulnerabilities (Update A)
# ICSA-15-288-01 : 3S CODESYS Runtime Toolkit Null Pointer Dereference Vulnerability
# ICSA-13-142-01 : 3S CODESYS Gateway Use After Free
# ICSA-14-030-01 : 3S CoDeSys Runtime Toolkit NULL Pointer Dereference
# ICSA-13-011-01 : 3S CoDeSys Vulnerabilities
# ICSA-12-006-01 : 3S CoDeSys Vulnerabilities
# ICSA-15-258-02 : 3S CODESYS Gateway Server Buffer Overflow Vulnerability
# 7-Technologies
# ICSA-11-018-02 : 7-Technologies IGSS 8 ODBC Server Remote Heap Corruption


fh = open('scada-data-ics_cert.txt')

l = list(fh)

icsa_adv = re.compile(r'^ICSA-\d{1,4}-\w{1,4}-\w{1,4}')
comment = re.compile('^#')

vendor_name = ""
adv_count = 0

for line in l:

    if comment.match(line):
        next
    elif icsa_adv.match(line):
        adv_count=adv_count+1
    else:
        if vendor_name:
            print "%d => %s" %(adv_count,vendor_name)
        vendor_name=line.strip()
        adv_count = 0

#RESULTS
# 1 => 360 Systems
# 1 => AGG Software
# 1 => AMTELCO
# 1 => ARC Informatique
# 1 => Accuenergy
# 1 => Automated Solutions
# 1 => Baxter
# 1 => Beckhoff
# 1 => Beckwith Electric
# 1 => Beijer Electronics
# 1 => C3-ilex
# 1 => CG Automation
# 1 => CIMON, Inc.
# 1 => CSWorks
# 1 => Canary Labs, Inc.
# 1 => CareFusion
# 1 => Carlo Gavazzi
# 1 => Clorius Controls A/S
# 1 => Digi International
# 1 => Digital Electronics
# 1 => EasyIO
# 1 => Eaton's Cooper Power Systems
# 1 => Elecsys
# 1 => Everest Software LLC
# 1 => Festo
# 1 => Fiat-Chrysler Automobile US LLC
# 1 => Fox-IT
# 1 => Fultek
# 1 => Galil
# 1 => Harman-Kardon
# 1 => I-GEN
# 1 => IBC Solar
# 1 => IDS
# 1 => Infinite Automation Systems
# 1 => Intellicom
# 1 => Janitza
# 1 => Johnson Controls
# 1 => Korenix
# 1 => Koyo
# 1 => MACTek
# 1 => Magnetrol
# 1 => Meinberg
# 1 => Microsoft
# 1 => Monroe Electronics
# 1 => Morpho
# 1 => N-Tron
# 1 => Network Vision
# 1 => NovaTech
# 1 => OPTO 22
# 1 => ORing
# 1 => Ocean Data
# 1 => OleumTech
# 1 => Open Automation Software
# 1 => Optimalog
# 1 => PACTware Consortium
# 1 => Pepperl+Fuchs
# 1 => Philips
# 1 => Phoenix Contact Software
# 1 => Post Oak Traffic Systems
# 1 => ProSoft Technology
# 1 => QNX
# 1 => RLE Nova-Wind
# 1 => Resource Data Management
# 1 => SMA Solar Technology AG
# 1 => SafeNet
# 1 => Samsung
# 1 => ScadaTEC
# 1 => Scadatec Limited
# 1 => Sensys Networks
# 1 => Sierra Wireless
# 1 => Sixnet
# 1 => SpecView
# 1 => Sunway
# 1 => TURCK
# 1 => Triangle MicroWorks
# 1 => Triangle MicroWorks
# 1 => Trihedral Engineering Ltd
# 1 => Tropos
# 1 => Unified Automation
# 1 => Unitronics
# 1 => WAGO
# 1 => xArrow
# 2 => Alstom
# 2 => Arbiter Systems
# 2 => AzeoTech
# 2 => COPA-DATA
# 2 => Catapult Software
# 2 => Cisco
# 2 => CodeWrights GmbH
# 2 => Cooper Power Systems
# 2 => Elipse
# 2 => Endress+Hauser
# 2 => GarrettCom
# 2 => Inductive Automation
# 2 => IniNet Solutions GmbH
# 2 => Kepware Technologies
# 2 => Measuresoft
# 2 => NCCIC Advisory: April 2011 : Targeted Phishing Attacks
# 2 => NCCIC Advisory: May 2011 : Osama Bin Laden-Themed Phishing
# 2 => Nordex
# 2 => Omron Corporation
# 2 => SCADA Engine
# 2 => SUBNET Solutions Inc.
# 2 => Schweitzer Engineering Laboratories
# 2 => Sinapsi
# 2 => Software Toolbox
# 2 => Triangle Research International, Inc.
# 2 => Tridium
# 2 => XZERES
# 3 => Certec
# 3 => MICROSYS
# 3 => RealFlex Technologies
# 3 => RuggedCom
# 3 => Sielco Sistemi
# 3 => Wind River
# 4 => Hospira
# 4 => MatrikonOPC
# 4 => Mitsubishi Electric Automation
# 4 => Progea
# 5 => IOServer
# 5 => Innominate
# 5 => OSIsoft
# 6 => Cogent Real-Time Systems Inc
# 6 => InduSoft
# 7 => ABB
# 7 => Emerson
# 7 => ICONICS
# 7 => Moxa
# 8 => 3S-Smart Software Solutions
# 9 => 7-Technologies
# 9 => Honeywell
# 11 => WellinTech
# 12 => Ecava
# 13 => Other
# 14 => Advantech
# 14 => Invensys
# 16 => Rockwell Automation
# 20 => GE
# 41 => Schneider Electric
# 75 => Siemens


