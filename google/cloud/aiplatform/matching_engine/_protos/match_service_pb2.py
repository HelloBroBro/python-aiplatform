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
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\nCgoogle/cloud/aiplatform/matching_engine/_protos/match_service.proto\x12$google.cloud.aiplatform.container.v1\x1a\x17google/rpc/status.proto"\xc6\x03\n\x0cMatchRequest\x12\x19\n\x11\x64\x65ployed_index_id\x18\x01 \x01(\t\x12\x11\n\tfloat_val\x18\x02 \x03(\x02\x12\x15\n\rnum_neighbors\x18\x03 \x01(\x05\x12\x42\n\trestricts\x18\x04 \x03(\x0b\x32/.google.cloud.aiplatform.container.v1.Namespace\x12Q\n\x11numeric_restricts\x18\x0b \x03(\x0b\x32\x36.google.cloud.aiplatform.container.v1.NumericNamespace\x12,\n$per_crowding_attribute_num_neighbors\x18\x05 \x01(\x05\x12\x1c\n\x14\x61pprox_num_neighbors\x18\x06 \x01(\x05\x12-\n%leaf_nodes_to_search_percent_override\x18\x07 \x01(\x05\x12.\n&fraction_leaf_nodes_to_search_override\x18\t \x01(\x01\x12\x19\n\x11\x65mbedding_enabled\x18\x08 \x01(\x08\x12\x14\n\x0c\x65mbedding_id\x18\n \x01(\t"\xdd\x01\n\tEmbedding\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfloat_val\x18\x02 \x03(\x02\x12\x42\n\trestricts\x18\x03 \x03(\x0b\x32/.google.cloud.aiplatform.container.v1.Namespace\x12Q\n\x11numeric_restricts\x18\x05 \x03(\x0b\x32\x36.google.cloud.aiplatform.container.v1.NumericNamespace\x12\x1a\n\x12\x63rowding_attribute\x18\x04 \x01(\x03"\xea\x01\n\rMatchResponse\x12N\n\x08neighbor\x18\x01 \x03(\x0b\x32<.google.cloud.aiplatform.container.v1.MatchResponse.Neighbor\x12\x43\n\nembeddings\x18\x02 \x03(\x0b\x32/.google.cloud.aiplatform.container.v1.Embedding\x1a\x44\n\x08Neighbor\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x64istance\x18\x02 \x01(\x01\x12\x1a\n\x12\x63rowding_attribute\x18\x03 \x01(\x03"B\n\x19\x42\x61tchGetEmbeddingsRequest\x12\x19\n\x11\x64\x65ployed_index_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x03(\t"a\n\x1a\x42\x61tchGetEmbeddingsResponse\x12\x43\n\nembeddings\x18\x01 \x03(\x0b\x32/.google.cloud.aiplatform.container.v1.Embedding"\x95\x02\n\x11\x42\x61tchMatchRequest\x12\x63\n\x08requests\x18\x01 \x03(\x0b\x32Q.google.cloud.aiplatform.container.v1.BatchMatchRequest.BatchMatchRequestPerIndex\x1a\x9a\x01\n\x19\x42\x61tchMatchRequestPerIndex\x12\x19\n\x11\x64\x65ployed_index_id\x18\x01 \x01(\t\x12\x44\n\x08requests\x18\x02 \x03(\x0b\x32\x32.google.cloud.aiplatform.container.v1.MatchRequest\x12\x1c\n\x14low_level_batch_size\x18\x03 \x01(\x05"\xa2\x02\n\x12\x42\x61tchMatchResponse\x12\x66\n\tresponses\x18\x01 \x03(\x0b\x32S.google.cloud.aiplatform.container.v1.BatchMatchResponse.BatchMatchResponsePerIndex\x1a\xa3\x01\n\x1a\x42\x61tchMatchResponsePerIndex\x12\x19\n\x11\x64\x65ployed_index_id\x18\x01 \x01(\t\x12\x46\n\tresponses\x18\x02 \x03(\x0b\x32\x33.google.cloud.aiplatform.container.v1.MatchResponse\x12"\n\x06status\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status"D\n\tNamespace\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x61llow_tokens\x18\x02 \x03(\t\x12\x13\n\x0b\x64\x65ny_tokens\x18\x03 \x03(\t"\xb4\x02\n\x10NumericNamespace\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\tvalue_int\x18\x02 \x01(\x03H\x00\x12\x15\n\x0bvalue_float\x18\x03 \x01(\x02H\x00\x12\x16\n\x0cvalue_double\x18\x04 \x01(\x01H\x00\x12K\n\x02op\x18\x05 \x01(\x0e\x32?.google.cloud.aiplatform.container.v1.NumericNamespace.Operator"x\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\x08\n\x04LESS\x10\x01\x12\x0e\n\nLESS_EQUAL\x10\x02\x12\t\n\x05\x45QUAL\x10\x03\x12\x11\n\rGREATER_EQUAL\x10\x04\x12\x0b\n\x07GREATER\x10\x05\x12\r\n\tNOT_EQUAL\x10\x06\x42\x07\n\x05Value2\xa2\x03\n\x0cMatchService\x12r\n\x05Match\x12\x32.google.cloud.aiplatform.container.v1.MatchRequest\x1a\x33.google.cloud.aiplatform.container.v1.MatchResponse"\x00\x12\x81\x01\n\nBatchMatch\x12\x37.google.cloud.aiplatform.container.v1.BatchMatchRequest\x1a\x38.google.cloud.aiplatform.container.v1.BatchMatchResponse"\x00\x12\x99\x01\n\x12\x42\x61tchGetEmbeddings\x12?.google.cloud.aiplatform.container.v1.BatchGetEmbeddingsRequest\x1a@.google.cloud.aiplatform.container.v1.BatchGetEmbeddingsResponse"\x00\x62\x06proto3'
)


_MATCHREQUEST = DESCRIPTOR.message_types_by_name["MatchRequest"]
_EMBEDDING = DESCRIPTOR.message_types_by_name["Embedding"]
_MATCHRESPONSE = DESCRIPTOR.message_types_by_name["MatchResponse"]
_MATCHRESPONSE_NEIGHBOR = _MATCHRESPONSE.nested_types_by_name["Neighbor"]
_BATCHGETEMBEDDINGSREQUEST = DESCRIPTOR.message_types_by_name[
    "BatchGetEmbeddingsRequest"
]
_BATCHGETEMBEDDINGSRESPONSE = DESCRIPTOR.message_types_by_name[
    "BatchGetEmbeddingsResponse"
]
_BATCHMATCHREQUEST = DESCRIPTOR.message_types_by_name["BatchMatchRequest"]
_BATCHMATCHREQUEST_BATCHMATCHREQUESTPERINDEX = _BATCHMATCHREQUEST.nested_types_by_name[
    "BatchMatchRequestPerIndex"
]
_BATCHMATCHRESPONSE = DESCRIPTOR.message_types_by_name["BatchMatchResponse"]
_BATCHMATCHRESPONSE_BATCHMATCHRESPONSEPERINDEX = (
    _BATCHMATCHRESPONSE.nested_types_by_name["BatchMatchResponsePerIndex"]
)
_NAMESPACE = DESCRIPTOR.message_types_by_name["Namespace"]
_NUMERICNAMESPACE = DESCRIPTOR.message_types_by_name["NumericNamespace"]
_NUMERICNAMESPACE_OPERATOR = _NUMERICNAMESPACE.enum_types_by_name["Operator"]
MatchRequest = _reflection.GeneratedProtocolMessageType(
    "MatchRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _MATCHREQUEST,
        "__module__": "google.cloud.aiplatform.matching_engine._protos.match_service_pb2"
        # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.container.v1.MatchRequest)
    },
)
_sym_db.RegisterMessage(MatchRequest)

Embedding = _reflection.GeneratedProtocolMessageType(
    "Embedding",
    (_message.Message,),
    {
        "DESCRIPTOR": _EMBEDDING,
        "__module__": "google.cloud.aiplatform.matching_engine._protos.match_service_pb2"
        # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.container.v1.Embedding)
    },
)
_sym_db.RegisterMessage(Embedding)

MatchResponse = _reflection.GeneratedProtocolMessageType(
    "MatchResponse",
    (_message.Message,),
    {
        "Neighbor": _reflection.GeneratedProtocolMessageType(
            "Neighbor",
            (_message.Message,),
            {
                "DESCRIPTOR": _MATCHRESPONSE_NEIGHBOR,
                "__module__": "google.cloud.aiplatform.matching_engine._protos.match_service_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.container.v1.MatchResponse.Neighbor)
            },
        ),
        "DESCRIPTOR": _MATCHRESPONSE,
        "__module__": "google.cloud.aiplatform.matching_engine._protos.match_service_pb2"
        # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.container.v1.MatchResponse)
    },
)
_sym_db.RegisterMessage(MatchResponse)
_sym_db.RegisterMessage(MatchResponse.Neighbor)

BatchGetEmbeddingsRequest = _reflection.GeneratedProtocolMessageType(
    "BatchGetEmbeddingsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _BATCHGETEMBEDDINGSREQUEST,
        "__module__": "google.cloud.aiplatform.matching_engine._protos.match_service_pb2"
        # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.container.v1.BatchGetEmbeddingsRequest)
    },
)
_sym_db.RegisterMessage(BatchGetEmbeddingsRequest)

BatchGetEmbeddingsResponse = _reflection.GeneratedProtocolMessageType(
    "BatchGetEmbeddingsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _BATCHGETEMBEDDINGSRESPONSE,
        "__module__": "google.cloud.aiplatform.matching_engine._protos.match_service_pb2"
        # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.container.v1.BatchGetEmbeddingsResponse)
    },
)
_sym_db.RegisterMessage(BatchGetEmbeddingsResponse)

BatchMatchRequest = _reflection.GeneratedProtocolMessageType(
    "BatchMatchRequest",
    (_message.Message,),
    {
        "BatchMatchRequestPerIndex": _reflection.GeneratedProtocolMessageType(
            "BatchMatchRequestPerIndex",
            (_message.Message,),
            {
                "DESCRIPTOR": _BATCHMATCHREQUEST_BATCHMATCHREQUESTPERINDEX,
                "__module__": "google.cloud.aiplatform.matching_engine._protos.match_service_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.container.v1.BatchMatchRequest.BatchMatchRequestPerIndex)
            },
        ),
        "DESCRIPTOR": _BATCHMATCHREQUEST,
        "__module__": "google.cloud.aiplatform.matching_engine._protos.match_service_pb2"
        # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.container.v1.BatchMatchRequest)
    },
)
_sym_db.RegisterMessage(BatchMatchRequest)
_sym_db.RegisterMessage(BatchMatchRequest.BatchMatchRequestPerIndex)

BatchMatchResponse = _reflection.GeneratedProtocolMessageType(
    "BatchMatchResponse",
    (_message.Message,),
    {
        "BatchMatchResponsePerIndex": _reflection.GeneratedProtocolMessageType(
            "BatchMatchResponsePerIndex",
            (_message.Message,),
            {
                "DESCRIPTOR": _BATCHMATCHRESPONSE_BATCHMATCHRESPONSEPERINDEX,
                "__module__": "google.cloud.aiplatform.matching_engine._protos.match_service_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.container.v1.BatchMatchResponse.BatchMatchResponsePerIndex)
            },
        ),
        "DESCRIPTOR": _BATCHMATCHRESPONSE,
        "__module__": "google.cloud.aiplatform.matching_engine._protos.match_service_pb2"
        # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.container.v1.BatchMatchResponse)
    },
)
_sym_db.RegisterMessage(BatchMatchResponse)
_sym_db.RegisterMessage(BatchMatchResponse.BatchMatchResponsePerIndex)

Namespace = _reflection.GeneratedProtocolMessageType(
    "Namespace",
    (_message.Message,),
    {
        "DESCRIPTOR": _NAMESPACE,
        "__module__": "google.cloud.aiplatform.matching_engine._protos.match_service_pb2"
        # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.container.v1.Namespace)
    },
)
_sym_db.RegisterMessage(Namespace)

NumericNamespace = _reflection.GeneratedProtocolMessageType(
    "NumericNamespace",
    (_message.Message,),
    {
        "DESCRIPTOR": _NUMERICNAMESPACE,
        "__module__": "google.cloud.aiplatform.matching_engine._protos.match_service_pb2"
        # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.container.v1.NumericNamespace)
    },
)
_sym_db.RegisterMessage(NumericNamespace)

_MATCHSERVICE = DESCRIPTOR.services_by_name["MatchService"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _MATCHREQUEST._serialized_start = 135
    _MATCHREQUEST._serialized_end = 589
    _EMBEDDING._serialized_start = 592
    _EMBEDDING._serialized_end = 813
    _MATCHRESPONSE._serialized_start = 816
    _MATCHRESPONSE._serialized_end = 1050
    _MATCHRESPONSE_NEIGHBOR._serialized_start = 982
    _MATCHRESPONSE_NEIGHBOR._serialized_end = 1050
    _BATCHGETEMBEDDINGSREQUEST._serialized_start = 1052
    _BATCHGETEMBEDDINGSREQUEST._serialized_end = 1118
    _BATCHGETEMBEDDINGSRESPONSE._serialized_start = 1120
    _BATCHGETEMBEDDINGSRESPONSE._serialized_end = 1217
    _BATCHMATCHREQUEST._serialized_start = 1220
    _BATCHMATCHREQUEST._serialized_end = 1497
    _BATCHMATCHREQUEST_BATCHMATCHREQUESTPERINDEX._serialized_start = 1343
    _BATCHMATCHREQUEST_BATCHMATCHREQUESTPERINDEX._serialized_end = 1497
    _BATCHMATCHRESPONSE._serialized_start = 1500
    _BATCHMATCHRESPONSE._serialized_end = 1790
    _BATCHMATCHRESPONSE_BATCHMATCHRESPONSEPERINDEX._serialized_start = 1627
    _BATCHMATCHRESPONSE_BATCHMATCHRESPONSEPERINDEX._serialized_end = 1790
    _NAMESPACE._serialized_start = 1792
    _NAMESPACE._serialized_end = 1860
    _NUMERICNAMESPACE._serialized_start = 1863
    _NUMERICNAMESPACE._serialized_end = 2171
    _NUMERICNAMESPACE_OPERATOR._serialized_start = 2042
    _NUMERICNAMESPACE_OPERATOR._serialized_end = 2162
    _MATCHSERVICE._serialized_start = 2174
    _MATCHSERVICE._serialized_end = 2592
# @@protoc_insertion_point(module_scope)
