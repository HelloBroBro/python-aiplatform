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

import dataclasses
from typing import List, Optional, Sequence, Union

from google.protobuf import timestamp_pb2


@dataclasses.dataclass
class RagFile:
    """RAG file (output only).

    Attributes:
        name: Generated resource name. Format:
            ``projects/{project}/locations/{location}/ragCorpora/{rag_corpus_id}/ragFiles/{rag_file}``
        display_name: Display name that was configured at client side.
        description: The description of the RagFile.
    """

    name: Optional[str] = None
    display_name: Optional[str] = None
    description: Optional[str] = None


@dataclasses.dataclass
class VertexPredictionEndpoint:
    """VertexPredictionEndpoint.

    Attributes:
        publisher_model: 1P publisher model resource name. Format:
            ``publishers/google/models/{model}`` or
            ``projects/{project}/locations/{location}/publishers/google/models/{model}``
        endpoint: 1P fine tuned embedding model resource name. Format:
            ``endpoints/{endpoint}`` or
            ``projects/{project}/locations/{location}/endpoints/{endpoint}``.
        model:
            Output only. The resource name of the model that is deployed
            on the endpoint. Present only when the endpoint is not a
            publisher model. Pattern:
            ``projects/{project}/locations/{location}/models/{model}``
        model_version_id:
            Output only. Version ID of the model that is
            deployed on the endpoint. Present only when the
            endpoint is not a publisher model.
    """

    endpoint: Optional[str] = None
    publisher_model: Optional[str] = None
    model: Optional[str] = None
    model_version_id: Optional[str] = None


@dataclasses.dataclass
class RagEmbeddingModelConfig:
    """RagEmbeddingModelConfig.

    Attributes:
        vertex_prediction_endpoint: The Vertex AI Prediction Endpoint resource
            name. Format:
            ``projects/{project}/locations/{location}/endpoints/{endpoint}``
    """

    vertex_prediction_endpoint: Optional[VertexPredictionEndpoint] = None


@dataclasses.dataclass
class EmbeddingModelConfig:
    """EmbeddingModelConfig.

    The representation of the embedding model config. Users input a 1P embedding
    model as a Publisher model resource, or a 1P fine tuned embedding model
    as an Endpoint resource.

    Attributes:
        publisher_model: 1P publisher model resource name. Format:
            ``publishers/google/models/{model}`` or
            ``projects/{project}/locations/{location}/publishers/google/models/{model}``
        endpoint: 1P fine tuned embedding model resource name. Format:
            ``endpoints/{endpoint}`` or
            ``projects/{project}/locations/{location}/endpoints/{endpoint}``.
        model:
            Output only. The resource name of the model that is deployed
            on the endpoint. Present only when the endpoint is not a
            publisher model. Pattern:
            ``projects/{project}/locations/{location}/models/{model}``
        model_version_id:
            Output only. Version ID of the model that is
            deployed on the endpoint. Present only when the
            endpoint is not a publisher model.
    """

    publisher_model: Optional[str] = None
    endpoint: Optional[str] = None
    model: Optional[str] = None
    model_version_id: Optional[str] = None


@dataclasses.dataclass
class Weaviate:
    """Weaviate.

    Attributes:
        weaviate_http_endpoint: The Weaviate DB instance HTTP endpoint
        collection_name: The corresponding Weaviate collection this corpus maps to
        api_key: The SecretManager resource name for the Weaviate DB API token. Format:
            ``projects/{project}/secrets/{secret}/versions/{version}``
    """

    weaviate_http_endpoint: Optional[str] = None
    collection_name: Optional[str] = None
    api_key: Optional[str] = None


@dataclasses.dataclass
class VertexFeatureStore:
    """VertexFeatureStore.

    Attributes:
        resource_name: The resource name of the FeatureView. Format:
            ``projects/{project}/locations/{location}/featureOnlineStores/
              {feature_online_store}/featureViews/{feature_view}``
    """

    resource_name: Optional[str] = None


@dataclasses.dataclass
class VertexVectorSearch:
    """VertexVectorSearch.

    Attributes:
        index_endpoint (str):
            The resource name of the Index Endpoint. Format:
            ``projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}``
        index (str):
            The resource name of the Index. Format:
            ``projects/{project}/locations/{location}/indexes/{index}``
    """

    index_endpoint: Optional[str] = None
    index: Optional[str] = None


@dataclasses.dataclass
class RagManagedDb:
    """RagManagedDb."""


@dataclasses.dataclass
class Pinecone:
    """Pinecone.

    Attributes:
        index_name: The Pinecone index name.
        api_key: The SecretManager resource name for the Pinecone DB API token. Format:
            ``projects/{project}/secrets/{secret}/versions/{version}``
    """

    index_name: Optional[str] = None
    api_key: Optional[str] = None


@dataclasses.dataclass
class RagVectorDbConfig:
    """RagVectorDbConfig.

    Attributes:
        vector_db: Can be one of the following: RagManagedDb, Pinecone,
        VertexVectorSearch.
        rag_embedding_model_config: The embedding model config of the Vector DB.
    """

    vector_db: Optional[
        Union[
            VertexVectorSearch,
            Pinecone,
            RagManagedDb,
        ]
    ] = None
    rag_embedding_model_config: Optional[RagEmbeddingModelConfig] = None


