'''

##################################################################################
Data set for stage block including random tech-sounding names for the DLL
name + string replace and binary types for the http-stager-client.
##################################################################################

'''
#CUSTOMIZE THIS#
transform_names = ['DebugCommunications','SystemIntern','EncryptFull','CablePlatform','CommDebug','SafetyDebug',
'CommnicationsDebug','InternSystem','FullEncrypt','PlatformCable','DebugComm', 'DebugSafely',
'NetworkComm','NetworkInternals','NetworkEncryption','NetworkPlatform','NetworkDebug','DebugNetwork']

#CUSTOMIZE THIS#
#**If you change this, you'll need to adjust the#
#elif statements in the consistencyCheck func in profile.py#
binary_types = [{'name':'jpg','content_type':'image/jpeg'},
{'name':'png','content_type':'image/png',},
{'name':'gif','content_type':'image/gif',},
{'name':'ico','content_type':'image/x-icon',},
{'name':'mp3','content_type':'audio/mpeg',},
]