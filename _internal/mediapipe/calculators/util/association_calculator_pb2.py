# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/util/association_calculator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7mediapipe/calculators/util/association_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\x9b\x01\n\x1c\x41ssociationCalculatorOptions\x12#\n\x18min_similarity_threshold\x18\x01 \x01(\x02:\x01\x31\x32V\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xef\xa4\x98\x83\x01 \x01(\x0b\x32\'.mediapipe.AssociationCalculatorOptions')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.calculators.util.association_calculator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_ASSOCIATIONCALCULATOROPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _globals['_ASSOCIATIONCALCULATOROPTIONS']._serialized_start=109
  _globals['_ASSOCIATIONCALCULATOROPTIONS']._serialized_end=264
# @@protoc_insertion_point(module_scope)
