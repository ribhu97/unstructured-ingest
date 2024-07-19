"""
setup.py

unstructured - pre-processing tools for unstructured data

Copyright 2022 Unstructured Technologies, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from pathlib import Path
from typing import List, Union

from setuptools import find_packages, setup
from unstructured.__version__ import __version__


def load_requirements(file: Union[str, Path]) -> List[str]:
    path = file if isinstance(file, Path) else Path(file)
    requirements: List[str] = []
    if not path.is_file():
        raise FileNotFoundError(f"path does not point to a valid file: {path}")
    if not path.suffix == ".in":
        raise ValueError(f"file should have .in extension: {path}")
    file_dir = path.parent.resolve()
    with open(file, encoding="utf-8") as f:
        raw = f.read().splitlines()
        requirements.extend([r for r in raw if not r.startswith("#") and not r.startswith("-")])
        recursive_reqs = [r for r in raw if r.startswith("-r")]
    for recursive_req in recursive_reqs:
        file_spec = recursive_req.split()[-1]
        file_path = Path(file_dir) / file_spec
        requirements.extend(load_requirements(file=file_path.resolve()))
    # Remove duplicates and any blank entries
    return list({r for r in requirements if r})


csv_reqs = load_requirements("requirements/extra-csv.in")
doc_reqs = load_requirements("requirements/extra-docx.in")
docx_reqs = load_requirements("requirements/extra-docx.in")
epub_reqs = load_requirements("requirements/extra-epub.in")
image_reqs = load_requirements("requirements/extra-pdf-image.in")
markdown_reqs = load_requirements("requirements/extra-markdown.in")
msg_reqs = load_requirements("requirements/extra-msg.in")
odt_reqs = load_requirements("requirements/extra-odt.in")
org_reqs = load_requirements("requirements/extra-pandoc.in")
pdf_reqs = load_requirements("requirements/extra-pdf-image.in")
ppt_reqs = load_requirements("requirements/extra-pptx.in")
pptx_reqs = load_requirements("requirements/extra-pptx.in")
rtf_reqs = load_requirements("requirements/extra-pandoc.in")
rst_reqs = load_requirements("requirements/extra-pandoc.in")
tsv_reqs = load_requirements("requirements/extra-csv.in")
xlsx_reqs = load_requirements("requirements/extra-xlsx.in")

all_doc_reqs = list(
    set(
        csv_reqs
        + docx_reqs
        + epub_reqs
        + image_reqs
        + markdown_reqs
        + msg_reqs
        + odt_reqs
        + org_reqs
        + pdf_reqs
        + pptx_reqs
        + rtf_reqs
        + rst_reqs
        + tsv_reqs
        + xlsx_reqs,
    ),
)


setup(
    name="unstructured-ingest",
    description="A library that prepares raw documents for downstream ML tasks.",
    long_description=open("README.md", encoding="utf-8").read(),  # noqa: SIM115
    long_description_content_type="text/markdown",
    keywords="NLP PDF HTML CV XML parsing preprocessing",
    url="https://github.com/Unstructured-IO/unstructured-ingest",
    python_requires=">=3.9.0,<3.13",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    author="Unstructured Technologies",
    author_email="devops@unstructuredai.io",
    license="Apache-2.0",
    packages=find_packages(),
    version=__version__,
    entry_points={
        "console_scripts": ["unstructured-ingest=unstructured_ingest.main:main"],
    },
    extras_require={
        # Document specific extra requirements
        "all-docs": all_doc_reqs,
        "csv": csv_reqs,
        "doc": doc_reqs,
        "docx": docx_reqs,
        "epub": epub_reqs,
        "image": image_reqs,
        "md": markdown_reqs,
        "msg": msg_reqs,
        "odt": odt_reqs,
        "org": org_reqs,
        "pdf": pdf_reqs,
        "ppt": ppt_reqs,
        "pptx": pptx_reqs,
        "rtf": rtf_reqs,
        "rst": rst_reqs,
        "tsv": tsv_reqs,
        "xlsx": xlsx_reqs,
        # Extra requirements for data connectors
        "airtable": load_requirements("requirements/airtable.in"),
        "astra": load_requirements("requirements/astra.in"),
        "azure": load_requirements("requirements/azure.in"),
        "azure-cognitive-search": load_requirements(
            "requirements/azure-cognitive-search.in",
        ),
        "biomed": load_requirements("requirements/biomed.in"),
        "box": load_requirements("requirements/box.in"),
        "chroma": load_requirements("requirements/chroma.in"),
        "clarifai": load_requirements("requirements/clarifai.in"),
        "confluence": load_requirements("requirements/confluence.in"),
        "delta-table": load_requirements("requirements/delta-table.in"),
        "discord": load_requirements("requirements/discord.in"),
        "dropbox": load_requirements("requirements/dropbox.in"),
        "elasticsearch": load_requirements("requirements/elasticsearch.in"),
        "gcs": load_requirements("requirements/gcs.in"),
        "github": load_requirements("requirements/github.in"),
        "gitlab": load_requirements("requirements/gitlab.in"),
        "google-drive": load_requirements("requirements/google-drive.in"),
        "hubspot": load_requirements("requirements/hubspot.in"),
        "jira": load_requirements("requirements/jira.in"),
        "kafka": load_requirements("requirements/kafka.in"),
        "mongodb": load_requirements("requirements/mongodb.in"),
        "notion": load_requirements("requirements/notion.in"),
        "onedrive": load_requirements("requirements/onedrive.in"),
        "opensearch": load_requirements("requirements/opensearch.in"),
        "outlook": load_requirements("requirements/outlook.in"),
        "pinecone": load_requirements("requirements/pinecone.in"),
        "postgres": load_requirements("requirements/postgres.in"),
        "qdrant": load_requirements("requirements/qdrant.in"),
        "reddit": load_requirements("requirements/reddit.in"),
        "s3": load_requirements("requirements/s3.in"),
        "sharepoint": load_requirements("requirements/sharepoint.in"),
        "salesforce": load_requirements("requirements/salesforce.in"),
        "sftp": load_requirements("requirements/sftp.in"),
        "slack": load_requirements("requirements/slack.in"),
        "wikipedia": load_requirements("requirements/wikipedia.in"),
        "weaviate": load_requirements("requirements/weaviate.in"),
        # Legacy extra requirements
        "huggingface": load_requirements("requirements/huggingface.in"),
        "local-inference": all_doc_reqs,
        "paddleocr": load_requirements("requirements/extra-paddleocr.in"),
        "embed-huggingface": load_requirements("requirements/embed-huggingface.in"),
        "embed-octoai": load_requirements("requirements/embed-octoai.in"),
        "embed-vertexai": load_requirements("requirements/embed-vertexai.in"),
        "embed-voyageai": load_requirements("requirements/embed-voyageai.in"),
        "openai": load_requirements("requirements/embed-openai.in"),
        "bedrock": load_requirements("requirements/embed-aws-bedrock.in"),
        "databricks-volumes": load_requirements("requirements/databricks-volumes.in"),
        "singlestore": load_requirements("requirements/singlestore.in"),
    },
    package_dir={"unstructured": "unstructured"},
    package_data={"unstructured": ["nlp/*.txt", "py.typed"]},
)
