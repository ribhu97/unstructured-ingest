import typing as t
from dataclasses import dataclass

import click

from unstructured_ingest.cli.interfaces import (
    CliConfig,
)
from unstructured_ingest.connector.pinecone import PineconeWriteConfig, SimplePineconeConfig


@dataclass
class PineconeCliConfig(SimplePineconeConfig, CliConfig):
    @staticmethod
    def get_cli_options() -> t.List[click.Option]:
        options = [
            click.Option(
                ["--api-key"],
                required=True,
                type=str,
                help="API key used for authenticating to a Pinecone instance.",
                envvar="PINECONE_API_KEY",
                show_envvar=True,
            ),
            click.Option(
                ["--index-name"],
                required=True,
                type=str,
                help="The name of the pinecone index to connect to.",
            ),
            click.Option(
                ["--environment"],
                required=True,
                type=str,
                help="The environment where the index lives. Eg. 'gcp-starter' or 'us-east1-gcp'",
            ),
        ]
        return options


@dataclass
class PineconeCliWriteConfig(PineconeWriteConfig, CliConfig):
    @staticmethod
    def get_cli_options() -> t.List[click.Option]:
        options = [
            click.Option(
                ["--batch-size"],
                default=50,
                type=int,
                help="Number of records per batch",
            ),
            click.Option(
                ["--num-processes"],
                default=2,
                type=int,
                help="Number of parallel processes with which to upload elements",
            ),
            click.Option(
                ["--namespace"],
                default=None,
                type=str,
                required=False,
                help="The namespace where the vectors will be upserted in the index",
            ),
        ]
        return options


def get_base_dest_cmd():
    from unstructured_ingest.cli.base.dest import BaseDestCmd

    cmd_cls = BaseDestCmd(
        cmd_name="pinecone",
        cli_config=PineconeCliConfig,
        additional_cli_options=[PineconeCliWriteConfig],
        write_config=PineconeWriteConfig,
    )
    return cmd_cls
