# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server_utility/server_utility.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='server_utility/server_utility.proto',
  package='mavsdk.rpc.server_utility',
  syntax='proto3',
  serialized_options=b'\n\030io.mavsdk.server_utilityB\022ServerUtilityProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#server_utility/server_utility.proto\x12\x19mavsdk.rpc.server_utility\x1a\x14mavsdk_options.proto\"^\n\x15SendStatusTextRequest\x12\x37\n\x04type\x18\x01 \x01(\x0e\x32).mavsdk.rpc.server_utility.StatusTextType\x12\x0c\n\x04text\x18\x02 \x01(\t\"g\n\x16SendStatusTextResponse\x12M\n\x15server_utility_result\x18\x01 \x01(\x0b\x32..mavsdk.rpc.server_utility.ServerUtilityResult\"\xf3\x01\n\x13ServerUtilityResult\x12\x45\n\x06result\x18\x01 \x01(\x0e\x32\x35.mavsdk.rpc.server_utility.ServerUtilityResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\x80\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x02\x12\x1b\n\x17RESULT_CONNECTION_ERROR\x10\x03\x12\x1b\n\x17RESULT_INVALID_ARGUMENT\x10\x04*\xf9\x01\n\x0eStatusTextType\x12\x1a\n\x16STATUS_TEXT_TYPE_DEBUG\x10\x00\x12\x19\n\x15STATUS_TEXT_TYPE_INFO\x10\x01\x12\x1b\n\x17STATUS_TEXT_TYPE_NOTICE\x10\x02\x12\x1c\n\x18STATUS_TEXT_TYPE_WARNING\x10\x03\x12\x1a\n\x16STATUS_TEXT_TYPE_ERROR\x10\x04\x12\x1d\n\x19STATUS_TEXT_TYPE_CRITICAL\x10\x05\x12\x1a\n\x16STATUS_TEXT_TYPE_ALERT\x10\x06\x12\x1e\n\x1aSTATUS_TEXT_TYPE_EMERGENCY\x10\x07\x32\x93\x01\n\x14ServerUtilityService\x12{\n\x0eSendStatusText\x12\x30.mavsdk.rpc.server_utility.SendStatusTextRequest\x1a\x31.mavsdk.rpc.server_utility.SendStatusTextResponse\"\x04\x80\xb5\x18\x01\x42.\n\x18io.mavsdk.server_utilityB\x12ServerUtilityProtob\x06proto3'
  ,
  dependencies=[mavsdk__options__pb2.DESCRIPTOR,])

_STATUSTEXTTYPE = _descriptor.EnumDescriptor(
  name='StatusTextType',
  full_name='mavsdk.rpc.server_utility.StatusTextType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_TEXT_TYPE_DEBUG', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_TEXT_TYPE_INFO', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_TEXT_TYPE_NOTICE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_TEXT_TYPE_WARNING', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_TEXT_TYPE_ERROR', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_TEXT_TYPE_CRITICAL', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_TEXT_TYPE_ALERT', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_TEXT_TYPE_EMERGENCY', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=536,
  serialized_end=785,
)
_sym_db.RegisterEnumDescriptor(_STATUSTEXTTYPE)

StatusTextType = enum_type_wrapper.EnumTypeWrapper(_STATUSTEXTTYPE)
STATUS_TEXT_TYPE_DEBUG = 0
STATUS_TEXT_TYPE_INFO = 1
STATUS_TEXT_TYPE_NOTICE = 2
STATUS_TEXT_TYPE_WARNING = 3
STATUS_TEXT_TYPE_ERROR = 4
STATUS_TEXT_TYPE_CRITICAL = 5
STATUS_TEXT_TYPE_ALERT = 6
STATUS_TEXT_TYPE_EMERGENCY = 7


_SERVERUTILITYRESULT_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mavsdk.rpc.server_utility.ServerUtilityResult.Result',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESULT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_NO_SYSTEM', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_CONNECTION_ERROR', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_INVALID_ARGUMENT', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=405,
  serialized_end=533,
)
_sym_db.RegisterEnumDescriptor(_SERVERUTILITYRESULT_RESULT)


