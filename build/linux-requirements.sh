#!/bin/bash

apt-get update && apt-get install -qq -y bash gcc python3-dev \
    postgresql postgresql-contrib libpq-dev
