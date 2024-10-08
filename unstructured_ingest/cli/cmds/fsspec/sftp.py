import typing as t
from dataclasses import dataclass

import click

from unstructured_ingest.cli.base.src import BaseSrcCmd
from unstructured_ingest.cli.interfaces import (
    CliConfig,
)
from unstructured_ingest.connector.fsspec.sftp import SimpleSftpConfig

CMD_NAME = "sftp"


@dataclass
class SftpCliConfig(SimpleSftpConfig, CliConfig):
    @staticmethod
    def get_cli_options() -> t.List[click.Option]:
        options = [
            click.Option(
                ["--username"],
                required=True,
                type=str,
                help="Username for sftp connection",
            ),
            click.Option(
                ["--password"],
                required=True,
                type=str,
                help="Password for sftp connection",
            ),
            click.Option(
                ["--look-for-keys"],
                required=False,
                default=False,
                is_flag=True,
                type=bool,
                help="Whether to search for private key files in ~/.ssh/",
            ),
            click.Option(
                ["--allow-agent"],
                required=False,
                default=False,
                is_flag=True,
                type=bool,
                help="Whether to connect to the SSH agent.",
            ),
        ]
        return options


def get_base_src_cmd() -> BaseSrcCmd:
    cmd_cls = BaseSrcCmd(
        cmd_name=CMD_NAME,
        cli_config=SftpCliConfig,
        is_fsspec=True,
    )
    return cmd_cls
