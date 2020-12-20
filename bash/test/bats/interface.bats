#!/usr/bin/env bats

yf=../../dist/main
@test "Compiled source" {
  FILE=../../dist/main
  [ -f "$FILE" ]
}

@test "Proper action headers" {  
  headers=$(./$yf actions -t MSFT | head -n1)
  result="Date,Dividends,Stock Splits"

  [ "$headers" = "$result" ]
}

@test "Proper calendar row labels" {
  labels=$(./$yf calendar -t MSFT | awk -F ',' '{ print $1 }' | xargs)
  result="Earnings Date Earnings Average Earnings Low Earnings High Revenue Average Revenue Low Revenue High"

  [ "$labels" = "$result" ]
}

@test "Proper dividends headers" {
  headers=$(./$yf dividends -t MSFT | head -n1)
  result="Date,Dividends"

  [ "$headers" = "$result" ]
}