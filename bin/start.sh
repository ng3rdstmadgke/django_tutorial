#!/bin/bash
function usage {
cat >&2 <<EOS
######################################################################################################
# uwisgi起動コマンド
#
# [usage]
#  $0 [options]
#
# [options]
#  -h | --help:
#    ヘルプを表示
#  -m | --mode <MODE>:
#    起動モードを指定。 (dev|prod)
#  -d | --daemon
#    バックグラウンドで実行
######################################################################################################
EOS
exit 1
}

function error {
  echo "[error] $1" >&2
  exit 1
}

function info {
  echo "[info] $1"
}

MODE=
OPTIONS=
args=() # 引数(ARG1, ARG2)を格納する配列
while [ "$#" != 0 ]; do
  case $1 in
    -h | --help      ) usage;;
    -m | --mode      ) shift;MODE="$1";;
    -d | --daemon    ) shift;OPTIONS="$OPTIONS -d";;
    -* | --*         ) error "$1 : 不正なオプションです" ;;
    *                ) args+=("$1");; # 引数を配列に追加します
  esac
  shift
done

[ "${#args[@]}" != 0 ] && usage
[ "$MODE" != "dev" -a "$MODE" != "prod" ] && usage

PROJECT_ROOT="$(cd $(dirname $0)/..; pwd)"

cd "$PROJECT_ROOT"

if [ "${MODE}" = "prod" ]; then
  docker run $OPTIONS -p "8000:8000" -v "${PROJECT_ROOT}:/usr/src/app" --env-file "${PROJECT_ROOT}/.env" mysite:latest
elif [ "${MODE}" = "dev" ]; then
  docker run $OPTIONS -p "8000:8000" -v "${PROJECT_ROOT}:/usr/src/app" --env-file "${PROJECT_ROOT}/.env" mysite:latest uwsgi --ini uwsgi-dev.ini
fi