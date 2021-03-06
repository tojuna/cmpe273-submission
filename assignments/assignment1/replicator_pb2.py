# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: replicator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='replicator.proto',
  package='replicator_package',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10replicator.proto\x12\x12replicator_package\"\x16\n\x03\x64ml\x12\x0f\n\x07message\x18\x01 \x01(\t\"(\n\x03rec\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08received\x18\x02 \x01(\x08\x32\x41\n\x04repl\x12\x39\n\x05query\x12\x17.replicator_package.dml\x1a\x17.replicator_package.recb\x06proto3'
)




_DML = _descriptor.Descriptor(
  name='dml',
  full_name='replicator_package.dml',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='replicator_package.dml.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=40,
  serialized_end=62,
)


_REC = _descriptor.Descriptor(
  name='rec',
  full_name='replicator_package.rec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='replicator_package.rec.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='received', full_name='replicator_package.rec.received', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=64,
  serialized_end=104,
)

DESCRIPTOR.message_types_by_name['dml'] = _DML
DESCRIPTOR.message_types_by_name['rec'] = _REC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

dml = _reflection.GeneratedProtocolMessageType('dml', (_message.Message,), {
  'DESCRIPTOR' : _DML,
  '__module__' : 'replicator_pb2'
  # @@protoc_insertion_point(class_scope:replicator_package.dml)
  })
_sym_db.RegisterMessage(dml)

rec = _reflection.GeneratedProtocolMessageType('rec', (_message.Message,), {
  'DESCRIPTOR' : _REC,
  '__module__' : 'replicator_pb2'
  # @@protoc_insertion_point(class_scope:replicator_package.rec)
  })
_sym_db.RegisterMessage(rec)



_REPL = _descriptor.ServiceDescriptor(
  name='repl',
  full_name='replicator_package.repl',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=106,
  serialized_end=171,
  methods=[
  _descriptor.MethodDescriptor(
    name='query',
    full_name='replicator_package.repl.query',
    index=0,
    containing_service=None,
    input_type=_DML,
    output_type=_REC,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_REPL)

DESCRIPTOR.services_by_name['repl'] = _REPL

# @@protoc_insertion_point(module_scope)
