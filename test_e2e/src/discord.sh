#!/usr/bin/env bash

set -e

SRC_PATH=$(dirname "$(realpath "$0")")
SCRIPT_DIR=$(dirname "$SRC_PATH")
cd "$SCRIPT_DIR"/.. || exit 1
OUTPUT_FOLDER_NAME=discord
OUTPUT_ROOT=${OUTPUT_ROOT:-$SCRIPT_DIR}
OUTPUT_DIR=$OUTPUT_ROOT/structured-output/$OUTPUT_FOLDER_NAME
WORK_DIR=$OUTPUT_ROOT/workdir/$OUTPUT_FOLDER_NAME
DOWNLOAD_DIR=$SCRIPT_DIR/download/$OUTPUT_FOLDER_NAME
max_processes=${MAX_PROCESSES:=$(python3 -c "import os; print(os.cpu_count())")}
CI=${CI:-"false"}

# shellcheck disable=SC1091
source "$SCRIPT_DIR"/cleanup.sh
function cleanup() {
	cleanup_dir "$OUTPUT_DIR"
	cleanup_dir "$WORK_DIR"
	if [ "$CI" == "true" ]; then
		cleanup_dir "$DOWNLOAD_DIR"
	fi
}
trap cleanup EXIT

if [ -z "$DISCORD_TOKEN" ]; then
	echo "Skipping Discord ingest test because the DISCORD_TOKEN env var is not set."
	exit 8
fi

RUN_SCRIPT=${RUN_SCRIPT:-./unstructured_ingest/main.py}
PYTHONPATH=${PYTHONPATH:-.} "$RUN_SCRIPT" \
	discord \
	--num-processes "$max_processes" \
	--metadata-exclude coordinates,file_directory,metadata.data_source.date_processed,metadata.last_modified,metadata.detection_class_prob,metadata.parent_id,metadata.category_depth \
	--download-dir "$DOWNLOAD_DIR" \
	--preserve-downloads \
	--reprocess \
	--output-dir "$OUTPUT_DIR" \
	--verbose \
	--channels 1099442333440802930,1099601456321003600 \
	--token "$DISCORD_TOKEN" \
	--work-dir "$WORK_DIR"

"$SCRIPT_DIR"/check-diff-expected-output.sh $OUTPUT_FOLDER_NAME
