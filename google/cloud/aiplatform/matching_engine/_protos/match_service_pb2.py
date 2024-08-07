# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/matching_engine/_protos/match_service.proto
"""Generated protocol buffer code."""

from google.protobuf.internal import builder as _builder
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database


# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nCgoogle/cloud/aiplatform/matching_engine/_protos/match_service.proto\x12$google.cloud.aiplatform.container.v1\x1a\x17google/rpc/status.proto"7\n\x0fSparseEmbedding\x12\x11\n\tfloat_val\x18\x01 \x03(\x02\x12\x11\n\tdimension\x18\x02 \x03(\x03"\xff\x04\n\x0cMatchRequest\x12\x19\n\x11\x64\x65ployed_index_id\x18\x01 \x01(\t\x12\x11\n\tfloat_val\x18\x02 \x03(\x02\x12O\n\x10sparse_embedding\x18\x0c \x01(\x0b\x32\x35.google.cloud.aiplatform.container.v1.SparseEmbedding\x12\x45\n\x03rrf\x18\r \x01(\x0b\x32\x36.google.cloud.aiplatform.container.v1.MatchRequest.RRFH\x00\x12\x15\n\rnum_neighbors\x18\x03 \x01(\x05\x12\x42\n\trestricts\x18\x04 \x03(\x0b\x32/.google.cloud.aiplatform.container.v1.Namespace\x12Q\n\x11numeric_restricts\x18\x0b \x03(\x0b\x32\x36.google.cloud.aiplatform.container.v1.NumericNamespace\x12,\n$per_crowding_attribute_num_neighbors\x18\x05 \x01(\x05\x12\x1c\n\x14\x61pprox_num_neighbors\x18\x06 \x01(\x05\x12-\n%leaf_nodes_to_search_percent_override\x18\x07 \x01(\x05\x12.\n&fraction_leaf_nodes_to_search_override\x18\t \x01(\x01\x12\x19\n\x11\x65mbedding_enabled\x18\x08 \x01(\x08\x12\x14\n\x0c\x65mbedding_id\x18\n \x01(\t\x1a\x14\n\x03RRF\x12\r\n\x05\x61lpha\x18\x01 \x01(\x02\x42\t\n\x07ranking"\xae\x02\n\tEmbedding\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfloat_val\x18\x02 \x03(\x02\x12O\n\x10sparse_embedding\x18\x06 \x01(\x0b\x32\x35.google.cloud.aiplatform.container.v1.SparseEmbedding\x12\x42\n\trestricts\x18\x03 \x03(\x0b\x32/.google.cloud.aiplatform.container.v1.Namespace\x12Q\n\x11numeric_restricts\x18\x05 \x03(\x0b\x32\x36.google.cloud.aiplatform.container.v1.NumericNamespace\x12\x1a\n\x12\x63rowding_attribute\x18\x04 \x01(\x03"\x83\x02\n\rMatchResponse\x12N\n\x08neighbor\x18\x01 \x03(\x0b\x32<.google.cloud.aiplatform.container.v1.MatchResponse.Neighbor\x12\x43\n\nembeddings\x18\x02 \x03(\x0b\x32/.google.cloud.aiplatform.container.v1.Embedding\x1a]\n\x08Neighbor\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x64istance\x18\x02 \x01(\x01\x12\x17\n\x0fsparse_distance\x18\x04 \x01(\x01\x12\x1a\n\x12\x63rowding_attribute\x18\x03 \x01(\x03"B\n\x19\x42\x61tchGetEmbeddingsRequest\x12\x19\n\x11\x64\x65ployed_index_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x03(\t"a\n\x1a\x42\x61tchGetEmbeddingsResponse\x12\x43\n\nembeddings\x18\x01 \x03(\x0b\x32/.google.cloud.aiplatform.container.v1.Embedding"\x95\x02\n\x11\x42\x61tchMatchRequest\x12\x63\n\x08requests\x18\x01 \x03(\x0b\x32Q.google.cloud.aiplatform.container.v1.BatchMatchRequest.BatchMatchRequestPerIndex\x1a\x9a\x01\n\x19\x42\x61tchMatchRequestPerIndex\x12\x19\n\x11\x64\x65ployed_index_id\x18\x01 \x01(\t\x12\x44\n\x08requests\x18\x02 \x03(\x0b\x32\x32.google.cloud.aiplatform.container.v1.MatchRequest\x12\x1c\n\x14low_level_batch_size\x18\x03 \x01(\x05"\xa2\x02\n\x12\x42\x61tchMatchResponse\x12\x66\n\tresponses\x18\x01 \x03(\x0b\x32S.google.cloud.aiplatform.container.v1.BatchMatchResponse.BatchMatchResponsePerIndex\x1a\xa3\x01\n\x1a\x42\x61tchMatchResponsePerIndex\x12\x19\n\x11\x64\x65ployed_index_id\x18\x01 \x01(\t\x12\x46\n\tresponses\x18\x02 \x03(\x0b\x32\x33.google.cloud.aiplatform.container.v1.MatchResponse\x12"\n\x06status\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status"D\n\tNamespace\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x61llow_tokens\x18\x02 \x03(\t\x12\x13\n\x0b\x64\x65ny_tokens\x18\x03 \x03(\t"\xb4\x02\n\x10NumericNamespace\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\tvalue_int\x18\x02 \x01(\x03H\x00\x12\x15\n\x0bvalue_float\x18\x03 \x01(\x02H\x00\x12\x16\n\x0cvalue_double\x18\x04 \x01(\x01H\x00\x12K\n\x02op\x18\x05 \x01(\x0e\x32?.google.cloud.aiplatform.container.v1.NumericNamespace.Operator"x\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\x08\n\x04LESS\x10\x01\x12\x0e\n\nLESS_EQUAL\x10\x02\x12\t\n\x05\x45QUAL\x10\x03\x12\x11\n\rGREATER_EQUAL\x10\x04\x12\x0b\n\x07GREATER\x10\x05\x12\r\n\tNOT_EQUAL\x10\x06\x42\x07\n\x05Value2\xa2\x03\n\x0cMatchService\x12r\n\x05Match\x12\x32.google.cloud.aiplatform.container.v1.MatchRequest\x1a\x33.google.cloud.aiplatform.container.v1.MatchResponse"\x00\x12\x81\x01\n\nBatchMatch\x12\x37.google.cloud.aiplatform.container.v1.BatchMatchRequest\x1a\x38.google.cloud.aiplatform.container.v1.BatchMatchResponse"\x00\x12\x99\x01\n\x12\x42\x61tchGetEmbeddings\x12?.google.cloud.aiplatform.container.v1.BatchGetEmbeddingsRequest\x1a@.google.cloud.aiplatform.container.v1.BatchGetEmbeddingsResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR,
    "google.cloud.aiplatform.matching_engine._protos.match_service_pb2",
    _globals,
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_SPARSEEMBEDDING"]._serialized_start = 134
    _globals["_SPARSEEMBEDDING"]._serialized_end = 189
    _globals["_MATCHREQUEST"]._serialized_start = 192
    _globals["_MATCHREQUEST"]._serialized_end = 831
    _globals["_MATCHREQUEST_RRF"]._serialized_start = 800
    _globals["_MATCHREQUEST_RRF"]._serialized_end = 820
    _globals["_EMBEDDING"]._serialized_start = 834
    _globals["_EMBEDDING"]._serialized_end = 1136
    _globals["_MATCHRESPONSE"]._serialized_start = 1139
    _globals["_MATCHRESPONSE"]._serialized_end = 1398
    _globals["_MATCHRESPONSE_NEIGHBOR"]._serialized_start = 1305
    _globals["_MATCHRESPONSE_NEIGHBOR"]._serialized_end = 1398
    _globals["_BATCHGETEMBEDDINGSREQUEST"]._serialized_start = 1400
    _globals["_BATCHGETEMBEDDINGSREQUEST"]._serialized_end = 1466
    _globals["_BATCHGETEMBEDDINGSRESPONSE"]._serialized_start = 1468
    _globals["_BATCHGETEMBEDDINGSRESPONSE"]._serialized_end = 1565
    _globals["_BATCHMATCHREQUEST"]._serialized_start = 1568
    _globals["_BATCHMATCHREQUEST"]._serialized_end = 1845
    _globals["_BATCHMATCHREQUEST_BATCHMATCHREQUESTPERINDEX"]._serialized_start = 1691
    _globals["_BATCHMATCHREQUEST_BATCHMATCHREQUESTPERINDEX"]._serialized_end = 1845
    _globals["_BATCHMATCHRESPONSE"]._serialized_start = 1848
    _globals["_BATCHMATCHRESPONSE"]._serialized_end = 2138
    _globals["_BATCHMATCHRESPONSE_BATCHMATCHRESPONSEPERINDEX"]._serialized_start = 1975
    _globals["_BATCHMATCHRESPONSE_BATCHMATCHRESPONSEPERINDEX"]._serialized_end = 2138
    _globals["_NAMESPACE"]._serialized_start = 2140
    _globals["_NAMESPACE"]._serialized_end = 2208
    _globals["_NUMERICNAMESPACE"]._serialized_start = 2211
    _globals["_NUMERICNAMESPACE"]._serialized_end = 2519
    _globals["_NUMERICNAMESPACE_OPERATOR"]._serialized_start = 2390
    _globals["_NUMERICNAMESPACE_OPERATOR"]._serialized_end = 2510
    _globals["_MATCHSERVICE"]._serialized_start = 2522
    _globals["_MATCHSERVICE"]._serialized_end = 2940
# @@protoc_insertion_point(module_scope)
