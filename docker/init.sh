#!/usr/bin/env bash
set -euo pipefail

SITE_NAME="${SITE_NAME:-suite.nacionalcarnes.com.br}"
ADMIN_PASSWORD="${ADMIN_PASSWORD:-admin}"
MYSQL_ROOT_PASSWORD="${MYSQL_ROOT_PASSWORD:-admin}"

export PATH="${NVM_DIR}/versions/node/v${NODE_VERSION_DEVELOP}/bin/:${PATH}"

if [ ! -d "/home/frappe/frappe-bench/apps/frappe" ]; then
  bench init --skip-redis-config-generation frappe-bench
  cd frappe-bench
  bench set-mariadb-host mariadb
  bench set-redis-cache-host redis://redis:6379
  bench set-redis-queue-host redis://redis:6379
  bench set-redis-socketio-host redis://redis:6379
  sed -i '/redis/d' ./Procfile
  sed -i '/watch/d' ./Procfile
  bench get-app erpnext
  bench get-app hrms
  bench get-app /workspace/apps/nacional_suite
  bench new-site "$SITE_NAME" --force --mariadb-root-password "$MYSQL_ROOT_PASSWORD" --admin-password "$ADMIN_PASSWORD" --no-mariadb-socket
  bench --site "$SITE_NAME" install-app hrms
  bench --site "$SITE_NAME" install-app nacional_suite
  bench --site "$SITE_NAME" set-config developer_mode 1
  bench --site "$SITE_NAME" enable-scheduler
  bench --site "$SITE_NAME" clear-cache
  bench use "$SITE_NAME"
else
  cd frappe-bench
fi

bench start
