# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.aiplatform.v1beta1",
    manifest={
        "RagQuery",
        "RetrieveContextsRequest",
        "RagContexts",
        "RetrieveContextsResponse",
    },
)


class RagQuery(proto.Message):
    r"""A query to retrieve relevant contexts.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text (str):
            Optional. The query in text format to get
            relevant contexts.

            This field is a member of `oneof`_ ``query``.
        similarity_top_k (int):
            Optional. The number of contexts to retrieve.
        ranking (google.cloud.aiplatform_v1beta1.types.RagQuery.Ranking):
            Optional. Configurations for hybrid search
            results ranking.
    """

    class Ranking(proto.Message):
        r"""Configurations for hybrid search results ranking.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            alpha (float):
                Optional. Alpha value controls the weight between dense and
                sparse vector search results. The range is [0, 1], while 0
                means sparse vector search only and 1 means dense vector
                search only. The default value is 0.5 which balances sparse
                and dense vector search equally.

                This field is a member of `oneof`_ ``_alpha``.
        """

        alpha: float = proto.Field(
            proto.FLOAT,
            number=1,
            optional=True,
        )

    text: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="query",
    )
    similarity_top_k: int = proto.Field(
        proto.INT32,
        number=2,
    )
    ranking: Ranking = proto.Field(
        proto.MESSAGE,
        number=4,
        message=Ranking,
    )


class RetrieveContextsRequest(proto.Message):
    r"""Request message for
    [VertexRagService.RetrieveContexts][google.cloud.aiplatform.v1beta1.VertexRagService.RetrieveContexts].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        vertex_rag_store (google.cloud.aiplatform_v1beta1.types.RetrieveContextsRequest.VertexRagStore):
            The data source for Vertex RagStore.

            This field is a member of `oneof`_ ``data_source``.
        parent (str):
            Required. The resource name of the Location from which to
            retrieve RagContexts. The users must have permission to make
            a call in the project. Format:
            ``projects/{project}/locations/{location}``.
        query (google.cloud.aiplatform_v1beta1.types.RagQuery):
            Required. Single RAG retrieve query.
    """

    class VertexRagStore(proto.Message):
        r"""The data source for Vertex RagStore.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            rag_corpora (MutableSequence[str]):
                Optional. Deprecated. Please use rag_resources to specify
                the data source.
            rag_resources (MutableSequence[google.cloud.aiplatform_v1beta1.types.RetrieveContextsRequest.VertexRagStore.RagResource]):
                Optional. The representation of the rag
                source. It can be used to specify corpus only or
                ragfiles. Currently only support one corpus or
                multiple files from one corpus. In the future we
                may open up multiple corpora support.
            vector_distance_threshold (float):
                Optional. Only return contexts with vector
                distance smaller than the threshold.

                This field is a member of `oneof`_ ``_vector_distance_threshold``.
        """

        class RagResource(proto.Message):
            r"""The definition of the Rag resource.

            Attributes:
                rag_corpus (str):
                    Optional. RagCorpora resource name. Format:
                    ``projects/{project}/locations/{location}/ragCorpora/{rag_corpus}``
                rag_file_ids (MutableSequence[str]):
                    Optional. rag_file_id. The files should be in the same
                    rag_corpus set in rag_corpus field.
            """

            rag_corpus: str = proto.Field(
                proto.STRING,
                number=1,
            )
            rag_file_ids: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=2,
            )

        rag_corpora: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        rag_resources: MutableSequence[
            "RetrieveContextsRequest.VertexRagStore.RagResource"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="RetrieveContextsRequest.VertexRagStore.RagResource",
        )
        vector_distance_threshold: float = proto.Field(
            proto.DOUBLE,
            number=2,
            optional=True,
        )

    vertex_rag_store: VertexRagStore = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="data_source",
        message=VertexRagStore,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query: "RagQuery" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="RagQuery",
    )


class RagContexts(proto.Message):
    r"""Relevant contexts for one query.

    Attributes:
        contexts (MutableSequence[google.cloud.aiplatform_v1beta1.types.RagContexts.Context]):
            All its contexts.
    """

    class Context(proto.Message):
        r"""A context of the query.

        Attributes:
            source_uri (str):
                For vertex RagStore, if the file is imported from Cloud
                Storage or Google Drive, source_uri will be original file
                URI in Cloud Storage or Google Drive; if file is uploaded,
                source_uri will be file display name.
            text (str):
                The text chunk.
            distance (float):
                The distance between the query dense
                embedding vector and the context text vector.
            sparse_distance (float):
                The distance between the query sparse
                embedding vector and the context text vector.
        """

        source_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        text: str = proto.Field(
            proto.STRING,
            number=2,
        )
        distance: float = proto.Field(
            proto.DOUBLE,
            number=3,
        )
        sparse_distance: float = proto.Field(
            proto.DOUBLE,
            number=4,
        )

    contexts: MutableSequence[Context] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Context,
    )


class RetrieveContextsResponse(proto.Message):
    r"""Response message for
    [VertexRagService.RetrieveContexts][google.cloud.aiplatform.v1beta1.VertexRagService.RetrieveContexts].

    Attributes:
        contexts (google.cloud.aiplatform_v1beta1.types.RagContexts):
            The contexts of the query.
    """

    contexts: "RagContexts" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RagContexts",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
