# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
# Generated code. DO NOT EDIT!
#
# Snippet for AppendRows
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-bigquery-storage


# [START bigquerystorage_v1beta2_generated_BigQueryWrite_AppendRows_sync]
from google.cloud import bigquery_storage_v1beta2


def sample_append_rows():
    # Create a client
    client = bigquery_storage_v1beta2.BigQueryWriteClient()

    # Initialize request argument(s)
    request = bigquery_storage_v1beta2.AppendRowsRequest(
        write_stream="write_stream_value",
    )

    # This method expects an iterator which contains
    # 'bigquery_storage_v1beta2.AppendRowsRequest' objects
    # Here we create a generator that yields a single `request` for
    # demonstrative purposes.
    requests = [request]

    def request_generator():
        for request in requests:
            yield request

    # Make the request
    stream = client.append_rows(requests=request_generator())

    # Handle the response
    for response in stream:
        print(response)


# [END bigquerystorage_v1beta2_generated_BigQueryWrite_AppendRows_sync]