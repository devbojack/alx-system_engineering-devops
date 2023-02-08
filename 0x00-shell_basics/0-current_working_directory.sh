#!/bin/bash
path=$(realpath "${BASH_SOURCE:-$0}")
DIR_PATH=$(dirname $path)
echo $DIR_PATH
