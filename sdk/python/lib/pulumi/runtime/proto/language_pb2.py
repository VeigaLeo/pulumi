# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pulumi/language.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .codegen import hcl_pb2 as pulumi_dot_codegen_dot_hcl__pb2
from . import plugin_pb2 as pulumi_dot_plugin__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15pulumi/language.proto\x12\tpulumirpc\x1a\x18pulumi/codegen/hcl.proto\x1a\x13pulumi/plugin.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x9f\x01\n\rAboutResponse\x12\x12\n\nexecutable\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x38\n\x08metadata\x18\x03 \x03(\x0b\x32&.pulumirpc.AboutResponse.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"n\n\x1dGetProgramDependenciesRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x0b\n\x03pwd\x18\x02 \x01(\t\x12\x0f\n\x07program\x18\x03 \x01(\t\x12\x1e\n\x16transitiveDependencies\x18\x04 \x01(\x08\"/\n\x0e\x44\x65pendencyInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"Q\n\x1eGetProgramDependenciesResponse\x12/\n\x0c\x64\x65pendencies\x18\x01 \x03(\x0b\x32\x19.pulumirpc.DependencyInfo\"J\n\x19GetRequiredPluginsRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x0b\n\x03pwd\x18\x02 \x01(\t\x12\x0f\n\x07program\x18\x03 \x01(\t\"J\n\x1aGetRequiredPluginsResponse\x12,\n\x07plugins\x18\x01 \x03(\x0b\x32\x1b.pulumirpc.PluginDependency\"\xb8\x02\n\nRunRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05stack\x18\x02 \x01(\t\x12\x0b\n\x03pwd\x18\x03 \x01(\t\x12\x0f\n\x07program\x18\x04 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x05 \x03(\t\x12\x31\n\x06\x63onfig\x18\x06 \x03(\x0b\x32!.pulumirpc.RunRequest.ConfigEntry\x12\x0e\n\x06\x64ryRun\x18\x07 \x01(\x08\x12\x10\n\x08parallel\x18\x08 \x01(\x05\x12\x17\n\x0fmonitor_address\x18\t \x01(\t\x12\x11\n\tqueryMode\x18\n \x01(\x08\x12\x18\n\x10\x63onfigSecretKeys\x18\x0b \x03(\t\x12\x14\n\x0corganization\x18\x0c \x01(\t\x1a-\n\x0b\x43onfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"*\n\x0bRunResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\t\x12\x0c\n\x04\x62\x61il\x18\x02 \x01(\x08\"D\n\x1aInstallDependenciesRequest\x12\x11\n\tdirectory\x18\x01 \x01(\t\x12\x13\n\x0bis_terminal\x18\x02 \x01(\x08\"=\n\x1bInstallDependenciesResponse\x12\x0e\n\x06stdout\x18\x01 \x01(\x0c\x12\x0e\n\x06stderr\x18\x02 \x01(\x0c\"K\n\x10RunPluginRequest\x12\x0b\n\x03pwd\x18\x01 \x01(\t\x12\x0f\n\x07program\x18\x02 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x03 \x03(\t\x12\x0b\n\x03\x65nv\x18\x04 \x03(\t\"U\n\x11RunPluginResponse\x12\x10\n\x06stdout\x18\x01 \x01(\x0cH\x00\x12\x10\n\x06stderr\x18\x02 \x01(\x0cH\x00\x12\x12\n\x08\x65xitcode\x18\x03 \x01(\x05H\x00\x42\x08\n\x06output\"\x86\x01\n\x16GenerateProgramRequest\x12=\n\x06source\x18\x01 \x03(\x0b\x32-.pulumirpc.GenerateProgramRequest.SourceEntry\x1a-\n\x0bSourceEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xbc\x01\n\x17GenerateProgramResponse\x12\x32\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x1d.pulumirpc.codegen.Diagnostic\x12>\n\x06source\x18\x02 \x03(\x0b\x32..pulumirpc.GenerateProgramResponse.SourceEntry\x1a-\n\x0bSourceEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"]\n\x16GenerateProjectRequest\x12\x18\n\x10source_directory\x18\x01 \x01(\t\x12\x18\n\x10target_directory\x18\x02 \x01(\t\x12\x0f\n\x07project\x18\x03 \x01(\t\"M\n\x17GenerateProjectResponse\x12\x32\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x1d.pulumirpc.codegen.Diagnostic\"\xb6\x01\n\x16GeneratePackageRequest\x12\x11\n\tdirectory\x18\x01 \x01(\t\x12\x0e\n\x06schema\x18\x02 \x01(\t\x12\x46\n\x0b\x65xtra_files\x18\x03 \x03(\x0b\x32\x31.pulumirpc.GeneratePackageRequest.ExtraFilesEntry\x1a\x31\n\x0f\x45xtraFilesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\x19\n\x17GeneratePackageResponse2\xe8\x06\n\x0fLanguageRuntime\x12\x63\n\x12GetRequiredPlugins\x12$.pulumirpc.GetRequiredPluginsRequest\x1a%.pulumirpc.GetRequiredPluginsResponse\"\x00\x12\x36\n\x03Run\x12\x15.pulumirpc.RunRequest\x1a\x16.pulumirpc.RunResponse\"\x00\x12@\n\rGetPluginInfo\x12\x16.google.protobuf.Empty\x1a\x15.pulumirpc.PluginInfo\"\x00\x12h\n\x13InstallDependencies\x12%.pulumirpc.InstallDependenciesRequest\x1a&.pulumirpc.InstallDependenciesResponse\"\x00\x30\x01\x12;\n\x05\x41\x62out\x12\x16.google.protobuf.Empty\x1a\x18.pulumirpc.AboutResponse\"\x00\x12o\n\x16GetProgramDependencies\x12(.pulumirpc.GetProgramDependenciesRequest\x1a).pulumirpc.GetProgramDependenciesResponse\"\x00\x12J\n\tRunPlugin\x12\x1b.pulumirpc.RunPluginRequest\x1a\x1c.pulumirpc.RunPluginResponse\"\x00\x30\x01\x12Z\n\x0fGenerateProgram\x12!.pulumirpc.GenerateProgramRequest\x1a\".pulumirpc.GenerateProgramResponse\"\x00\x12Z\n\x0fGenerateProject\x12!.pulumirpc.GenerateProjectRequest\x1a\".pulumirpc.GenerateProjectResponse\"\x00\x12Z\n\x0fGeneratePackage\x12!.pulumirpc.GeneratePackageRequest\x1a\".pulumirpc.GeneratePackageResponse\"\x00\x42\x34Z2github.com/pulumi/pulumi/sdk/v3/proto/go;pulumirpcb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pulumi.language_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/pulumi/pulumi/sdk/v3/proto/go;pulumirpc'
  _ABOUTRESPONSE_METADATAENTRY._options = None
  _ABOUTRESPONSE_METADATAENTRY._serialized_options = b'8\001'
  _RUNREQUEST_CONFIGENTRY._options = None
  _RUNREQUEST_CONFIGENTRY._serialized_options = b'8\001'
  _GENERATEPROGRAMREQUEST_SOURCEENTRY._options = None
  _GENERATEPROGRAMREQUEST_SOURCEENTRY._serialized_options = b'8\001'
  _GENERATEPROGRAMRESPONSE_SOURCEENTRY._options = None
  _GENERATEPROGRAMRESPONSE_SOURCEENTRY._serialized_options = b'8\001'
  _GENERATEPACKAGEREQUEST_EXTRAFILESENTRY._options = None
  _GENERATEPACKAGEREQUEST_EXTRAFILESENTRY._serialized_options = b'8\001'
  _ABOUTRESPONSE._serialized_start=113
  _ABOUTRESPONSE._serialized_end=272
  _ABOUTRESPONSE_METADATAENTRY._serialized_start=225
  _ABOUTRESPONSE_METADATAENTRY._serialized_end=272
  _GETPROGRAMDEPENDENCIESREQUEST._serialized_start=274
  _GETPROGRAMDEPENDENCIESREQUEST._serialized_end=384
  _DEPENDENCYINFO._serialized_start=386
  _DEPENDENCYINFO._serialized_end=433
  _GETPROGRAMDEPENDENCIESRESPONSE._serialized_start=435
  _GETPROGRAMDEPENDENCIESRESPONSE._serialized_end=516
  _GETREQUIREDPLUGINSREQUEST._serialized_start=518
  _GETREQUIREDPLUGINSREQUEST._serialized_end=592
  _GETREQUIREDPLUGINSRESPONSE._serialized_start=594
  _GETREQUIREDPLUGINSRESPONSE._serialized_end=668
  _RUNREQUEST._serialized_start=671
  _RUNREQUEST._serialized_end=983
  _RUNREQUEST_CONFIGENTRY._serialized_start=938
  _RUNREQUEST_CONFIGENTRY._serialized_end=983
  _RUNRESPONSE._serialized_start=985
  _RUNRESPONSE._serialized_end=1027
  _INSTALLDEPENDENCIESREQUEST._serialized_start=1029
  _INSTALLDEPENDENCIESREQUEST._serialized_end=1097
  _INSTALLDEPENDENCIESRESPONSE._serialized_start=1099
  _INSTALLDEPENDENCIESRESPONSE._serialized_end=1160
  _RUNPLUGINREQUEST._serialized_start=1162
  _RUNPLUGINREQUEST._serialized_end=1237
  _RUNPLUGINRESPONSE._serialized_start=1239
  _RUNPLUGINRESPONSE._serialized_end=1324
  _GENERATEPROGRAMREQUEST._serialized_start=1327
  _GENERATEPROGRAMREQUEST._serialized_end=1461
  _GENERATEPROGRAMREQUEST_SOURCEENTRY._serialized_start=1416
  _GENERATEPROGRAMREQUEST_SOURCEENTRY._serialized_end=1461
  _GENERATEPROGRAMRESPONSE._serialized_start=1464
  _GENERATEPROGRAMRESPONSE._serialized_end=1652
  _GENERATEPROGRAMRESPONSE_SOURCEENTRY._serialized_start=1607
  _GENERATEPROGRAMRESPONSE_SOURCEENTRY._serialized_end=1652
  _GENERATEPROJECTREQUEST._serialized_start=1654
  _GENERATEPROJECTREQUEST._serialized_end=1747
  _GENERATEPROJECTRESPONSE._serialized_start=1749
  _GENERATEPROJECTRESPONSE._serialized_end=1826
  _GENERATEPACKAGEREQUEST._serialized_start=1829
  _GENERATEPACKAGEREQUEST._serialized_end=2011
  _GENERATEPACKAGEREQUEST_EXTRAFILESENTRY._serialized_start=1962
  _GENERATEPACKAGEREQUEST_EXTRAFILESENTRY._serialized_end=2011
  _GENERATEPACKAGERESPONSE._serialized_start=2013
  _GENERATEPACKAGERESPONSE._serialized_end=2038
  _LANGUAGERUNTIME._serialized_start=2041
  _LANGUAGERUNTIME._serialized_end=2913
# @@protoc_insertion_point(module_scope)
