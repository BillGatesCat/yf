#!/usr/bin/env bats

@test "Compilation" {
  FILE=../../dist/main
  [ -f "$FILE" ]
}


