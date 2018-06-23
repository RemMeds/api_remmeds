#!/bin/bash

set -e
set -x


pytest
sonar-scanner \
    -Dsonar.projectKey=api_remmeds \
    -Dsonar.sources=. \
    -Dsonar.host.url=https://sonarcloud.io \
    -Dsonar.organization=remmeds \
    -Dsonar.login=71a0474c2d6a00ad268e14a1419ffd5ea04f720b