#!/usr/bin/env bash
.PHONY: build
build:
	@docker-compose build

.PHONY: rebuild
rebuild:
	@docker-compose build --no-cache

.PHONY: up
up:
	@docker-compose up -d

.PHONY: test-windows
test-windows:
	@cd back/ && mvn test Dtest="diezTests,DevopsApplicationTests" -Dso=windows

.PHONY: test-linux
test-linux:
	@cd back/ && mvn test Dtest="diezTests,DevopsApplicationTests" -Dso=linux

.PHONY: test-mac
test-mac: up
	@cd back/ && mvn test -Dtest="diezTests, DevopsApplicationTests" -Dso=mac

