# C2concealer

C2concealer is a command line tool that generates randomized C2 malleable profiles for use in Cobalt Strike. 

## Installation 

```bash
chmod u+x install.sh
./install.sh
```

## Example Usage

```bash
Usage:
	$ C2concealer --hostname google.com --variant 3

Flags:
	
	(optional)
	--hostname 
		The hostname used in HTTP client and server side settings. Default is None.
	--variant 
		An integer defining the number of HTTP client/server variants to generate. 
		Recommend between 1 and 5. Max 10.
```

## Example Console Output

```bash
root@kali:~# C2concealer --variant 1 --hostname google.com
[i] Searching for the c2lint tool on your system (part of Cobalt Strike). Might take 10-20 seconds.
[i] Found c2lint in the /opt/cobaltstrike/c2lint directory.

Choose an SSL option:
1. Self-signed SSL cert (just input a few details)
2. LetsEncrypt SSL cert (requies a temporary A record for the relevant domain to be pointed to this machine)
3. Existing keystore
4. No SSL

[?] Option [1/2/3/4]:
```

> Tip: Always use an SSL certificate. Preferably a cert from LetsEncrypt or similar.


> Tip: HTTP Variants allow you to select different IOCs for http traffic on different beacons. Recommend a value of at least 1. 

## How it works

We poured over the Cobalt Strike documentation and defined ranges of values that would make sense for each profile attribute. Sometimes that data is as simple as a random integer within some range and other times we need to pick a random value from a python dictionary. Either way, we started tool creation with defining the data that would make a valid profile. 

Then we divided each malleable profile section (or block) into a separate .py file, which contains the logic to draw random appropriate values for each attribute and then output a formatted string for that profile block. We concatenate all profile blocks together, run a few quick consistency checks and then run the profile through the Cobalt Strike linter (c2lint). The output is a profile that *should* work for your engagements. We always recommend testing the profile (including process injection and spawning) prior to running a campaign.

If you're looking into the code, we recommend starting with these two files: /C2concealer/__main__.py and /C2concealer/profile.py. After reviewing the comments, check out individuals profile block generators in the folder: /C2concealer/components.

## Customizing the tool

This is crucial. This is an open sourced version of a tool we've been using privately for about a year. Our private repo has several additional IOCs and a completely different data set. While running the tool provides an excellent start for building a Cobalt Strike malleable profile, we recommend digging into the following areas to customize the data that is randomly populating the tool:

/C2concealer/data/
- dns.py (customize the dns subdomains)
- file_type_prepend.py (customize how http-get-server repsonses look ... aka c2 control instructions)
- params.py (two dictionaries containing common parameter names and a generic wordlist)
- post_ex.py (spawn_to process list...definitely change this one)
- reg_headers.py (typical http headers like user-agent and server)
- smb.py (smb pipenames for use when comms go over smb)
- stage.py (data for changing IOCs related to the stager)
- transform.py (payload data transformations...no need to change this)
- urls.py (filetypes and url path components used for building URIs all across the tool...definitely change this)

In addition, you can customize various attributes all throughout the profile generation process. As an example, in the file: "/C2concealer/components/stageblock.py", you can change the range from which PE image size value is drawn from (near lines 73-74). Please look through all the different files in the components directory. 

If you've made it this far, then we know you'll get a lot of use out of this tool. The way we recommend viewing this tool is that we've built the skeleton code to automatically generate these profiles, now it's up to you to think through what values make sense for each attribute for your campaigns and update the data sources.

## Shoutouts

Big shoutout to Raphael Mudge for constantly improving on the malleable profile feature set and the documentation to learn about it. Also, huge thanks to @killswitch-GUI for his script that automates LetsEncrypt cert generation for CS team servers. Finally, two blog posts that made life so much easier: @bluescreenofjeff's post (https://bluescreenofjeff.com/2017-01-24-how-to-write-malleable-c2-profiles-for-cobalt-strike/) and Joe Vest's post (https://posts.specterops.io/a-deep-dive-into-cobalt-strike-malleable-c2-6660e33b0e0b).

## Version Changelog

Version 1.0
- Public version of FortyNorth Security's internal tool.
- Added support for CS 4.0 (specifically multiple HTTP variants)
- Updated README.md
