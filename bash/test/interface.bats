#!/usr/bin/env bats

@test "Compilation" {
  cd ..
  ./install.sh
  FILE=dist/main
  [ -f "$FILE" ]
}
