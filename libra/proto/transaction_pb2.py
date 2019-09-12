# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transaction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import access_path_pb2 as access__path__pb2
import events_pb2 as events__pb2
import proof_pb2 as proof__pb2
import transaction_info_pb2 as transaction__info__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='transaction.proto',
  package='types',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11transaction.proto\x12\x05types\x1a\x11\x61\x63\x63\x65ss_path.proto\x1a\x0c\x65vents.proto\x1a\x0bproof.proto\x1a\x16transaction_info.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xa0\x02\n\x0eRawTransaction\x12\x16\n\x0esender_account\x18\x01 \x01(\x0c\x12\x17\n\x0fsequence_number\x18\x02 \x01(\x04\x12!\n\x07program\x18\x03 \x01(\x0b\x32\x0e.types.ProgramH\x00\x12$\n\twrite_set\x18\x04 \x01(\x0b\x32\x0f.types.WriteSetH\x00\x12\x1f\n\x06script\x18\x08 \x01(\x0b\x32\r.types.ScriptH\x00\x12\x1f\n\x06module\x18\t \x01(\x0b\x32\r.types.ModuleH\x00\x12\x16\n\x0emax_gas_amount\x18\x05 \x01(\x04\x12\x16\n\x0egas_unit_price\x18\x06 \x01(\x04\x12\x17\n\x0f\x65xpiration_time\x18\x07 \x01(\x04\x42\t\n\x07payload\"W\n\x07Program\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x0c\x12-\n\targuments\x18\x02 \x03(\x0b\x32\x1a.types.TransactionArgument\x12\x0f\n\x07modules\x18\x03 \x03(\x0c\"E\n\x06Script\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x0c\x12-\n\targuments\x18\x02 \x03(\x0b\x32\x1a.types.TransactionArgument\"\x91\x01\n\x13TransactionArgument\x12\x30\n\x04type\x18\x01 \x01(\x0e\x32\".types.TransactionArgument.ArgType\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\":\n\x07\x41rgType\x12\x07\n\x03U64\x10\x00\x12\x0b\n\x07\x41\x44\x44RESS\x10\x01\x12\n\n\x06STRING\x10\x02\x12\r\n\tBYTEARRAY\x10\x03\"\x16\n\x06Module\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x0c\"_\n\x11SignedTransaction\x12\x15\n\rraw_txn_bytes\x18\x01 \x01(\x0c\x12\x19\n\x11sender_public_key\x18\x02 \x01(\x0c\x12\x18\n\x10sender_signature\x18\x03 \x01(\x0c\"\xb4\x01\n\x1aSignedTransactionWithProof\x12\x0f\n\x07version\x18\x01 \x01(\x04\x12\x34\n\x12signed_transaction\x18\x02 \x01(\x0b\x32\x18.types.SignedTransaction\x12,\n\x05proof\x18\x03 \x01(\x0b\x32\x1d.types.SignedTransactionProof\x12!\n\x06\x65vents\x18\x04 \x01(\x0b\x32\x11.types.EventsList\"\x84\x01\n\x17SignedTransactionsBlock\x12.\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x18.types.SignedTransaction\x12\x1c\n\x14validator_public_key\x18\x02 \x01(\x0c\x12\x1b\n\x13validator_signature\x18\x03 \x01(\x0c\"-\n\x08WriteSet\x12!\n\twrite_set\x18\x01 \x03(\x0b\x32\x0e.types.WriteOp\"b\n\x07WriteOp\x12&\n\x0b\x61\x63\x63\x65ss_path\x18\x01 \x01(\x0b\x32\x11.types.AccessPath\x12\r\n\x05value\x18\x02 \x01(\x0c\x12 \n\x04type\x18\x03 \x01(\x0e\x32\x12.types.WriteOpType\"-\n\x0c\x41\x63\x63ountState\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x0c\n\x04\x62lob\x18\x02 \x01(\x0c\"\xa0\x01\n\x13TransactionToCommit\x12,\n\nsigned_txn\x18\x01 \x01(\x0b\x32\x18.types.SignedTransaction\x12+\n\x0e\x61\x63\x63ount_states\x18\x02 \x03(\x0b\x32\x13.types.AccountState\x12\x1c\n\x06\x65vents\x18\x03 \x03(\x0b\x32\x0c.types.Event\x12\x10\n\x08gas_used\x18\x04 \x01(\x04\"\xe2\x02\n\x18TransactionListWithProof\x12.\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x18.types.SignedTransaction\x12%\n\x05infos\x18\x02 \x03(\x0b\x32\x16.types.TransactionInfo\x12\x35\n\x13\x65vents_for_versions\x18\x03 \x01(\x0b\x32\x18.types.EventsForVersions\x12?\n\x19\x66irst_transaction_version\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12;\n\x1aproof_of_first_transaction\x18\x05 \x01(\x0b\x32\x17.types.AccumulatorProof\x12:\n\x19proof_of_last_transaction\x18\x06 \x01(\x0b\x32\x17.types.AccumulatorProof*$\n\x0bWriteOpType\x12\t\n\x05Write\x10\x00\x12\n\n\x06\x44\x65lete\x10\x01\x62\x06proto3')
  ,
  dependencies=[access__path__pb2.DESCRIPTOR,events__pb2.DESCRIPTOR,proof__pb2.DESCRIPTOR,transaction__info__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])

_WRITEOPTYPE = _descriptor.EnumDescriptor(
  name='WriteOpType',
  full_name='types.WriteOpType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Write', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Delete', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1882,
  serialized_end=1918,
)
_sym_db.RegisterEnumDescriptor(_WRITEOPTYPE)

WriteOpType = enum_type_wrapper.EnumTypeWrapper(_WRITEOPTYPE)
Write = 0
Delete = 1


_TRANSACTIONARGUMENT_ARGTYPE = _descriptor.EnumDescriptor(
  name='ArgType',
  full_name='types.TransactionArgument.ArgType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='U64', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDRESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BYTEARRAY', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=669,
  serialized_end=727,
)
_sym_db.RegisterEnumDescriptor(_TRANSACTIONARGUMENT_ARGTYPE)


_RAWTRANSACTION = _descriptor.Descriptor(
  name='RawTransaction',
  full_name='types.RawTransaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender_account', full_name='types.RawTransaction.sender_account', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='types.RawTransaction.sequence_number', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='program', full_name='types.RawTransaction.program', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='write_set', full_name='types.RawTransaction.write_set', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='script', full_name='types.RawTransaction.script', index=4,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='module', full_name='types.RawTransaction.module', index=5,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_gas_amount', full_name='types.RawTransaction.max_gas_amount', index=6,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gas_unit_price', full_name='types.RawTransaction.gas_unit_price', index=7,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiration_time', full_name='types.RawTransaction.expiration_time', index=8,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='payload', full_name='types.RawTransaction.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=131,
  serialized_end=419,
)


_PROGRAM = _descriptor.Descriptor(
  name='Program',
  full_name='types.Program',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='types.Program.code', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arguments', full_name='types.Program.arguments', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modules', full_name='types.Program.modules', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=421,
  serialized_end=508,
)


_SCRIPT = _descriptor.Descriptor(
  name='Script',
  full_name='types.Script',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='types.Script.code', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arguments', full_name='types.Script.arguments', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=510,
  serialized_end=579,
)


_TRANSACTIONARGUMENT = _descriptor.Descriptor(
  name='TransactionArgument',
  full_name='types.TransactionArgument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='types.TransactionArgument.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='types.TransactionArgument.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRANSACTIONARGUMENT_ARGTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=582,
  serialized_end=727,
)


_MODULE = _descriptor.Descriptor(
  name='Module',
  full_name='types.Module',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='types.Module.code', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=729,
  serialized_end=751,
)


_SIGNEDTRANSACTION = _descriptor.Descriptor(
  name='SignedTransaction',
  full_name='types.SignedTransaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raw_txn_bytes', full_name='types.SignedTransaction.raw_txn_bytes', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender_public_key', full_name='types.SignedTransaction.sender_public_key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender_signature', full_name='types.SignedTransaction.sender_signature', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=753,
  serialized_end=848,
)


_SIGNEDTRANSACTIONWITHPROOF = _descriptor.Descriptor(
  name='SignedTransactionWithProof',
  full_name='types.SignedTransactionWithProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='types.SignedTransactionWithProof.version', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signed_transaction', full_name='types.SignedTransactionWithProof.signed_transaction', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proof', full_name='types.SignedTransactionWithProof.proof', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='events', full_name='types.SignedTransactionWithProof.events', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=851,
  serialized_end=1031,
)


_SIGNEDTRANSACTIONSBLOCK = _descriptor.Descriptor(
  name='SignedTransactionsBlock',
  full_name='types.SignedTransactionsBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transactions', full_name='types.SignedTransactionsBlock.transactions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validator_public_key', full_name='types.SignedTransactionsBlock.validator_public_key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validator_signature', full_name='types.SignedTransactionsBlock.validator_signature', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1034,
  serialized_end=1166,
)


_WRITESET = _descriptor.Descriptor(
  name='WriteSet',
  full_name='types.WriteSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='write_set', full_name='types.WriteSet.write_set', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1168,
  serialized_end=1213,
)


_WRITEOP = _descriptor.Descriptor(
  name='WriteOp',
  full_name='types.WriteOp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_path', full_name='types.WriteOp.access_path', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='types.WriteOp.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='types.WriteOp.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1215,
  serialized_end=1313,
)


_ACCOUNTSTATE = _descriptor.Descriptor(
  name='AccountState',
  full_name='types.AccountState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='types.AccountState.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blob', full_name='types.AccountState.blob', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1315,
  serialized_end=1360,
)


_TRANSACTIONTOCOMMIT = _descriptor.Descriptor(
  name='TransactionToCommit',
  full_name='types.TransactionToCommit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signed_txn', full_name='types.TransactionToCommit.signed_txn', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_states', full_name='types.TransactionToCommit.account_states', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='events', full_name='types.TransactionToCommit.events', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gas_used', full_name='types.TransactionToCommit.gas_used', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1363,
  serialized_end=1523,
)


_TRANSACTIONLISTWITHPROOF = _descriptor.Descriptor(
  name='TransactionListWithProof',
  full_name='types.TransactionListWithProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transactions', full_name='types.TransactionListWithProof.transactions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='infos', full_name='types.TransactionListWithProof.infos', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='events_for_versions', full_name='types.TransactionListWithProof.events_for_versions', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_transaction_version', full_name='types.TransactionListWithProof.first_transaction_version', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proof_of_first_transaction', full_name='types.TransactionListWithProof.proof_of_first_transaction', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proof_of_last_transaction', full_name='types.TransactionListWithProof.proof_of_last_transaction', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1526,
  serialized_end=1880,
)

_RAWTRANSACTION.fields_by_name['program'].message_type = _PROGRAM
_RAWTRANSACTION.fields_by_name['write_set'].message_type = _WRITESET
_RAWTRANSACTION.fields_by_name['script'].message_type = _SCRIPT
_RAWTRANSACTION.fields_by_name['module'].message_type = _MODULE
_RAWTRANSACTION.oneofs_by_name['payload'].fields.append(
  _RAWTRANSACTION.fields_by_name['program'])
_RAWTRANSACTION.fields_by_name['program'].containing_oneof = _RAWTRANSACTION.oneofs_by_name['payload']
_RAWTRANSACTION.oneofs_by_name['payload'].fields.append(
  _RAWTRANSACTION.fields_by_name['write_set'])
_RAWTRANSACTION.fields_by_name['write_set'].containing_oneof = _RAWTRANSACTION.oneofs_by_name['payload']
_RAWTRANSACTION.oneofs_by_name['payload'].fields.append(
  _RAWTRANSACTION.fields_by_name['script'])
_RAWTRANSACTION.fields_by_name['script'].containing_oneof = _RAWTRANSACTION.oneofs_by_name['payload']
_RAWTRANSACTION.oneofs_by_name['payload'].fields.append(
  _RAWTRANSACTION.fields_by_name['module'])
_RAWTRANSACTION.fields_by_name['module'].containing_oneof = _RAWTRANSACTION.oneofs_by_name['payload']
_PROGRAM.fields_by_name['arguments'].message_type = _TRANSACTIONARGUMENT
_SCRIPT.fields_by_name['arguments'].message_type = _TRANSACTIONARGUMENT
_TRANSACTIONARGUMENT.fields_by_name['type'].enum_type = _TRANSACTIONARGUMENT_ARGTYPE
_TRANSACTIONARGUMENT_ARGTYPE.containing_type = _TRANSACTIONARGUMENT
_SIGNEDTRANSACTIONWITHPROOF.fields_by_name['signed_transaction'].message_type = _SIGNEDTRANSACTION
_SIGNEDTRANSACTIONWITHPROOF.fields_by_name['proof'].message_type = proof__pb2._SIGNEDTRANSACTIONPROOF
_SIGNEDTRANSACTIONWITHPROOF.fields_by_name['events'].message_type = events__pb2._EVENTSLIST
_SIGNEDTRANSACTIONSBLOCK.fields_by_name['transactions'].message_type = _SIGNEDTRANSACTION
_WRITESET.fields_by_name['write_set'].message_type = _WRITEOP
_WRITEOP.fields_by_name['access_path'].message_type = access__path__pb2._ACCESSPATH
_WRITEOP.fields_by_name['type'].enum_type = _WRITEOPTYPE
_TRANSACTIONTOCOMMIT.fields_by_name['signed_txn'].message_type = _SIGNEDTRANSACTION
_TRANSACTIONTOCOMMIT.fields_by_name['account_states'].message_type = _ACCOUNTSTATE
_TRANSACTIONTOCOMMIT.fields_by_name['events'].message_type = events__pb2._EVENT
_TRANSACTIONLISTWITHPROOF.fields_by_name['transactions'].message_type = _SIGNEDTRANSACTION
_TRANSACTIONLISTWITHPROOF.fields_by_name['infos'].message_type = transaction__info__pb2._TRANSACTIONINFO
_TRANSACTIONLISTWITHPROOF.fields_by_name['events_for_versions'].message_type = events__pb2._EVENTSFORVERSIONS
_TRANSACTIONLISTWITHPROOF.fields_by_name['first_transaction_version'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT64VALUE
_TRANSACTIONLISTWITHPROOF.fields_by_name['proof_of_first_transaction'].message_type = proof__pb2._ACCUMULATORPROOF
_TRANSACTIONLISTWITHPROOF.fields_by_name['proof_of_last_transaction'].message_type = proof__pb2._ACCUMULATORPROOF
DESCRIPTOR.message_types_by_name['RawTransaction'] = _RAWTRANSACTION
DESCRIPTOR.message_types_by_name['Program'] = _PROGRAM
DESCRIPTOR.message_types_by_name['Script'] = _SCRIPT
DESCRIPTOR.message_types_by_name['TransactionArgument'] = _TRANSACTIONARGUMENT
DESCRIPTOR.message_types_by_name['Module'] = _MODULE
DESCRIPTOR.message_types_by_name['SignedTransaction'] = _SIGNEDTRANSACTION
DESCRIPTOR.message_types_by_name['SignedTransactionWithProof'] = _SIGNEDTRANSACTIONWITHPROOF
DESCRIPTOR.message_types_by_name['SignedTransactionsBlock'] = _SIGNEDTRANSACTIONSBLOCK
DESCRIPTOR.message_types_by_name['WriteSet'] = _WRITESET
DESCRIPTOR.message_types_by_name['WriteOp'] = _WRITEOP
DESCRIPTOR.message_types_by_name['AccountState'] = _ACCOUNTSTATE
DESCRIPTOR.message_types_by_name['TransactionToCommit'] = _TRANSACTIONTOCOMMIT
DESCRIPTOR.message_types_by_name['TransactionListWithProof'] = _TRANSACTIONLISTWITHPROOF
DESCRIPTOR.enum_types_by_name['WriteOpType'] = _WRITEOPTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RawTransaction = _reflection.GeneratedProtocolMessageType('RawTransaction', (_message.Message,), {
  'DESCRIPTOR' : _RAWTRANSACTION,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:types.RawTransaction)
  })
_sym_db.RegisterMessage(RawTransaction)

Program = _reflection.GeneratedProtocolMessageType('Program', (_message.Message,), {
  'DESCRIPTOR' : _PROGRAM,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:types.Program)
  })
_sym_db.RegisterMessage(Program)

Script = _reflection.GeneratedProtocolMessageType('Script', (_message.Message,), {
  'DESCRIPTOR' : _SCRIPT,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:types.Script)
  })
_sym_db.RegisterMessage(Script)

TransactionArgument = _reflection.GeneratedProtocolMessageType('TransactionArgument', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONARGUMENT,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:types.TransactionArgument)
  })
_sym_db.RegisterMessage(TransactionArgument)

Module = _reflection.GeneratedProtocolMessageType('Module', (_message.Message,), {
  'DESCRIPTOR' : _MODULE,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:types.Module)
  })
_sym_db.RegisterMessage(Module)

SignedTransaction = _reflection.GeneratedProtocolMessageType('SignedTransaction', (_message.Message,), {
  'DESCRIPTOR' : _SIGNEDTRANSACTION,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:types.SignedTransaction)
  })
_sym_db.RegisterMessage(SignedTransaction)

SignedTransactionWithProof = _reflection.GeneratedProtocolMessageType('SignedTransactionWithProof', (_message.Message,), {
  'DESCRIPTOR' : _SIGNEDTRANSACTIONWITHPROOF,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:types.SignedTransactionWithProof)
  })
_sym_db.RegisterMessage(SignedTransactionWithProof)

SignedTransactionsBlock = _reflection.GeneratedProtocolMessageType('SignedTransactionsBlock', (_message.Message,), {
  'DESCRIPTOR' : _SIGNEDTRANSACTIONSBLOCK,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:types.SignedTransactionsBlock)
  })
_sym_db.RegisterMessage(SignedTransactionsBlock)

WriteSet = _reflection.GeneratedProtocolMessageType('WriteSet', (_message.Message,), {
  'DESCRIPTOR' : _WRITESET,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:types.WriteSet)
  })
_sym_db.RegisterMessage(WriteSet)

WriteOp = _reflection.GeneratedProtocolMessageType('WriteOp', (_message.Message,), {
  'DESCRIPTOR' : _WRITEOP,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:types.WriteOp)
  })
_sym_db.RegisterMessage(WriteOp)

AccountState = _reflection.GeneratedProtocolMessageType('AccountState', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTSTATE,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:types.AccountState)
  })
_sym_db.RegisterMessage(AccountState)

TransactionToCommit = _reflection.GeneratedProtocolMessageType('TransactionToCommit', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONTOCOMMIT,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:types.TransactionToCommit)
  })
_sym_db.RegisterMessage(TransactionToCommit)

TransactionListWithProof = _reflection.GeneratedProtocolMessageType('TransactionListWithProof', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONLISTWITHPROOF,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:types.TransactionListWithProof)
  })
_sym_db.RegisterMessage(TransactionListWithProof)


# @@protoc_insertion_point(module_scope)