@dataclasses.dataclass
class RagCorpus:
    """RAG corpus(output only).

    Attributes:
        name: Generated resource name. Format:
            ``projects/{project}/locations/{location}/ragCorpora/{rag_corpus_id}``
        display_name: Display name that was configured at client side.
        description: The description of the RagCorpus.
        backend_config: The backend config of the RagCorpus. It can be a data
            store and/or retrieval engine.
    """

    name: Optional[str] = None
    display_name: Optional[str] = None
    description: Optional[str] = None
    backend_config: Optional[
        Union[
            RagVectorDbConfig,
            None,
        ]
    ] = None


@dataclasses.dataclass
class RagResource:
    """RagResource.

    The representation of the rag source. It can be used to specify corpus only
    or ragfiles. Currently only support one corpus or multiple files from one
    corpus. In the future we may open up multiple corpora support.

    Attributes:
        rag_corpus: A Rag corpus resource name or corpus id. Format:
            ``projects/{project}/locations/{location}/ragCorpora/{rag_corpus_id}``
            or ``{rag_corpus_id}``.
        rag_files_id: List of Rag file resource name or file ids in the same corpus. Format:
            ``{rag_file}``.
    """

    rag_corpus: Optional[str] = None
    rag_file_ids: Optional[List[str]] = None


@dataclasses.dataclass
class SlackChannel:
    """SlackChannel.

    Attributes:
        channel_id: The Slack channel ID.
        api_key: The SecretManager resource name for the Slack API token. Format:
            ``projects/{project}/secrets/{secret}/versions/{version}``
            See: https://api.slack.com/tutorials/tracks/getting-a-token.
        start_time: The starting timestamp for messages to import.
        end_time: The ending timestamp for messages to import.
    """

    channel_id: str
    api_key: str
    start_time: Optional[timestamp_pb2.Timestamp] = None
    end_time: Optional[timestamp_pb2.Timestamp] = None


@dataclasses.dataclass
class SlackChannelsSource:
    """SlackChannelsSource.

    Attributes:
        channels: The Slack channels.
    """

    channels: Sequence[SlackChannel]


@dataclasses.dataclass
class JiraQuery:
    """JiraQuery.

    Attributes:
        email: The Jira email address.
        jira_projects: A list of Jira projects to import in their entirety.
        custom_queries: A list of custom JQL Jira queries to import.
        api_key: The SecretManager version resource name for Jira API access. Format:
            ``projects/{project}/secrets/{secret}/versions/{version}``
            See: https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/
        server_uri: The Jira server URI. Format:
            ``{server}.atlassian.net``
    """

    email: str
    jira_projects: Sequence[str]
    custom_queries: Sequence[str]
    api_key: str
    server_uri: str


@dataclasses.dataclass
class JiraSource:
    """JiraSource.

    Attributes:
        queries: The Jira queries.
    """

    queries: Sequence[JiraQuery]


@dataclasses.dataclass
class SharePointSource:
    """SharePointSource.

    Attributes:
        sharepoint_folder_path: The path of the SharePoint folder to download
            from.
        sharepoint_folder_id: The ID of the SharePoint folder to download
            from.
        drive_name: The name of the drive to download from.
        drive_id: The ID of the drive to download from.
        client_id: The Application ID for the app registered in
            Microsoft Azure Portal. The application must
            also be configured with MS Graph permissions
            "Files.ReadAll", "Sites.ReadAll" and
            BrowserSiteLists.Read.All.
        client_secret: The application secret for the app registered
            in Azure.
        tenant_id: Unique identifier of the Azure Active
            Directory Instance.
        sharepoint_site_name: The name of the SharePoint site to download
            from. This can be the site name or the site id.
    """

    sharepoint_folder_path: Optional[str] = None
    sharepoint_folder_id: Optional[str] = None
    drive_name: Optional[str] = None
    drive_id: Optional[str] = None
    client_id: str = None
    client_secret: str = None
    tenant_id: str = None
    sharepoint_site_name: str = None


@dataclasses.dataclass
class SharePointSources:
    """SharePointSources.

    Attributes:
        share_point_sources: The SharePoint sources.
    """

    share_point_sources: Sequence[SharePointSource]


@dataclasses.dataclass
class Filter:
    """Filter.

    Attributes:
        vector_distance_threshold: Only returns contexts with vector
            distance smaller than the threshold.
        vector_similarity_threshold: Only returns contexts with vector
            similarity larger than the threshold.
        metadata_filter: String for metadata filtering.
    """

    vector_distance_threshold: Optional[float] = None
    vector_similarity_threshold: Optional[float] = None
    metadata_filter: Optional[str] = None


@dataclasses.dataclass
class RagRetrievalConfig:
    """RagRetrievalConfig.

    Attributes:
        top_k: The number of contexts to retrieve.
        filter: Config for filters.
    """

    top_k: Optional[int] = None
    filter: Optional[Filter] = None


@dataclasses.dataclass
class ChunkingConfig:
    """ChunkingConfig.

    Attributes:
        chunk_size: The size of each chunk.
        chunk_overlap: The size of the overlap between chunks.
    """

    chunk_size: int
    chunk_overlap: int


@dataclasses.dataclass
class TransformationConfig:
    """TransformationConfig.

    Attributes:
        chunking_config: The chunking config.
    """

    chunking_config: Optional[ChunkingConfig] = None