_SENDSTATUSTEXTREQUEST = _descriptor.Descriptor(
  name='SendStatusTextRequest',
  full_name='mavsdk.rpc.server_utility.SendStatusTextRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='mavsdk.rpc.server_utility.SendStatusTextRequest.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='mavsdk.rpc.server_utility.SendStatusTextRequest.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=182,
)


_SENDSTATUSTEXTRESPONSE = _descriptor.Descriptor(
  name='SendStatusTextResponse',
  full_name='mavsdk.rpc.server_utility.SendStatusTextResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_utility_result', full_name='mavsdk.rpc.server_utility.SendStatusTextResponse.server_utility_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=287,
)


_SERVERUTILITYRESULT = _descriptor.Descriptor(
  name='ServerUtilityResult',
  full_name='mavsdk.rpc.server_utility.ServerUtilityResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mavsdk.rpc.server_utility.ServerUtilityResult.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_str', full_name='mavsdk.rpc.server_utility.ServerUtilityResult.result_str', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SERVERUTILITYRESULT_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=290,
  serialized_end=533,
)

_SENDSTATUSTEXTREQUEST.fields_by_name['type'].enum_type = _STATUSTEXTTYPE
_SENDSTATUSTEXTRESPONSE.fields_by_name['server_utility_result'].message_type = _SERVERUTILITYRESULT
_SERVERUTILITYRESULT.fields_by_name['result'].enum_type = _SERVERUTILITYRESULT_RESULT
_SERVERUTILITYRESULT_RESULT.containing_type = _SERVERUTILITYRESULT
DESCRIPTOR.message_types_by_name['SendStatusTextRequest'] = _SENDSTATUSTEXTREQUEST
DESCRIPTOR.message_types_by_name['SendStatusTextResponse'] = _SENDSTATUSTEXTRESPONSE
DESCRIPTOR.message_types_by_name['ServerUtilityResult'] = _SERVERUTILITYRESULT
DESCRIPTOR.enum_types_by_name['StatusTextType'] = _STATUSTEXTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendStatusTextRequest = _reflection.GeneratedProtocolMessageType('SendStatusTextRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDSTATUSTEXTREQUEST,
  '__module__' : 'server_utility.server_utility_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.server_utility.SendStatusTextRequest)
  })
_sym_db.RegisterMessage(SendStatusTextRequest)

SendStatusTextResponse = _reflection.GeneratedProtocolMessageType('SendStatusTextResponse', (_message.Message,), {
  'DESCRIPTOR' : _SENDSTATUSTEXTRESPONSE,
  '__module__' : 'server_utility.server_utility_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.server_utility.SendStatusTextResponse)
  })
_sym_db.RegisterMessage(SendStatusTextResponse)

ServerUtilityResult = _reflection.GeneratedProtocolMessageType('ServerUtilityResult', (_message.Message,), {
  'DESCRIPTOR' : _SERVERUTILITYRESULT,
  '__module__' : 'server_utility.server_utility_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.server_utility.ServerUtilityResult)
  })
_sym_db.RegisterMessage(ServerUtilityResult)


DESCRIPTOR._options = None

_SERVERUTILITYSERVICE = _descriptor.ServiceDescriptor(
  name='ServerUtilityService',
  full_name='mavsdk.rpc.server_utility.ServerUtilityService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=788,
  serialized_end=935,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendStatusText',
    full_name='mavsdk.rpc.server_utility.ServerUtilityService.SendStatusText',
    index=0,
    containing_service=None,
    input_type=_SENDSTATUSTEXTREQUEST,
    output_type=_SENDSTATUSTEXTRESPONSE,
    serialized_options=b'\200\265\030\001',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVERUTILITYSERVICE)

DESCRIPTOR.services_by_name['ServerUtilityService'] = _SERVERUTILITYSERVICE

# @@protoc_insertion_point(module_scope)